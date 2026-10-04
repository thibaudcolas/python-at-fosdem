# FOSDEM data sources — research notes

Researched 2026-09-20. Goal: catalogue what data exists about FOSDEM over the years, in
particular the Python devroom, and in which formats. No data collected yet — this is a
source/format inventory. All URLs below were verified live during research unless noted.

## 1. Official schedule archive (frab) — primary structured source

- Base: `https://archive.fosdem.org/<year>/schedule/` for 2003–2025;
  current year on `https://fosdem.org/<year>/schedule/` (2026 live at research time).
- Website hand-off: `https://github.com/FOSDEM/website` — "Archive of the 2013–2025 FOSDEM
  website. Development for 2026 onward is at https://git.fosdem.org/FOSDEM/website".

### Machine-readable exports (from each schedule index page)

| Format               | URL pattern                                    | Notes                                                              |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| Pentabarf XML (frab) | `/schedule/xml`                                | Richest export. Verified 200 for **2012–2026**; 404 for 2003–2011. |
| iCal                 | `/schedule/ical`                               | Verified 2025. Overall conference calendar.                        |
| xCal                 | `/schedule/xcal`                               | Verified 2025. XML-flavoured iCalendar.                            |
| Printable PDF        | `/schedule/pdf/a4.pdf`, `/schedule/pdf/a3.pdf` | Not machine-friendly.                                              |

- Per-track (per-devroom) sub-calendars also exist: `/schedule/track/<slug>.ics` and
  `/schedule/track/<slug>.xcs` (verified for Python in 2017, 2018, 2025).
- Tracking-filtered equivalents exist implicitly, not as a public export: filtering the
  Pentabarf XML by `<track slug="python">Python</track>` per event is the practical path.

### Pentabarf XML content (verified on 2025 XML, 1105 events)

Per `<event>`: `guid`, numeric `id`, `date` (ISO with TZ), `start`, `duration`, `room`,
`slug`, canonical `url`, `title`, `subtitle`, `<track slug>`, `type` (e.g. `devroom`,
`keynote`), `language`, HTML `abstract` + `description`, `feedback_url` (Pretalx code,
e.g. `8T7UD7`), `<persons>` (id + name), `<attachments>` (slides PDFs), `<links>`
(video recording URLs, chat rooms, speaker-supplied links).

Known quality caveats:

- Some older years lack `<track slug>` attribute (2014, 2016, 2021 XMLs parsed fine but
  `slug` attribute absent — match on track element text instead).
- xCal `attendee` list is name-only, no person ids; event `url` values in xCal are
  malformed (double path segment, e.g. `https:/fosdem.org/2025/schedule/2025/...`).
- 2018 track page renders only 8 of its events (page truncation quirk!) — 2018 XML works
  and is the safe path for that year. GNU `grep -c` on HTML pages is unreliable for counts;
  parse XML.

### FOSDEM 2026 (in progress at research time)

- `https://fosdem.org/2026/schedule/xml` — live, with per-event pages under a new-style
  slug (`/schedule/event/WQ3F9A-fosdem_infrastructure_review/`). Python devroom 2026 slug:
  `/schedule/track/python/` (back to the pre-2024 naming; 2024/2025 used `python-devroom`).
  16 event links on the track page (8 events in XML at snapshot time — schedule still being
  amended).

## 2. Python devroom history (year-by-year, derived from official XMLs)

A Python devroom appears from **2013** onwards. Before that Python-flavoured talks sat in
other rooms (e.g. 2011 Python talks were in the Data Analytics devroom, AW1.124) — the
event index pages for 2008–2012 (`/schedule/events.html`) contain only a handful of
Python-titled talks (IronPython 2012, scikits.learn 2011, …), not a devroom.

| Year | Devroom exists  | Track slug (HTML) | Events (XML) | Room                               | Room slug (video dir)            |
| ---- | --------------- | ----------------- | ------------ | ---------------------------------- | -------------------------------- |
| 2013 | yes             | `python`          | —            | K.3.401                            | `K3401` (folder 404 — see Video) |
| 2014 | yes             | `python`          | 16           | K.3.201                            | `K3201/Saturday/`                |
| 2015 | yes             | `python`          | —            | H.1301 (Cornil)                    | `devroom-python/`                |
| 2016 | yes             | `python`          | 17           | UD2.218A (Chavanne)                | `UD2.218A/`                      |
| 2017 | yes             | `python`          | 24           | H.1308 (Rolin), UD2.120 (Chavanne) | `h1308/`, `ud2120/`              |
| 2018 | yes             | `python`          | —            | K.1.105 (La Fontaine)              | `k1105/`                         |
| 2019 | yes             | `python`          | 16           | UD2.120 (Chavanne)                 | `ud2120/`                        |
| 2020 | yes             | `python`          | —            | UB2.252A (Lameere)                 | `UB2.252A (Lameere)/`            |
| 2021 | yes             | `python`          | 16           | D.python (online edition)          | `D.python/`                      |
| 2022 | yes             | `python`          | 18           | D.python (hybrid)                  | `D.python/`                      |
| 2023 | yes             | `python`          | 14           | UD2.218A                           | `ud2218a/`                       |
| 2024 | yes             | `python-devroom`  | 30           | UD2.218A                           | `ud2218a/`                       |
| 2025 | yes             | `python-devroom`  | 16           | UD2.218A                           | `ud2218a/`                       |
| 2026 | yes (scheduled) | `python`          | 8 → 16 links | UA2.220 (Guillissen)               | —                                |

