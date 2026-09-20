#!/usr/bin/env python3
"""Collect Python devroom (track) data from FOSDEM Pentabarf XML archives.

Outputs:
- docs/knowledge-base/fosdem/python-devroom-talks.csv   (one row per talk)
- docs/knowledge-base/fosdem/python-devroom-speakers.json (unique speakers per year;
  no bios or profile URLs: speaker pages use name-slugs, not person ids, so no
  reliable URL can be computed from the XML)

Usage: python3 tools/collect_fosdem_python_devroom.py [--cache-dir DIR]
Pass --cache-dir to reuse previously downloaded XML instead of re-fetching.
"""

import argparse
import csv
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "docs" / "knowledge-base" / "fosdem"
YEARS = list(range(2012, 2027))
# Track "slug" attribute (or element text fallback) identifying the Python devroom.
TRACK_TEXTS = {"Python"}

UA = {"User-Agent": "python-at-fosdem-data-collector/1.0 (repo tool)"}


def xml_url(year: int) -> str:
    if year < 2026:
        return f"https://archive.fosdem.org/{year}/schedule/xml"
    return f"https://fosdem.org/{year}/schedule/xml"


def fetch(year: int, cache_dir: Path) -> bytes:
    cache = cache_dir / f"{year}.xml"
    if cache.exists():
        return cache.read_bytes()
    url = xml_url(year)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    cache.write_bytes(data)
    return data


def strip_html(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    # entities
    for ent, ch in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                    ("&#39;", "'"), ("&apos;", "'"), ("&nbsp;", " ")):
        text = text.replace(ent, ch)
    text = re.sub(r"&#\d+;", "?", text)
    return re.sub(r"\s+", " ", text).strip()


