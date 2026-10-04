# DjangoCon Europe 2026 talks

Collected from the official DjangoCon Europe 2026 schedule via its Pretalx frab JSON export: <https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json> (schedule version **1.4**, fetched 2026-09-20). The schedule page is at <https://2026.djangocon.eu/schedule/>. The conference ran 2026-04-15 to 2026-04-17, 2026, in Vilnius. All 30 scheduled slots (talks, keynotes, and workshops) are included; the export contains no break or registration placeholders.

Every talk record carries its canonical Pretalx talk URL and the export as source. Speaker names come from the export's person records; profile URLs are included where the export provides them (verified live for a sample).

Machine-readable version of this data: [`talks.json`](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/2026-python-events/djangocon-europe-2026/talks.json) in this directory.

## Talks

## 1. [Static Islands, Dynamic Sea](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/WH9A7C/)

**Speakers**: [Carlton Gibson](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/JHNLPQ/)

**When and where**: Wednesday, 2026-04-15, 10:00–10:55, room AMPHITHEATRE

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Python's dynamic nature is a feature, not a bug! Sometimes we want type safety too. Let's look at building "static islands" around Django's dynamic core. Type-safety where you need it, without sacrificing the flexibility of Python that you know and love.

**Description** (verbatim):

Python's dynamic nature isn't a bug—it's a feature. Django leveraged this from
the start, building elegant APIs that would be impossible in a rigidly typed
system. Duck typing, runtime introspection, and flexible interfaces gave us the
expressiveness we grew up with.

But sometimes we want more. Type safety at API boundaries. Auto-completion that
actually works. Data classes instead of ORM objects. The confidence that comes
with catching errors before runtime.

The answer isn't to abandon Python's dynamic core—it's to build static islands
where they help. Incremental typing lets us wrap specific layers (like the ORM)
in type-safe interfaces while leaving Django's liquid core untouched.

This talk explores when, why, and how to add these type-safe layers, and
demonstrates Mantle, utilities for typing around Django's liquid core. We'll
keep the Python you love, with those little extras when you need them.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/WH9A7C/>

## 2. [Oh, I Found a Security Issue](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/ZY8UHF/)

**Speakers**: [Markus Holtermann](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/BWWWMK/)

**When and where**: Wednesday, 2026-04-15, 11:00–11:30, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Ever thought about what happens when someone finds a security issue in Django? How do you disclose an issue responsibly? What happens after that? How does the Django team work on it? What happens until a security release is published? What comes afterward? And what impact have AI and LLMs on Django and its security?

**Description** (verbatim):

This talk is your behind the scenes guide to Django's best in class security processes. I’ll give an introduction to how the team handles security issues: the triaging, fixing, disclosure process, and releases.

I will then review the history of Django’s security issues to identify hotspots and areas to look out for. Lastly, I will explore the impact of AI and LLMs on the security of Django as well as its security team.

The talk will give you everything you need, to help you interact with Django’s security team when needed, and show how Django's security process can act as an example for other open source projects.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/ZY8UHF/>

## 3. [ATLAS: Building a Zero‑Budget IT Service Management Platform with Django in the Public Sector](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/ZQE3GP/)

**Speakers**: [Georgios Poulos](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/3EUCPF/)

**When and where**: Wednesday, 2026-04-15, 12:00–12:30, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

ATLAS is a production-grade IT Service Management platform built with Django for the Greek Ministry of Migration and Asylum. Designed and deployed with zero external budget, it centralizes IT requests into a workflow-driven system with Single Sign-On, role-based access control, automation, SLA monitoring, and real-time analytics. The system is used daily across the Ministry and has resulted in 70% faster incident response initiation and 98% user satisfaction.

**Description** (verbatim):

This talk presents ATLAS, a real-world Django application built and operated in the public sector under strict governance, security, and resource constraints.

The session starts by outlining the organizational challenges of handling IT service requests at scale and why traditional email-based workflows failed. It then dives into the system’s architecture, focusing on workflow-driven design, authentication and authorization strategies, automation with SLA tracking, and observability through metrics and dashboards. The SLA model does not only enforce operational discipline but is also aligned with the organization’s official performance objectives, enabling IT teams to track compliance against organizational targets and support data-driven decision-making.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/ZQE3GP/>

## 4. [AI-Assisted Contributions and Maintainer Load](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/X9APYZ/)

**Speakers**: [Paolo Melchiorre](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/BVRQXW/)

**When and where**: Wednesday, 2026-04-15, 12:35–13:05, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

AI-assisted contributions are changing how open source work happens.
This talk looks at real maintainer experiences from projects like **Django**, Python, GNOME, and OCaml, focusing on review load, responsibility, and the governance questions that appear when AI replaces understanding instead of supporting it.

**Description** (verbatim):

**AI tools** are increasingly used by contributors to _read code_, explore codebases, and generate changes. In many open source projects, this is already changing how issues are opened and how pull requests are submitted. While AI can help people get started, it also creates new challenges for maintainers.

This talk is based on _real discussions and concrete examples_ from the open source community. Maintainers in projects such as **Django**, Python, GNOME, and OCaml report similar patterns: large or unnecessary AI-generated changes, missing design discussion, references to _non-existent APIs_, and contributions that are technically correct but hard to review and maintain. In many cases, work is moved from contributors to already time-limited maintainers.

The focus of this talk is not on banning or promoting AI. The shared concern across these communities is **responsibility**. Problems appear when AI replaces _understanding_, _testing_, and _human accountability_, breaking the social processes that open source depends on.

The talk also looks at how projects are responding. Some add documentation, disclosure rules, or review guidelines. Others start wider discussions about _governance_, _sustainability_, and _legal risk_. These responses show that the issue goes beyond individual pull requests.

Instead of giving simple answers, this talk shares the **real questions** the community is asking today, and helps contributors and maintainers think more clearly about the future role of AI in Django and open source projects.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/X9APYZ/>

## 5. [Reliable Django Signals](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/3LKHFS/)