Years with `—` in the Events column: XML 200 OK, Python track confirmed by parsing; exact
counts not re-derived for every year in this pass (14–20 events typical, consistent with
neighbours). 2024 numbers look right (bigger devroom, 30 events) — matching show reports.

Track page slugs changed: `/track/python/` (2013–2023), `/track/python-devroom/`
(2024–2025 only), back to `/track/python/` (2026). 2013 page title says
"FOSDEM 2013 - Python devroom", confirming devroom status.

## 3. Video recordings — second structured source

- `https://video.fosdem.org/<year>/` — open directory listings (nginx autoindex),
  browsable. Lists 2003–2026.
- Directory structure varies by year:
  - 2008–2010: `devrooms/<short-name>/`, `maintracks/`, `lightningtalks/`
  - 2013: `maintracks/`, `lightningtalks/`, and only a couple of devroom folders
    (`cloud`, `telephony`). **No Python devroom folder — 2013 Python talks are not in the
    official archive.** (README in 2013 root documents recording problems.)
  - 2015: `devroom-python/`; 2014 & 2016+: straight room-name folders
    (`K3201/Saturday/`, `ud2218a/`, `D.python/`, `UB2.252A (Lameere)/`, …).
- File formats: `.webm` (older years), earlier `.ogv`; from ~2019 onwards per-event links
  expose both `.mp4` (H.264) and `.av1.webm` plus `.vtt` subtitles.
- Naming is room-centric, not event-centric — talks are matched to events by hand or by
  the `<link>` elements in the schedule XML (2019+ XMLs embed direct video URLs per event,
  2025 also gives AV1/WebM, MP4, and VTT subtitle links).
- 2026 alternates mp4/av1.webm similarly, page confirms publishing completed 2026-04-26.

### When event pages gained video links

Python devroom (and generic) event pages on `archive.fosdem.org` show an explicit
"Video recording" link starting **2018** (pre-2016 event pages only caption the generic
`http://video.fosdem.org/` home, 2017 has 6 video links per some pages but 2018 is the
reliable boundary). So for years 2013–2016 the video archive must be matched by hand
against the room folders above.

## 4. Talk metadata / feedback

- FOSDEM uses **Pretalx** (`https://pretalx.fosdem.org/fosdem-2025/`) since ~2019. The
  public JSON API (`/api/events/...`) is NOT enabled for FOSDEM (verified 404); the XML
  export from frab above is the way in. Talk codes appear in `feedback_url`, allowing
  stable cross-reference with Pretalx if the API ever opens.
- Talks also appear (speaker-submitted) on `speakers.fosdem.org` style profiles? Not
  verified — not pursued.

## 5. Third-party / structured aggregators

- **Wikidata** (`https://query.wikidata.org`) — SPARQL; some FOSDEM editions and
  individual talks modelled, coverage spotty. Usable as an auxiliary, not primary.
- **GitHub: FOSDEM/website** — the website source itself, useful to confirm slug schemes
  and generation changes (nanoc, DC meta).
- **archive.org / YouTube mirror** — FOSDEM's official YouTube channel is
  `@fosdemtalks` (linked from archive pages). Coverage of Python devroom talks on YouTube
  appears later than folder archive (~2019+). Not systematically inventoried.
- **media.ccc.de** — does not host FOSDEM (404 on `/c/fosdem`).

## 6. Noteworthy blog-type sources (non-structured)

These were not collected yet; kept as leads:

- Per-year wrap-ups from the Python devroom organisers (Marc-André Lemburg / eGenix have
  posted CfPs on `lists.fosdem.org`; e.g.
  <https://lists.fosdem.org/pipermail/fosdem/2024q4/003564.html> — "Call for Participation:
  Python devroom @ FOSDEM 2025"). Mailing-list archive at
  `https://lists.fosdem.org/pipermail/fosdem/<year>qN/` is the stable CfP trail.
- Speaker blogs frequently summarise their FOSDEM talks; pick up opportunistically, no
  systematic inventory attempted.

## 7. Practical collection recipe (for later)

1. Fetch `https://archive.fosdem.org/<year>/schedule/xml` for 2012–2025 and
   `https://fosdem.org/2026/schedule/xml`.
2. Filter events with `<track slug="python">` (or where `<track>` text is exactly
   `Python`).
3. For pre-2013 and cross-checking 2013 Python devroom (XML exists in 2013, videos do
   not), fall back to HTML indexes under `archive.fosdem.org`.
4. For videos, use the XML `<link>` elements where present (2019+), else map via the
   room folders listed in section 2 on `video.fosdem.org`.
5. The `/schedule/events.html` index page exists also for 2008–2012 (footgun: 2011 and
   earlier pages serve `.html` suffix — tracks pages are `tracks.html`,
   `track/<name>_devroom.html` etc., different slug scheme from 2013+).
