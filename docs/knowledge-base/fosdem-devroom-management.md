# Proposing and running a FOSDEM devroom

A collated report on proposing, organizing, and running a [developer room ("devroom")](https://archive.fosdem.org/2026/manuals/program/devroom/) at [FOSDEM](https://fosdem.org/), based on cited online sources: the official FOSDEM calls and manuals, example calls for participation, and organizers' retrospectives. It ends with the milestone plan for [FOSDEM 2027](https://fosdem.org/2027/), which takes place on **Saturday 30 and Sunday 31 January 2027** at the ULB Solbosch campus in Brussels, Belgium.

Devroom data files for this workspace live in `knowledge-base/fosdem/` (talk and speaker exports).

## How devrooms fit into FOSDEM

Devrooms are self-organized conference tracks, assigned to "self-organizing groups to work together on open source and free software projects, to discuss topics relevant to a broader subset of the community", with most content in the form of presentations ([2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/)). Because rooms are scarce, FOSDEM records and live-streams all devrooms and publishes the recordings under the same licence as all FOSDEM content ([2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/)).

A devroom is a mini-conference inside a bigger one: organizers run their own call for participation, select talks, build a schedule in FOSDEM's [Pretalx](https://fosdem.org/submit) instance, and then host the room on the day — introducing speakers, managing questions, keeping time, and minding the camera ([Devroom managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)). For most logistics (venue, A/V, streaming, video production), FOSDEM does the heavy lifting: "The high-quality live streaming and same-day final videos were amazing" ([Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)). The schedule also stays editable until the event, with changes reflected on the FOSDEM website within minutes, so speakers can be swapped right up to the day ([Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)).

## What FOSDEM is looking for in devroom proposals

The 2027 call repeats priorities that recur across recent FOSDEM editions ([2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/), [2024 edition](https://archive.fosdem.org/2024/news/2023-11-08-devrooms-announced/)):

- **Rooms by and for communities, first.** FOSDEM favors "promoting collaboration and community between different projects in niches which don't normally have their own spaces, rather than large projects with significant corporate backing", citing recent examples like Modern Email, Package Management, and Music Production.
- **Cross-project collaboration.** Proposals spanning project or domain boundaries are "strongly encouraged", and past years included combined rooms and cross-domain themes.
- **New proposals are welcome.** Rooms that exist one year are not guaranteed the next, and previously rejected rooms are still encouraged to apply ("If you submitted a proposal for a devroom in the last few years and got rejected, don't be disheartened and submit anyway!").
- **Two (or more) named managers.** Proposals need at least two named people responsible for the room, in case one is unavailable on the day.
- **Half-a-day rooms are fine.** A room that cannot fill a full day can apply for half a day — ideally jointly with another project, or asking FOSDEM to pair it with a similar half-day request.

The Rust devroom's history shows the upside of resilience: their first dedicated-room attempt in 2016 was rejected, so they ran a Birds-of-a-feather (BoF) session instead; its growing attendance (25+ people in 2016, 60+ in 2017) convinced them to reapply, and the Rust devroom has run every year since 2018, except 2021 ([Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).

### Selection is competitive, and decisions are not explained

Room proposals outnumber spaces by a lot: FOSDEM received 125 proposals for 70 rooms for 2025, and "the hard decisions are which good proposals to reject" ([comment](https://www.percona.com/blog/in-search-of-transparency-at-fosdem/#comment-23360) by FOSDEM program team member Johan Van de Wauw). One room's rejection caused public reflection on transparency ([Percona](https://www.percona.com/blog/in-search-of-transparency-at-fosdem/)), but the silver lining is that decisions are not punishment: rooms have come back the following year, and a project can always contribute talks to other related devrooms, BoFs, or the Fringe ([Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).

### How successful proposals came together

Recurring patterns in organizers' accounts:

- Build the organizing team from several projects or organizations: the first Robotics and Simulation devroom was proposed by one person, then run by a five-person team drawn from different companies and communities ([Robotics and Simulation](https://msadowski.github.io/Roboticist-visits-fosdem-2025/)).
- Choose a devroom when the topic has real communities but no home: the Wikimedia Performance Team organized a Web Performance devroom to cover underrepresented topics for which a standalone conference would have been too much logistics ([Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)).
- If a dedicated room seems out of reach, grow the topic through BoF sessions first and apply once attendance shows demand — the Rust devroom followed exactly that path ([Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).

## Milestones for a FOSDEM 2027 devroom

Key dates from the [FOSDEM 2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/), published on 7 September 2026:

| Date                         | Milestone                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 7 September 2026             | Call for devroom proposals published; [proposal form](https://pretalx.fosdem.org/fosdem-2027-call-for-devrooms/cfp) opens |
| 4 October 2026               | Deadline for devroom proposals                                                                                            |
| 20 October 2026              | Accepted devrooms announced                                                                                               |
| 27 October 2026 (or earlier) | Devrooms issue their calls for participation (CfP)                                                                        |
| 7 December 2026 (or earlier) | Complete devroom schedules published                                                                                      |
| 30–31 January 2027           | FOSDEM 2027; devrooms run                                                                                                 |

### Before submitting (now through 4 October 2026)

- [Decide the pitch](#what-fosdem-is-looking-for-in-devroom-proposals): audience, community (real projects and people, not one company), cross-project reach. If you cannot fill a full day, join forces with another project or request a half-day room ([2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/)).
- [Recruit a co-manager](#how-successful-proposals-came-together): every proposal needs two named managers ([2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/)).
- Submit through the [FOSDEM 2027 devroom proposal form](https://pretalx.fosdem.org/fosdem-2027-call-for-devrooms/cfp) (entries close 2026-10-04 00:00 UTC). [Questions and proposal help](mailto:program@fosdem.org) go to <program@fosdem.org>.
- Plan for selection odds in the [selection realities](#selection-is-competitive-and-decisions-are-not-explained): about 55 of 125 room proposals were rejected for 2025, so sketch a plan B ([Fringe event](https://fosdem.org/2026/fringe/), a BoF, a [stand](https://fosdem.org/2027/news/call-for-stands/), or joining a related devroom) ([Percona comment](https://www.percona.com/blog/in-search-of-transparency-at-fosdem/#comment-23360), [Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).

### After acceptance (late October 2026)

Once rooms are announced, FOSDEM contacts managers through a closed mailing list and per-room email aliases; the precise mechanics (also in Pretalx) are documented for reference in the [2026 managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/), and FOSDEM's 2027 edition will update them:

- Send the list of manager and reviewer email addresses to <devrooms@fosdem.org>; managers with full access get talk review, scheduling, video control on the day, and video review afterwards. Every room keeps **two managers** on this list.
- Watch the FOSDEM `devroom-manager` mailing list closely — that is where logistics mail lands, and it is the official channel for announcements; per-room aliases are add-ons for cross-room talk moves.
- Send your CfP to the main [FOSDEM mailing list](https://lists.fosdem.org/listinfo/fosdem) (moderated, so allow a day), in line with the 27 October milestone; publish your CfP and (optionally) a dedicated devroom website like the [Python 2026](https://gist.github.com/malemburg/4f2d1ceeb24d26c35740390cf712af5e) and [Railways and Open Transport 2026](https://github.com/OpenRailAssociation/FOSDEM/blob/main/2026-cfp.md) examples did.
- Ask <devrooms@fosdem.org> for an optional devroom mailing list if your organization team or audience is bigger than two people.

### Running the call for participation (late October to mid-November 2026)

- Announce early (27 October is the coordinated date from the [call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/)); earlier is fine.
- Set a submission deadline that leaves room for review plus schedule work: the 2026 Python devroom used 1 December with the schedule on 15 December ([Python 2026 CfP](https://gist.github.com/malemburg/4f2d1ceeb24d26c35740390cf712af5e)); Railways and Open Transport used 7 December and 15 December ([OpenRail 2026 CfP](https://github.com/OpenRailAssociation/FOSDEM/blob/main/2026-cfp.md)).
- Most proposals are submitted during this window; you can expect to reject a sizable share ([Rust devroom](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)). In the CfP, be explicit about what is in and out of scope, the on-site requirement, and the recording licence — both example CfPs do this ([Python](https://gist.github.com/malemburg/4f2d1ceeb24d26c35740390cf712af5e), [OpenRail](https://github.com/OpenRailAssociation/FOSDEM/blob/main/2026-cfp.md)).
- Use Pretalx for submissions, reviews, and accept/reject mail; the organizer workflow is covered in the [2026 managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/). Decide early who reviews (managers, plus an optional invited reviewer team) and close your CfP by switching on its access code when you are done.
- Ask accepted speakers to confirm attendance; reject-but-suggest is a good fallback for strong proposals that do not fit ([Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).

### Building the schedule (late November to 7 December 2026)

- Enter **all** accepted talks and speaker details into Pretalx; the FOSDEM website, schedules, and video metadata are generated from it. Being early avoids the December crunch, when people are hard to reach ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)).
- Respect the [2027 room constraints](https://fosdem.org/2027/news/call-for-devrooms/): Saturday rooms run 7.5–8.5 hours of content from **10:30** (ending 18:00–19:00), Sunday rooms run 7–8 hours from **09:00–10:00** (ending 17:00), with **no lunch breaks** in devroom schedules.
- Coordinate changeover times with neighboring/related devrooms when possible; keep small buffers rather than rigidly packed schedules ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)).
- Use Pretalx's schedule validation ("Check") so your released schedule is error-free: errors block schedule releases ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)).
- Chase speaker confirmations early: only confirmed talks appear on the website, and people go offline in late December ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)).

### Logistics and preparation (December 2026 – January 2027)

- Prepare for cancellations: keep a couple of reserve talks in Pretalx, chosen from speakers who are attending anyway so they can be swapped in with little effort ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)); require on-site availability in your CfP, since remote presentations are not an option ([OpenRail 2026 CfP](https://github.com/OpenRailAssociation/FOSDEM/blob/main/2026-cfp.md), [Python 2026 CfP](https://gist.github.com/malemburg/4f2d1ceeb24d26c35740390cf712af5e)).
- For the room: plan staffing for at least **three to four organizers on the day** — Wikimedia's minimum for a well-run room is one moderator/timekeeper, one camera/stream operator, one crowd/door manager, and someone on photos/social; 500+-seat rooms also need queue management ([Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/), [Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).
- Read the manual before the event, not during: the [2026 managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/) covers the video workflow, the on-day Matrix rooms for devroom managers, and emergency contact protocols. Have someone on your team own each role explicitly.
- Monitor capacity: rooms fill up, and FOSDEM enforces room limits for safety — the Quantum devroom had to turn people away ([Unitary Foundation](https://unitary.foundation/posts/2025_fosdem_recap/)), and the manual asks rooms to place somebody at the door with "full" signs when there is a risk of overcrowding ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)). A bigger room is not guaranteed, so promote your livestream link in community channels ahead of the event ([Unitary Foundation](https://unitary.foundation/posts/2025_fosdem_recap/)).
- Organizers usually pick up **blue devroom shirts** at the event, which identify you to attendees, volunteers, and video staff; get there with time to spare ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/), [Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)).

### During the event (30–31 January 2027)

- Arrive before your first talk to test A/V: speakers' laptops on the room's HDMI input and microphones fitted and switched on; adapters are available from the room or building video team ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/)).
- Have a run-of-show plan: talk order, speaker names, timings, and who introduces what. FOSDEM's video staff are shared across the floor rather than dedicated to your room, so video adjustments go through chat and someone should keep an eye on the camera ([Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)).
- Track timekeeping, room overflow, and the stream/camera; keep one person on each ([Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)).
- Expect last-minute cancellations even in well-run rooms; have a plan to shuffle or fill gaps rather than leaving holes ([PowerDNS](https://blog.powerdns.com/fosdem-2025-a-look-back-at-the-dns-devroom)).
- Meet your speakers before their talks, even briefly — the Quantum organizers met most of theirs five minutes before their slot and wished they had arranged something earlier ([Unitary Foundation](https://unitary.foundation/posts/2025_fosdem_recap/)).

### After the event

- Review your speakers' videos promptly at [review.video.fosdem.org](https://review.video.fosdem.org): speakers receive review links with devroom managers CC'd. Video production is fast — same-day videos were already landing while the Wikimedia devroom was still running ([managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/), [Wikimedia](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/)).
- Recap attendance, talk counts, and feedback for your community's next edition: rooms are never guaranteed a slot, and prior successes help the next proposal ([2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/), [Rust Foundation](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/)).
- Write a retrospective like the ones linked below: first-time organizers consistently report they were glad they did ([Unitary Foundation](https://unitary.foundation/posts/2025_fosdem_recap/), [Robotics](https://msadowski.github.io/Roboticist-visits-fosdem-2025/)).

## Sources

### Official FOSDEM documentation

- [FOSDEM 2027 news](https://fosdem.org/2027/news/) — FOSDEM 2027 date and venue announcement (30–31 January 2027, ULB Solbosch campus), plus the devroom and stands calls.
- [FOSDEM 2027 call for devrooms](https://fosdem.org/2027/news/call-for-devrooms/) — primary 2027 source: requirements, room rules, and dates.
- [2026 devroom managers manual](https://archive.fosdem.org/2026/manuals/program/devroom/) ([source](https://raw.githubusercontent.com/FOSDEM/website/master/content/manuals/program/devroom.md)) — communication channels, Pretalx workflow, scheduling hints, on-the-day and video-review duties.
- [FOSDEM 2024 devrooms announcement](https://archive.fosdem.org/2024/news/2023-11-08-devrooms-announced/) — a recent edition of the same announcement, useful for comparing timelines across years.
- [FOSDEM submit](https://fosdem.org/submit) — the Pretalx portal that talk submissions go through (the 2027 devroom proposal form is [separate](https://pretalx.fosdem.org/fosdem-2027-call-for-devrooms/cfp)).
- [FOSDEM code of conduct](https://fosdem.org/2027/practical/conduct/) — link it from your CfP.
- [FOSDEM fringe](https://fosdem.org/2026/fringe/) — the community-run event option around FOSDEM, for a plan B.

### Example calls for participation

- [Python devroom 2026 CfP](https://gist.github.com/malemburg/4f2d1ceeb24d26c35740390cf712af5e) — a compact, complete CfP example with timelines, topics, and logistics.
- [Railways and Open Transport devroom 2026 CfP](https://github.com/OpenRailAssociation/FOSDEM/blob/main/2026-cfp.md) — an example of a niche room with clear scope and submission process.

### Organizer retrospectives

- [Organizing and running a developer room at FOSDEM](https://diff.wikimedia.org/2020/04/27/organizing-and-running-a-developer-room-at-fosdem/) (2020) — the most detailed first-person account, incl. staffing levels, video workflow, and speaker logistics.
- [Lessons from organizing our first FOSDEM devroom](https://unitary.foundation/posts/2025_fosdem_recap/) (2025) — first-time lessons: scheduling gaps, livestream promotion, room overflow, speaker welfare.
- [FOSDEM 2025: A look back at the DNS devroom](https://blog.powerdns.com/fosdem-2025-a-look-back-at-the-dns-devroom) (2025) — a mature devroom's program recap, including last-minute cancellations.
- [A roboticist visits FOSDEM 2025](https://msadowski.github.io/Roboticist-visits-fosdem-2025/) (2025) — more participant tips than organizer advice, but useful for proposals.
- [FOSDEM 2026: Rust devroom in review](https://rustfoundation.org/media/guest-blog-fosdem-2026-rust-devroom-in-review/) (2026) — recurring devroom from the organizers' side: BoF-to-devroom path, rejection rates, room capacity.

### Community accountability

- [In search of transparency at FOSDEM](https://www.percona.com/blog/in-search-of-transparency-at-fosdem/) (2024) — devroom selection controversies; see the comments for how FOSDEM's program team weighs incoming proposals.