**Speakers**: [Haki Benita](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/8QRVC3/)

**When and where**: Wednesday, 2026-04-15, 14:40–15:10, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

The existing implementation of Django Signals does not address fault tolerance in any way, which makes Signals unreliable for mission critical workflows! In this talk I present an alternative underlying implementation using the new tasks framework in Django 6 which makes Signals fault tolerant and reliable.

**Description** (verbatim):

Django signals are extremely useful for decoupling modules and implementing complicated workflows. However, the underlying transport for Django Signals makes them unreliable and subject to unexpected failures.

In the talk I demonstrate several strategies for decoupling modules, including Django Signals, and discuss different aspects such as user experience and fault tolerance.

Finally, I present an alternative underlying transport implementation for Django Signals using the new tasks framework in Django 6 that addresses the shortcomings of all other approaches. The alternative implementation makes Django Signals reliable for mission critical workflow and for applications that require high reliability and fault tolerance.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/3LKHFS/>

## 6. [Django forms in the age of HTMx: the single field form](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/ZLRWH9/)

**Speakers**: [Hanne Moa](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/ZJAQE7/)

**When and where**: Wednesday, 2026-04-15, 15:15–15:45, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

There are many ways to do "interesting" things with forms...

With HTMx it is possible to treat any HTML tag as a form, without using form tags. It becomes easy to alter just one field of a form: click on the field to swap out the presentation with a suitable input field, then submit that single field on pressing Enter.

What is not necessarily so easy is adapting the use of Django's forms so that they are used both for validation and rendering of that single field, and smuggling in the necessary context a form widget needs if one skips the &lt;form&gt;-tag and uses widget templates to render the inputs.

Incidentally it does become easy to have plugin-able forms...

This talk will briefly look at previous "interesting" (ab)uses of Django forms, followed by demonstrating some hands-on techniques and patterns for working with single fields, using a special made demonstration site and a production service that was converted in 2024-2025 from a SPA using REACT to an MPA using HTMx: Argus.

Django: https://docs.djangoproject.com/
HTMx: https://htmx.org
Live Argus demo: https://argus-demo.uninett.no/
Argus code: https://github.com/Uninett/Argus
Code for singlefield demo: https://github.com/Uninett/singlefieldform
Slides: https://github.com/Uninett/singlefieldform/tree/main/slides

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/ZLRWH9/>

## 7. [Scaling the database - using multiple databases with Django](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/MSJQLT/)

