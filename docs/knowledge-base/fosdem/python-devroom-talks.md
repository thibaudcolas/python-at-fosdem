---
tags:
  - draft
  - fosdem
  - python-devroom
---

# Python devroom talks dataset

!!! note "Draft status"

    This page describes data collected on 2026-09-20. The FOSDEM 2026 schedule is still being amended, so the 2026 counts below are an incomplete snapshot and will change until the schedule is finalized.

The [Python devroom](https://fosdem.org/2026/schedule/track/python/) is the dedicated Python track at FOSDEM. It first appeared in 2013; before that, Python talks were distributed across other rooms and tracks rather than gathered in one place. The track slug has changed over the years — most editions use `python`, but 2024 used `python-devroom` (see the [2024 devroom](https://archive.fosdem.org/2024/schedule/track/python-devroom/)).

## Datasets

Two files hold the collected data, gathered by the `tools/collect_fosdem_python_devroom.py` collection script in the repo:

- [python-devroom-talks.csv](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/fosdem/python-devroom-talks.csv) — one row per talk, covering every edition of the devroom from 2013 through 2026.
- [python-devroom-speakers.json](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/fosdem/python-devroom-speakers.json) — per-year speaker lists derived from the same schedule data.

## Year-by-year overview

| Year | Talks | Room                               |
| ---- | ----- | ---------------------------------- |
| 2013 | 17    | K.3.401                            |
| 2014 | 16    | K.3.201                            |
| 2015 | 17    | H.1301 (Cornil)                    |
| 2016 | 17    | UD2.218A                           |
| 2017 | 24    | H.1308 (Rolin), UD2.120 (Chavanne) |
| 2018 | 4     | K.1.105 (La Fontaine)              |
| 2019 | 16    | UD2.120 (Chavanne)                 |
| 2020 | 17    | UB2.252A (Lameere)                 |
| 2021 | 16    | D.python                           |
| 2022 | 9     | D.python                           |
| 2023 | 14    | UD2.218A                           |
| 2024 | 15    | UD2.218A                           |
| 2025 | 16    | UD2.218A                           |
| 2026 | 8     | UA2.220 (Guillissen)               |

Rooms are listed as they appear in the schedule data; 2017 has two rooms because that edition's talks were spread across the two.

## CSV columns

The [speakers CSV](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/fosdem/python-devroom-talks.csv) has one row per talk with these columns:

- `year` — the FOSDEM edition year.
- `date` — the date of the talk, in `YYYY-MM-DD` format.
- `start` — the scheduled start time, in `HH:MM` format.
- `duration` — the scheduled duration, in `HH:MM` format.
- `room` — the room the talk was assigned to.
- `title` — the talk title.
- `subtitle` — the subtitle, if any; empty otherwise.
- `track` — the schedule track slug (the devroom track).
- `type` — the type of the event, such as a talk.
- `language` — the language the talk was given in.
- `url` — link to the talk's page on the FOSDEM website.
- `video_url` — link to the video recording, if any.
- `slides_url` — link to the slides, if any.
- `other_links` — any additional links associated with the talk.
- `speakers` — comma-separated list of speaker names.
- `feedback_url` — link to the feedback form for the talk.
- `slug` — the event identifier used in FOSDEM's system.
- `abstract` — the talk's abstract text.
- `description` — the talk's longer description text.

## Data provenance

The data was collected from the official FOSDEM schedule exports:

- For 2012 through 2025, the archived schedule XML at `https://archive.fosdem.org/<YEAR>/schedule/xml` (for example, the [2025 XML](https://archive.fosdem.org/2025/schedule/xml)).
- For 2026, the current schedule XML at [fosdem.org/2026/schedule/xml](https://fosdem.org/2026/schedule/xml).

Talk counts were cross-checked against the per-track iCal exports (for example, the [2025 Python track iCal](https://archive.fosdem.org/2025/schedule/track/python.ics)).

## Data quirks

- The low talk counts for 2018 (4 talks) and 2022 (9 talks) are genuine in the source data — they reflect how the schedule was exported at the time, not a collection error.
- The 2013 edition has no video recordings available.
- Video links start appearing in the XML schedule data from 2018 onward.
- Speaker bios are not part of the schedule export, so they are not included in these datasets.
