# Python devroom talks at FOSDEM 2026

Collected from the official FOSDEM 2026 schedule: the Pentabarf XML export at <https://fosdem.org/2026/schedule/xml> (primary structured source) and, for verification, each talk's event page on the live schedule site. Collected 2026-09-20; all linked URLs were verified live on that date.

The Python devroom ran on Saturday 31 January 2026 in room UA2.220 (Guillissen), with 8 events scheduled between 15:00 and 19:00 CET (UTC+1). Both the XML export and the [track page](https://fosdem.org/2026/schedule/track/python/) listed the same 8 talks at collection time.

FOSDEM's schedule export separates abstract from description. Every Python-track talk had an empty description in both the XML and its event page, so no long-form descriptions exist in the source data; each talk shows its abstract only, reproduced verbatim.

Machine-readable version of this data: [`talks.json`](talks.json) in this directory.

## Talks

## 1. [The Bakery: How PEP810 sped up my bread operations business](https://fosdem.org/2026/schedule/event/HAAABD-python-pep810/)

**Speakers**: [Jacob Coffee](https://fosdem.org/2026/schedule/speaker/jacob_coffee/)

**When and where**: Saturday 31 January 2026, 15:00-15:30 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/HAAABD-python-pep810/)):

Discover how PEP 810's explicit lazy imports can dramatically improve Python application startup times. Using a real CLI tool as a case study, that we totally use in our real business, this talk demonstrates practical techniques to optimize import performance while maintaining code clarity and safety.

Description: no description available in source data.

**Links**:

- [Slides: Slides](https://fosdem.org/2026/events/attachments/HAAABD-python-pep810/slides/266934/talk_-_co_chhdrub.pdf)
- [Video recording (AV1/WebM; preferred) - 144.0 MB](https://video.fosdem.org/2026/ua2220/HAAABD-python-pep810.av1.webm)
- [Video recording (MP4; for legacy systems) - 501.2 MB](https://video.fosdem.org/2026/ua2220/HAAABD-python-pep810.mp4)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/HAAABD/feedback/)

Source: <https://fosdem.org/2026/schedule/event/HAAABD-python-pep810/>, <https://fosdem.org/2026/schedule/xml>

## 2. [The GIL and API Performance: Past, Present, and Free-Threaded Future](https://fosdem.org/2026/schedule/event/ABJMWD-the_gil_and_api_performance_past_present_and_free-threaded_future/)

**Speakers**: [Ruben Hias](https://fosdem.org/2026/schedule/speaker/ruben_hias/)

**When and where**: Saturday 31 January 2026, 15:30-16:00 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/ABJMWD-the_gil_and_api_performance_past_present_and_free-threaded_future/)):

Python’s Global Interpreter Lock has shaped the way developers build concurrent applications for nearly three decades. While the GIL simplified the CPython ecosystem, it also imposed well-known limits on CPU-bound work and multithreaded scalability. With the introduction of free-threaded Python (3.14t), that is about to change.

This talk explores the history and purpose of the GIL, why it existed for so long, and the innovations that finally made its removal viable. We’ll look at how free-threading affects real workloads through concrete benchmarks. We'll investigate the often overlooked effect of freethreading on webservers. You’ll see how modern servers like Granian, ASGI frameworks, and WSGI stacks behave when threads are no longer serialized by the interpreter.

By the end, you’ll understand not only what the GIL is, but what its disappearance means for scaling Python applications in production. Whether you're building high-throughput APIs, tuning async code, or planning future architecture, free-threaded Python opens the door to new performance ceilings - along with new tradeoffs every developer should know.

Description: no description available in source data.

**Links**:

- [Slides: Slides](https://fosdem.org/2026/events/attachments/ABJMWD-the_gil_and_api_performance_past_present_and_free-threaded_future/slides/266979/the_gil_a_fw7etsx.pdf)
- [Video recording (AV1/WebM; preferred) - 100.7 MB](https://video.fosdem.org/2026/ua2220/ABJMWD-the_gil_and_api_performance_past_present_and_free-threaded_future.av1.webm)
- [Video recording (MP4; for legacy systems) - 593.2 MB](https://video.fosdem.org/2026/ua2220/ABJMWD-the_gil_and_api_performance_past_present_and_free-threaded_future.mp4)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/ABJMWD/feedback/)

Source: <https://fosdem.org/2026/schedule/event/ABJMWD-the_gil_and_api_performance_past_present_and_free-threaded_future/>, <https://fosdem.org/2026/schedule/xml>

## 3. [Modern Python monorepo with `uv`, `workspaces`, `prek` and shared libraries](https://fosdem.org/2026/schedule/event/WE7NHM-modern-python-monorepo-apache-airflow/)

**Speakers**: [Jarek Potiuk](https://fosdem.org/2026/schedule/speaker/jarek_potiuk/)

**When and where**: Saturday 31 January 2026, 16:00-16:30 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/WE7NHM-modern-python-monorepo-apache-airflow/)):

Apache Airflow is the most popular Data Workflow Orchestrator - developed under the Apache Software Foundation umbrella. We have 120+ Python distributions in our rep, and we often release ~ 100 of them every two week.

All those distributions are built from a single monorepo.

[jarekpotiuk:~/code/airflow]  find . -name 'pyproject.toml' | wc
     120     120    4248

This had always posed a lot of challenges and we had a lot of tooling to make it possible, however with the recent development of Python Packaging tools, multipel Packaging PEPs implemented, and with new wave of tools such as uv and prek, our setup is finally manageable and we removed 1000s of line of custom code we wrote before after we applied uv workspaces, switched to prek, started using inline script metadata.

It's a breeze to have monorepo now. This talk explains how.

Bonus content. If you know the differences between dynamically and statically linked libraries in C and other languages, or used NPM - you might recognise the need of being able to use different versions of the same library in the same system. It's not possible in Python. Or is it?

We've figured out a way to eat cake and have it too - and we have "statically linked" libraries in Python. How did we do it?

You will find out how from the talk.

Description: no description available in source data.

**Links**:

- [Video recording (AV1/WebM; preferred) - 86.3 MB](https://video.fosdem.org/2026/ua2220/WE7NHM-modern-python-monorepo-apache-airflow.av1.webm)
- [Video recording (MP4; for legacy systems) - 626.0 MB](https://video.fosdem.org/2026/ua2220/WE7NHM-modern-python-monorepo-apache-airflow.mp4)
- [Presentation](https://docs.google.com/presentation/d/1vPWYJ_9GmUNZfFl7gJvl7evYHb4zGjAPq2BVXhiJNR8/edit?usp=sharing)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/WE7NHM/feedback/)

Source: <https://fosdem.org/2026/schedule/event/WE7NHM-modern-python-monorepo-apache-airflow/>, <https://fosdem.org/2026/schedule/xml>

## 4. [PyInfra: Because Your Infrastructure Deserves Real Code in Python, Not YAML Soup](https://fosdem.org/2026/schedule/event/VEQTLH-infrastructure-as-python/)

**Speakers**: [Loïc Tosser "wowi42"](https://fosdem.org/2026/schedule/speaker/loic_tosser_wowi42/)

**When and where**: Saturday 31 January 2026, 16:30-17:00 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/VEQTLH-infrastructure-as-python/)):

Remember when we said "Infrastructure as Code"? Somehow, the industry heard "Infrastructure as YAML" and ran with it. Now we're drowning in a sea of indentation-sensitive, template-riddled, Jinja2-abused configuration files that make even the most battle-hardened sysadmins weep into their mechanical keyboards.

Enter PyInfra—where your infrastructure is actually code. Real Python. With loops that don’t require learning a DSL. With functions that are... wait for it... actual functions. With error handling that doesn’t involve praying to the YAML gods and sacrificing a virgin bracket.

In this talk, you’ll see how to:
- Write infrastructure automation that your IDE actually understands
- Debug with real stack traces instead of "ERROR: The task includes an option with an undefined variable"
- Use actual Python conditionals instead of when: ansible_os_family == "Debian" and not (ansible_distribution == "Ubuntu" and ansible_distribution_version is version('20.04', '>='))
- Import and reuse code like a civilized developer, not copy-paste playbooks like it’s 1999
- Test your infrastructure code with pytest, not "let’s run it in staging and see what breaks"

We’ll explore how a typical Ansible playbook can be transformed into clean, maintainable Python with PyInfra, shrinking from 500 lines of YAML to 50 lines of readable code. You’ll discover the joy of list comprehensions over with_items, and the power of deployment logic that can actually think.

Stop treating your infrastructure like a configuration file. It’s 2026—your servers deserve better than YAML. They deserve Python.

Warning: This talk may cause uncontrollable urges to refactor all your Ansible playbooks. Side effects include increased productivity, better sleep, and colleagues actually understanding your infrastructure code.

Link to the marp: https://marp.kalvad.com/fosdem_2026 (gifs are not working in pdf)

Description: no description available in source data.

**Links**:

- [Video recording (AV1/WebM; preferred) - 197.6 MB](https://video.fosdem.org/2026/ua2220/VEQTLH-infrastructure-as-python.av1.webm)
- [Video recording (MP4; for legacy systems) - 603.9 MB](https://video.fosdem.org/2026/ua2220/VEQTLH-infrastructure-as-python.mp4)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/VEQTLH/feedback/)

Source: <https://fosdem.org/2026/schedule/event/VEQTLH-infrastructure-as-python/>, <https://fosdem.org/2026/schedule/xml>

## 5. [Ducks to the rescue - ETL using Python and DuckDB](https://fosdem.org/2026/schedule/event/S7RELZ-ducks_to_the_rescue_-_etl_using_python_and_duckdb/)

**Speakers**: [Marc-André Lemburg](https://fosdem.org/2026/schedule/speaker/marc-andre_lemburg/)

**When and where**: Saturday 31 January 2026, 17:00-17:30 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/S7RELZ-ducks_to_the_rescue_-_etl_using_python_and_duckdb/)):

Summary:

ETL stands for "extract, transform, load" and is a synonym for moving data around. This has traditionally often required managing complex systems in the cloud or large data centers. The talk will demonstrate how all this can be greatly simplified by applying modern tools for the task: Python and DuckDB, both open source and readily available to run on most systems - even your notebook.

Description:

ETL stands for "extract, transform, load" and is a synonym for moving data from one system to another.

Traditionally, ETL was done in exactly that order: first you extract the data you want to process, then you transform it and then you load it into the target system. More modern approaches based on data lakes, swap the T and L, since transformation is more efficiently done in a database system, especially when it comes to large volumes of data.

In order to make all this work, the usual approach is to have a workflow system, taking care of managing all the intermediate steps, a large data lake database and distributed storage systems. This results in lots of complexity, need for system/cluster administration and maintenance.

Now, with today's computers, most data sizes used in ETL no longer need all this complexity. Even notebooks or single VMs can handle the load, when used with external object storage, so all you really just need is the right software stack to manage your ETL - without all the overhead:

- Python has grown to be the number one programming language on the planet and is especially well suited for integration work due to its many readily available connectors to plenty of backend systems. It often comes preinstalled on Linux machines and is easy to install on most other systems.

- DuckDB has emerged as one of the most capable embedded OLAP database systems and supports data lakes with the DuckLake extension, right out of the box. Installation is just a uv add duckdb away.

Both can be run on the same machine and are very resource friendly.

The talk will give an overview of the typical steps involved in ETL processes, give a short intro to DuckDB and showcase how DuckDB can be put to good use when implementing ETL processes. If time permits, I can also cover a few advanced topics addressing optimization strategies.

Resources:

- [Python.org](https://www.python.org/)

- [DuckDB – An in-process SQL OLAP database management system](https://duckdb.org/)

Description: no description available in source data.

**Links**:

- [Slides: Slides for the talk](https://fosdem.org/2026/events/attachments/S7RELZ-ducks_to_the_rescue_-_etl_using_python_and_duckdb/slides/267095/fosdem-20_fwmer9v.pdf)
- [Video recording (AV1/WebM; preferred) - 119.4 MB](https://video.fosdem.org/2026/ua2220/S7RELZ-ducks_to_the_rescue_-_etl_using_python_and_duckdb.av1.webm)
- [Video recording (MP4; for legacy systems) - 544.9 MB](https://video.fosdem.org/2026/ua2220/S7RELZ-ducks_to_the_rescue_-_etl_using_python_and_duckdb.mp4)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/S7RELZ/feedback/)

Source: <https://fosdem.org/2026/schedule/event/S7RELZ-ducks_to_the_rescue_-_etl_using_python_and_duckdb/>, <https://fosdem.org/2026/schedule/xml>

## 6. [Is it time for a Django Admin rewrite? If so, how?](https://fosdem.org/2026/schedule/event/UBNWNL-django-admin-deux/)

**Speakers**: [Emma Delescolle](https://fosdem.org/2026/schedule/speaker/emma_delescolle/)

**When and where**: Saturday 31 January 2026, 17:30-18:00 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/UBNWNL-django-admin-deux/)):

[Django](https://www.djangoproject.com)'s built-in admin is powerful, but it's essentially a separate framework within Django and it's 20 years old.

Wouldn't it be nice to be able to work with an admin interface that works like the rest of Django, built on generic CBVs, plugins, and view factories? [Django-Admin2](https://github.com/jazzband/django-admin2), was an attempt at doing just that and it was a fairly successful ptoject.

10 years later, after looking at reviving that project, I realized we needed a fresh approach: Meet [Django-Admin-Deux](https://codeberg.org/emmaDelescolle/django-admin-deux): a proof-of-concept Django admin replacement where CRUD operations are just actions, knowledge transfers both ways, and everything feels like Django.

Let's have a look at what python features and architecture makes this possible

Description: no description available in source data.

**Links**:

- [Video recording (AV1/WebM; preferred) - 96.0 MB](https://video.fosdem.org/2026/ua2220/UBNWNL-django-admin-deux.av1.webm)
- [Video recording (MP4; for legacy systems) - 651.0 MB](https://video.fosdem.org/2026/ua2220/UBNWNL-django-admin-deux.mp4)
- [Slides](https://levit-url.cc/admin-deux)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/UBNWNL/feedback/)

Source: <https://fosdem.org/2026/schedule/event/UBNWNL-django-admin-deux/>, <https://fosdem.org/2026/schedule/xml>

## 7. [Building a sovereign digital workplace with the help of Python, an example of the french administration](https://fosdem.org/2026/schedule/event/L7NG9J-building_a_sovereign_digital_workplace_with_the_help_of_python_an_example_of_the/)

**Speakers**: [Manuel Raynaud](https://fosdem.org/2026/schedule/speaker/manuel_raynaud/)

**When and where**: Saturday 31 January 2026, 18:00-18:30 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/L7NG9J-building_a_sovereign_digital_workplace_with_the_help_of_python_an_example_of_the/)):

The French digital agency (DINUM) has undertaken to develop an open-source collaborative digital workplace to make the work of public servants simpler and more effective.

This collaborative digital workplace is distributed under an open-source license to allow anyone who wishes to take its applications and integrate them into their preferred tools.

By participating in existing open-source communities, the digital workplace enables the emergence of digital commons that facilitate independence for those who wish to deploy and use them.

Designed with a modular approach, it can be partially or progressively adopted or complement an existing offer.

I propose to present two applications, both technically and functionally, that are integrated into this collaborative suite:

- Collaborative editing and documentation: The Suite [Docs](https://github.com/suitenumerique/docs), based on Prosemirror and Blocknotejs. Developed jointly with Germany and the Netherlands.

- File sharing: [Drive](https://github.com/suitenumerique/drive)

These applications share the same technical stack, which relies on Python and the Django framework, Django Rest Framework, and PostgreSQL.

Beyond a list of libraries used, I will present the quality processes we have implemented, the complete workflow from the idea of a new feature to its implementation and deployment. I will share our dev handbook (also under an open-source license) that compiles our best practices.

How what could be qualified as a "Boring Stack" (meaning proven and battle-tested) allows us to focus on solving complex problems.

Description: no description available in source data.

**Links**:

- [Video recording (AV1/WebM; preferred) - 88.4 MB](https://video.fosdem.org/2026/ua2220/L7NG9J-building_a_sovereign_digital_workplace_with_the_help_of_python_an_example_of_the.av1.webm)
- [Video recording (MP4; for legacy systems) - 691.2 MB](https://video.fosdem.org/2026/ua2220/L7NG9J-building_a_sovereign_digital_workplace_with_the_help_of_python_an_example_of_the.mp4)
- [Presentation support](https://docs.numerique.gouv.fr/docs/1aa048d2-cdf9-4c0d-8499-dd3dac4f2586/)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/L7NG9J/feedback/)

Source: <https://fosdem.org/2026/schedule/event/L7NG9J-building_a_sovereign_digital_workplace_with_the_help_of_python_an_example_of_the/>, <https://fosdem.org/2026/schedule/xml>

## 8. [Lightning Talks](https://fosdem.org/2026/schedule/event/YYTRKQ-lightning_talks/)

**Speakers**: [Marc-André Lemburg](https://fosdem.org/2026/schedule/speaker/marc-andre_lemburg/)

**When and where**: Saturday 31 January 2026, 18:30-19:00 (UTC+1), room [UA2.220 (Guillissen)](https://fosdem.org/2026/schedule/room/ua2220/)

**Type**: devroom — **Language**: en

**Abstract** (verbatim from the [schedule XML](https://fosdem.org/2026/schedule/xml) and the [event page](https://fosdem.org/2026/schedule/event/YYTRKQ-lightning_talks/)):

After the success of last year's impromptu lightning talks session, we will have an official one in the Python Devroom for 2026.

Please submit your talks using this form:

- [Lightning Talk Submission Form](https://docs.google.com/forms/d/e/1FAIpQLSfh1zpbP6KgMmexQeT6jlcX1_o8W26zovBUVVudxopBMfjGsg/viewform?usp=header)

- The form will be opened for submissions at around 14:00 CET on Saturday, Jan 31, 2026.

Lightning Talks are at most 5 minutes and should be Python related.

Note: All presentations in this slot will be recorded and made available under a CC-BY license.

Thank you,
Python Devroom Organizers

Description: no description available in source data.

**Links**:

- [Video recording (AV1/WebM; preferred) - 115.5 MB](https://video.fosdem.org/2026/ua2220/YYTRKQ-lightning_talks.av1.webm)
- [Video recording (MP4; for legacy systems) - 595.3 MB](https://video.fosdem.org/2026/ua2220/YYTRKQ-lightning_talks.mp4)
- Feedback: [Submit feedback for this talk](https://pretalx.fosdem.org/fosdem-2026/talk/YYTRKQ/feedback/)

Source: <https://fosdem.org/2026/schedule/event/YYTRKQ-lightning_talks/>, <https://fosdem.org/2026/schedule/xml>