**Speakers**: [Jake Howard](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/CQZJUD/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

The question is simple: How do you scale Django beyond a single database? The answer isn't simple, but it _is_ fun and interesting.

**Description** (verbatim):

As your Django application gets popular, you'll need to scale up. Maybe you need to run more web workers, more CPU cores, or even spread across more servers. This works great, up to a point.

Your database is likely at the core of your application, but whilst it's easy to throw more resources at a database, it's much harder to scale to multiple. After a while, you'll outgrow a single database. Maybe performance isn't the issue, and instead you need the rock-solid reliability which can only come from multiple database servers.

Django supports multiple database connections, but leaves it up to you to manage how to use them and which queries to send where. But, how? How do you split your data between multiple databases? How do you tell Django which to use when? If your infrastructure already has replicas, how can you use them effectively.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/MSJQLT/>

## 8. [Partitioning very large tables with Django and PostgreSQL](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/YPQ8YK/)

**Speakers**: [Tim Bell](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/SKMQND/)

**When and where**: Wednesday, 2026-04-15, 16:50–17:20, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Database tables in PostgreSQL cause increasing performance and maintenance issues as they grow larger. We look at ways of managing those problems with partitioning, the choices available, and how to partition existing tables at Kraken scale with Django.

**Description** (verbatim):

## Introduction

Database systems like PostgreSQL provide a useful layer of abstraction: you can store and retrieve data using SQL (via the Django ORM) without having to worry about how the database manages the data under the hood. Database indexes enable fast queries, and automatic vacuuming cleans up old row versions and deleted rows. But as tables become extremely large, the abstraction starts to break down, and performance issues become apparent. In this talk, I'll describe what options are available (including partitioning) to manage large database tables, and how we're approaching this problem at Kraken Tech.

## The problem

At Kraken Tech, one of our installations of Kraken has a table with about 9 billion rows and is about 3 TB in size. This table takes around 20 hours to vacuum, and it requires vacuuming about once a day. During a recent bigint conversion project (see my talk from DjangoCon Europe 2025), this long and frequent vacuuming interfered with the other maintenance work we were doing on the table. We'd like to reduce the time taken to vacuum; other performance improvements would also be welcome. We'd also like the solution we adopt to be generally applicable to other large tables.

One approach would be to delete old data from the table and store it in another storage system instead (such as S3). However, that would also require application-level changes to enable access to the old data, and those changes wouldn't necessarily generalise to other tables.

Another approach would be to start with a brand new table for all new data. The new table will be fast (until it grows to the size of the old table), and the old table will stop needing to be vacuumed once no more writes to it are needed. This approach will also require application-level changes to access both databases, and will only defer the problem, not solve it.

A third approach is to partition the table using PostgreSQL's native support for partitioning. Partitioning splits a large table into a number of smaller tables, with each row being assigned to one of the partitions depending on the value of its partition key. These smaller tables have their own indexes and are vacuumed separately as needed, which will address the problem of slow vacuuming. And accessing a partitioned table is transparent to the application, mostly.

## Requirements, choices and compromises

PostgreSQL supports different types of partitioning: range, list and hash; that's one choice we need to make. Another choice is how many partitions will be used, and when to add new ones.

But the biggest choice, and the one with the most requirements and consequences, is which column(s) to use for the partition key. There usually will be a compromise here, since the partition key that offers the most performance improvement will often not support desired constraints. And Django imposes its own requirements that affect the choice of partition key.

## Partitioning existing tables

For our use case at Kraken Tech, we would like to partition existing tables without imposing any system downtime. The PostgreSQL extension `pg_partman` provides support for "online" partitioning that enables this, but via manual processes that don't scale across the large number of installed systems we support. We have developed a Python package `psycopack` for replicating PostgreSQL tables and performing schema changes in the process; we are working on enhancing that tool to support partitioning as well.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/YPQ8YK/>

## 9. [Django from the trenches: Advanced Indexing and Concurrency in Django and PostgreSQL](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/KYPGJ8/)

**Speakers**: [Haki Benita](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/8QRVC3/)

**When and where**: Wednesday, 2026-04-15, 11:00–12:30, room NEW STAGE

**Type**: Long Workshop — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Building applications to serve actual users is really hard! Traffic spike, data accumulates, queries becomes slow, response time suffer and you sre left completely baffled!

In this workshop we'll optimize real-life scenarios in a Django application using advanced indexing techniques in PostgreSQL. We will also identify and tackle concurrency issues and experiment with different approaches to prevent them, without bringing the system to a halt.

By the end of this workshop you'll learn how to prepare your Django application for the real life.

**Description** (verbatim):

Building applications to serve actual users is really hard! Traffic spike, data accumulates, queries becomes slow, response time suffer and you sre left completely baffled!

In this workshop we'll optimize real-life scenarios in a Django application using advanced indexing techniques in PostgreSQL. We will also identify and tackle concurrency issues and experiment with different approaches to prevent them, without bringing the system to a halt.

By the end of this workshop you'll learn how to prepare your Django application for the real life.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/KYPGJ8/>

## 10. [llms.txt and Django](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/DDP7TX/)

**Speakers**: [Thibaud Colas](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/Y8QPW8/)

**When and where**: Wednesday, 2026-04-15, 15:15–16:45, room NEW STAGE

**Type**: Long Workshop — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

The llms.txt format is an emerging standard to structure information for Large Language Models. It’s a desirable addition to the docs of Python packages.

Let’s review how to adopt it! We’ll discuss the fundamentals of the format and its benefits as a user of the docs, and as a maintainer. How to produce and consume those files across different tools (Sphinx, mkdocs, Django). How to optimize them for different LLMs with an eval suite. Tools and techniques you should be able to reuse through other engineering tasks with LLMs.

**Description** (verbatim):

The llms.txt format is an emerging standard to structure information for Large Language Models. It’s a desirable addition to the docs of Python packages. We have been [busy adopting it for Wagtail](https://wagtail.org/blog/llmstxt-preparing-wagtail-docs-for-ai-tools/), and can now share how it all went.

Let’s review how to adopt it! We’ll discuss the fundamentals of the format and its benefits as a user of the docs, and as a maintainer. How to produce and consume those files across different tools (Sphinx, mkdocs, Django). How to optimize them for different LLMs with an eval suite. Tools and techniques you should be able to reuse through other engineering tasks with LLMs.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/DDP7TX/>

## 11. [A Practical Guide To Agentic Coding For Django Developers](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/3BGDDQ/)

**Speakers**: [Marlene Mhangami](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/MSY7X7/)

**When and where**: Thursday, 2026-04-16, 09:30–10:25, room AMPHITHEATRE

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

AI Agents have become increasingly good at generating code. Developers who know how to use agentic tools as they program can increase their productivity significantly. In this talk, Marlene will share how Django Developers can get the most out of coding agents in their development workflows. She'll walk through how she uses MCP (Model Context Protocol), Agent Skills and Instructions to create semi-autonomous agents that can complete multi-step tasks end-to-end. She'll also walk through best practices for validating the output of agents end to end with unit tests and Playwright. As part of this talk we'll also discuss the societal implications of AI on developers and how we can best prepare for the future thats both coming and already here.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/3BGDDQ/>

## 12. [Digitising Historical Caving Data with Python and Django](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/9GZGLP/)

**Speakers**: [Andrew Northall](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/GJUXR3/)

**When and where**: Thursday, 2026-04-16, 10:30–11:00, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

A pipeline using Python, Django, and LLMs to extract, structure and publish 2,700 incidents, turning old typewritten documents into useful data.

**Description** (verbatim):

Endless quantities of old but critically important data is trapped in paper journals and reports across the world. Is it possible to extract this data and make it available to the masses, even when the data is highly specialised and of poor quality? That is what I did for reports of caving incidents and accidents dating back 50 years.

The National Speleological Society has published American Caving Accidents since 1967, documenting thousands of incidents, and despite being freely available as PDFs, these are unindexed, poorly scanned, and basically impossible to use as a learning tool.

In this talk, I'll show you how I built a system that programmatically processed these documents into a structured, publicly searchable database. You'll see the full pipeline: how to OCR degraded/low quality documents, custom code to untangle multi-column layouts, and LLM processing stages to extract and format the data whilst maintaining 100% accuracy.

I'll cover some of the more unusual challenges: handling dates like "Autumn 1996" with a custom model field, building a pluggable processing step system in Django, and how to intake and normalise large quantities of low quality data in a relational database.

Have you ever looked at a stack of old documents and thought: "there's valuable data in here, if only someone could extract it"? This talk is about what happens when you actually try.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/9GZGLP/>

## 13. [Beyond print(): Observability to debug you Django apps](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/DLX7N7/)

**Speakers**: [Laís Carvalho](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/L9XBYZ/)

**When and where**: Thursday, 2026-04-16, 11:05–11:35, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Most Django developers have been there: something is slow, users are complaining, and the first instinct is to sprinkle `print()` statements or scroll through server logs hoping for a clue. Without proper observability, diagnosing performance bottlenecks in a Django application (or any application, for that matter) is guesswork.
Observability is the practice of understanding what is happening inside your application by looking at the signals it produces: traces, metrics, and logs. While the concept is well-established in infrastructure and DevOps circles, it remains under-explored in the day-to-day workflow of many Django developers. Yet Django's middleware architecture, ORM, and request/response cycle make it particularly well-suited for instrumentation.

In this talk, I will walk through how to add observability to a Django app using Pydantic Logfire. I'll cover the **Four Golden Signals of observability** (latency, traffic, errors, and saturation), explain why they matter for your Django app, and show how to expose them with minimal setup. Through a live demo, you will see how to use metrics dashboards in action to monitor your system. You'll also see how to leverage AI to query your logs and traces in natural language or with SQL.
Attendees will leave this talk with a practical, reproducible workflow for adding observability to their own Django projects, along with an understanding of which signals to monitor and why.

Prerequisites: Attendees should be comfortable with Django basics. No prior experience with observability tooling is required.
Outline breakdown:

- 0–3 min **The problem**: Why print() and log scrolling don’t scale.
- 3–7 min **Observability 101 for Django developers**: The Four Golden Signals (latency, traffic, errors, saturation) explained with Django-specific examples.
- 7–12 min **Setting up Observability - Instrumenting observability in a Django project**: logging handler, Django instrumentation, PostgreSQL instrumentation. Live demo: showing traces appearing in the Live view.
- 12–19 min **Built-in dashboards and system metrics**: Enabling system metrics. Walkthrough of System Metrics dashboard. Mapping charts to the Golden Signals (CPU → saturation, process count → traffic). Building custom error charts with SQL queries. Live demo.
- 19–23 min **Putting it all together**: How to think about what to monitor. Practical tips for setting thresholds and correlating signals across dashboards.
- 23–25 min Wrap-up: Summary, resources, and where to go next.
- 25-30 min: Q&A

**Description** (verbatim):

Most Django developers have been there: something is slow, users are complaining, and the first instinct is to sprinkle `print()` statements or scroll through server logs hoping for a clue. Without proper observability, diagnosing performance bottlenecks in a Django application (or any application, for that matter) is guesswork.
Observability is the practice of understanding what is happening inside your application by looking at the signals it produces: traces, metrics, and logs. While the concept is well-established in infrastructure and DevOps circles, it remains under-explored in the day-to-day workflow of many Django developers. Yet Django's middleware architecture, ORM, and request/response cycle make it particularly well-suited for instrumentation.

In this talk, I will walk through how to add observability to a Django app. I'll cover the **Four Golden Signals of observability** (latency, traffic, errors, and saturation), explain why they matter for your Django app, and show how to expose them with minimal setup. Through a live demo, you will see how to use observability standards to monitor your system. You'll also see how to leverage AI to query your logs and traces in natural language or with SQL.
Attendees will leave this talk with a practical, reproducible workflow for adding observability to their own Django projects, along with an understanding of which signals to monitor and why.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/DLX7N7/>

## 14. [Role-based access control in Django - How we forked Guardian](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/D3X8M9/)

**Speakers**: [Gergő Simonyi](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/TDJ7A8/)

**When and where**: Thursday, 2026-04-16, 12:05–12:35, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Django's built-in access control system is very good for basic operations and Guardian is a natural extension to the object level. However, our customers wanted more: a group hierarchy, just-in-time privileged access, delegating permissions to other users, custom permissions. This talk tells the story of how an authentication company built a role-based authorization system for Django.

**Description** (verbatim):

Django's built-in access control system is very good for basic operations and Guardian is a natural extension to the object level. However, our customers wanted more: a group hierarchy, just-in-time privileged access, delegating permissions to other users, custom permissions. This talk tells the story of how an authentication company built a role-based authorization system for Django.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/D3X8M9/>

## 15. [Is it time for a Django Admin rewrite? If so, how?](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/WUZSPX/)

**Speakers**: [Emma Delescolle](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/XREAEA/)

**When and where**: Thursday, 2026-04-16, 12:40–13:10, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Django's built-in admin is powerful, but it's essentially a separate framework within Django and it's 20 years old.

Wouldn't it be nice to be able to work with an admin interface that works like the rest of Django, built on generic views, plugins, and view factories? This is the idea I explored: a proof-of-concept Django admin replacement, powered by pluggy and generic views, where CRUD operations are just actions, knowledge transfers both ways, and everything feels like Django.

Let's explore together the concepts and ideas behind it.

**Description** (verbatim):

What if customizing Django's admin felt like writing any other Django view? Not just a cosmetic refresh, but a radically new approach relying on Django itself, factory-generated views and with a plugin-first design.

Talk Structure:

1. The Problem Space (5 min)
   - Django admin's 20-year legacy: what it got right and where it shows its age
   - The extension dilemma: 3rd-party ecosystem and collisions between extensions
   - Developer experience gap: different patterns for regular Django vs. admin
   - Community feedback: recurring requests that would be hard to implement
2. Architectural Foundations (7 min)
   - View Factories: How views get generated dynamically
   - Action System: Actions are the recipes followed by view factories
   - Plugin Hooks: djp/pluggy integration and hook patterns
   - Out-of-the-box enhancements
3. Examples & Demo (8 min)
   - Starting with familiar API: @register(Product) and list_display
   - Customizing `list_display`
   - Customizing `layout`
   - Creating your own plugins
   - Testing tools: `BaseCRUDTestCase`
   - Demo (pre-recorded)
4. Migration & Adoption (4 min)
   - Running side-by-side with existing admin
   - Early adopters (well-know projects that already have plugins)
   - Extension compatibility matrix: no-effort, medium-effort, hard cases
5. The Path Forward (2 min)
   - What's next: roadmap and timeline
   - Other potential benefits mid-term
   - Call to action

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/WUZSPX/>

## 16. [Django Task Workers in Subinterpreters: Single-Server Django Applications Without Process Overhead](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/BC3BJY/)

**Speakers**: [Melhin Ahammad](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/PSQY8D/)

**When and where**: Thursday, 2026-04-16, 14:40–15:10, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Deploying Django with background tasks usually means juggling Celery, Redis, and separate worker processes which often mean adding complexity and operational overhead.

What if you could run everything in a single process while keeping isolation and performance?

**Description** (verbatim):

Deploying Django applications with background tasks typically requires managing multiple processes and queues. But what if you could run everything in a single process without sacrificing isolation or performance?

This talk shows how Python 3.14's `subinterpreters` enable a practical pattern for self-contained Django applications:

**The Pattern**:

- Web server and task workers run in separate subinterpreters within one process
- True isolation prevents memory leaks and state contamination between components
- Simplified deployment: one process, one server, one application

**What This Solves:**

- **Deployment simplicity**: No separate worker processes, no queue infrastructure
- **Resource efficiency**: Shared memory space with isolated execution
- **Self-contained applications**: Perfect for internal tools, small services, or edge deployments

**We'll walk through code showing:**

- Setting up Django web server and task workers in InterpreterPoolExecutor
- Inter-interpreter communication using shared queues between webserver and task worker
- We will also look at a version using PostgreSQL as a backend and how to run tasks
- Running CPU-intensive tasks (image processing, PDF parsing) without blocking web responses
- Gotchas and errors that occur, how to monitor them, and how to build in a mechanism for recovery
- **Error recovery mechanisms**:
  - Worker subinterpreter crash detection and automatic restart
  - Graceful shutdown handling for in-flight tasks

**We will also discuss:**

- Limited third-party library support
- Difficulties in exception handling and retry mechanisms

This is a practical pattern for real Django applications that need background processing without the complexity of traditional distributed task queues. You'll leave with concrete examples you can adapt for your own single-server Django deployments.

**Target audience**: Django developers who deploy their own applications and want simpler background task processing.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/BC3BJY/>

## 17. [When SaaS Is Not Allowed: Shipping Django as a Desktop App](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/UJZX9Z/)

**Speakers**: [Jochen Wersdörfer](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/7AHZEN/)

**When and where**: Thursday, 2026-04-16, 15:15–15:45, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

What if your Django app cannot rely on servers at all? This talk shows how to package Django inside Electron for confidential, offline, compute-heavy workloads, based on Steel-IQ, an open-source steel-industry simulation tool. You will see a production architecture running across macOS, Windows, and Linux, plus practical lessons from building and running it.

**Description** (verbatim):

Some teams face constraints that make standard web deployment impossible: confidential data that must never leave user machines, air-gapped environments, and workloads that are too expensive to run centrally.

This talk presents a production pattern for turning Django into a desktop application by packaging it inside Electron. The case study is Steel-IQ, an open-source steel-industry simulation tool for multi-decade decarbonization scenarios, shipped for local execution with sensitive data.

Structure (30 minutes):

1. Why this architecture exists: confidentiality, offline environments, heavy compute.
2. System design: Electron + Django + django-tasks workers + SQLite (including WAL mode).
3. Packaging and distribution: python-build-standalone, uv, installers, and update paths via GitHub Actions.
4. Production failure modes: startup checks, graceful shutdown, orphan process cleanup, migrations, and memory behavior.
5. Demonstration and decision checklist: when this approach is right, and when to choose alternatives.

Audience and level:

- Intermediate to advanced Django developers.
- Useful for teams building internal tools, offline-first products, or applications with strict data constraints.
- No prior Electron experience required.

Attendee takeaways:

1. A reference architecture for embedding Django inside Electron in production.
2. A concrete packaging strategy for standalone Python across platforms.
3. Process-management patterns for reliability and recovery.
4. Operational lessons for long-running local workloads.
5. A decision framework for when desktop-packaged Django is a fit.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/UJZX9Z/>

## 18. [Advanced ORM kung-fu for on-demand filtering, sorting, and summing 40 million financial transactions](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/XLSYHM/)

**Speakers**: [Mathias Wedeken](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/NP83RK/)

**When and where**: Thursday, 2026-04-16, 16:15–16:45, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Fetching some items from the database, creating a grouped list of those items with a bunch of calculations on related items... sounds super-easy in python. Alas, in my use case,it made me include a "please wait while we're generating the data" modal in the frontend.  
That's when I remembered a dear friend saying “Whatever it is you have to do, Postgres can do it, and fast!” Enter the ORM and its deep bag of tricks- chained annotations, subqueries, window functions, conditionals-in-query, digging into JSONB-arrays, and all this with no raw SQL (almost).

**Description** (verbatim):

When the base data is a collection of 40 million postings in a table that grows longer every day, distributed across 472,000 accounts on roughly 5,000 properties; when the use case is filtering, grouping, summing, and sorting these; and when all of this has to happen on-demand for users trying to keep track of what the real-time financial situation of their property is- that's when you realise that using the ORM for mere data access and working the data in Python might not be the ticket. And, when users suddenly want to compare their property to some of the 5,000 others, your Python-first approach will expose the users to a considerable wait which, frankly, can be a bit embarrassing. You don't want to be that guy.
I'm going to talk about how I pushed all this heavy lifting to Postgres using the Django ORM and (almost) no raw SQL - with techniques like chained annotations, window functions for cumulative summing, subqueries with OuterRef, conditional statements in the query, and, for extra fun, digging into JSONB-arrays because hey- there's a json blob describing how all of this data finally has to be sorted. I'll also be touching on the subject of materialized views. The benefits of this approach are not only dramatically better performance (what my friend said...) but also, super-readable and solid code.
If you're a Django developer working with large and growing datasets, or if you're curious how your app can benefit from the performance of Postgres without writing raw SQL, this talk is for you.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/XLSYHM/>

## 19. [How to understand the employer's perspective when you apply for a job](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/8QGZVD/)

**Speakers**: [Daniele Procida](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/FDRCZ3/)

**When and where**: Thursday, 2026-04-16, 11:05–12:35, room NEW STAGE

**Type**: Long Workshop — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

I have hired several dozen people for numerous different roles, I have interviewed hundreds, and reviewed thousands of applications - and I see the avoidable mistakes that are made over and over again. In this workshop I will share the employer's perspective, to help participants do better in their quest for a new role.

**Description** (verbatim):

One of roles at Canonical is hiring lead. Since 2022, I have hired several dozen people for numerous different roles. I have interviewed hundreds, and reviewed thousands of applications.

A candidate's expectations of what they ought to do can be far apart from that of a prospective employer. I have seen hundreds of candidates fare much less well in the process than they should have done, simply because they were not able to understand the process from the employer's perspective.

It _particularly_ harms candidates unfamiliar with the industry, from other cultures, or without personal networks of people who are already industry insiders. They make unnecessary mistakes. They emphasise and focus on the wrong things. They neglect things that could give them real advantage.

It's one of my missions in life to help address that unfairness.

I want to share and explain the employer's perspective, so that applying for jobs becomes less like trying to understand the workings of a black box. I will also show how to approach job applications in ways that help a candidate provide what the employer needs.

This is a hands-on workshop, in which participants will have the chance to revise their own approaches based on insider insights, There will also be plenty of opportunity for questions and discussion of strategy and technique, in writing CVs, submitting applications and taking part in interviews and assessments.

There's a vast amount of bad advice and false information about how to succeed as a job applicant. The perspectives and advice in this session come directly from my own position and experience as someone who assesses, interviews and hires candidates: they are what I wish all the candidates I meet already knew and did.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/8QGZVD/>

## 20. [Django and AI: A Community Conversation](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/S8GYY9/)

**Speakers**: [Laura Gates](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/JUFWZE/), [Thibaud Colas](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/Y8QPW8/)

**When and where**: Thursday, 2026-04-16, 15:15–16:45, room NEW STAGE

**Type**: Long Workshop — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

A facilitated Open Space workshop bringing the Django community together to collectively explore, debate and document the key themes, concerns and opportunities around Django and generative AI – from developer tools to ethics, policy and beyond.

**Description** (verbatim):

The Django community is at a pivotal moment in its relationship with generative AI. From code generation tools reshaping developer workflows to ethical questions about training data and environmental impact, there's no shortage of opinions, but limited space for structured, collective sense-making. This workshop proposes a facilitated Open Space-style discussion that brings the Django community together to surface, explore, and document the key themes, concerns and opportunities around Django and AI. Rather than prescribing answers, we want to harness the room's collective expertise to map the landscape as practitioners experience it.

The session, hosted by Thibaud Colas and Laura Gates, will use a participatory format drawn from Open Space Technology, where attendees propose and lead breakout discussions around the sub-topics that matter most to them – whether that's AI-assisted development, ethical frameworks for Django projects integrating LLMs, the Django Software Foundation's approach to AI policy, or something we haven't anticipated. Thibaud brings deep technical leadership and a long-standing commitment to ethical open-source practice as product lead for the Wagtail CMS, while Laura brings experience facilitating open space and participatory events across academic, charity and corporate settings. Together, we'll synthesise the session's outputs into a documented resource for the wider Django community.

This workshop is for anyone in the Django ecosystem – whether you're enthusiastic about AI, cautious, or still figuring out where you stand. No prior AI expertise is needed; the goal is an inclusive, grounded conversation that reflects the full range of community perspectives and produces something genuinely useful beyond the room.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/S8GYY9/>

## 21. [Body of knowledge](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/AS7ZTU/)

**Speakers**: [Daniele Procida](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/FDRCZ3/)

**When and where**: Friday, 2026-04-17, 09:30–10:25, room AMPHITHEATRE

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

What really makes Django's documentation so good? What's significant about the idea of a handbook? And why does software need to pay attention to the body?

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/AS7ZTU/>

## 22. [Zero-Migration Encryption: Building Drop-in Encrypted Field in Django](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/EGA3KM/)

**Speakers**: [Vjeran Grozdanic](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/SYTSVG/)

**When and where**: Friday, 2026-04-17, 10:30–11:00, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

We built a drop in replacement to many of the standard Django Fields to encrypt the data in our database columns with almost no overhead, and zero database migration.

**Description** (verbatim):

Django doesn't come with a solution to encrypt database data out-of-the-box. While community projects exist, they often require complex migration processes or double-writing to new columns. At Sentry, for our high-traffic distributed system, we needed a solution that would abstract encryption logic without worrying about encryption keys on a case-by-case basis or performing risky migrations on millions of existing entries.

We built EncryptedFields, a custom Field base class that provides drop-in, no database migration, replacements for CharField, JSONField, and TextField. Our approach allows for a "hybrid" state: the field handles both old plain-text formats and the new encrypted format on-the-fly. This eliminated the need for complex data migrations or secondary columns, making the transition safe and seamless for our engineers.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/EGA3KM/>

## 23. [Auto-prefetching with model field fetch modes in Django 6.1](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/DHCJ9P/)

**Speakers**: [Jacob Walls](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/7QDHKK/)

**When and where**: Friday, 2026-04-17, 11:05–11:35, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Configure your models to automatically prefetch related objects when needed with model field fetch modes, new in Django 6.1. This talk will cover usage, tradeoffs, and what distinguishes the "fetch peers" mode from prefetch_related() and select_related().

**Description** (verbatim):

New in Django 6.1, model field fetch modes provide a way to avoid the deluge of queries from accessing un-fetched objects during a loop (also known as the "N+1 queries" problem). You may be familiar with how Django's prefetch_related() and select_related() methods can prevent these queries, but unlike those tools, the "fetch peers" mode does not require maintaining a list of fields to fetch. This can significantly improve project maintenance, especially when QuerySets are constructed at some distance from where they are used.

In this talk, we'll cover what's new about fetch modes, what tradeoffs are entailed, how to configure fetch modes per-model via managers, and how to use the "raise" mode to surface issues in development or put guardrails around performance-intensive sections of code (like the django-seal package).

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/DHCJ9P/>

## 24. [Improving One of Django's Most Used APIs — And It's Not the One You're Thinking Of](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/U3ZMQV/)

**Speakers**: [Andrew Miller](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/RBQPU8/)

**When and where**: Friday, 2026-04-17, 12:05–12:35, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

When we say "API", most people think REST or GraphQL. But Django has plenty of other APIs; one of the most common and confusing is manage.py runserver, especially when a beginner comes to deploy their first project. This talk explores Django's deployment story through the lens of API design, introduces django-prodserver as a path forward, and asks: what would it take to make going to production as obvious as starting development?

**Description** (verbatim):

**The Setup: APIs Are Everywhere**

We'll start with a quick tour of what "API" really means—not just REST, but Python imports, command-line interfaces, and the configuration files we use every day. Django's `settings.py` is arguably its most-used API: the interface through which we configure databases, middleware, installed apps, and everything else. And `manage.py` commands are APIs too—contracts between Django and developers about how to run, migrate, and manage projects.

This reframing sets up the core question: if `runserver` is an API, what is it communicating? And is that message actually helpful?

**The Problem: Django's Deployment Cliff**

Deployment breaks down into three parts: setting up the environment, getting code there, and running processes. Django provides great documentation, but when it comes to actually running your app in production, you're on your own. Even the name `runserver` is misleading—it doesn't say "development." It just says "run the server," and for a beginner, that sounds like the whole story. Many miss the jump entirely—not realising a different approach is needed for production. And when they do, configuring Gunicorn, Uvicorn, or Celery workers is daunting—and can feel like a betrayal of the "batteries included" promise.

We can add warnings and documentation, but that can add noise and not signal. The reception of adding the warning "do not use in production" to `runserver` has been mixed and if I'm honest it's a poor solution and quick fix to a larger problem. That's coming from me—the one who proposed and implemented it! If the API design itself is confusing, no amount of documentation or warnings will fix that.

**A Possible Solution: django-prodserver**

I've built and published `django-prodserver`, a package that brings a production process configuration API into the familiar `manage.py` interface, configured through `settings.py`, where it belongs. A `PRODUCTION_PROCESSES` dictionary lets you name and define your processes, with backends for popular WSGI/ASGI servers and background workers. Swap backends by changing one line. The package also includes a `devserver` command—mirroring the symmetry we might want in Django itself.

**Live Demo**

I'll take an existing project deployed on a Dokku VPS and show what changes when prodserver enters the picture. The goal is to make the "aha" moment tangible: this is what a cleaner deployment API could feel like.

**The Bigger Picture: What Could Django Provide?**

We can't just change `runserver, Django's stability guarantees mean experimenting with core commands is risky. That's actually a good thing. But packages like django-prodserver give us a safe space to try ideas in the open. What naming makes sense? What hooks should Django expose for the ecosystem to build on? Could this eventually lead to production server support in core? I'll share some thoughts and invite the community to shape what comes next for prodserver and more broadly for designing new APIs through the experimental API feature that has been proposed.

**Takeaways**

Attendees will leave with:

- A new way of thinking about Django's CLI and settings as API surfaces
- Practical knowledge of django-prodserver they can use today
- Ideas for how the community can shape Django's deployment future
- Considerations for API design and how the experimental APIs proposal could open new paths for Django's development

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/U3ZMQV/>

## 25. [Where did it all `BEGIN;`?](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/XBBRYC/)

**Speakers**: [Sam Searles-Bryant](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/FZCKT9/), [Charlie Denton](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/KZTTYE/)

**When and where**: Friday, 2026-04-17, 12:40–13:10, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

We're all familiar with Django's `atomic` context for managing database transactions, but Django existed for several versions before it existed. How were transactions managed before 2013? How are transactions managed now? And how might they be managed in the future?

**Description** (verbatim):

Until 2013, Django's `atomic` context manager didn't exist. This talk will explore how we had to manage database transactions -- as well as save-points, rollbacks, and commits -- before the ergonomics of `atomic` and what changed when it was introduced. By understanding what tools Django users had in Django 1.5 to make their code atomic, durable, or both, we can understand what problems `atomic` solved and how it made writing Django applications better.

Fast-forward to 2026 and we all take `atomic` for granted. But what problems might it have for modern development? We take a look at where `atomic` can cause confusion and suggest some ways to handle that in the future using `django-subatomic`.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/XBBRYC/>

## 26. [How Django is helping to build the biggest X-ray observatory to date](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/GX9KHL/)

**Speakers**: [Loes Crama](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/CVHGWK/)

**When and where**: Friday, 2026-04-17, 14:40–15:10, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Explore how Django is applied to ESA's NewAthena project, where significant amounts of data are managed in a scientific context, illustrating how a web framework can be extended to enable a large-scale space mission.

**Description** (verbatim):

The European Space Agency (ESA) is leading the development of NewAthena (the New Advanced Telescope for High ENergy Astrophysics), an X-ray observatory designed to explore cosmic phenomena such as black holes, neutron stars, and galaxy clusters. The telescope utilizes a 12-meter focal length mirror assembly composed of 600 mirror modules. These modules are manufactured using Silicon Pore Optics (SPO), a technology that transforms silicon wafers into precision mirror plates. In total, the assembly involves approximately 2,400 mirror stacks and 100,000 individual plates.

Each component must be tracked through a series of physical, mechanical, and chemical processes at various locations throughout Europe. At each step in this production chain, data is collected to assess the state and quality of the components. This includes logging components' status, recording geometric specifications and process parameters, and maintaining a complete history of the production chain.

This talk will explore how Django serves as the software backbone for managing this data. It presents how tracking systems for scientists and engineers are built using Django’s standard core tooling, as well as additional packages where needed. In doing so, this talk demonstrates how a general-purpose web framework can be adapted to support a scientific and engineering environment within a space mission context.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/GX9KHL/>

## 27. [Django templates on the frontend?](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/7A87Q7/)

**Speakers**: [Christophe Henry](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/FC3WLA/)

**When and where**: Friday, 2026-04-17, 15:15–15:45, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Django Template Transpiler is a project to transpile Django templates into Javascript render functions, much like what Handlebars can do. It is intended to solve use-cases where small parts of your UI needs to be rendered both on the backend (because corresponding data already exists) or on the front-end (in result of user interaction) and issuing HTTP queries to perform SSR is inconvenient because of bad internet access.

**Description** (verbatim):

In recent years, the Python community has widely adopted HTMX and Hotwire's Turbo. The paradigm of these frameworks is to use AJAX requests to handle changes in the web page. However, there are situations where each HTTP request has a cost, either in bandwidth, volume quota, or any other form of resource cost. In such situations, your application cannot afford to make an HTTP request every time a subform is added to a Django Formset, for instance.

After encountering this situation several times, I decided to start working on django-template-transpiler, a tool written in Rust that converts Django templates into a JS function that renders the DTL on client side, similar to what Handlebars can do. The rationale to allow the developers to make your page dynamic, whil minimizing the number of HTTP queries and render both on server-side and client-side using your Django templates as a single source of truth.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/7A87Q7/>

## 28. [What's in your dependencies? Supply chain attacks on Python projects](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/3VP3W7/)

**Speakers**: [Mateusz Bełczowski](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/FLBRLU/)

**When and where**: Friday, 2026-04-17, 16:15–16:45, room AMPHITHEATRE

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Every pip install is an act of trust. Attackers have exploited that trust - phishing maintainers, hijacking CI/CD pipelines, turning popular packages into malware. Learn how these attacks work and practical defenses for your projects.

**Description** (verbatim):

Your Django project doesn't just depend on Django - it depends on dozens, sometimes hundreds, of packages. Each one is code that runs with your privileges. What happens when one of them gets compromised?

This isn't theoretical. Attackers have phished maintainers to publish malicious versions of trusted packages. They've exploited CI/CD pipelines to inject crypto miners into popular libraries. They've registered typosquatted package names and waited for developers to mistype.

This talk examines how these attacks work and what you can do about them.

We'll look at real incidents to understand the attack patterns - how attackers get in, what payloads they deploy, and how compromises get detected. And we'll build a practical defense toolkit: scanning for known vulnerabilities, evaluating new dependencies before installing them, and hardening your workflow against supply chain attacks.

The talk is aimed at Django developers who want to understand the threat landscape and leave with concrete steps they can implement immediately. No security background required - just familiarity with pip and the general shape of a Django project.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/3VP3W7/>

## 29. [Improve your CV with help of your Django friends](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/EGHWNC/)

**Speakers**: [Jure Cuhalev](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/WBZZTD/)

**When and where**: Friday, 2026-04-17, 11:05–11:55, room NEW STAGE

**Type**: Workshop — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

CVs are marketing documents that have the primary goal to help Software Engineers get to a job interview. In this workshop we'll look at some general best practices, and provide feedback to each others CVs to increase our chances to land a new role.

**Description** (verbatim):

When searching for a new job a Software Engineer is often reduced to a 2-page PDF document - CV - that they need to submitted to be even considered for a job interview. With this in mind we need to treat it as marketing document, that benefits from going through a few stages of reviews from our peers in the field.

We'll start the workshop with some basic guidelines of how to read CVs with the idea that CV can be adjusted for specific job role (e.g. Backend Engineer with FinTech experience). We'll then split into groups and try to read each others' CVs (and possibly LinkedIn descriptions) to help provide feedback on how to better refine them for the next career step.

Pre-requisites needed: current CV in English language that participant can share (e.g. uploaded somewhere online); computer or similar device to view participants CVs.

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/EGHWNC/>

## 30. [Django-Admin-Deux: From First Steps to Custom Plugins](https://pretalx.evolutio.pt/djangocon-europe-2026/talk/83B97E/)

**Speakers**: [Emma Delescolle](https://pretalx.evolutio.pt/djangocon-europe-2026/speaker/XREAEA/)

**When and where**: Friday, 2026-04-17, 15:15–16:45, room NEW STAGE

**Type**: Long Workshop — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.evolutio.pt/djangocon-europe-2026/schedule/export/schedule.json)):

Django's built-in admin is powerful, but it's essentially a separate framework within Django and it's 20 years old.

Wouldn't it be nice to be able to work with an admin interface that works like the rest of Django, built on generic views, plugins, and view factories? This is the idea behind [Django-Admin-Deux](https://codeberg.org/emmaDelescolle/django-admin-deux): a proof-of-concept Django admin replacement where CRUD operations are just actions, knowledge transfers both ways, and everything feels like Django.

This workshop will explore the concepts behind Django-Admin-Deux in details and we will build together:

- an application that uses it
- a custom plugin

**Description** (verbatim):

What if customizing Django's admin felt like writing any other Django view? Django-Admin-Deux aims at doing just that. It is not just a cosmetic refresh, it's a radically new approach relying on factory-generated views with a plugin-first design. Let's have a closer look!

Workshop Structure:

1. Architectural Foundations (20 min)
   - View Factories: How Django-Admin-Deux generates views dynamically
   - Action System: Actions are the recipes followed by view factories, including non-model-related ones like dashboards
   - Plugin Hooks: what hooks are available?
   - Dataclasses: Django-Admin-Deux uses a series of dataclasses to make extending it type-safe and practical, let's look at them
2. A practical example: using Django-Admin-Deux (30 min)
   - Simple (migration from the stock admin)
   - Enhancements (`list_display` with enhanced features, Form `Layout`, `Collection`s)
   - Adding custom `View`s and `Action`s
   - Permission system (from stock admin compatibility to composable permissions)
   - Visibility, debugging and testing
3. A more advanced example: let's build a plugin (30 min)
   - Structure of a plugin
   - Minimum requirements
   - Enhancing existing `View`s and `Action`s
   - Announcing and checking feature availability

Prerequisites:

- Familiarity with Django and the admin in general
- Starter repository will be provided before the workshop

Source: <https://pretalx.evolutio.pt/djangocon-europe-2026/talk/83B97E/>