def is_python_track(ev):
    """Match Python devroom tracks. Track text/slugiphies vary by year:
    'Python' (most years), 'Python Devroom devroom' (2024). Slug attribute may
    be absent (2014/2016/2021) so always check element text too."""
    tr = ev.find("track")
    if tr is None:
        return False
    slug = (tr.get("slug") or "").strip().lower()
    text = (tr.text or "").strip()
    return slug in {"python", "python-devroom"} or text.lower() in {
        "python",
        "python devroom",
        "python devroom devroom",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()

    parser = argparse.ArgumentParser  # noqa: F841 (keep flake quiet on refactor)
    cache_dir = Path(args.cache_dir) if args.cache_dir else Path(__file__).parent / "_fosdem_xml_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    talks = []
    speakers_by_year = {}  # year -> {person_id: {"id", "name", "titles"}}
    total_events = {}

    for year in YEARS:
        data = fetch(year, cache_dir)
        root = ET.fromstring(data)
        year_talks = 0
        rooms = set()
        yspk = speakers_by_year.setdefault(year, {})

        # Per-event <date> is missing in 2013-2023 XMLs; use the parent <day date>.
        # Canonical <url>: 2013-2023 XMLs have none; 2024's literally carries
        # fosdem.org/2025/... (published wrong in the XML). We build a canonical
        # URL from each year's own schedule: <event id> + slug, but slugs are not
        # in old XMLs. Simplest canonical scheme that works for every year is the
        # per-id page pattern used by the archives themselves;
        # verified 200: /<year>/schedule/event/<id>/ redirects.
        # NOTE: verify redirect works per year; on failure keep XML url text.
        conf_url = "https://archive.fosdem.org" if year < 2026 else "https://fosdem.org"

        python_event_nodes = []
        for day in root.findall("day"):
            day_date = day.get("date", "")
            for ev in day.iter("event"):
                if not is_python_track(ev):
                    continue
                python_event_nodes.append((day_date, ev))

        for day_date, ev in python_event_nodes:
            year_talks += 1
            room = (ev.findtext("room") or ev.get("room") or "").strip()
            rooms.add(room)

            track = ev.find("track")
            title = (ev.findtext("title") or "").strip()
            subtitle = (ev.findtext("subtitle") or "").strip()

            # Canonical URL: only 2025/2026 XMLs carry correct URLs (2024's
            # literal value wrongly says fosdem.org/2025). Build from each
            # year's <slug>: 2013-2023 uses /<year>/schedule/event/<slug>/,
            # 2024 onwards /<year>/schedule/event/fosdem-<year>-<id>-<slug>/
            # (the <slug> element in 2024+ already contains the full form).
            xml_url = (ev.findtext("url") or "").strip()
            slug = (ev.findtext("slug") or "").strip()
            if year in (2025, 2026) and xml_url:
                url = xml_url
            elif slug:
                url = f"{conf_url}/{year}/schedule/event/{slug}/"
            else:
                url = ""

            video_urls, slide_urls, other_urls = [], [], []
            links_el = ev.find("links")
            if links_el is not None:
                for a in links_el.findall("link"):
                    href = (a.get("href") or (a.text or "")).strip()
                    if not href:
                        continue
                    low = href.lower()
                    if "video.fosdem.org" in low or low.endswith(
                        (".webm", ".mp4", ".ogv", ".av1.webm", ".vtt")
                    ):
                        video_urls.append(href)
                    else:
                        other_urls.append(href)
            att_el = ev.find("attachments")
            if att_el is not None:
                for a in att_el.findall("attachment"):
                    href = (a.get("href") or (a.text or "")).strip()
                    if href:
                        slide_urls.append(href)

            spk = []
            persons = ev.find("persons")
            if persons is not None:
                for p in persons.findall("person"):
                    pid = p.get("id") or ""
                    pname = (p.text or "").strip()
                    spk.append((pid, pname))
                    rec = yspk.get(pid)
                    if not rec:
                        rec = yspk[pid] = {"id": pid, "name": pname, "talks": []}
                    if title not in rec["talks"]:
                        rec["talks"].append(title)

            talks.append(
                {
                    "year": year,
                    "date": (ev.findtext("date") or "").strip() or day_date,
                    "start": (ev.findtext("start") or "").strip(),
                    "duration": (ev.findtext("duration") or "").strip(),
                    "room": room,
                    "title": title,
                    "subtitle": subtitle,
                    "track": (track.text or "").strip() if track is not None else "",
                    "type": (ev.findtext("type") or "").strip(),
                    "language": (ev.findtext("language") or "").strip(),
                    "url": url,
                    "video_url": ";".join(dict.fromkeys(video_urls)),
                    "slides_url": ";".join(dict.fromkeys(slide_urls)),
                    "other_links": ";".join(dict.fromkeys(other_urls)),
                    "speakers": ";".join(f"{pid}:{name}" for pid, name in spk),
                    "feedback_url": (ev.findtext("feedback_url") or "").strip(),
                    "slug": (ev.findtext("slug") or ev.get("slug") or "").strip(),
                    "abstract": strip_html(ev.findtext("abstract") or ""),
                    "description": strip_html(ev.findtext("description") or ""),
                }
            )
        total_events[year] = (year_talks, sorted(rooms))
        print(f"{year}: {year_talks} events, rooms: {sorted(rooms)}")

    # CSV
    cols = [
        "year", "date", "start", "duration", "room", "title", "subtitle", "track",
        "type", "language", "url", "video_url", "slides_url", "other_links",
        "speakers", "feedback_url", "slug", "abstract", "description",
    ]
    with (OUT_DIR / "python-devroom-talks.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(talks)

    # JSON speakers
    out_speakers = []
    for year in YEARS:
        for pid in sorted(speakers_by_year[year], key=lambda k: (len(k), k)):
            rec = speakers_by_year[year][pid]
            out_speakers.append({"year": year, **rec})
    (OUT_DIR / "python-devroom-speakers.json").write_text(
        json.dumps(out_speakers, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(f"\n{len(talks)} talks total; {len(out_speakers)} unique (year, speaker) pairs")


if __name__ == "__main__":
    main()
