# PyCon DE & PyData 2026 talks

Collected from the official PyCon DE & PyData 2026 schedule via its Pretalx frab JSON export at <https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json> (schedule version **0.25, a draft revision**, fetched 2026-09-20). The schedule page is at <https://pretalx.com/pyconde-pydata-2026/schedule/>.

The talk.json keeps even the lighter programme items because in this export they carry real content or speakers: panels, invited and sponsored talks, lightning-talk blocks, and open spaces are all kept; the two "Opening Session" and "Closing Session" plenary placeholders remain in the data with empty speaker lists for completeness. The pretalx JSON API at `/api/events/pyconde-pydata-2026/talks/` returned 404 at collection time, so this frab export is the used source.

Every talk record carries its canonical Pretalx talk URL and the export as source. Speaker names come from the export's person records; profile URLs are included where the export provides them (verified live for a sample).

Machine-readable version of this data: [`talks.json`](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/2026-python-events/pycon-de-pydata-2026/talks.json) in this directory.

## Talks

Machine-readable version of this data: [`talks.json`](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/2026-python-events/pycon-de-pydata-2026/talks.json) in this directory.

## Talks

## 1. [Opening Session](https://pretalx.com/pyconde-pydata-2026/talk/BQPEUG/)

**Speakers**: Not listed in the source data

**When and where**: Tuesday, 2026-04-14, 10:00–10:30, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Plenary — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Opening Session

**Description** (verbatim):

Opening Session

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BQPEUG/>

## 2. [From Scratch to Scale: Turning LLM Code into Architecture Insights](https://pretalx.com/pyconde-pydata-2026/talk/BFL7MQ/)

**Speakers**: [Sebastian Raschka](https://pretalx.com/pyconde-pydata-2026/speaker/GVDHSU/)

**When and where**: Tuesday, 2026-04-14, 10:30–11:15, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python has been at the center of my work in machine learning and AI for more than a decade. It is where I start from scratch, experiment with ideas, and build systems that help me understand how large language models really work.

In this keynote, we will explore how Python enables this entire journey, from defining model architectures and training loops to scaling data and computation across devices. I will also reflect on how Python continues to support both the large models of today and the evolving systems of tomorrow, even as new backends take over the heavy lifting.

**Description** (verbatim):

Python has been at the center of my work in machine learning and AI for more than a decade. It is where I start from scratch, experiment with ideas, and build systems that help me understand how large language models really work.

In this keynote, I will look at what it means to build and study LLMs in Python today. Starting from small, from-scratch implementations, I will show how Python and PyTorch help us understand modern model architectures, compare new designs against reference code, and learn details that papers often leave out. I will then connect those implementation lessons to current LLM trends, especially the push to reduce inference costs and KV-cache pressure as reasoning models and agentic workflows need longer contexts. At the end, I will also share a practical roadmap of libraries, open projects, and learning resources for going from first principles to real-world LLM development.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BFL7MQ/>

## 3. [Sentinel Values in Python: Semantics, Double Dispatch, and the Limits of Typing](https://pretalx.com/pyconde-pydata-2026/talk/88TTRY/)

**Speakers**: [Florian Wilhelm](https://pretalx.com/pyconde-pydata-2026/speaker/8LQU9C/)

**When and where**: Tuesday, 2026-04-14, 11:45–12:15, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python relies heavily on special values such as `None`, `NotImplemented`, `Ellipsis`, and `dataclasses.MISSING`. These values are not incidental: they encode language semantics, enable control flow between objects, and shape API design.

This talk examines sentinel values as a first-class concept in Python. We will look at why None is often the wrong representation for absence, how NotImplemented enables double dispatch in rich comparisons, and where sentinel values appear throughout the standard library.

A central focus is typing. While sentinel values are ubiquitous at runtime, Python currently has no standardized way to express them precisely in type hints. We will examine why Optional, overloads, and Literal fall short, what limited narrowing is possible today, and why creating a “real” custom sentinel with reliable type narrowing is still unsolved.

Finally, we will discuss [PEP 661](https://peps.python.org/pep-0661/), i.e., the deferred proposal to standardize sentinel values and their typing semantics, and what its deferral means in practice. Using real-world examples, including Pydantic’s experimental missing concept, this talk provides a clear mental model for sentinel values and realistic guidance for using them in typed Python codebases today.

**Description** (verbatim):

Sentinel values are a fundamental but under-documented part of Python’s design. They are used to represent absence, unsupported operations, incomplete state, and to coordinate control flow between objects. Yet, they are often treated as ad-hoc implementation details.

This talk starts by clarifying what sentinel values are and why None is frequently semantically overloaded and incorrect for modelling “missing” or “unset” values. We then examine built-in sentinels such as `NotImplemented`, `Ellipsis`, and `dataclasses.MISSING`, with a detailed look at how `NotImplemented` enables double dispatch in equality and ordering operations.

The second half of the talk focuses on typing, where sentinel values expose fundamental tensions between Python’s dynamic semantics and static type systems. We will discuss:

- why Optional[T] does not mean “unset”
- why Literal appears attractive for sentinels but rarely works in practice
- what limited type narrowing is possible today and under which assumptions
- why a fully reliable, user-defined sentinel with correct narrowing is currently not achievable in a portable way

To ground this in practice, we will look at real-world patterns used in production code, including Pydantic’s experimental missing concept, and explain the trade-offs these designs make.

Finally, we will examine [PEP 661](https://peps.python.org/pep-0661/), the proposal to standardize sentinel values and their typing semantics. We will explain what it would solve, why it was deferred, and what that deferral means for library and API authors today.

The talk concludes with concrete, honest guidelines: when sentinel values are the right tool, how to design APIs around them, and how to communicate absence clearly in typed Python code without pretending the type system can do more than it currently can.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/88TTRY/>

## 4. [The foundation model revolution for tabular data](https://pretalx.com/pyconde-pydata-2026/talk/KLN78E/)

**Speakers**: [Frank Hutter](https://pretalx.com/pyconde-pydata-2026/speaker/X9K7V8/)

**When and where**: Tuesday, 2026-04-14, 12:25–12:55, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Sponsored Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Tabular data, spreadsheets organized in rows and columns, are ubiquitous across healthcare, business and finance. The fundamental prediction task of filling in missing values of a label column based on the rest of the columns is essential for thousands of use cases of high societal and commercial value. While gradient-boosted decision trees have dominated tabular data for the past 20 years, we demonstrate that this is rapidly changing, with the foundation model revolution having arrived at tabular data. We will show the methods behind this and their extensions to causality, interpretability and robustness, and demo various agentic extensions.

**Description** (verbatim):

Tabular data, spreadsheets organized in rows and columns, are ubiquitous across healthcare, business and finance. The fundamental prediction task of filling in missing values of a label column based on the rest of the columns is essential for thousands of use cases of high societal and commercial value. While gradient-boosted decision trees have dominated tabular data for the past 20 years, we demonstrate that this is rapidly changing, with the foundation model revolution having arrived at tabular data. We will show the methods behind this and their extensions to causality, interpretability and robustness, and demo various agentic extensions.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/KLN78E/>

## 5. [Stop Waiting, Start Shipping: Real-World Strategy for Open-Source LLMs](https://pretalx.com/pyconde-pydata-2026/talk/9CYWET/)

**Speakers**: [Sebastian Raschka](https://pretalx.com/pyconde-pydata-2026/speaker/GVDHSU/), [Alexander CS Hendorf](https://pretalx.com/pyconde-pydata-2026/speaker/K9DZKF/)

**When and where**: Tuesday, 2026-04-14, 14:30–15:45, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Panel — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Chinese and American open-source LLMs are competing head-to-head — from DeepSeek and Qwen to Llama and Mistral. The model landscape is broader than ever, yet in Germany the debate still circles around waiting for the next breakthrough. Alexander Hendorf and Sebastian Raschka discuss what these models can and cannot do today, what biases to watch for, and which deployment strategies actually work in practice. The session reserves substantial time for questions and discussion with the audience.

**Description** (verbatim):

Alexander Hendorf and Sebastian Raschka sit down for a fireside chat on the current state of open-source LLMs.

With Chinese models like DeepSeek and Qwen competing directly with Llama and Mistral, the choice of capable open-source models has never been wider — so why are so many teams still waiting for the next generation instead of building with what is already here?

Questions we want to discuss:

- What role do Chinese and American OSS models play in the current competitive landscape?
- Where do open-source models still fall short of proprietary ones, and where has the gap closed?
- What biases should practitioners be aware of and how to handle them?
- Are AI agents a fundamental shift or are we seeing diminishing returns?
- What deployment strategies actually work — especially for European teams that rely on talent and domain expertise rather than hyperscaler compute?

Half the session is reserved for audience questions.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/9CYWET/>

## 6. [Panel: Evolution, Revolution, or Illusion? The Future of Python and Coding in the Age of AI](https://pretalx.com/pyconde-pydata-2026/talk/WAJQR7/)

**Speakers**: [Sebastian Neubauer](https://pretalx.com/pyconde-pydata-2026/speaker/NEBKEY/), [Markus Klein](https://pretalx.com/pyconde-pydata-2026/speaker/GSRLAK/), [Asya Melnik](https://pretalx.com/pyconde-pydata-2026/speaker/XG9398/), [Serhii Sokolenko](https://pretalx.com/pyconde-pydata-2026/speaker/ZUECPC/), [Ines Montani](https://pretalx.com/pyconde-pydata-2026/speaker/FZKG9N/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:30, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Panel — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Software engineering is changing fast. With AI now writing and reasoning about code, does it still make sense to learn Python or any language at all?

Is this the evolution of our craft, a true revolution, or just hype from those who benefit most? Join us to debate the future of Python, the risks of AI-driven development, and what skills will actually matter next.

**Description** (verbatim):

Software engineering is at a crossroads. With AI systems now capable of generating, debugging, and even reasoning about code, the very definition of programming is being challenged.
Does it still make sense to invest years learning Python, or any programming language, if machines can translate natural language specifications into working software? Are we witnessing the evolution of coding into a higher-level craft, the revolution of the software industry, or merely an illusion fueled by hype from those who benefit most?
This panel moderated by Sebastian Neubauer will confront these questions head-on. We will debate whether programming languages remain essential, whether software engineers are at risk of obsolescence, or whether the demand for engineers may actually explode in ways we cannot yet imagine. We will also explore the risks of over-reliance on AI, including potential security vulnerabilities, fragile or unexplainable systems, and the loss of deep understanding of the software we build.
Come prepared for uncomfortable questions, bold predictions, and no easy answers. This is a session designed to challenge assumptions, spark debate, and imagine the possible futures of Python and software engineering in an AI-assisted world.

Note: Join our interactive workshop to explore the future of Python and AI-assisted coding on Wednesday . Everyone is welcome to share ideas, debate risks, the future of Python and help shape what software engineering could look like in the age of AI.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/WAJQR7/>

## 7. [Lightning Talks 1](https://pretalx.com/pyconde-pydata-2026/talk/NXEVSE/)

**Speakers**: Not listed in the source data

**When and where**: Tuesday, 2026-04-14, 17:50–19:00, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Lightning Talks — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Lightning Talks 1

**Description** (verbatim):

Lightning Talks 1

Source: <https://pretalx.com/pyconde-pydata-2026/talk/NXEVSE/>

## 8. [Python Hates Being PID 1: Writing Container-Aware Code for Kubernetes](https://pretalx.com/pyconde-pydata-2026/talk/JJDCW3/)

**Speakers**: [Kavish Nareshchandra Dahekar](https://pretalx.com/pyconde-pydata-2026/speaker/JLP8VR/)

**When and where**: Tuesday, 2026-04-14, 11:45–12:15, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

On Kubernetes, your Python app runs in a hostile environment, fighting for resources in a straitjacket, bombarded with signals, and being killed and ruthlessly dragged back to life time and again. This is in stark contrast to the wonderful weather of a Linux web server or the blissful utopia of localhost. If not hardened properly, your Python app will find the burden of being containerized too hard to bear. And the result? Zombies!

Whether you are a Kubernetes expert, or you just deployed your first containerized Hello World, we will together explore how the Python Interpreter, the Linux Kernel and Kubernetes interact with each other.

We will uncover why Python struggles as an init process, how Kubernetes CPU-limits fight the Global Interpreter Lock (GIL) and why Python’s Garbage Collector cannot save you from sudden OOM kills. Most importantly, we will see how to identify, debug, and avoid containerized Python pitfalls. The goal of this talk is to help you stop treating your container like a server and learn to write Cloud-Native Python that knows exactly where it lives.

**Description** (verbatim):

**The Problem** : The large-scale adoption of Kubernetes means more Python developers are now writing code that runs as a containerized workload on Kubernetes. However, most of us still write applications with a standard Linux server in mind. In a containerized environment, these assumptions are either untrue or dangerous. Python apps not hardened for a containerized environment lead to production failures that are notoriously hard to debug:

- Unexplained Latency: API requests that stall for hundreds of milliseconds due to Linux CFS Quota throttling, even when monitoring shows low CPU usage.
- Silent OOM Kills: Containers that vanish instantly without a traceback because they hit a Cgroup limit that the Python Garbage Collector cannot see.
- Zombie Processes: Subprocesses that were never truly killed and are now exhausting the process table because Python ignores its duties as PID 1.

**The Solution** : This talk will briefly get you up to speed with containerization before taking a technical deep dive into the interactions between Kubernetes, the CPython interpreter and the Linux container runtime. We will move beyond basic Dockerfile best practices and focus on hardening the application code itself to survive in a hostile Kubernetes environment.

**Pre-requisites** : This talk is aimed towards intermediate to senior Python Developers and Data Engineers having basic familiarity with Docker. No advanced Kubernetes or Linux Kernel knowledge required, we will run through the foundational topics in brief.

**Outline (30 Minutes)**

1. Who am I? (2 mins)
2. The Lie of the Container (3 mins)
   - Understanding how the container runtime isolates your process and the resources it needs.
3. The PID 1 Problem (4 mins)
   - How the Linux kernel treats PID 1 processes and why the standard Python interpreter fails these duties.
   - Present well established solutions to the problem (init: true, tini, etc) and common pitfalls.
4. The CPU Quota & Memory Limit (8 mins)
   - How container CPU limits in Kubernetes translate to Linux CFS (Completely Fair Scheduler) quotas.
   - Visualizing how the enforcement of CFS quotas interacts with the Python GIL to cause latency spikes.
   - Python’s memory management and the dreaded OOM kill.
5. Hardening your Python Code (8 mins)
   - How to use the Cgroup file system or psutil to achieve true resource awareness.
   - Strategies for avoiding CPU throttling and tuning numeric libraries (Pandas/Numpy) from attempting to use too many cores.
   - Why `gc.collect()` is often insufficient and how to release memory before the OOM killer strikes.
6. Conclusion & Checklist (5 mins)
   - A "Production-Ready" checklist for Python on K8s.
   - Q&A.

**After this talk you will** :

- Understand the lifecycle of a containerized Python app and handle shutdowns gracefully.
- Fine-tune a containerized Python app for stability and avoid CPU throttling and OOM kills.
- Look beyond the standard system calls to write truly resource aware Python apps.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/JJDCW3/>

## 9. [Beyond Stateless: Why Your Web Service Architecture is Fighting Against Performance](https://pretalx.com/pyconde-pydata-2026/talk/BQYTVM/)

**Speakers**: [Heiner Wolf](https://pretalx.com/pyconde-pydata-2026/speaker/P9MRFG/)

**When and where**: Tuesday, 2026-04-14, 12:25–13:10, room Titanium [2nd Floor]

**Type**: Talk (long) — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

We've been told for years that stateless services are the holy grail of
scalable web architectures. But what if this foundational principle is
actually hurting development speed and runtime performance?

Coding agents follow our example. They do what we would have done, only
10 times more. They also apply the "stateless is good" myth.

This talk challenges the dominant paradigm by demonstrating how
stateful, object-oriented programming can automatically scale to
millions of users without the typical infrastructure complexity.

I'll show how keeping objects with their state in distributed memory
eliminates the need for explicit caching strategies, reduces database
bottlenecks, and dramatically simplifies your code base. You'll see how
a simple Python class can transparently scale across multiple servers,
handling millions of concurrent users without implementing REST
endpoints, message queues, or cache invalidation logic.

So you can guide your agent to do scalability the right way.

**Description** (verbatim):

## The Problem Many Face

Every developer of a successful web service knows this progression: You start with a simple FastAPI or Django app. It works great locally. Then you deploy it, traffic grows, and suddenly you're working primarily on infrastructure complexity. Load balancers, cache layers, database replicas, message queues, and before you know it, your simple microservice based business logic has become a complex distributed system mesh including careful cache invalidation logic.

But what if this complexity isn't inevitable? What if it's actually the result of a historical mistake that became "best practice"?

## Challenging the Stateless Dogma

This talk challenges a fundamental assumption of modern web architecture: that stateless services are superior for scalability. I'll demonstrate that this belief, born from the constraints of early web servers, is now actively harmful to both performance and developer productivity. The truth is: separating logic from state (the core of stateless architecture) creates most of the complexity we fight daily. Every database query, every cache lookup, every message queue: they're all workarounds for the fact that we threw away our object's state after each request.

## Key Takeaways

- Stateless isn't a virtue, it's a workaround: modern systems can and should maintain state efficiently across requests.
- Your objects can be the cache: when objects persist in distributed memory, explicit caching becomes redundant.
- Scale by writing normal Python code: the same object-oriented patterns work from prototype to web-scale.
- Performance through simplicity: eliminating layers of infrastructure translation improves both latency and throughput.
- Focus on business logic, not plumbing: let the framework handle distribution, persistence, and failover.

## Who Should Attend

Python developers who:

- are building or maintaining web services,
- have experienced the pain of cache invalidation,
- want to scale without changing their programming model,
- are curious about alternatives to microservices.

## A Paradigm Shift

Just as we moved from manual memory management to garbage collection, it's time to move on from manual state management. Your Python objects should live as long as they're needed, not just for the duration of a request. This isn't theoretical. Systems using this approach power gaming platforms with millions of concurrent users, financial systems requiring microsecond latency, and IoT platforms managing billions of devices. The technology exists. We just need to unlearn the "stateless is good" mantra.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BQYTVM/>

## 10. [How to mix conda and pip without causing “environmental” damage.](https://pretalx.com/pyconde-pydata-2026/talk/7H9DF8/)

**Speakers**: [Mahe Iram Khan](https://pretalx.com/pyconde-pydata-2026/speaker/GY9UGD/)

**When and where**: Tuesday, 2026-04-14, 14:30–15:00, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Ever mixed conda and pip and ended up with a broken conda environment, yet, swear it worked before? This talk explains why! Learn the difference between pip and conda, what happens when you mix them and how to combine them safely using the latest community developed tools and updates in conda.

**Description** (verbatim):

Users frequently run `pip` inside their `conda` environments, sometimes successfully, sometimes with unintentional consequences. Confusing errors and broken environments often lead users to ask: when is it safe to use `pip` in a `conda` environment, and when is it not?

In this presentation I will answer this question.

I will begin by discussing the differences between `pip` and `conda` (a question conda maintainers get asked a lot!), starting with the specific use-cases of both tools.
This will include an “enlightenment” moment: `pip` and `conda` solve slightly different problems, one is a Python package installer, the other is a language agnostic package and environment manager.

I will then explain the differences between `.conda` packages, tarballs, and Python wheels, revealing how these format differences make interoperability difficult and mixing tools unreliable.
Users end up mixing `pip` and `conda` because sometimes the packaging ecosystem leaves them no other choice. Users often report, "I tried installing a package with `conda`, but it didn't work, so I ran `pip install` instead and it worked”. This mixing, sadly, has consequences, which I refer to as “environmental damage”.
I will highlight this damage in my talk.

`pip` and `conda` are two separate ecosystems but over time many community efforts (most recent being `conda-pypi`), have tried to improve interoperability. I will explain how the latest updates in `conda` along with the features in `conda-pypi` have now made it possible to `conda install` Python wheels from PyPI directly into `conda` environments. Thereby bringing us a step closer to better interoperability.

I will conclude the presentation with best-practice recommendations for using `pip` and `conda` together.
By the end of this presentation, users will have learned when to use `pip`, when to use `conda`, why they are different and how to combine them safely.

Here is a link to the conda-pypi repository on GitHub: https://github.com/conda-incubator/conda-pypi

Time outline of the presentation:
3 mins- self introduction and introduction to the topic (what to expect)
5 mins- difference between pip and conda and their use cases
10 mins- different package formats, problems with mixing pip and conda
5 mins- wheels support feature in conda-pypi and updates in conda
5 mins- how it helps users and best practices
2 mins- closing remarks

**Links**:

- [Slides](https://docs.google.com/presentation/d/1XDSMG0V0zQByrjuL2H3YA3hqEYOvSsXqC5uDZLXwp-8/edit?usp=sharing)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/7H9DF8/>

## 11. [Destructive Testing: 10 Practical Ways to Expose Hidden Application Risks](https://pretalx.com/pyconde-pydata-2026/talk/YKQ33N/)

**Speakers**: [Pascal Puchtler](https://pretalx.com/pyconde-pydata-2026/speaker/WMUYJV/)

**When and where**: Tuesday, 2026-04-14, 15:10–15:55, room Titanium [2nd Floor]

**Type**: Talk (long) — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Modern applications rarely fail in obvious ways. Instead, they break at the edges: unexpected inputs, race conditions, misused APIs, and assumptions nobody realized they were making. This talk presents ten practical and repeatable ways to intentionally break an application, using a QA mindset with a strong Python focus.

The session is designed to help QAs sharpen their investigative approach and move beyond happy-path testing, while giving developers concrete insight into where real-world failures often originate. Each “way to break an application” highlights a common risk area such as data handling, state management, timing, configuration, or integration boundaries.

Attendees will learn how to think more destructively (in a productive way), design better tests, and recognize fragile design decisions earlier. The goal is not to assign blame, but to improve collaboration and software quality by understanding how systems actually fail in practice.

**Description** (verbatim):

Quality assurance is not about confirming that software works — it is about discovering how it fails. This talk explores ten concrete ways to break an application on purpose, based on real-world testing patterns and common failure modes seen in modern software systems.

The focus is on practical thinking, not theory. While Python is used as the primary example language for test automation and experimentation, the concepts apply to any technology stack. The session is relevant for QAs, test engineers, and developers who want to build more resilient systems and improve cross-discipline collaboration.

Goals of the Talk

- Improve destructive testing and exploratory thinking for QAs
- Help developers understand common blind spots in application design
- Demonstrate how Python can be used effectively to probe system weaknesses
- Encourage a shared quality mindset across roles

Source: <https://pretalx.com/pyconde-pydata-2026/talk/YKQ33N/>

## 12. [Pair & Share: How formal Mentoring pushed REWE Analytics to a new level](https://pretalx.com/pyconde-pydata-2026/talk/HKFCBM/)

**Speakers**: [Axel Buddendiek](https://pretalx.com/pyconde-pydata-2026/speaker/8CDX7B/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Titanium [2nd Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

As one of Europe’s largest retail corporations, REWE Group owns and manages prominent supermarket chains such as REWE and PENNY, among many other subsidiaries. In this talk I will give a brief overview of how we introduced a formal mentoring program, Pair & Share, at the central analytics department of REWE Group with its more than 150 data scientists, engineers, analysts and other colleagues.

Before Pair and Share, there was no formal process for personal, technical or methodological growth. Although there are plenty of possibilities, further training and education was self-organized and fragmented. To increase growth among our colleagues and build and strengthen inter-team exchange, we introduced the formal mentoring program, Pair & Share.

This talk will cover a brief overview of REWE Group and our analytics department followed by a motivation for Pair & Share. Afterwards I will explain how we planned the mentoring program and defined the parameters like the matching process, the time frame and how to recruit participants. I will also share my experiences of the first six months of mentoring, what kind of roadblocks but also pleasant surprises we encountered. The talk will be concluded with an outline of how we plan to continue and improve the program.

**Description** (verbatim):

Did you ever wonder how to bring your analytics department to the next level? Do you want to help colleagues to network, learn or pass on their knowledge? And did you ever want to start your own mentoring program in a large corporation? Think no more, as I will describe in detail how we set up a mentoring program, Pair & Share, in REWE Group’s analytics department, with its 150 data scientists, data engineers, analysts and other data people. As one of Europe’s largest retail corporations, REWE Group owns and manages prominent supermarket chains such as REWE and PENNY, among many other subsidiaries. However, before Pair and Share there was no formal process for personal, technical or methodological growth within REWE Analytics. Although there are plenty of possibilities, further training and education was self-organized and fragmented. To increase growth among our colleagues and build and strengthen inter-team exchange, we introduced the formal mentoring program, Pair & Share.

This talk will cover a brief overview of REWE Group and our analytics department, who we are and what we do. This is followed by a description of why, while we found personal growth and training to be fine, we realized that we could do better with Pair & Share. Afterwards, I will explain how we planned the details of the mentoring program and defined the parameters like the matching process, time frame and how to recruit participants. As the first iteration of mentoring comes to an end in March 2026, I will share my experiences of the first six months of mentoring. This will include the kind of roadblocks we faced, how participants shaped their own mentoring experience and what pleasant surprises we encountered. As we measured participant satisfaction with regular pulse checks as well as many feedback sessions, I will conclude the talk with an overview of what went well and how we plan to do better with the next iteration of mentoring.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/HKFCBM/>

## 13. [Building Trust in Your Data Pipelines with Observability](https://pretalx.com/pyconde-pydata-2026/talk/U9KQU9/)

**Speakers**: [Stefan Dienst](https://pretalx.com/pyconde-pydata-2026/speaker/NPTXJK/)

**When and where**: Tuesday, 2026-04-14, 17:10–17:40, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

In the daily work of a data engineer, building new data pipelines often takes priority, while maintaining them and ensuring their correctness becomes an afterthought. This focus can quickly turn into a pitfall: failures go undetected, incorrect data silently propagates, and complaints from stakeholders arrive before engineers notice any issues. In practice, incorporating observability into every new data pipeline helps avoid these problems and enables teams to steadily increase system complexity while maintaining trust and peace of mind.

In this talk, I introduce observability in the context of data pipelines, covering its three core pillars: metrics, alarms, and logs. We will explore concepts like the four golden signals, alarm fatigue and structured logging and how they apply to data pipelines. I will show easy to implement first steps and share real-world experiences, where improved observability helped uncover previously unknown incorrect behavior and build trust in data systems.

This talk is well suited for data engineers that had little exposure to observability and want to learn about strategies how to keep sane while managing a jungle of pipelines.

**Description** (verbatim):

This talk explores how observability can be applied to data pipelines to improve reliability, data quality, and confidence in complex data systems.

The talk begins with an introduction to observability in the context of data engineering. It explains the three core pillars: metrics, alarms, and logs, and discusses why observability is particularly important for data pipelines, where failures are often silent and correctness issues may only surface through stakeholder complaints.

The first section focuses on metrics. It demonstrates how straightforward it can be to instrument data pipelines with basic metrics using Python. The talk then discusses which metrics are worth monitoring, adapting established concepts such as the four golden signals to data engineering use cases. A concrete example based on a near–real-time event processing pipeline illustrates how fine-grained metrics can reveal systematic failures for specific event types.

The second section focuses on alerting. It addresses the challenge that engineers rarely have time to continuously inspect dashboards and therefore rely on alarms to surface important issues. The talk outlines what makes a good alarm, emphasizing that alarms should be actionable, reliable, and provide sufficient context for investigation. A scenario with excessive and noisy alarms is used to illustrate alarm fatigue and a strategy how to get out of such a situation is described.

The final section covers log messages and their importance to reason about how a pipeline ended up in a specific state. It discusses why logs are often difficult to work with in data pipelines, as they may contain a mixture of critical errors, informational messages, and low-level framework output. The talk introduces structured logging as a way to add context and make logs easier to search, filter, and aggregate. Examples include monitoring the distribution of log levels to uncover hidden issues and using centralized logging to identify dependencies between pipelines that are otherwise hard to detect.

The talk concludes by emphasizing how the three pillars of observability build trust in a data pipeline.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/U9KQU9/>

## 14. [Fight your garbage data: implementation of a pythonic data quality monitoring framework in PySpark](https://pretalx.com/pyconde-pydata-2026/talk/PFXR9G/)

**Speakers**: [Rostislaw Krassow](https://pretalx.com/pyconde-pydata-2026/speaker/7LKG3C/), [Joshua Finger](https://pretalx.com/pyconde-pydata-2026/speaker/SZXX8F/)

**When and where**: Tuesday, 2026-04-14, 12:25–13:10, room Helium [3rd Floor]

**Type**: Talk (long) — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The timeless phrase “garbage in, garbage out” is even more important today with the growing usage of non-deterministic generative neuronal networks, which amplifies the effect of bad data quality. This presentation describes Data Quality Monitor — a tool to bring transparency into data quality and help drive real improvements.

In the talk, we'll cover what defines a successful data quality monitoring solution and share findings from our initial evaluation of available open-source frameworks. Next, we'll showcase our implementation based on DQX. DQX is a lightweight, open-source framework for performing row-level data quality checks programmatically, with business rules organized in manageable YAML files. DQX, originally developed by Databricks Labs, integrates seamlessly with PySpark, making it easy and affordable to run data quality checks within our IoT data lake. Finally, we will discuss the organizational processes and structures required to effectively respond to data quality issues.

**Description** (verbatim):

In the talk we share our expirience from the project implemented in Q3 2025. We start with the motivation for the project, involved stakeholders and their needs. We will then define the criteria for a successful data quality monitoring solution and share findings from our evaluation of existing frameworks. We will also discuss why popular frameworks like Great Expectations or SODA did not meet our requirements.

Next, we will demonstrate our implementation based on DQX—a lightweight, open-source Python library designed for traceable, row-level data quality checks before and after data is persisted. DQX, developed and maintained by Databricks labs, allows developers to concentrate on the core implementation while providing business users YAML files for maintenance of business rules. Furthermore, DQX’s seamless integration with PySpark enables efficient and cost-effective quality monitoring within our IoT data lake.

Finally, we move beyond the code to the organisational reality. We will discuss how we embedded Data Quality Monitor into the organisation and share our opinion on the hard questions: who is responsible for maintaining rules? who monitors the results?

**Talk outline**

- Motivation for the project

  - Initial situation and objectives

- Framework evaluation

  - Evaluation criteria for a successful data quality monitoring

  - Comparison of available frameworks

- Our implementation with DQX

  - How to use built-in data quality checks

  - How to add custom data quality checks

  - Automated rule generation with DQX Profiler

  - Output and visualisation options

  - Python project structure

- Embedding in organisation

  - Rule maintenance

  - How to communicate data quality issues

- Summary

**Key takeaways**

- Understanding of most important criteria when choosing the framework for data quality monitoring from perspective of a data engineer and an architect

- Understanding of DQX framework

- Ideas how to integrate data quality monitoring into organisations.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/PFXR9G/>

## 15. [Hype, Hope, or Headache? Making Sense of GenAI, LLMs, and AI Agents with Anecdotal Evidence](https://pretalx.com/pyconde-pydata-2026/talk/WSNBD9/)

**Speakers**: [Sebastian Neubauer](https://pretalx.com/pyconde-pydata-2026/speaker/NEBKEY/)

**When and where**: Tuesday, 2026-04-14, 14:30–15:00, room Helium [3rd Floor]

**Type**: Talk — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

After nearly 20 years in data science, from MLPs, SVMs, and random forests to deep learning, I’ve seen many “revolutions” come and go. The current tectonic shift around GenAI and LLMs feels different from previous hype cycles. Even with some understanding how these things work, I am still blown away by the stream of stunning new capabilities. But they also introduce new kinds of risks that go far beyond technical performance. This talk offers a pragmatic, experience-driven perspective on GenAI in industrial settings, including supply chains and the emerging wave of AI agents. We’ll disentangle real opportunities from snake oil, especially where hype-driven promises meet senior management expectations. An anti-bullshit take on the possibilities ahead, with honesty, anecdotes, and (for those who know me, of course) a bit of humor.

**Description** (verbatim):

After nearly 20 years in data science I’ve seen many “revolutions” come and go: neural networks, SVMs, bayesian statistics, random forests, XGBoost and deep learning. Each came with bold promises, and each eventually settled into a realistic place in production systems (read: became boring). Generative AI, however, feels fundamentally different.

In this talk, I’ll share my view _why_ the current GenAI hype stands apart from previous cycles: technically, culturally, and organizationally. Even with some understanding how these things work, I am still blown away by the stream of stunning new capabilities. This is not a “GenAI is bad” rant. Instead, it’s a critical attempt to understand the shift we’re seeing, and the risks that come with it if we don’t adjust our thinking.

Using industrial examples such as supply chains (just because I work in this field), but also personal experience, I’ll show where LLM-based approaches still have serious limitations today, and where GenAI can realistically add value. We’ll disentangle different categories of risk from technical fragility, evaluation problems and mere costs to organizational overconfidence and misuse.

A big part of the talk dives into the rapidly emerging field of AI Agents. We’ll explore what AI agents actually are, where they make sense today, and where the current hype is just snake oil, particularly to senior decision-makers who may underestimate complexity, costs, and failure modes.

The goal of this talk is not to slow innovation, but to enable better decisions. If we want GenAI to be a success in real-world systems, we need to understand both the change it represents and the limits it still has.

An anti-bullshit take on the possibilities ahead, with honesty, anecdotes, and (for those who know me, of course) a bit of humor.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/WSNBD9/>

## 16. [Demystifying Parallel Programming in Python: from CPU to quantum processors, including GPU and TPU](https://pretalx.com/pyconde-pydata-2026/talk/HBFL78/)

**Speakers**: [Gaël Pegliasco](https://pretalx.com/pyconde-pydata-2026/speaker/HYCGGE/)

**When and where**: Tuesday, 2026-04-14, 15:10–15:55, room Helium [3rd Floor]

**Type**: Talk (long) — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

This talk provides a beginner-friendly overview of Python’s parallel programming ecosystem. You’ll discover the key libraries and techniques—JIT compilation, multithreading, multiprocessing, distributed computing, HPC/grid computing, and even a first look at quantum programming—to help you write faster, more efficient code, regardless of your hardware.

**Description** (verbatim):

# Demystifying Parallel Programming in Python

## Understanding the Hardware Basics

- A gentle introduction to modern processors: What are CPUs, GPUs, TPUs, and quantum processors?
- Essential terminology explained: cores, hyper-threading, cache memory, multithreading, multiprocessing, multitasking, SIMD, NUMA, and more—no prior knowledge required!

## Parallel Programming Techniques for Beginners

A practical overview of Python’s parallel programming tools, organized by approach:

- Just-In-Time (JIT) compilation: Speed up your code without changing your workflow
- Multithreading: Do more at once, and removing the GIL with Python 3.13+
- Multiprocessing: Use all your CPU cores
- Distributed computing: Scale your code across multiple machines
- Quantum programming: A first look at the future of computing

## Hands-On Examples

- JIT compilation made easy: PyPy, Numba, and JAX
- The GIL and Python 3.13: What’s changing and why it matters
- Distributed computing for everyone: Celery and Dask on HPC clusters
- GPU computing for beginners: CuPy, cuDF, and Numba
- Your first quantum “Hello World”: A taste of the quantum revolution

## Conclusion

By the end of this talk, you’ll have a clear map of Python’s parallel programming landscape.
No experience needed—just bring your curiosity and let’s explore together!

Source: <https://pretalx.com/pyconde-pydata-2026/talk/HBFL78/>

## 17. [Come for the Code, Stay for the People.](https://pretalx.com/pyconde-pydata-2026/talk/PK8XNB/)

**Speakers**: [Valerio Maggio](https://pretalx.com/pyconde-pydata-2026/speaker/S3GNBU/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Helium [3rd Floor]

**Type**: Talk — **Track**: General: Community & Diversity — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

"Come for the language, stay for the community." If you've been around Python long enough, you've heard this before. I don't know when I first heard it, but I know exactly when I understood it.

This talk is a personal reflection on seventeen years within the Python community—from my first tentative steps as a volunteer to organising conferences myself. It's a story about discovering that Python was always about more than code. It's about the people, the values, and the unexpected ways a community can shape a career and a life.

This isn't just my story. It's a story I've seen repeated in countless faces at registration desks, in hallway conversations, in first-time speakers finding their voice. I want to talk about what I've learned about kindness, mentorship, and the quiet power of feeling like you belong somewhere.

I'll end with an open question: as the ways we connect continue to evolve, how do we preserve what matters while welcoming a new generation?

If you're new to this community and wondering what all the fuss is about, this talk is especially for you.

**Description** (verbatim):

I have a confession to make: after seventeen years in the Python community and countless technical talks attended and organized, this is the first time I'm putting myself out there to talk about community itself. It feels vulnerable. It feels necessary.

**How it started**

My journey began the way many do—volunteering. Stuffing badge holders, directing people to rooms, answering the same question about Wi-Fi passwords a hundred times. It wasn't glamorous, but it was transformative. Volunteering was my first taste of what it means to contribute to something larger than myself, and it opened doors I didn't even know existed.

Back then, I came for the code. I had no idea I'd stay for the people.

**More than code**

Through seventeen years, the Python community taught me things I carry with me everywhere. Things that have nothing to do with syntax or libraries.

The value of patience and kindness when someone asks a "basic" question—because we were all beginners once. The importance of explicit inclusion, because "everyone is welcome" means nothing without deliberate action. The power of mentorship, both giving and receiving. The understanding that community health requires active maintenance, not passive hope.

This is what "stay for the people" actually means.

**Who this talk is for**

Having attended and organized Python conferences for years, I've noticed something consistent: there are always newcomers. People experiencing their first Python event, unsure of what to expect, wondering if they belong. This talk is for them.

But it's also for anyone thinking about community engagement—whether in Developer Relations, open source maintainership, or simply as someone who cares about the spaces they inhabit.

**Looking forward**

I don't have all the answers. I want to end with questions rather than conclusions. How do we engage with a generation that communicates differently? How do we preserve depth in an age of fragmented attention? What can newcomers teach us about building community in ways we haven't imagined?

My hope is that this talk sparks conversations that continue long after I leave the stage. And honestly? I hope to revisit this topic in ten years and see how wrong—or right—we were.

**Links**:

- [Slides](https://speakerdeck.com/leriomaggio/come-for-the-code-stay-for-the-commnunity)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/PK8XNB/>

## 18. [Reaching the next level of abstraction: meta classes and what they enable](https://pretalx.com/pyconde-pydata-2026/talk/EE39VN/)

**Speakers**: [Valentin Zieglmeier](https://pretalx.com/pyconde-pydata-2026/speaker/8BUF9Y/)

**When and where**: Tuesday, 2026-04-14, 11:45–12:15, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyCon: Python Language & Ecosystem — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python is especially powerful due to its deep meta programming capabilities. In this talk, I give an overview of one example: meta classes. I show how you can use them to customize class creation, ensure data integrity, or define your own syntactic sugar for classes.

**Description** (verbatim):

Python is accessible and easy, but what makes it especially fun and powerful are its deep meta programming capabilities. One salient example are meta classes, which allow us to deeply hook into the class creation process. But, they seem quite complex at first glance, which may have deterred you so far from exploring them. In my talk, I want to alleviate your uncertainty and give you concrete examples of how meta classes work and what they enable you to do. We will look at using them to customize class creation, ensure data integrity by adding custom validators, or defining custom syntactic sugar that reduces boilerplate.

Outline:

- Programming and meta programming
- Everything is an object
- Higher-order functions
- Meta class basics: customizing class creation and enforcing constraints
- Advanced example: custom syntactic sugar
- With great power comes great responsibility

Source: <https://pretalx.com/pyconde-pydata-2026/talk/EE39VN/>

## 19. [Exploring Germany's Urban Geography with Census and OpenStreetMap Data](https://pretalx.com/pyconde-pydata-2026/talk/WQGXJ3/)

**Speakers**: [Travis Hathaway](https://pretalx.com/pyconde-pydata-2026/speaker/HA3SES/)

**When and where**: Tuesday, 2026-04-14, 12:25–13:10, room Platinum [2nd Floor]

**Type**: Talk (long) — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

When conducting studies of the urban form, an important resource many researchers turn to is the massive OpenStreetMap dataset. But, as extensive as this dataset is, it lacks one very important aspect about the cities it covers: the people who live there. In this talk, I show you how to add this missing element to your research by bringing in German Census data to create rich analysis capable of answering some of the most pressing issues facing our cities today. I exemplify this by walking you through my own research in urban geography and sustainability with a study of how equitably distributed emergency care hospitals are in cities across Germany. Throughout, we look at how Python and PostgreSQL can be used as effective tools to enable this research and keep it organized.

**Description** (verbatim):

By the end of this talk, audience members will be empowered with the tools they need to help identify and bring light to important problems affecting their cities. To achieve this, I show how to combine data on urban structure from OpenStreetMap and demographic data from the German Census in PostgreSQL. Once the data is gathered, I then show how to do the actual analysis and present the findings with Python.

The presentation will be broken up into the following sections:

**Laying the foundation**

The first step is creating an organized database that will serve as the data source for the rest of the study. I show how to use "PgOSM Flex" for this plus a tool that I wrote in Python to make it easy to import German Census data into PostgreSQL.

**Asking meaningful questions**

With all the data in place, it's time to formulate a research question to drive our analysis. Formulating a meaningful research question can keep our analysis on track and much better organized. To get there, we explore the data we have available and consider the types of questions we can actually answer.

**Analyze and present**

Now that we have a clear question in mind, we'll construct the queries we need to generate the data necessary for our analysis. Once exported from PostgreSQL, we perform the analysis and generate the final reports using popular scientific libraries in Python.

**Final thoughts**

To conclude the talk, I share how this analysis could be extended by including even more datasets. I also discuss the limitations of these types of studies while offering practical advice on how you can make a positive impact with your research.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/WQGXJ3/>

## 20. [Making my Apache Spark™ talk more interesting using AI](https://pretalx.com/pyconde-pydata-2026/talk/KBGXKC/)

**Speakers**: [Celeste Horgan](https://pretalx.com/pyconde-pydata-2026/speaker/KVW9PZ/)

**When and where**: Tuesday, 2026-04-14, 14:30–15:00, room Platinum [2nd Floor]

**Type**: Sponsored Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Writing talks is hard, but being a good conference speaker is even harder. Resultantly, this talk is recursive: I'll take a talk previously written for a London data science meetup on using Apache Spark and Apache Kafka to build ML data processing pipelines, and revamp it using Snowflake's Cortex Code CLI!

**Description** (verbatim):

In this talk, we'll walk through a basic Apache Spark data pipeline which reads in an image dataset, processes it, and detects raccoons. That said, sponsored talks are always boring: let's see what we can do to spice things up using AI! We'll use Snowflake's Cortex Code CLI coding agent together to improve the talk live, taking suggestions from the audience as we go!

Attendees to the talk can expect to learn the following:

- What Apache Spark is, what it excels at, and how to set up a basic cluster
- How to use HuggingFace ViT (vision transformer) to run a basic computer vision setup
- A little bit about Snowflake's new coding agent, Cortex Code CLI (the part where we advertise at you, but I promise it will be fun)
- Building a basic Streamlit app
- .. and whatever other fun we get up to together!

Join for a session full of fun experimentation with interesting tools – and learn a bit about data pipelines too! This session is suitable for beginner to intermediates!coding agent, live!

Source: <https://pretalx.com/pyconde-pydata-2026/talk/KBGXKC/>

## 21. [AsyncIO vs Threads: who survives in the No-GIL Era?](https://pretalx.com/pyconde-pydata-2026/talk/UUHYUS/)

**Speakers**: [Igor Anokhin](https://pretalx.com/pyconde-pydata-2026/speaker/NXW3BB/)

**When and where**: Tuesday, 2026-04-14, 15:10–15:40, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyCon: Python Language & Ecosystem — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AsyncIO vs threads isn't about "which is faster" - it's about scheduling, memory, and the kind of load you run. We'll unpack what threads and asyncio do under the hood (OS scheduler vs event loop + epoll), run practical benchmarks, and show why many "async" libraries still rely on thread pools (aiofiles, Motor, Django bridges). Then we'll repeat the same tests on Python 3.14's free-threaded (no-GIL) build and discuss when an interpreter upgrade can beat an async rewrite.

**Description** (verbatim):

Concurrency in Python is full of stereotypes: "threads are useless because of the GIL", "async is always faster", "just make everything async". This session replaces opinions with mechanics and measurements, and updates the story for Python 3.14's free-threaded (no-GIL) build.

What we'll cover

1. How things actually work under the hood

- A Python thread is an OS thread (pthread_create/clone). The OS scheduler runs it like any other thread - the GIL only matters when Python bytecode executes.
- asyncio is also scheduling: one OS thread, many Tasks, cooperative switching at await, and readiness notifications via epoll/select.

2. Why IO-heavy workloads often look "equally fast" in threads and asyncio

- both models hide IO latency by switching while waiting;
- the real difference shows up in scalability and cost: per-thread memory/stack + OS limits vs lightweight Tasks.

3. When "async" is secretly a thread pool

- aiofiles delegates file operations to run_in_executor();
- Motor (async MongoDB driver) runs the synchronous PyMongo core in a ThreadPoolExecutor;
- frameworks like Django must bridge sync and async worlds (sync_to_async), adding overhead and sharp edges.

4. Benchmarks that mirror real services

- 100 / 1,000 / 10,000 concurrent IO waits: why "10k threads" fails but "10k tasks" is fine;
- memory and CPU overhead comparison (what you pay for concurrency);
- a microservice-style endpoint (FastAPI-like) in sync/threaded vs async mode.

5. What changes with free-threading (no-GIL)

- a high-level view of what CPython changes to make it possible;
- rerunning the same benchmark with and without the GIL;
- when an interpreter upgrade can deliver "async-rewrite-level" gains for mixed CPU+IO workloads.

Takeaways

- a practical checklist for choosing threading vs asyncio vs multiprocessing;
- performance vs resource-usage intuition you can apply to real services;
- guidance on how to read "async" claims in library docs.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/UUHYUS/>

## 22. [The Art of the Optimal: A Pythonic Approach to Complex Decision-Making](https://pretalx.com/pyconde-pydata-2026/talk/JPTTMK/)

**Speakers**: [Justine Broihan](https://pretalx.com/pyconde-pydata-2026/speaker/PUH8YU/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Platinum [2nd Floor]

**Type**: Sponsored Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

As Python developers, we frequently tackle complex decision-making problems by writing custom scripts and heuristic algorithms. While a standard greedy algorithm might provide a quick, intuitive fix, it rarely finds the best possible solution—often leaving significant efficiency, performance, and cost-savings on the table.

In this talk, we will explore the untapped power of mathematical optimization. We will start with a classic operations challenge. You will see firsthand how a standard rule-based Python heuristic compares to a mathematical optimization model, and how rigorously defining constraints and objectives can guarantee a globally optimal solution.

But optimization isn't just for traditional logistics! We will also bridge the gap to Machine Learning. We will demonstrate how optimization techniques can be utilized as a powerful verification step for ML models, such as calculating the minimum pixel changes required to trick a neural network into a misclassification.

While we can only scratch the surface of these vast topics, you will walk away with a fresh perspective on problem-solving. Whether you are automating business operations or building robust ML pipelines, you will learn when to graduate from basic heuristics and start leveraging the "art of the optimal".

**Description** (verbatim):

As Python developers, we frequently tackle complex decision-making problems by writing custom scripts and heuristic algorithms. While a standard greedy algorithm might provide a quick, intuitive fix, it rarely finds the best possible solution—often leaving significant efficiency, performance, and cost-savings on the table.

In this talk, we will explore the untapped power of mathematical optimization. We will start with a classic operations challenge: the Paintshop Problem. You will see firsthand how a standard rule-based Python heuristic compares to a mathematical optimization model, and how rigorously defining constraints and objectives can guarantee a globally optimal solution.

But optimization isn't just for traditional logistics! We will also bridge the gap to Machine Learning. We will demonstrate how optimization techniques can be utilized as a powerful verification step for ML models, such as calculating the minimum pixel changes required to trick a neural network into a misclassification.

While we can only scratch the surface of these vast topics, you will walk away with a fresh perspective on problem-solving. Whether you are automating business operations or building robust ML pipelines, you will learn when to graduate from basic heuristics and start leveraging the true "art of the optimal."

Source: <https://pretalx.com/pyconde-pydata-2026/talk/JPTTMK/>

## 23. [Type Errors for Better Agent-Assisted Development](https://pretalx.com/pyconde-pydata-2026/talk/8YGQZC/)

**Speakers**: [Kyle Into](https://pretalx.com/pyconde-pydata-2026/speaker/ZDYGBP/)

**When and where**: Tuesday, 2026-04-14, 17:10–17:40, room Platinum [2nd Floor]

**Type**: Sponsored Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Type annotations aren't just for humans anymore. As AI coding agents write more Python, type checkers offer something unique: fast, concrete diagnostics about what went wrong and where. In this talk, I explore connecting Pyrefly to Claude Code, feeding type errors back to the agent as it works, and whether this is the missing feedback signal for agentic development.

**Description** (verbatim):

As AI coding agents take on larger Python tasks, a practical question emerges: what's the best way to catch the bugs they introduce? Tests are thorough but slow. Linting is fast but shallow. Type checking occupies an interesting middle ground: deep enough to catch semantic errors, fast enough to run on every edit, and concrete enough to tell the agent exactly what to fix.

In this talk, I explore connecting Pyrefly, a Python type checker built at Meta, to Claude Code. I'll walk through integration options and discuss practical considerations like token costs and setup complexity. Whether you're building tools for AI agents or using them in your daily work, you'll leave with a clearer picture of where type checking fits in the agentic development loop.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/8YGQZC/>

## 24. [Kickstart Coding at Scale: How Project Template Automation Unlocks Developer Productivity](https://pretalx.com/pyconde-pydata-2026/talk/AWFFUS/)

**Speakers**: [Yannik Tausch](https://pretalx.com/pyconde-pydata-2026/speaker/EHUYXK/)

**When and where**: Tuesday, 2026-04-14, 11:45–12:15, room Europium [3rd Floor]

**Type**: Sponsored Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

As your company grows, so does your software landscape. Different CI configurations, inconsistent linting rules, varying packaging approaches: every new project reinvents the wheel. Scaffolding tools like cookiecutter help with the initial setup — but what happens six months later, when best practices have evolved, and your template has moved on? That’s where most approaches fall apart. And a centralized, “magic” pipeline is no better — it’s opaque, brittle, and leaves no room for customization. Using Copier, we built a standardized yet customizable project template — a paved road that guides developers without boxing them in. But the real game changer is what comes after: Copier’s built-in update mechanism lets us propagate template improvements to hundreds of existing projects. A GitHub bot runs monthly, opens Pull Requests with the latest changes, and a Streamlit dashboard tracks adoption across the organization. Attendees will learn how to build flexible templates, automate ongoing maintenance at scale, and manage version drift — so developers can focus on writing code instead of fighting boilerplate.

**Description** (verbatim):

**The Problem**
As organizations scale, their repository count grows — and with it, the diversity of project setups. Different CI configurations, inconsistent linting rules, varying packaging approaches: every new project reinvents the wheel. Developers spend valuable time on boilerplate instead of writing code. Another approach — a centralized, "magic" build pipeline — trades one problem for another: it's opaque, brittle, and leaves no room for project-specific needs. We illustrate this with a concrete example: pre-commit configuration.

**A Paved Road with Copier**
The Python tool Copier goes beyond one-time scaffolding — it’s a lifecycle management tool. When the template evolves, copier update merges improvements into existing projects, respecting local customizations. This is what sets it apart from cookiecutter and similar tools. We built an internal project template that generates CI workflows, pre-commit configuration, conda packaging, documentation scaffolding, and more — all customizable through simple yes/no questions during setup. Crucially, projects can deviate from the template whenever needed, without breaking the update mechanism. This section includes a live demo.

**Automated Migration at Scale**
A template is only useful if projects stay up to date. We built a GitHub bot that runs monthly across all repositories in our organization, executes copier update, and opens Pull Requests with the changes. Merge conflicts are minimized by encouraging teams not to diverge too far from the template. For the conflicts that do arise, mergiraf helps with resolution — but maintainers may still need to step in.

**Tracking Progress with a Dashboard**
To answer "how many projects are up-to-date?", we built a Streamlit dashboard that shows the template version for each repository, with search filters and charts. This gives the team visibility into adoption progress and helps identify repositories that are falling behind.

**Lessons Learned**
We share practical lessons from rolling this out across a large organization — what worked, what's still challenging, and where we see current limitations.

**Takeaways**
Attendees will learn how to:

- Use Copier to create and continuously update project templates that standardize without locking developers in.
- Automate template updates across repositories via a GitHub bot and automated Pull Requests.
- Use a dashboard to track which projects are up-to-date and which are lagging.
- Reduce "boilerplate fatigue" so teams can focus on shipping code.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AWFFUS/>

## 25. [Programming Quantum Networks in Python](https://pretalx.com/pyconde-pydata-2026/talk/NF7MKB/)

**Speakers**: [Samuel Oslovich](https://pretalx.com/pyconde-pydata-2026/speaker/WWGHWA/)

**When and where**: Tuesday, 2026-04-14, 12:25–13:10, room Europium [3rd Floor]

**Type**: Invited Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Quantum networks connect quantum devices including quantum computers, enabling applications not realizable in classical networks, such as secure quantum computing in the cloud and quantum key distribution. These networks are now moving from theory to reality, and as part of the Quantum Internet Alliance, we are actively building a prototype quantum network in Europe, driven by applications developed in Python.

In this talk, we will introduce quantum networking and demonstrate how to program quantum network applications in Python by walking through the quantum teleportation protocol. We'll conclude by sharing resources so that you can begin experimenting with quantum network programming yourself. No prior quantum experience required.

**Description** (verbatim):

Quantum networks connect quantum devices including quantum computers, enabling applications not possible in classical networks, such as secure quantum computing in the cloud and quantum key distribution. These networks are now moving from theory to reality, and as part of the Quantum Internet Alliance, we are actively building a prototype quantum network in Europe, driven by applications developed in Python.

Even though quantum systems are governed by the rules of quantum mechanics, you don't need to be an expert in quantum physics to start programming them!

Developing applications for quantum networks reveals new challenges. For example, unlike in classical networks where data is copied and retransmitted, quantum information cannot be copied. Once lost, it is irretrievable. This motivates a new networking primitive for transferring data, the quantum teleportation protocol.

In this talk, we will walk through the quantum teleportation protocol step-by-step using the NetQASM SDK and the SquidASM simulator, Python tools developed by our research group for quantum network programming and simulation. We'll conclude by sharing resources so that you can begin experimenting with quantum network programming yourself. No prior quantum experience required.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/NF7MKB/>

## 26. [From Hard Problems to Proven Solutions: Solving Decision Problems with Gurobi](https://pretalx.com/pyconde-pydata-2026/talk/333HDN/)

**Speakers**: [Silke Horn](https://pretalx.com/pyconde-pydata-2026/speaker/WHE7N9/)

**When and where**: Tuesday, 2026-04-14, 14:30–15:00, room Europium [3rd Floor]

**Type**: Sponsored Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Join us as we demonstrate how to formulate and solve hard decision problems with Gurobi. You’ll learn practical modeling techniques that integrate naturally with NumPy, SciPy.sparse, and pandas. We’ll show how mathematical optimization computes reliable solutions with provable guarantees — enabling robust, transparent decision-making.

**Description** (verbatim):

Many real-world applications require making the best possible decisions under complex constraints — whether in scheduling, resource allocation, routing, or planning. These problems quickly become difficult as the number of interacting choices grows.

This session introduces mathematical optimization as a practical tool for solving such problems. Using Gurobi, we demonstrate how to formulate decision problems and compute solutions that satisfy all constraints and come with clear guarantees about their quality.

You’ll see how to express optimization models using familiar data structures such as NumPy arrays, SciPy.sparse matrices, and pandas DataFrames.

By the end of the session, you’ll have an understanding of how to approach modeling and solving complex decision problems — and how optimization can be used to support reliable, data-driven decisions.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/333HDN/>

## 27. [Python in Climate Tech: Vehicle-to-Grid](https://pretalx.com/pyconde-pydata-2026/talk/QVLTKD/)

**Speakers**: [Christopher Sedlaczek-Bock](https://pretalx.com/pyconde-pydata-2026/speaker/JPCWXQ/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Europium [3rd Floor]

**Type**: Sponsored Talk — **Track**: General: Others — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

This talk dives into how Python helps us to bridge the gap between automotive and energy industries. Learn how Python helps in enabling Vehicle-to-Grid and therefore the bi-directional integration of EV batteries into the power grid, enabling further use and growth of renewable energies, stabilizing power grids and enhancing the accessibility of electric mobility.

**Description** (verbatim):

At The Mobility House Energy, our mission is to enable a zero-emission future by connecting the worlds of mobility and energy. By intelligently integrating electric vehicle batteries into the power grid, we unlock flexibility that supports renewable energy expansion, enhances grid stability, and makes electric mobility more accessible and affordable.

In this talk, we share how Python became a key enabler on our journey to delivering Vehicle-to-Grid solutions at scale. From early simulations and prototyping to operating production-grade energy systems, Python supports us across the entire development lifecycle. It allows us to rapidly validate ideas, process and analyze complex energy and mobility data, and deploy robust services that are battle-tested in the real-world and on energy markets.

We will also explore how adopting Python in production reshaped our collaboration model. Data scientists and software engineers now work closer together, sharing tools, codebases, and responsibilities. At the same time, we will openly discuss the technical and organizational challenges we encountered—from performance bottlenecks to system integration—and the practical solutions that helped us overcome them.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/QVLTKD/>

## 28. [Solving Marketplace Cold Start at Scale with Ranking](https://pretalx.com/pyconde-pydata-2026/talk/GVHZW9/)

**Speakers**: [Theodore Meynard](https://pretalx.com/pyconde-pydata-2026/speaker/EZMJWT/)

**When and where**: Tuesday, 2026-04-14, 11:45–12:15, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Cold start is a critical bottleneck for marketplaces: new items lack behavioral signals and reviews, so ranking models under-expose them, delaying the very signals needed to rank them well. This talk shares practical solutions developed at scale for a travel marketplace, including guaranteed exposure at key positions, efficient real-time re-ranking, and targeted boosting for unactivated items. Attendees will learn how experiment-driven iteration shaped a robust system that accelerates early traction for new items without sacrificing overall marketplace health.

**Description** (verbatim):

Cold start cripples two‑sided marketplaces: new items lack behavioral signals and social proof, ranking models under‑expose them, which delays the very signals needed to rank them well. This talk shares our journey to break down this loop at GetYourGuide, a marketplace for travel experiences. We evolved our exploration/activation framework over the past three years with three complementary interventions: guaranteed exposure at strategic positions, a real‑time reranker to allocate that exposure efficiently under tight latency budgets, and guardrail boosting for unactivated items when primary assessment slots are empty.

The talk is a pragmatic case study: we’ll show how experiment‑led exploration shaped the system over the last 3 years. We will share what worked, what did not, and how we managed trade-offs between short-term revenue and long-term marketplace health. Attendees will leave with a blueprint for safely accelerating early traction in their own marketplaces, combining learning‑to‑rank with exposure guarantees without sacrificing overall business health.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GVHZW9/>

## 29. [Personalized Restaurant Recommendations at Scale combining Transformer with Gradient-Boosted Ranking](https://pretalx.com/pyconde-pydata-2026/talk/DVCKHF/)

**Speakers**: [Marcel Kurovski](https://pretalx.com/pyconde-pydata-2026/speaker/AA99AD/), [Steffen Klempau](https://pretalx.com/pyconde-pydata-2026/speaker/8BCJ9W/)

**When and where**: Tuesday, 2026-04-14, 12:25–13:10, room Palladium [2nd Floor]

**Type**: Talk (long) — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Wolt’s Universal Venue Ranker (UVR) is a large-scale, sequence-aware ranking model for personalized restaurant recommendations, deployed across more than 30 countries. UVR replaces three previously independent models—Neural Collaborative Filtering, a second-pass ranker, and a first-time-user model—by combining a transformer with a gradient-boosted decision tree for ranking.

The model follows a two-stage design. In the first stage, an encoder-style transformer learns a personalized user state representation from historical restaurant purchase sequences enriched with spatiotemporal signals such as time and location. In the second stage, a CatBoostRanker uses the transformer output as an input feature alongside additional user-, venue-, user–venue-, and delivery-specific features to score and rank candidate venues.

In this talk, we present the model and service architecture, the training and evaluation setup, and both offline and online results from a multi-country online A/B test, demonstrating significant improvements in global conversion rate and new venue trial rate. We also share practical lessons from deploying and operating a multi-stage ranking model under strict latency constraints at global scale.

**Description** (verbatim):

Personalized restaurant ranking is a core machine learning problem in food delivery platforms, requiring models to balance relevance, exploration, latency, and robustness across highly heterogeneous markets. In this talk, we present UVR (Universal Venue Ranker), Wolt’s production ranking model for restaurant recommendations, currently deployed in more than 30 countries.

UVR unifies the capabilities of three previously separate models—Neural Collaborative Filtering (NCF), a second-pass ranker, and a first-time-user (FTU) model—into a single, sequence-aware ranking approach. Beyond improving recommendation quality, this consolidation significantly reduced model complexity, operational overhead, and long-term maintenance cost.

The model follows a two-stage architecture implemented using widely adopted Python-based machine learning technologies, including PyTorch, CatBoost, and Flyte. The first stage is an encoder-style transformer trained with a classification loss on a next-purchase prediction task. It learns a compact user state representation from historical restaurant purchase sequences enriched with spatiotemporal information, such as purchase time and user location. This stage outputs a personalized venue relevance score.

The second stage is a CatBoostRanker, trained with a learning-to-rank loss on grouped venue requests. It combines the transformer-derived score with a rich set of additional features, including user-specific attributes, venue metadata, user–venue interaction features, and delivery-related signals. This separation of objectives—classification for representation learning and ranking for final scoring—proved critical for both model performance and training stability.

We will walk through the end-to-end training and evaluation pipeline, covering feature construction, offline validation using ranking metrics, and a multi-country online A/B testing setup. UVR delivered significant and substantial improvements in global conversion rate and new venue trial rate, a key driver of long-term user retention. We will discuss how offline improvements translated into online gains.

A dedicated section of the talk focuses on production and serving architecture, including low-latency inference and orchestration of training and deployment workflows using Flyte. We also share hard-earned lessons from training a multi-stage ranking model, such as preventing data leakage between models trained with different objectives and on different data as well as handling cold-start.

Finally, we outline our roadmap toward extending UVR into a cross-domain ranking model for both restaurants and stores, enabling knowledge transfer across domains while preserving strong personalization guarantees.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/DVCKHF/>

## 30. [What Breaks When Automatic Speech Recognition Systems Go Multilingual](https://pretalx.com/pyconde-pydata-2026/talk/LYCBNT/)

**Speakers**: [Rashmi Nagpal](https://pretalx.com/pyconde-pydata-2026/speaker/8RV9AV/)

**When and where**: Tuesday, 2026-04-14, 15:10–15:55, room Palladium [2nd Floor]

**Type**: Talk (long) — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Building machine learning models for audio deepfake detection seems straightforward until datasets span multiple languages, such as Hindi, Korean, Mandarin, and German. In practice, multilingual Automatic Speech Recognition (ASR) systems often fail in production because language-specific acoustic variations and assumptions about the processing pipeline break down at scale.

This talk examines the engineering challenges of building a multilingual deepfake detection system using a Python-centric pipeline. It covers practical issues encountered during large-scale audio preprocessing, including memory-efficient data loading, resumable feature-extraction workflows, and validation strategies designed to prevent cross-lingual leakage. The session also shares lessons from deploying a multilingual ASR-based system, with a focus on pipeline structure, evaluation correctness, and operational robustness in real-world settings.

**Description** (verbatim):

In a multilingual Automatic Speech Recognition (ASR) dataset containing over 440,000 audio samples, preprocessing methods that were effective for one language often failed silently for others. This resulted in shifts in acoustic features, misleading validation outcomes, and prolonged jobs that failed due to assumptions that held true only in monolingual contexts. This presentation examines the issues that arise when extending ASR systems to multilingual data, using a real-world deepfake detection system that includes Hindi, Korean, Mandarin, and German. It addresses the engineering challenges encountered while developing and operating a Python-based pipeline at scale.

The session will discuss practical issues in large-scale audio processing, including the creation of memory-efficient data loaders, the design of workflows that support resumable preprocessing and feature extraction, and strategies for managing long-running jobs to avoid redundant computations. Additionally, it will cover validation strategies for multilingual ASR systems, emphasizing that language imbalance and shared pipelines can lead to cross-lingual leakage, which skews evaluation results if not explicitly addressed.

Key takeaways include:

1. Multilingual ASR pipelines reveal language-specific issues that are not present in monolingual systems.
2. Scalable audio processing requires memory-efficient and resumable Python workflows.
3. Cross-lingual evaluation necessitates explicit control over language imbalance and leakage.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/LYCBNT/>

## 31. [When Space Weather Breaks Your GPS: Building an Explainable Early Warning System](https://pretalx.com/pyconde-pydata-2026/talk/99UMEL/)

**Speakers**: [Vincenzo Ventriglia](https://pretalx.com/pyconde-pydata-2026/speaker/FRRAE7/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Have you ever happened to use GPS and realised that it is not working properly? The Sun could be responsible.

In this talk, I present a **real-world machine learning forecasting system** designed to predict a Space Weather phenomenon affecting GNSS accuracy and radio communications. The system is based on **CatBoost** and integrates data from space- and ground-based observations. **SHAP** is used to debug model behaviour and to build trust in model outputs. The talk focuses on **model design and evaluation choices**, showing how interpretability and uncertainty-aware forecasting can be combined in a real-time operational pipeline.

**Description** (verbatim):

**Space Weather** doesn’t just produce beautiful auroras: it can silently disrupt navigation systems, radio links, and satellite-based technologies we rely on every day.

Travelling Ionospheric Disturbances (TIDs) are wave-like structures in the ionosphere that affect GNSS accuracy and HF communications. From an ML perspective, forecasting TIDs is a challenging rare-event prediction problem involving imbalanced data and heterogeneous physical inputs.

In this talk, I will present an operational machine learning approach developed within the T-FORS project to forecast TID occurrence over Europe. The model is built using **CatBoost** and integrates data from space- and ground-based observations.

The talk focuses on **model design and evaluation choices**. In particular, I will show how **SHAP** can be used to debug model behaviour, validate feature relevance, and build trust in predictions in a high-risk operational context.

Along the way, I’ll share practical engineering lessons on:

- handling class imbalance,
- incorporating domain knowledge into ML pipelines,
- producing **uncertainty-aware outputs** via **Conformal Prediction**, and
- running **interpretable models in real-time forecasting systems**.

The talk is aimed at data scientists and ML practitioners interested in applied forecasting, interpretable models, uncertainty quantification and ML at the boundary between data and physics.

---

**Talk outline**

- 0-4: What is Space Weather and why should we care
- 4-7: Framing TID forecasting as an ML problem
- 7-10: Model design with CatBoost
- 10-13: Explainability with SHAP
- 13-18: Uncertainty quantification with Conformal Prediction
- 18-22: Cost-sensitive learning and real-time operations
- 22-25: Lessons learned
- 25-30: Q&A

**Links**:

- [Personal Website](https://viventriglia.github.io/portfolio/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/99UMEL/>

## 32. [It Works on My Machine: Why LLM Apps Fail Users (Not Tests)](https://pretalx.com/pyconde-pydata-2026/talk/3UHPZB/)

**Speakers**: [Thomas Prexl](https://pretalx.com/pyconde-pydata-2026/speaker/UZ9VMC/), [Frank Rust](https://pretalx.com/pyconde-pydata-2026/speaker/SGPHNQ/)

**When and where**: Tuesday, 2026-04-14, 17:10–17:40, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

LLM applications frequently pass tests but fail users in production. This talk examines the gap between evaluation metrics and user experience through three lenses: **Expectations** (what "working" means to users), **Functional** (system-level vs. component-level success), and **Operational** (real-world reliability).

Drawing from production experience, we'll share scenarios of expectation mismatches, silent failures, and undetected drift—plus practical strategies for bridging the gap. The core message: evaluation should answer whether your system serves users, not whether it passes tests.

**Description** (verbatim):

You've deployed an LLM application. Your tests show that it's working. The metrics look good. Then a user says **it's broken.**

This happens more often than you would expect.

In this talk, we'll share our experience of building and maintaining LLM applications, and discuss what we've learned about the discrepancy between evaluation results and user experience.

We will explore three dimensions of evaluation through the lens of user experience:

## Expectations: What does 'working' actually mean to your users?

Sometimes the gap between tests and reality comes down to expectations. Questions that seem obviously hard to users turn out to be easy for the LLM—and vice versa. Understanding this mismatch is the first step to building systems that users actually trust.

## Functional: Does the system do what it's supposed to do?

When you're working with LLMs, individual components might pass tests while the whole system fails. With prompts, model parameters, evaluation criteria, metadata, and ever-growing datasets all interacting, the complexity compounds quickly.

## Operational: Does it remain reliable in real-world conditions?

In this section, we'll share practical lessons from operating LLM applications in production: how we use observability tools like Opik to monitor model behavior, how telemetry helps us understand actual usage patterns, and how dedicated validation endpoints allow us to detect issues in on-premises deployments before users do.

We'll discuss real-life scenarios we've encountered, such as when users expected different results to those delivered by our system, when external changes affected the system silently, and when performance drifted in ways that our metrics didn't detect.

This isn't a talk about frameworks or tools (even though we'll mention a few). It's about the human element of evaluation: **ensuring that the system we built serves the people using it.**

Whether you're just starting out with LLM applications or running them at scale, you'll probably recognize these scenarios. We'll share the strategies and patterns that we've developed, not as prescriptive rules, but as a starting point for your own approach.

## Outline

1. Why users report the LLM application is broken while it passes every test
2. Three dimensions of the problem
   - Expectations
   - Functional
   - Operational
3. Real-life scenarios
4. Our current strategies and patterns
5. Evaluation = understanding if the system serves users, not proving it's good

Source: <https://pretalx.com/pyconde-pydata-2026/talk/3UHPZB/>

## 33. [From Prompt to Production: How to use AI Code Assistants for Python Data Systems](https://pretalx.com/pyconde-pydata-2026/talk/RRLTBU/)

**Speakers**: [Serhii Sokolenko](https://pretalx.com/pyconde-pydata-2026/speaker/ZUECPC/)

**When and where**: Tuesday, 2026-04-14, 11:45–13:15, room Ferrum [2nd Floor]

**Type**: Tutorial — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

**Code-generating LLMs have matured** to the point where they can reliably scaffold **data pipelines and data agents**, when used in a **supervised, engineering-first workflow**. This tutorial demonstrates how to combine modern **AI coding assistants** with a **production-ready Python deployment platform (Tower.dev)** to build and operate **real data systems**.

Participants will learn how to structure **collaborative Human/AI Assistant development loops**, where engineers provide **architecture, domain knowledge, and review**, while AI accelerates implementation. We will build a **data pipeline** and a **lightweight data agent**, iterating with an AI assistant to **generate, test, and improve code**.

The session also covers critical **operational concerns** such as:

- **Security**
- **Scaling**
- **Observability**
- **Debugging**

You will also see how **production feedback can be looped back into the assistant** to continuously improve generated code.

This is **not about “vibe coding”** a website. It is about **disciplined, review-driven AI collaboration** that meaningfully improves productivity for **data practitioners at all levels**.

**Description** (verbatim):

This **90-minute hands-on tutorial** shows how to **design, build, and deploy Python data pipelines and data agents** using AI coding assistants in a **supervised engineering workflow**.

### Outline

- **The state of AI code generation** for data engineering
- Designing **collaborative Human/LLM development loops**
- Building a **data pipeline with structured AI assistance**
- Creating a **simple data agent**
- Deploying and operating **Python workloads in production** using **Tower.dev**
- Using **logs, observability, and runtime feedback** to guide AI-driven refactoring
- **Best practices, risks, and guardrails**

Participants will leave with **practical patterns for integrating AI into real-world data engineering workflows**, from **prototype to production**.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/RRLTBU/>

## 34. [Your First Open Source Contribution in Python: From Fork to Pull Request](https://pretalx.com/pyconde-pydata-2026/talk/KKCYJN/)

**Speakers**: [Camila Maia](https://pretalx.com/pyconde-pydata-2026/speaker/GXBKTT/)

**When and where**: Tuesday, 2026-04-14, 14:30–16:00, room Ferrum [2nd Floor]

**Type**: Tutorial — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Contributing to open source can feel intimidating, even for experienced Python developers. In this hands-on tutorial, participants will make their first real open source contribution to a Python project, learning the complete workflow from fork to pull request.

Using a real-world Python library, attendees will practice reading an unfamiliar codebase, making a small but meaningful change, running tests, and opening a pull request following community standards. The focus is on practical skills, tooling, and confidence — not theory.

By the end of the session, participants will understand how to start contributing to Python open source projects and feel prepared to continue contributing beyond the workshop.

**Description** (verbatim):

Open source is a core pillar of the Python ecosystem, yet many developers struggle to make their first contribution. The barriers are often not technical ability, but uncertainty around workflows, expectations, and collaboration practices.

This 90-minute hands-on tutorial guides participants through their first real contribution to an open source Python project, focusing on clarity, safety, and reproducibility. Rather than working on toy examples, attendees will contribute to ScanAPI, an actively maintained open source Python library used for automated API integration testing and live documentation.

The tutorial is designed to demystify the contribution process while remaining technically grounded and respectful of real-world open source practices.

What participants will learn:

1. Understanding an Open Source Python Project

- How to quickly navigate an unfamiliar Python repository
- Reading project structure, tests, and documentation
- Understanding contribution guidelines and expectations

2. Open Source Workflow in Practice

- Forking and cloning a repository
- Creating a local development environment
- Working with branches and commits

3. Making a First Contribution

- Working on a well-scoped, beginner-friendly issue
- Writing or updating Python code, tests, or documentation
- Running tests locally and validating changes

4. Opening a Pull Request

- Writing a clear and respectful pull request description
- Understanding automated checks (CI)
- Responding to maintainers’ feedback

5. Contributing Sustainably

- How to continue contributing after the workshop
- Common mistakes to avoid
- How open source communities scale through good engineering and collaboration

All tutorial tasks are carefully scoped and prepared in advance to ensure a smooth experience within the 90-minute timeframe. Participants will leave with a forked repository, a commit, and a pull request opened or ready, as well as the confidence to contribute to other Python open source projects.

Why ScanAPI?

ScanAPI is a production-grade Python library distributed via PyPI and maintained in the open. It has been recognized by GitHub as part of initiatives focused on securing the open source supply chain, making it an excellent real-world example of sustainable Python open source development. The project is supported by the Cumbuca Dev open source community, which focuses on building inclusive, contributor-friendly environments through strong engineering practices.

**Links**:

- [canva link](https://canva.link/wtdsbs7m7ndjux6)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/KKCYJN/>

## 35. [How to Search Through 800 Billion Records in Real Time](https://pretalx.com/pyconde-pydata-2026/talk/ZYUJH3/)

**Speakers**: [Mirano Tuk](https://pretalx.com/pyconde-pydata-2026/speaker/P9UQXL/), [Filip Bacic](https://pretalx.com/pyconde-pydata-2026/speaker/U8YKKZ/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Ferrum [2nd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Large-scale distributed systems rarely produce clean data streams. In practice, hundreds of services continuously emit overlapping updates, retries, corrections, and partial state. Turning that constant stream of noisy events into a reliable, searchable dataset in real time, while processing hundreds of billions of records per day, requires careful architectural choices.

This talk shares practical lessons from building a Kafka-based ETL pipeline that transforms massive volumes of events into a coherent dataset suitable for real-time search. After a brief overview of the system architecture, we focus on several key techniques: reducing redundant processing through key deduplication and short-lived buffers, defining when messages can be safely acknowledged without risking data loss, and keeping long-running ETL services healthy under heavy Kafka workloads.

The session emphasizes concrete engineering trade-offs and operational realities rather than theory. Attendees will leave with practical patterns for building more reliable and efficient streaming pipelines.

**Description** (verbatim):

Large-scale distributed systems rarely produce clean data streams. In practice, hundreds of services continuously emit overlapping updates, retries, corrections, and partial state. Turning that constant stream of noisy events into a reliable, searchable dataset in real time, while processing hundreds of billions of records per day, requires careful architectural choices.

This talk shares practical lessons from building a Kafka-based ETL pipeline that transforms massive volumes of events into a coherent dataset suitable for real-time search. After a brief overview of the system architecture, we focus on several key techniques: reducing redundant processing through key deduplication and short-lived buffers, defining when messages can be safely acknowledged without risking data loss, and keeping long-running ETL services healthy under heavy Kafka workloads.

The session emphasizes concrete engineering trade-offs and operational realities rather than theory. Attendees will leave with practical patterns for building more reliable and efficient streaming pipelines.

**Links**:

- [Slides](https://pycon.tuk.hr)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/ZYUJH3/>

## 36. [Agent-Based Hyperparameter Optimization for Gradient Boosted Trees](https://pretalx.com/pyconde-pydata-2026/talk/BAXEXY/)

**Speakers**: [Huijo Kim](https://pretalx.com/pyconde-pydata-2026/speaker/QVC73Q/)

**When and where**: Tuesday, 2026-04-14, 17:10–17:40, room Ferrum [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

### Teaching an LLM to Tune GBDT — and Beyond

Hyperparameter optimization for gradient boosted tree models is a repetitive yet cognitively demanding task. Practitioners must combine statistical intuition with detailed, library-specific knowledge—often buried across hundreds of pages of documentation for tools such as XGBoost, LightGBM, or CatBoost. As models and configurations grow in complexity, traditional approaches like grid search, random search, or even Bayesian optimization struggle to incorporate semantic understanding of model behavior.

Using LGBM as a concrete case study, I demonstrate how MCP and skills-powered agents, orchestrated in a structured workflow, can analyze model behavior and propose targeted hyperparameter adjustments grounded in both theory and library-specific constraints.

**Description** (verbatim):

### Why This Problem Matters in Practice

Hyperparameter tuning consumes a disproportionate amount of experimentation time, yet most tuning failures stem from recurring structural issues — not random chance. Experienced practitioners can spot these patterns, but automated optimizers only see scalar objective values.

### What Is New or Different

This work reframes hyperparameter optimization as an iterative reasoning process rather than a pure search problem. Intermediate diagnostic artifacts (parameter importance, generalization gaps, plateau signals) become first-class inputs that guide subsequent decisions. Encoding this reasoning via agents enables systematic reuse of expert heuristics that are otherwise applied informally.

### Scope and Limitations

The case study uses LightGBM as the sample demo, but the architecture is generic and can be applied to any ML model. The talk explicitly discusses scenarios where agent-based optimization adds limited value or introduces unnecessary complexity.

### Audience Takeaways

Attendees will gain:

- A blueprint for putting an LLM in any decision loop with guardrails
- If you do ML: a new way to think about HPO
- If you don't: a reusable pattern for agent-driven automation

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BAXEXY/>

## 37. [SQL is Dead, Long Live SQL: Engineering reliable analytics agent from scratch](https://pretalx.com/pyconde-pydata-2026/talk/AF9DNH/)

**Speakers**: [Mehdi Ouazza](https://pretalx.com/pyconde-pydata-2026/speaker/MPYCX8/), [Dumky de Wilde](https://pretalx.com/pyconde-pydata-2026/speaker/VHNV7X/)

**When and where**: Tuesday, 2026-04-14, 11:45–13:15, room Dynamicum [Ground Floor]

**Type**: Tutorial — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Is it still worth learning SQL in 2026, or can we just "chat" with our data? This hands-on tutorial explores that exact question by pushing Text-to-SQL to its absolute limits. This won't be just happy paths; we will deliberately expose where LLMs fail : ambiguity, hallucinations, and "dirty" data...and build the engineering stack required to fix them!

You will build a local data Agent from scratch using DuckDB, MCP and a minimalist semantic layer. By the end, you will understand the hard boundaries of AI reasoning, how a semantic layer acts as a safety net, and why knowing SQL is still (since 1974) the most critical skill for building reliable analytics agents.

**Description** (verbatim):

This session is a "reality check" for AI analytics. We combine theory with engineering to answer one question: Where are the limits of Text-to-SQL? Participants will experience the frustration of a hallucinating LLMs and the satisfaction of fixing it with a realistic minimalist local setup.

Learning objectives:

1. Map the limits: Identify exactly where LLMs break (e.g., complex joins, specific business logic, non-standard schemas).
2. Bridge the gap: Learn how a semantic layer translates fuzzy English into deterministic SQL.
3. Modern architecture: Overview and hands-on on DuckDB Model Context Protocol (MCP) to give agents standard, safe tools to do analytics.
4. The verdict: Understand why SQL is becoming the "Assembly Language" of the AI era, and why you still need to be fluent in it and what is still missing to just "chat with our data".

Prerequisites:

- Laptop with Python 3.10+.
- Beginner SQL knowledge (joins, aggregations).
- No prior AI/LLM experience required.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AF9DNH/>

## 38. [A minimalist introduction to Ansible](https://pretalx.com/pyconde-pydata-2026/talk/9ZKYRD/)

**Speakers**: [Raniere Silva](https://pretalx.com/pyconde-pydata-2026/speaker/DVTDFJ/)

**When and where**: Tuesday, 2026-04-14, 14:30–16:00, room Dynamicum [Ground Floor]

**Type**: Tutorial — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

[Ansible](https://docs.ansible.com/) is a popular [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) tool for server configuration and software deployment. This tutorial will cover things that I wish the first day that I started using Ansible to manage the projects at my work.

**Description** (verbatim):

[Ansible](https://docs.ansible.com/) is a popular Python package for declarative configuration of servers that includes batteries (for example, encrypted vault for secrets and Jinja template engine). As a Swiss Army knife, Ansible is capable of solving my problems but come with many features that novices will not know how to use. This tutorial is hands-on and will guide attendees to learn the core features of Ansible. Attendees must have Podman or Docker installed in the machine they will use during the tutorial.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/9ZKYRD/>

## 39. [Catch the LLM if you Can: Watermarking LLMs](https://pretalx.com/pyconde-pydata-2026/talk/3JLSEF/)

**Speakers**: [Subhosri Basu](https://pretalx.com/pyconde-pydata-2026/speaker/EYPGPQ/)

**When and where**: Tuesday, 2026-04-14, 16:30–17:00, room Dynamicum [Ground Floor]

**Type**: Talk — **Track**: General: Ethics & Privacy — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

With Large Language Models (LLMs), generating high-quality text and images is easy and so is
misusing it. As AI-generated content becomes harder to distinguish from human generated content,
developers are increasingly asking: How can we verify whether a piece of text comes from an LLM?
We’ll explore Python’s simplicity and rich ecosystem of libraries to solve this problem.

This talk introduces the foundations of LLM watermarking and shows how developers can implement
these techniques entirely in Python. We’ll discuss two core approaches, EXP sampling method and
KGW method. We will go through the implementation of the KGW method using simple,
transparent code, and compare it with the EXP approach. There's no need for a large model or a GPU
cluster to understand how these systems work and the core ideas can be implemented in pure
Python using simple code. The code repositories, which includes both methods will be provided so
that the attendees can follow along.

Along the way, we’ll discuss the trade-offs and the limitations of current research. And for those
wondering, “Do I have to implement all this myself?”, the talk concludes with a quick overview of MarkLLM, an existing open-source toolkit that provides a unified Python interface for experimenting with watermarking algorithms.

Attendees will leave with a clear understanding of how watermarking works, when it’s useful, and
how to integrate these techniques into real-world Python projects.

**Description** (verbatim):

During the talk we will cover:

1. Why Watermarking Matters?
   - What can go wrong when AI-generated content becomes indistinguishable from human writing
   - Why provenance and transparency are becoming essential to trust and safety.
2. How LLM Watermarking Works?
   - What is a watermark and what isn't
   - The core idea behind statistical watermarking
3. Two Key Algorithms implemented using Python's established frameworks
   - EXP Watermark: modifying logits with pseudo-random perturbations.
   - KGW Green-List Watermark: partitioning tokens into “green” and “red” lists to bias sampling.
   - Python implementation of the KGW method and comparing it with the EXP method.
4. How you can use MarkLLM (open-source toolkit)
   - How to use the toolkit for experiments in your own workflows.
5. Real-World Challenges and Limitations
   - How robust and evasive are the current algorithms

Key Takeaways: - Watermarking is a promising tool for provenance. - Understanding these methods helps build more transparent and trustworthy AI systems.
This talk is for people who:

- Care about ethics and privacy in AI and want to understand what watermarking can (and cannot) solve.
- Build applications using LLMs and want mechanisms for verifying generated text.
- Are ML researchers or hobbyists interested in how watermarking algorithms function at a technical level.
- Work in AI safety, trust & transparency, or responsible AI and need practical tools for content provenance.

Note: No prior experience with LLM architecture is required, basic familiarity with probability is recommended; no advanced math needed.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/3JLSEF/>

## 40. [Offline Fallback for a Mobile LoRaWAN Gateway](https://pretalx.com/pyconde-pydata-2026/talk/7JXYKH/)

**Speakers**: [Jannis Lübbe](https://pretalx.com/pyconde-pydata-2026/speaker/KSM737/)

**When and where**: Tuesday, 2026-04-14, 17:10–17:40, room Dynamicum [Ground Floor]

**Type**: Talk — **Track**: General: Infrastructure - Hardware & Cloud — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

LoRaWAN gateways typically depend on cloud-based network servers, creating a vulnerability during internet outages. This talk presents a hybrid solution: a Raspberry Pi-based mobile gateway that operates on The Things Stack Sandbox while simultaneously decoding all device messages locally.

The system leverages existing network infrastructure for broad coverage during normal operation, while maintaining full local data access when connectivity fails. This is particularly valuable for emergency response scenarios and remote monitoring where sensor data must remain available regardless of network conditions.

The implementation uses Python for gateway orchestration and API integration, while incorporating existing JavaScript libraries (`lora-packet` and device decoders) for LoRaWAN decryption and payload decoding. Data is stored locally in SQLite for reliability and easy access.

**Description** (verbatim):

LoRaWAN (Long Range Wide Area Network) is widely used for IoT sensor deployments due to its long range and low power consumption. Operating at 868MHz across Europe, it's ideal for remote monitoring applications—from water level sensors to asset tracking and personnel location systems. However, traditional LoRaWAN deployments rely on cloud-based network servers, making them vulnerable to internet outages.

**The Challenge**

While networks like The Things Stack provide good geographic coverage, gaps remain—particularly in remote areas where emergency response units operate. A mobile gateway can close these gaps, but standard configurations still require internet connectivity. You could deploy a completely local network with your own network server, but this sacrifices the existing infrastructure's coverage.

**The Solution**

This talk presents a hybrid architecture that combines cloud-based operation with local resilience. The system primarily operates through The Things Stack Sandbox, leveraging its network coverage. Simultaneously, a Raspberry Pi-based mobile gateway decodes all messages from your devices locally in parallel. During normal operation, you benefit from cloud features. When internet connectivity fails, your sensor data remains accessible locally on the gateway.

**Technical Implementation**

The solution consists of:

1. **Raspberry Pi Gateway**: Configured as a mobile LoRaWAN gateway for The Things Stack Sandbox, suitable for vehicle deployment
2. **Session Key Management**: Python service retrieving session keys for your devices via The Things Stack API
3. **Local Message Processing**: Real-time decryption and decoding of LoRaWAN messages without internet dependency
4. **Data Storage**: SQLite-based local storage for reliable data persistence

**Python and JavaScript Integration**

The core implementation uses Python for gateway orchestration, API integration, and data management. For LoRaWAN encryption/decryption and payload decoding, the system leverages existing JavaScript libraries—specifically `lora-packet` and community-maintained device decoders. This talk demonstrates practical patterns for Python/JavaScript interoperability.

**Real-World Context**

Drawing from volunteer emergency response experience, this solution addresses operational requirements where sensor data must remain available regardless of infrastructure status. The system ensures continuity of critical information during incidents.

**What You'll Learn**

- Designing resilient edge computing architectures for IoT
- Integrating Python with JavaScript libraries
- LoRaWAN security fundamentals (session keys, encryption)
- Building offline-first systems with SQLite
- API integration with The Things Stack

**Open Source**

Complete implementation available on GitHub, providing a reproducible setup valuable for volunteer organizations, research projects, and scenarios requiring IoT infrastructure that remains operational during connectivity disruptions.

**Target Audience**

Python developers interested in IoT and edge computing. No prior LoRaWAN experience required.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/7JXYKH/>

## 41. ["Honey, I vibe coded some crypto" - Security in the age of LLMS](https://pretalx.com/pyconde-pydata-2026/talk/CMDHUN/)

**Speakers**: [Gabriela Bogk](https://pretalx.com/pyconde-pydata-2026/speaker/RNBVEV/)

**When and where**: Wednesday, 2026-04-15, 09:05–09:50, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

What only a few years ago started out as smart tab completion turned into a way of working in which a growing number of programmers don't even bother to open up an IDE anymore. Let's take a moment to contemplate the changing nature of software engineering as a profession, and to explore chances to avoid looming disaster.

**Description** (verbatim):

What only a few years ago started out as smart tab completion turned into a way of working in which a growing number of programmers don't even bother to open up an IDE anymore. Let's take a moment to contemplate the changing nature of software engineering as a profession, and to explore chances to avoid looming disaster. ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎

Source: <https://pretalx.com/pyconde-pydata-2026/talk/CMDHUN/>

## 42. [Demystifying Containers with Python: Building a Minimal Engine from Scratch](https://pretalx.com/pyconde-pydata-2026/talk/BLC7FS/)

**Speakers**: [Alexander Zaytsev](https://pretalx.com/pyconde-pydata-2026/speaker/U3VPD3/)

**When and where**: Wednesday, 2026-04-15, 10:15–10:45, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Containers are a fundamental part of the modern developer's toolkit, yet they are frequently misunderstood and described as "lightweight virtual machines." This talk demystifies containerization by building a functional, minimal engine from scratch using only the python standard library. We will step away from high-level tools like docker to explore how the linux kernel provides isolation through features like `namespaces` and `chroot`. Using a hands-on approach, we will demonstrate how to set up a sandboxed environment, isolate a filesystem, and execute processes within it. This session is designed for developers who use containers daily but haven't yet had the opportunity to look under the hood or explore the underlying operating system principles. By implementing a simplified version of these tools, you will gain a clearer, more practical understanding of the core mechanics that make containerization possible.

**Description** (verbatim):

In modern software development, containers have become a standard tool for deploying code. However, they are frequently misunderstood and described as "lightweight virtual machines." For many developers - especially those transitioning from academia, like myself - the layer between their python code and the operating system kernel is often overlooked. This talk is based on the idea that the best way to understand a concept is to implement it in its simplest form. By bypassing the complexity of modern container orchestrators, we can focus on the fundamental system calls that make isolation possible.

During the session, we will demonstrate the core mechanics of containerization by building a minimal engine in python. We will begin by preparing a root filesystem to show what a container image actually is at its most basic level. We will implement isolation using the `os.chroot()` function to trap a process in a specific directory and will talk about linux namespaces, which isolate what a process can see, and `cgroups`, which limit how much of the hardware resources a process can use.

The main takeaways of this talk include a clear technical distinction between virtual machines and containers and the realization that a container is essentially a process with a restricted view of the host system. You will gain practical knowledge of the `os` module for system-level tasks and the confidence to explore low-level computer science concepts by implementing them in python. By the end of this session, you will have a practical understanding of the basic principles that make containerization possible.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BLC7FS/>

## 43. [How to create effective data visualizations](https://pretalx.com/pyconde-pydata-2026/talk/GBKUNF/)

**Speakers**: [Dominik Haitz](https://pretalx.com/pyconde-pydata-2026/speaker/LCLSQC/)

**When and where**: Wednesday, 2026-04-15, 10:55–11:25, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk — **Track**: PyData: Visualisation & Notebooks — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

What distinguishes a lousy plot from a beautiful chart that communicates insights effectively? This talk will show you the underlying principles of good data visualization, offer lots of practical tips and tricks and give an overview of the data visualization landscape in Python.
After the talk, you will be able to create better charts, whether for exploring your own data or for communicating results to others.

**Description** (verbatim):

In this talk, you will learn about:

- **Fundamental principles** of data visualization
  - The Grammar of Graphics
  - Visual hierarchy
  - Data storytelling
- **Best practices** regarding:
  - Which colors to use
  - Visual comparability
  - Pros/cons of several chart types
  - Context and audience: Adding text and annotations
- The **data visualization landscape in Python**
  - What libraries exist: matplotlib, plotly, altair etc., including add-ons and lesser-known ones
  - What are their differences and strengths?
  - Which library is suited for which usecase?

Equipped with the knowledge presented in this talk, you will understand why certain charts are more aesthetically pleasing and more effective at conveying information than others. Apply the shown principles, take into account best practices and choose the right tools in Python to create more beautiful and impactful data visualizations.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GBKUNF/>

## 44. [Production ML across 2015-2035: A Journey to the Past and the Future](https://pretalx.com/pyconde-pydata-2026/talk/PMMEAG/)

**Speakers**: [Alejandro Saucedo](https://pretalx.com/pyconde-pydata-2026/speaker/EQMGKH/)

**When and where**: Wednesday, 2026-04-15, 11:35–12:05, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

This talk is an exciting journey that revisits the past decade of Production Machine Learning from 2015 until now, and provides a pragmatic outlook of the next decade towards 2035. We’ll revisit some of the cornerstone python projects that served as the foundation of the "messy innovation" boom (feature stores, orchestration, model serving, monitoring), as well as how it transitioned towards the LLMOps era shifting the stack from training-centric to inference-centric. We will also provide a pragmatic set of predictions for the next decade of MLOps, including some of the trends in ML monitoring, agentic systems and beyond - this will provide actionable guidance to all practitioners to ensure we stay ahead of the curve on the expected skills and domains required to thrive in the near future to come.

**Description** (verbatim):

# Outline

1. Motivations;
2. MLOps Foundations;
   3.1) The Past - 2015 - Genesis;
   3.2) The Past - 2018 - Messy Innovation;
   3.3) The Past - 2023 - LLMOps;
3. The Future - 2025-2035 Outlook;
4. Reflections.

# Description

The lifecycle of a machine learning model only begins once it’s in production. In this talk we take a practical journey through the last decade of production ML, tracing back the early beginnings of MLOps to the respective research and projects that helped drive the movement forward. We cover how the ecosystem went through explosive growth through COVID with a broad range of tools and vendors tacking similar problems in very different ways. We then talk about the most recent trends in LLMOps which has shifted the stack from training-centric to inference-centric as pre-trained models have become broadly available. Namely on how the locus of engineering moves to the application layer (ie inference time), introducing new artifacts such as prompts, vector databases, and tool metadata, and accelerating another wave of ecosystem heterogeneity.

With those lessons in place, we look forward to 2035 through a set of pragmatic milestones for consolidation and standardization: how monitoring and observability become more ubiquitous, how MLOps and LLMOps stacks align, how time-to-production compresses, and how operations gradually evolves toward more autonomous patterns (progressive rollouts, agent-assisted RCA, and early self-healing behaviors).

Finally, we close with actionable guidance grounded in production reality: how to right-size platform complexity to organizational scale, where to invest early to reduce future operational debt, and how to increase the scale of ML delivery while actively reducing system complexity. Attendees should leave with a coherent mental model of the MLOps landscape, a sharper understanding of why production ML remains hard, and a concrete set of engineering priorities for building reliable ML systems through the next decade.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/PMMEAG/>

## 45. [The Multimodal Era of Machine Learning (and How Python Made It Possible)](https://pretalx.com/pyconde-pydata-2026/talk/LPUC9T/)

**Speakers**: [Hilde Kühne](https://pretalx.com/pyconde-pydata-2026/speaker/NHKXFV/)

**When and where**: Wednesday, 2026-04-15, 13:25–14:10, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Multimodal learning - systems that combine vision, language, audio, and other sensory inputs—has moved from a niche research topic to a central paradigm in modern machine learning. Today’s most influential models no longer operate on a single modality but instead learn rich representations by combining language with images, videos, sound. This shift has fundamentally changed how we build, train, and evaluate current machine learning systems. Python has played a decisive role in this transformation. Acting as a unifying layer across modalities, Python enabled researchers and practitioners to seamlessly combine computer vision, natural language processing, and speech within a single ecosystem. Python-based frameworks lowered the barriers between research communities, and accelerated the rise of large-scale, weakly supervised, and foundation models. However, this success has also introduced new challenges. The ease of experimentation masks growing issues around scalability, reproducibility, and evaluation. Multimodal systems increasingly depend on complex Python-based stacks whose abstractions can obscure underlying assumptions and costs.
...

**Description** (verbatim):

Multimodal learning—systems that combine vision, language, audio, and other sensory inputs—has moved from a niche research topic to a central paradigm in modern machine learning. Today’s most influential models no longer operate on a single modality but instead learn rich representations by combining language with images, videos, sound. This shift has fundamentally changed how we build, train, and evaluate current machine learning systems. Python has played a decisive role in this transformation. Acting as a unifying layer across modalities, Python enabled researchers and practitioners to seamlessly combine computer vision, natural language processing, and speech within a single ecosystem. Python-based frameworks lowered the barriers between research communities, and accelerated the rise of large-scale, weakly supervised, and foundation models. However, this success has also introduced new challenges. The ease of experimentation masks growing issues around scalability, reproducibility, and evaluation. Multimodal systems increasingly depend on complex Python-based stacks whose abstractions can obscure underlying assumptions and costs.
This keynote will reflect on the current state of multimodal learning, examine how Python shaped its trajectory, and critically discuss the technical and conceptual challenges that lie ahead aiming to provide a perspective on where machine learning in general and multimodal learning in particular is succeeding, where it is struggling, and what role the Python community can play in shaping its next phase.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/LPUC9T/>

## 46. [PyLadies Fireside Chat](https://pretalx.com/pyconde-pydata-2026/talk/QBJRBJ/)

**Speakers**: [Tereza Iofciu](https://pretalx.com/pyconde-pydata-2026/speaker/NMACLQ/), [Dawn Wages](https://pretalx.com/pyconde-pydata-2026/speaker/WS7BU8/), [Jessica Greene (she/her)](https://pretalx.com/pyconde-pydata-2026/speaker/HEGPKL/)

**When and where**: Wednesday, 2026-04-15, 14:20–15:20, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Panel — **Track**: General: Community & Diversity — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

What does it mean to build with Python when AI is reshaping everything? Join Dawn Gibson Wages, Jessica Greene, and host Tereza Iofciu for an honest conversation about Python, local AI, and the craft of being a developer today.

**Description** (verbatim):

Join us for this fireside chat, where Tereza Iofciu sits down with Dawn Gibson Wages, community and DevRel lead at Anaconda with a passion for local-first AI and Python environments, and Jessica Greene, Senior ML Engineer at Ecosia and PyLadies community lead, for a candid conversation about building with Python in the age of AI. Careers, craft, community, and the questions the hype tends to skip.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/QBJRBJ/>

## 47. [Start-Ups & Investors](https://pretalx.com/pyconde-pydata-2026/talk/CNNUZC/)

**Speakers**: [Ina Schlie](https://pretalx.com/pyconde-pydata-2026/speaker/93FF78/), [Carlina Bennison](https://pretalx.com/pyconde-pydata-2026/speaker/89EKYK/), [Sara Jourdan](https://pretalx.com/pyconde-pydata-2026/speaker/H9BQVG/), [Jovana Walter](https://pretalx.com/pyconde-pydata-2026/speaker/CVREN7/)

**When and where**: Wednesday, 2026-04-15, 16:15–17:25, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Panel — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Starting a company doesn't require a garage or an MBA — it takes a real problem, a strong team, and someone willing to turn a project into a product. This panel brings together founders, investors, and startup builders from academia, corporate careers, and venture capital for an honest conversation about what it really takes to build a startup in AI, software, and open source.

At PyCon DE & PyData, we're surrounded by people solving real problems with code and data every day. This session is for anyone who's ever wondered: could my project become a product? The answer might surprise you.

**Description** (verbatim):

The Python and AI community is full of people who build tools, train models, and solve hard problems — but the leap from project to product often feels like a different world entirely. This panel closes that gap.

Four women from very different backgrounds — a former SAP SVP turned startup investor, a TU Darmstadt researcher turned Forbes 30 Under 30 founder, a venture capital managing partner, and an AI startup ecosystem builder — share what founding and funding a company actually looks like.

No polished success stories, no pitching. Just real talk about first steps, financing, team building, and the support systems that exist but few people know about.

Why this panel at PyCon DE & PyData? Because the people in this room are exactly who Germany's AI and open-source startup ecosystem needs. You understand the technology. You work with data. You build things that work.

What's often missing isn't the idea or the skill — it's the confidence, the network, and the knowledge of how to start. This panel provides all three.

We'll cover five themes: the spark that starts a founding journey, the reality behind startup clichés, what technical founders need beyond code, how to find the right networks and funding, and concrete first steps anyone can take.

The panel is especially aimed at developers considering turning a side project into a startup, researchers exploring the path from paper to product, and professionals in industry wondering whether the leap from a corporate career is right for them. We also want to actively encourage more women to see themselves as founders — which is why representation on this stage matters.

Whether you leave with a concrete next step, a new contact, or simply a more realistic picture of what founding looks like — this session is designed to make the startup world feel less like an exclusive club and more like a path that's open to you.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/CNNUZC/>

## 48. [Lightning Talks 2](https://pretalx.com/pyconde-pydata-2026/talk/UFGB7T/)

**Speakers**: Not listed in the source data

**When and where**: Wednesday, 2026-04-15, 18:10–19:25, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Lightning Talks — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Lightning Talks 2

**Description** (verbatim):

Lightning Talks 2

Source: <https://pretalx.com/pyconde-pydata-2026/talk/UFGB7T/>

## 49. [Wetterdienst: Fast, Unified Access to Open Weather Data with Polars](https://pretalx.com/pyconde-pydata-2026/talk/V8DNCL/)

**Speakers**: [Benjamin](https://pretalx.com/pyconde-pydata-2026/speaker/MVPZYU/)

**When and where**: Wednesday, 2026-04-15, 10:15–10:45, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Weather and environmental data power analytics, ML, and operations—but APIs differ wildly and data prep is slow. Wetterdienst is a Python library that provides a unified, Polars‑first interface to multiple weather services (DWD, ECCC, EA, NOAA/NWS, Geosphere Austria, IMGW, Eaufrance, WSV, and more). It standardizes request patterns, returns tidy (long) data, converts to SI units, handles caching, timezones (UTC by default), and retries—so teams can focus on analysis instead of plumbing. This talk introduces Wetterdienst’s provider architecture, core request patterns, performance practices with Polars, and how to integrate via Python, CLI, or its REST API. We’ll walk through real examples (station discovery, parameter selection, timeseries retrieval), exporting to databases, and patterns for robust pipelines in ETL and ML.

**Description** (verbatim):

## Problem

Accessing weather data means wrestling with inconsistent APIs, formats, and units—slowing down data engineering and making pipelines hard to reproduce.

## Solution

Wetterdienst is a Python library providing a unified, Polars-first interface to multiple open weather services (DWD, ECCC, EA, NOAA/NWS, Geosphere Austria, IMGW, Eaufrance, WSV, and more). It standardizes request patterns, returns tidy long-format data in SI units, and handles caching, timezones, and retries—so teams can focus on analysis instead of plumbing.

## Core concepts:

- **Polars-first** — All data operations use Polars (v1.15+); pandas supported for some I/O
- **Declarative request pattern** — Provider → stations → values; tidy/long output by default
- **Sensible defaults** — UTC timestamps, SI units, humanized parameter names
- **Reliability** — Disk-based caching via diskcache, stamina-based retries, timezone handling
- **Provider architecture** — Consistent interfaces across DWD, ECCC, EA, NOAA/NWS, Geosphere, IMGW, Eaufrance, WSV, and more
- **Multiple interfaces** — Python API, CLI, and REST

## Outline

- Introduction
- Journey — How Wetterdienst came to life
- Wetterdienst — Architecture, concepts, and request patterns
- Value — What wetterdienst offers you, me and everyone else
- Demo — Live: station discovery, timeseries retrieval, station metadata, climate stripes and more via app

## Target Audience

Data engineers, scientists, and platform teams who need reliable weather data for analytics, ML, and operations.

## Prerequisites

Basic Python and DataFrame experience (Polars or pandas); familiarity with ETL/ML pipelines helpful.

## Key Takeaways

- A unified, Polars-first workflow to access and normalize open weather data
- Practical patterns for station discovery, timeseries retrieval, unit conversion, and caching
- How to integrate Wetterdienst via Python, CLI, and REST, and export to common formats and databases

## Links

📦 Repo https://github.com/earthobservations/wetterdienst
📖 Docs https://wetterdienst.readthedocs.io/
🌐 App https://wetterdienst.eobs.org/
💡 Examples https://github.com/earthobservations/wetterdienst/tree/main/examples

Source: <https://pretalx.com/pyconde-pydata-2026/talk/V8DNCL/>

## 50. [From Struggling to Mastery: A Practical Guide to Data Pipeline Operations](https://pretalx.com/pyconde-pydata-2026/talk/PARU7X/)

**Speakers**: [Akif Cakir](https://pretalx.com/pyconde-pydata-2026/speaker/BAZU7P/)

**When and where**: Wednesday, 2026-04-15, 10:55–11:25, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

How mature are your data pipeline operations? A Roadmap to Operational Excellence.

Data teams often struggle to scale their pipeline operations, trapped in a cycle of manual fixes and reactive fire-fighting. But what does "good" actually look like? In this talk, we introduce a standardized 5-level maturity model for Data Operations, focusing on three critical pillars: Orchestration, Data Quality, and Data SLOs.

We will deconstruct the journey from "Struggling" (manual scripts, no guarantees) to "Mastery" (automated, resilient, and measured). Attendees will leave with a concrete framework to assess their team’s current standing and a clear, step-by-step roadmap to raise the bar toward operational excellence.

**Description** (verbatim):

The Problem: The "it works on my machine" trap. As data teams grow, ad-hoc processes that worked for a single engineer crumble under the weight of production requirements. Teams often know they need to improve, but they lack a unified definition of success. Without clear standards, it is impossible to measure progress.

This talk presents a comprehensive Operational Excellence Maturity Pyramid, designed to guide data teams from chaos to stability. We will explore a 5-level classification system (Struggling, Basic, Decent, Strong, and Mastery) applied across three foundational pillars of data engineering.

1. Orchestration Maturity We will move beyond simple cron jobs and local scripts.

- Struggling: Manual scheduling, no dependency management, lack of idempotency.

- Mastery: Dynamic DAGs, event-driven triggers, automated backfills, modular infrastructure-as-code, and self-healing pipelines and more.

2. Data Quality Maturity Data trust is hard to gain and easy to lose. We will define how to shift from reactive to proactive quality management.

- Struggling: No testing program; quality issues are discovered by stakeholders downstream.

- Mastery: Comprehensive coverage (Write-Audit-Publish patterns), automated anomaly detection, and "circuit breakers" that stop bad data before it hits the warehouse.

3. Data SLOs (Service Level Objectives) Maturity You cannot improve what you do not measure.

Struggling: Undefined targets; "best effort" delivery.

Mastery: Fully measurable SLIs (Service Level Indicators), defined Error Budgets, and automated alerting on burn rates.

-- What You Will Learn: This session is not just theoretical; it is a practical guide for data engineers, platform leads, and managers. By the end of this talk, you will be able to:

- Audit your current stack: Use the provided scorecard to classify your team's maturity level in each pillar.

- Identify gaps: Understand exactly why you are stuck at the "Basic" or "Decent" levels.

- Plan your roadmap: Walk away with actionable steps to advance to the next level, turning your data operations into a competitive advantage rather than a maintenance burden.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/PARU7X/>

## 51. [Empowering Data Scientists with Zero Platform Friction: Deploying Streamlit & Friends in 3 Minutes](https://pretalx.com/pyconde-pydata-2026/talk/9MUDUY/)

**Speakers**: [Bernhard Schäfer](https://pretalx.com/pyconde-pydata-2026/speaker/GGSPQV/), [Nicolas Renkamp](https://pretalx.com/pyconde-pydata-2026/speaker/G7TJBW/)

**When and where**: Wednesday, 2026-04-15, 11:35–12:20, room Titanium [2nd Floor]

**Type**: Talk (long) — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

A data scientist builds a Streamlit or Dash prototype, the business wants to validate it, and the hard parts begin: getting access to live data, making the app available company-wide, and ensuring every user only sees what they are allowed to see. Following "best practices" turn a simple demo into weeks of platform work, leaving data scientists frustrated and blocking them from shipping apps to end users.

In this talk we will **live-demo** Merck's self-service app service we have developed and hardened over multiple years. It lets **teams deploy Streamlit (and friends) in 3 minutes** while meeting best practices like SSO, CI/CD, and governed data access control. The platform has become essential for Merck to ship data apps at scale: in 2025 it powered **750+ active apps** reaching **8,000+ unique end users**.

**Under the hood, we show:** how a use-case based access model enables scoped resource permissions so apps can safely access data on-behalf of the user. We also show starter templates that generate a deployable Git repo with example pages (e.g. Snowflake access or internal LLM chatbot). Finally, we cover the guardrails needed to operate this safely.

**What you will learn:** a cost-effective reference architecture based on AWS that you can adapt to your hyperscaler or platform, practical patterns for balancing the trade-off between central control and decentral freedom, and how templates and CI/CD help teams iterate quickly without compromising security or reliability.

**Description** (verbatim):

This session is for anyone who has built a Streamlit (or Dash, R Shiny, FastAPI, React) prototype and then hit the wall when it needed to be shared with real users: access to live data, SSO, permissioning, deployment, and operational guardrails.

We will present the workflow and the architecture from both sides: as a data scientist shipping an app, and as a platform admin operating the service safely at scale.

## What we will demo

We will demo the end-to-end workflow from zero to a running app using our internal app service. The platform includes a web console for self-service provisioning and configuration and the deployment runtime managing the state of the application.

- Using the web console to create and configure a new app from a framework template (Streamlit, Dash, R Shiny, FastAPI, React).
- How a Git repository is created and the first version is deployed behind the scenes, including a working starter app with example pages.

## Key design decisions (the parts that are usually hard)

- Identity propagation: the app receives the signed-in user identity from SSO and uses it for downstream authorization.
- Authorization at the data layer: dataset permissions are scoped to use-case resource, making sure tokens can not be exploited.
- Safe multi-tenancy: per-app isolation plus resource limits to prevent noisy-neighbor problems.
- Repeatable delivery: templates plus CI/CD conventions so a new app starts from a working, deployable baseline.
- Day-2 operations: guardrails like quotas, rate limiting, and idle shutdown to keep the platform reliable and cheap.

## Running at scale

- Production usage: 750+ active apps and 8k+ unique end users (2025).
- Infrastructure run rate under 10k USD per month (excluding engineering time).

## Who should attend

- Data scientists and analysts who want to ship apps beyond a demo.
- Data platform and DevOps engineers building self-service tooling for governed environments.
- Teams standardizing how internal data & AI products are delivered to business users.

## Takeaways

- For data scientists: what a good internal app hosting platform should provide, and which requirements you should ask your platform team for (governed on-behalf of data access, templates, CI/CD, guardrails).
- For platform teams: a blueprint you can adapt beyond AWS, including the architecture and tradeoffs necessary to operate fine-grained authorization and a multi-tenant runtime at scale.

**If you do not have such an app platform in your company yet, use this talk as a checklist to start the conversation with your IT or platform teams. :-)**

Source: <https://pretalx.com/pyconde-pydata-2026/talk/9MUDUY/>

## 52. [Learnings Building DevOps as a Software Engineer](https://pretalx.com/pyconde-pydata-2026/talk/ZESFRG/)

**Speakers**: [Gaweng Tan](https://pretalx.com/pyconde-pydata-2026/speaker/RCAW7T/)

**When and where**: Wednesday, 2026-04-15, 14:20–14:50, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

When I joined my current company as a software engineer, I encountered a blank slate: no CI/CD pipelines, no deployment infrastructure, barely any monitoring—in short, no software infrastructure at all. This talk shares the key learnings from building a DevOps environment from the ground up. I’ll walk through the essentials: which foundations were laid first, what tools and practices made the difference, and how automation became a daily habit. Through real-world examples, I will demonstrate how pragmatic and incremental steps can jump-start productivity, reduce manual toil, and help teams avoid common pitfalls.

**Description** (verbatim):

What do you do when you join a company as a software engineer, and there’s zero DevOps in place—but product delivery can’t wait? In this talk, I’ll share firsthand insights from building core DevOps infrastructure from the ground up, while simultaneously delivering the first software products under tight deadlines.
I’ll outline the key priorities and quick wins that enabled rapid, reliable releases—such as setting up basic CI/CD pipelines, introducing automated tests, and using containerization for reproducible deployments. Rather than aiming for “perfect” infrastructure from day one, I’ll show how to build DevOps foundations incrementally and pragmatically, integrating automation step by step as part of everyday development work.
Through practical examples, I’ll discuss how to achieve reliability without losing agility, how to avoid common pitfalls in “build as you go” DevOps, and how to balance product delivery with infrastructure improvements. Attendees will leave with actionable tips on how to bootstrap DevOps quickly, so teams can ship software confidently—even when starting from scratch.

**Links**:

- [Slides](https://slides.gtan.eu/slides/pycon-learnings-devops/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/ZESFRG/>

## 53. [Architecture Under Constraints: Designing Systems That Still Evolve](https://pretalx.com/pyconde-pydata-2026/talk/ZLRFR9/)

**Speakers**: [Eduard Thamm](https://pretalx.com/pyconde-pydata-2026/speaker/XFAALW/)

**When and where**: Wednesday, 2026-04-15, 15:00–15:45, room Titanium [2nd Floor]

**Type**: Talk (long) — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Most systems are built under constraints: legacy code, regulation, organizational boundaries, and long-term accountability. This talk explores how Staff+ engineers and tech leads can make sound architectural decisions when “perfect” isn’t an option. Focusing on platforms and tooling, it presents practical ways to identify real constraints, preserve flexibility, avoid over-engineering, and communicate trade-offs that hold up over time - technically and organizationally.

**Description** (verbatim):

Modern systems rarely exist in ideal conditions. They grow over years, integrate with legacy services, operate under regulatory or security constraints, and are shaped by organizational boundaries just as much as by code. Yet architectural guidance often assumes greenfield projects and unlimited freedom.

This talk focuses on architectural decision-making under real-world constraints, using systems as the primary lens. Rather than discussing specific frameworks or patterns, it presents a practical way of thinking about architecture when trade-offs are unavoidable and decisions must hold up over time.

Drawing from experience in regulated production environments, we will explore how to distinguish true constraints from accidental ones, how to think in terms of long-lived capabilities rather than short-lived components, and how to preserve optionality even when systems appear “locked in.” Examples will touch on Python-heavy platforms such as backend services, internal tools, data pipelines, and automation systems.

The session also addresses the human side of architecture: how Staff+ engineers and technical leaders communicate trade-offs, document decisions in a way that survives team changes, and align engineering, product, and compliance perspectives without over-engineering.

This talk is aimed at experienced engineers, tech leads, and engineering leaders who want to design systems that can evolve - even when constraints dominate the problem space.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/ZLRFR9/>

## 54. [Black Hole Stars: An Astronomical Mystery (Mostly) Solved with NumPyro and JAX](https://pretalx.com/pyconde-pydata-2026/talk/EXXWMV/)

**Speakers**: [Raphael Hviding](https://pretalx.com/pyconde-pydata-2026/speaker/QHTKP7/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The James Webb Space Telescope has revealed a mysterious population of "Little Red Dots": extremely distant objects that have upended our understanding of the early Universe. However, revealing the true nature of these marvels requires computationally-intensive statistical modeling of complex astronomical data. In this talk, we explore how we used JAX and NumPyro to help solve this puzzle. We will introduce these powerful Python tools, demonstrate how they accelerate complex statistical data analysis, and show how they provided evidence that Little Red Dots may in fact be "Black Hole Stars."

**Description** (verbatim):

The James Webb Space Telescope (JWST) has transformed extragalactic astronomy. In particular, it has uncovering a puzzling population of compact, red objects in the distant universe known as "Little Red Dots" (LRDs). These sources exhibit distinctive features not seen in typical galaxies and therefore their nature remains a subject of intense debate. Are they supermassive black holes hiding behind screens of dust? Massive dead galaxies appearing too early in the universe? Or something entirely new? To find out, we need to perform computationally heavy statistical analysis on the astronomical data. However traditional tools have been too slow or made many assumptions to reduce the complexity of the JWST data that can lead to inaccurate results.

In this talk, I will introduce the modern Python stack that now makes this possible: JAX and NumPyro. JAX allows you to write standard Python code that runs on GPUs and automatically computes derivatives, while NumPyro leverages that power for incredibly fast statistical modeling. We will start with the basics, using simple examples to demonstrate how JAX can speed up existing workflows and how NumPyro makes Bayesian inference accessible.

Then, we will look at the "Little Red Dot" mystery as a case study. I will show how we built a custom inference engine (`unite`) to process thousands of JWST observations. By leveraging JAX's speed and NumPyro's flexibility, we were able to efficiently and accurately test complex physical models against the data, uncovering evidence that these unique may in fact be supermassive black holes embedded in dense gas clouds: essentially, stars powered not by fusion but by black holes.

This talk is for anyone interested in high-performance Python and especially for (data) scientists interested in modern scientific methods in designing scalable inference pipelines. You will leave with a solid introduction to JAX and NumPyro and an appreciation for how these tools are already helping solve the Universe's greatest mysteries.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/EXXWMV/>

## 55. ["You are an intelligent business analyst": how i learned to talk to business](https://pretalx.com/pyconde-pydata-2026/talk/LVRLSU/)

**Speakers**: [Darya Petrashka](https://pretalx.com/pyconde-pydata-2026/speaker/37RKBL/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Titanium [2nd Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Developers don’t need to become business analysts, but they do need business skills. This talk shows how learning to communicate with stakeholders, uncover real business needs, and bridge gaps between tech and business can dramatically increase your impact. Learn practical techniques to become a trusted technical partner and deliver solutions that truly matter.

**Description** (verbatim):

I never planned to become a business analyst. In fact, I avoided it. I imagined endless meetings, unclear requirements, and conversations that had nothing to do with “real” technical work. I wanted to stay hands-on as a developer and data scientist.

But reality proved something important: you can't escape the business side if you want to build meaningful solutions. And once I learned how to talk to business stakeholders, everything changed: my impact, my influence, and the outcomes of the projects I worked on.

In this talk, we’ll explore the practical business skills every developer needs but is rarely taught:
• How to identify key stakeholders and understand what they really want
• How to navigate communication in international, cross-functional teams
• How to uncover business pain points before they become blockers
• How to fix broken communication loops
• How to become the go-to technical partner the business trusts

By the end, you won’t just see yourself as a strong technical contributor: you’ll see how to position yourself as an essential part of the broader business ecosystem, shaping better decisions and delivering solutions that truly matter.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/LVRLSU/>

## 56. [Ty mypy: The New Generation of Python Type Checking](https://pretalx.com/pyconde-pydata-2026/talk/QB7VLW/)

**Speakers**: [Stefan Kraus](https://pretalx.com/pyconde-pydata-2026/speaker/KGBECS/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Python Language & Ecosystem — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python’s static typing ecosystem has long been shaped by mypy, but a new contender has entered the space: ty, a high-performance type checker from Astral that has recently exited alpha. With a focus on speed, modern ergonomics, and tight tooling integration, Ty represents a new direction for Python type checking.

In this talk, we’ll explore what ty looks like in practice. We’ll cover its core features, how it behaves on real-world codebases, and what changes when type checking becomes fast enough to run constantly. We’ll also compare ty directly with mypy, highlighting strengths, limitations, and trade-offs teams should understand before adopting it.

This session will help Python developers evaluate whether ty is ready for production use today—and what it suggests about the future of Python typing tools.

**Description** (verbatim):

Static typing in Python has matured significantly over the past decade, with mypy becoming the de facto standard for many teams. At the same time, developers continue to struggle with slow feedback loops, noisy errors, and friction in CI and local workflows. ty, a new type checker from Astral.sh, aims to address these issues with a fundamentally different set of design priorities—and it has now reached a post-alpha, production-ready stage.

This talk takes a practical, experience-based look at ty from the perspective of a Python developer using it on real code. We’ll start by briefly reviewing the current state of Python type checking and the problems that motivated ty’s design. From there, we’ll dive into ty’s feature set, performance characteristics, and developer experience, focusing on what actually changes when type checking becomes fast and ergonomic enough to feel “always on.”

A central part of the talk will be a direct comparison with mypy: where ty already excels, where it behaves differently, and where mypy remains the better choice today. Rather than framing this as a replacement story, we’ll explore the trade-offs between the two tools and what kinds of teams benefit most from each.

By the end of the session, attendees will have a clear mental model of how ty works, how mature it is today, and whether it’s a good fit for their own projects. More broadly, we’ll look at what ty signals about the future direction of Python’s typing ecosystem.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/QB7VLW/>

## 57. [Ship Data with Confidence: Declarative Validation for PySpark & Pandas](https://pretalx.com/pyconde-pydata-2026/talk/93SXWY/)

**Speakers**: [Ryan Sequeira](https://pretalx.com/pyconde-pydata-2026/speaker/7LMGT3/)

**When and where**: Wednesday, 2026-04-15, 10:15–10:45, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Tired of data quality issues crashing your PySpark and Pandas pipelines? This talk introduces [dataframe-expectations](https://github.com/getyourguide/dataframe-expectations), a lightweight, open-source library for declarative data validation. We will dive into the library's design and demonstrate how to easily define and apply data quality expectations to catch errors early, reduce debugging time, and ship more reliable data products, faster. Learn to build more robust data pipelines and move from reactive problem-solving to proactive data validation.

**Description** (verbatim):

This session introduces a practical, open-source solution to a critical challenge facing data engineers and scientists: how to proactively guarantee data quality. In today's fast-paced development cycles, data pipelines are increasingly complex and reliant on numerous upstream sources, elevating the risk of data quality issues that have the potential to cause production failures. While monitoring and alerting systems are essential for flagging these failures, they are fundamentally reactive; their value is entirely dependent on the quality and coverage of the underlying validation logic that engineers must build and maintain. The true goal is to shift from reactive clean-up to proactive prevention. This talk demonstrates a more effective approach: stopping bad data from ever reaching production by embedding clear, declarative validation directly into your data pipelines. This provides immediate visibility into errors, allowing you to catch and fix data quality issues at the earliest possible stage of development.

[dataframe-expectations](https://github.com/getyourguide/dataframe-expectations) is an attempt to address this problem through a lightweight, open-source Python library designed for declarative data validation in both PySpark and Pandas. This session will explore the key design choices behind its implementation and architecture, including its lightweight nature, which ensures the library doesn't become a bottleneck by impacting CI/CD run times or bloating container image sizes, making it ideal for data pipelines, unit tests and end-to-end tests alike. Through examples, we will walk through its fluent, chainable API and showcase its extensive list of reusable, parameterized expectations. We will then dive into advanced features, including powerful decorator-based validation that seamlessly integrates quality checks into your existing code, and a flexible tag-based filtering system that allows you to dynamically decide which expectations to run at runtime.

Attendees will leave with a clear, actionable strategy for integrating declarative data quality checks into their pipelines, understanding how a simple, extensible tool can dramatically increase the reliability of their data products and, ultimately, their development velocity.

**Links**:

- [Presentation](https://docs.google.com/presentation/d/1UiGjgexfaEfXyjIy02cbY_T7QBpVJ189SpHbxb_fvOU)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/93SXWY/>

## 58. [Accuracy Is Overrated: Ship Stable Forecasts (Without Lying to Yourself)](https://pretalx.com/pyconde-pydata-2026/talk/B8KVNJ/)

**Speakers**: [Illia Babounikau](https://pretalx.com/pyconde-pydata-2026/speaker/HZFYWE/)

**When and where**: Wednesday, 2026-04-15, 10:55–11:25, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Forecasting talks love a clean ending: “and then we improved WMAPE by 3.7%.”
Nice. Now put that model into production without suffering from instability.

You retrain your model on a few new weeks of data and suddenly the one-year forecast jumps 15–20%. Planning teams redo decisions, trust erodes, and your “accurate” model becomes unusable. This talk is about forecast stability: how much forecasts change when you add new data and rerun the same pipeline.

We run a simple experiment: train a model, forecast one year ahead, add recent data, retrain, and measure forecast-to-forecast change. We repeat this across common forecasting approaches including ETS/ARIMA, Prophet, XGBoost with lag features, AutoGluon ensembles, neural/global models, and TimeGPT-style APIs.

You will see that high accuracy does not guarantee usable forecasts, and that some models are systematically more volatile than others. We then cover practical ways to stabilise forecasts without freezing them, focusing on reconciliation and ensembling (including origin ensembling).

This talk is for forecasting practitioners who want models users actually trust, not just good metrics.

**Description** (verbatim):

Forecasting talks love a clean ending: “and then we improved WMAPE by 3.7%.”
Nice. Now put that model into production without suffering from instability.

Because here is what users actually see: the forecast changes every week. The “one-year view” jumps 15 to 20 percent because you retrained on three extra Mondays. Planning teams redo decisions. Operations loses trust. Your model becomes an expensive random-number generator with excellent dashboards.

This talk is about forecast stability: how much your future forecast moves when you add a small amount of new data, retrain, and run the same pipeline again. Not error versus actuals. Forecast versus forecast.

You will see a simple but uncomfortable experiment:

- Taking a demand-style time series dataset with seasonality, promotions, and noise (Kaggle competition style).
- Training a model and produce a one-year-ahead forecast.
- Adding a few recent weeks of data, retrain, forecast again.
- Measuring how much the overlapping horizon changed.

We repeat this across model families people actually use:

- Statistical baselines like ETS and ARIMA
- Prophet
- Feature-based ML with lag features such as XGBoost
- AutoML and ensembles with AutoGluon TimeSeries
- Neural and global models where relevant
- And yes, what happens when you add an API model like TimeGPT into the mix (no hype, just behaviour under updates)

You will see something totally "unexpected": a model can be “accurate” and still be operationally useless because its forecast revisions are chaotic. And you will see the opposite too: models with slightly worse headline accuracy that people actually trust, because next year does not get rewritten every week.

This is not a philosophical debate. It is a measurable property of forecasting systems that most teams never track.

So what do we do about it?
We focus on techniques that improve stability without turning forecasts into fossils:

1. Reconciliation
   Hierarchical and temporal reconciliation as a stabiliser, not just a coherence tool. If SKU-level forecasts panic while higher-level signals stay calm, reconciliation can prevent nonsense from propagating into decisions.

2. Ensembling and origin ensembling
   Combining models is not only about accuracy. Averaging forecasts across models and across forecast origins dampens noise and makes forecast updates behave like signals instead of mood swings.

Who this talk is for:

Forecasting practitioners, data scientists working on demand forecasting, and anyone who has ever heard: “Your model looks good, but I don’t trust it.”

What you’ll take away:

- A methodology to measure forecast stability using forecast-to-forecast change.
- A mental model for when forecast revisions are useful and when they are just noise.
- Practical patterns you can implement immediately in Python to make forecasts calmer without hiding real change.

If you optimise only accuracy metrics, you are grading homework.
If you care about stability, you are building a forecasting product.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/B8KVNJ/>

## 59. [Causal Inference through the lens of probabilistic programming](https://pretalx.com/pyconde-pydata-2026/talk/Q9DU8N/)

**Speakers**: [Dr. Juan Orduz](https://pretalx.com/pyconde-pydata-2026/speaker/ADJDMC/)

**When and where**: Wednesday, 2026-04-15, 11:35–12:20, room Helium [3rd Floor]

**Type**: Talk (long) — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Causal inference asks the hardest question in data science: "What would have happened if things were different?" While traditional methods often rely on rigid rules, statistical tests or "black box" adjustments, Probabilistic Programming Languages (PPLs) like PyMC and NumPyro offer a transparent, flexible, and powerful lens to view these problems.

In this talk, we move beyond the standard "correlation is not causation" disclaimer. We will build a unified workflow that starts with robust A/B testing, moves to bias adjustment in observational data using multilevel models, and culminates with advanced Deep Causal Latent Variable Models (CEVAE).

**Description** (verbatim):

Why should you use a Probabilistic Programming Language (PPL) for Causal Inference? Because causal problems are inherently about uncertainty and structure—two things PPLs handle natively.

In this session, we will demonstrate how to translate causal diagrams (DAGs) directly into code, using PyMC and NumPyro to estimate causal effects with rigorous uncertainty quantification. We will cover three distinct levels of complexity, drawing on real-world examples and recent research:

1. The "Simple" Case: Enhancing A/B Tests Even in randomized experiments, PPLs provide massive value. We will show how to:

   - Use Prior Predictive Checks to prevent "silly" estimates (Twyman's Law) by incorporating domain knowledge into priors (e.g., preventing the model from predicting a 1000% lift). We also describe how to perform a _power_ analysis in a Bayesian framework.

   - Implement Bayesian CUPED to reduce variance and increase statistical power without collecting more data. We can combine these variance-reduction methods with smarter priors as described above.

2. The Observational Challenge: Confounding & Structure When we can't randomize, we must adjust. We will explore (through concrete examples):

   - Backdoor Adjustment: Show how PPLs implement the "do-operator" to estimate Average Treatment Effects (ATE) in the presence of observed confounders.

   - Multilevel Causal Models: Demonstrate how to use multilevel models to account for time-invariant unobserved confounders. We discuss the pros and cons compared with similar methods, such as fixed effects.

3. The Frontier: Deep Latent Variable Models: What if confounders are unobserved? We will introduce advanced methods combining Deep Learning with Probabilistic Programming:

   - An introduction to the Causal Effect Variational Autoencoder (CEVAE).

By the end of this talk, you will understand how to view causal inference not as a collection of isolated statistical tricks, but as a coherent modeling process powered by probabilistic programming.

### References

- **A/B Testing & Priors:** [Prior Predictive Checks for Metric Lift](https://juanitorduz.github.io/prior_predictive_ab_testing/) & [Power Analysis](https://juanitorduz.github.io/power_sample_size_exclude_null/)
- **Variance Reduction:** [Bayesian CUPED](https://juanitorduz.github.io/bayesian_cuped/)
- **Observational Data:** [Introduction to Causal Inference with PyMC](https://juanitorduz.github.io/intro_causal_inference_ppl_pymc/)
- **Hierarchical Models:** [Multilevel Causal Inference](https://juanitorduz.github.io/ci_multilevel/)
- **CEVAE Paper:** Louizos, C., Shalit, U., Mooij, J., Sontag, D., Zemel, R., & Welling, M. (2017). [Causal Effect Inference with Deep Latent-Variable Models](https://arxiv.org/abs/1705.08821).
- **Code Reference:** Adapting concepts from _CausalML_ (Robert Osazuwa Ness), specifically [Chapter 11: Bayesian Causal Graphical Inference](https://github.com/altdeep/causalML/blob/master/book/chapter%2011/Chapter_11_Bayesian_Causal_Graphical_Inference.ipynb).

**Links**:

- [slides](https://juanitorduz.github.io/html/causal_inference_ppl.html)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/Q9DU8N/>

## 60. [Small Language Models for Tool Calling Are Better Than You Think](https://pretalx.com/pyconde-pydata-2026/talk/AZ7GD3/)

**Speakers**: [Gabi Kadlecova](https://pretalx.com/pyconde-pydata-2026/speaker/GULAGN/)

**When and where**: Wednesday, 2026-04-15, 14:20–14:50, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Large language models have been widely used in tool-calling workflows thanks to their strong performance in generating appropriate function calls. However, due to their size and cost, they are inaccessible to small-scale builders, and server-side computing makes data privacy challenging. Small language models (SLMs) are a promising, affordable alternative that can run on local hardware, ensuring higher privacy.

Unfortunately, SLMs struggle with this task - they pass wrong arguments when calling functions with many parameters, and make mistakes when the conversation spans multiple turns. On the other hand, for production applications with specific API sets, we often don't need general-purpose LLMs - we need reliable, specialized models.

This talk demonstrates how to increase the accuracy of SLMs (under 8B parameters) for custom tool calling tasks. We will share how leveraging knowledge distillation helps to get the most out of SLMs in low-data settings - they can even outperform LLMs! We will present the whole pipeline from data generation, fine-tuning, and local deployment.

**Description** (verbatim):

Large language models have been widely used in tool-calling workflows thanks to their strong performance in generating appropriate function calls. However, due to their size and cost, they are inaccessible to small-scale builders, and server-side computing makes data privacy challenging. Small language models (SLMs) are a promising, affordable alternative that can run on local hardware, ensuring higher privacy.

Unfortunately, SLMs struggle with this task - they pass wrong arguments when calling functions with many parameters, and make mistakes when the conversation spans multiple turns. On the other hand, for production applications with specific API sets, we often don't need general-purpose LLMs - we need reliable, specialized models.

This talk demonstrates how to increase the accuracy of SLMs (under 8B parameters) for custom tool calling tasks. We will share how leveraging knowledge distillation helps to get the most out of SLMs in low-data settings - they can even outperform LLMs! We will present the whole pipeline from data generation, fine-tuning, and local deployment.

**What you'll learn:**

1. **Tool calling:** Different tool calling settings (single and multi-turn)
2. **Distillation**: Using large models as teachers to train specialized, compact models that maintain reliability with lower computational cost.
3. **Tool calling data generation:** Challenges in generating diverse tool calling data.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AZ7GD3/>

## 61. [Building Non-Biased Synthetic Datasets: What Actually Works (and What Fails)](https://pretalx.com/pyconde-pydata-2026/talk/M33SNJ/)

**Speakers**: [Shiva Banasaz Nouri](https://pretalx.com/pyconde-pydata-2026/speaker/NCHBH9/)

**When and where**: Wednesday, 2026-04-15, 15:00–15:45, room Helium [3rd Floor]

**Type**: Talk (long) — **Track**: PyData: Generative AI & Synthetic Data — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Synthetic data is often presented as an easy fix for missing or sensitive datasets, but in practice, it can silently introduce bias, leakage, and misleading evaluation results. This talk presents a practical, end-to-end pipeline for creating synthetic datasets that are reproducible, task-aligned, and bias-aware. We will walk through design decisions that matter: template-based generation vs. free-form generation, entity balancing, controlling distributional skew, filtering failure cases, and validating dataset quality before training any model. The session emphasizes what actually works in real pipelines, common failure modes that look fine at first glance, and concrete best practices for Python developers to apply when building synthetic datasets for machine learning, NLP, or evaluation.

**Description** (verbatim):

This talk focuses on the engineering side of synthetic dataset creation, treating data as a first-class artifact rather than a byproduct of modeling. It presents a concrete, reusable pipeline for building synthetic datasets that are reproducible, bias-aware, and suitable for evaluation.

1. Why Synthetic Data Is Not Automatically “Safe”
   We begin by examining common assumptions about synthetic data. While synthetic datasets avoid privacy issues, they often introduce hidden bias, distribution collapse, or label leakage. This section highlights real-world failure modes and explains why many synthetic datasets perform well in benchmarks but fail in practice.

2. What are the Main Properties of Synthetic Data 1. Simulated Data 2. Anonymized 3. Not Copied 4. Compliant 5. It is based on statistical property of real data.

3. Defining the Task Before Generating Any Data
   A dataset pipeline must start with a clear task definition. We discuss how ambiguous task definitions lead to incoherent data and misleading results, and how to formally specify label semantics, constraints, and negative space before generation begins.

4. Template-Based vs. Free-Form Generation
   This section compares controlled template-based generation with unconstrained LLM prompting. We show why decomposing generation into templates, placeholders, and curated value lists dramatically improves consistency, debuggability, and bias control.

5. Bias Control by Construction
   Rather than detecting bias after the fact, we show how to prevent it during generation. Topics include balanced entity lists, randomized substitution, avoiding demographic collapse, and preventing unintended correlations between labels and surface patterns.

6. Pipeline Architecture and Tooling
   We walk through a practical Python-based pipeline, covering modular generation stages, deterministic sampling, versioning, and reproducibility. Emphasis is placed on making dataset generation repeatable and auditable, just like code.

7. Filtering, Validation, and Quality Gates
   Synthetic data must be filtered aggressively. This section covers structural validation, label consistency checks, distributional sanity checks, and lightweight heuristics that catch most generation errors before model training.

8. Measuring Dataset Difficulty and Coverage
   We discuss simple, task-agnostic ways to estimate dataset diversity and difficulty, ensuring that synthetic data does not collapse into trivially easy examples or overly clean language.

9. What Did Not Work (and Why)
   This section summarizes failed approaches, including direct JSON generation, inline annotation, and large one-shot prompts. Understanding these failures helps avoid repeating common mistakes.

10. When Synthetic Data Is the Right Tool and When It Is Not
    We close with guidance on appropriate use cases for synthetic datasets, their limitations, and how they should complement, not replace, real data and human evaluation.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/M33SNJ/>

## 62. [From Ticket to Draft: How Munich Automates Citizen Inquiries with AI](https://pretalx.com/pyconde-pydata-2026/talk/39MHWT/)

**Speakers**: [Leon Lukas](https://pretalx.com/pyconde-pydata-2026/speaker/9FM8HN/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The City of Munich is modernizing its communication: With the transition to the Zammad ticketing system, there is a unique opportunity to not only manage citizen inquiries but to proactively process them using Artificial Intelligence. The Zammad-AI project utilizes a two-stage process consisting of intelligent classification and RAG-based (Retrieval-Augmented Generation) response drafting to significantly reduce the workload of administrative staff.
In this talk, we demonstrate how we integrated Zammad-AI via an internal Kafka message bus to process tickets in real-time. We explore the technical workflow—from thematic context analysis to the generation of valid response drafts based on a department-specific knowledge base.

**Description** (verbatim):

## 3. Session Outline (30 Minutes)

### I. Context & The Pre-Study | **5 min**

- **The Shift:** Transitioning from legacy email communication to **Zammad** within Munich's city administration.
- **Proving the Case:** Utilizing LLMs to analyze historical ticket data to calculate automation potential and project significant time savings before development began.

### II. Architecture: Integration & Pipeline | **6 min**

- **Event-Driven Design:** Connecting to Zammad via the city-internal **Kafka** message bus.
- **Real-time Processing:** How new tickets are captured and routed to the AI component seamlessly.

### III. The Two-Stage Process | **12 min**

- **Step 1: Classification & Extraction:** Analyzing thematic context through rule-based logic and LLM-powered information extraction.
- **Step 2: Response Generation:** A **RAG (Retrieval-Augmented Generation)** approach leveraging a knowledge base maintained by subject matter experts.
- **Human-in-the-Loop:** Integrating response drafts into the agent UI for review vs. automated **"dark processing"** for high-confidence categories.

### IV. Scaling & Lessons Learned | **4 min**

- **Multi-Tenant Capability:** Designing for configurability and deployment across various city departments.
- **Key Benefits:** Efficiency gains, response consistency, and establishing a "Single Voice of the City."

### V. Q&A | **3 min**

- Open discussion on technical tooling, model selection, and legal/privacy frameworks.

---

## 4. Key Takeaways for Attendees

- **Validating Automation:** Techniques for using LLMs to audit historical data and justify development through projected time savings.
- **Practical AI Integration:** How to integrate AI services into existing enterprise infrastructures like Zammad and Kafka.
- **Modular Workflow:** The importance of separating classification from generation for higher system reliability.
- **Operational Insights:** Lessons from scaling AI solutions across diverse governmental branches.

**Links**:

- [Github](https://it-at-m.github.io/zammad-ai/)
- [More Info on AI in Munich](https://ki.muenchen.de/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/39MHWT/>

## 63. [Beyond Vibe-Coding: A Practitioner's Guide to Spec-Driven Development in AI Engineering](https://pretalx.com/pyconde-pydata-2026/talk/CVPVPK/)

**Speakers**: [Alina Dallmann](https://pretalx.com/pyconde-pydata-2026/speaker/BZLFAX/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI-assisted coding became the default. Tools like GitHub Copilot, Cursor, and Claude can generate hundreds of lines of Python in seconds. However, the real challenge isn't how fast we generate code — it's how we ensure that generated code actually represents our intent, follows best practices, and integrates cleanly into existing systems.

In this talk, I present Spec-Driven Development (SDD), a way to engineer the context in which AI writes code. Using a realistic example from my work building production-grade retrieval-augmented generation systems, I show how specifications can become a practical way to interact with AI coding tools — grounded in a concrete use case, from spec to implementation.

**Description** (verbatim):

AI Engineering is fundamentally about system building. It is the transition from demos to production-grade Python systems that must be scalable, reliable, and testable. In my experience, one way to achieve this consistently with AI-generated code is to stop coding first — and start specifying first.

Spec-Driven Development is a practical methodology for AI-assisted development. It is not about heavy bureaucracy; it's about creating a "Single Source of Truth" that both humans and AI agents can rely on.

In this talk, I will walk through a realistic feature in a production-grade retrieval-augmented generation system. I will demonstrate how I used SpecKit — one example of a structured spec workflow, usable with different AI coding assistants — to move from a feature request to a reviewable spec, a research document, interface contracts, and a phased task plan — all before writing a single line of implementation code.

**What You Will Learn:**

- _What is Spec-Driven Development?_
- _The Paradigm Shift:_ Why "specifying" may be the new "coding" in a world of Large Language Models.
- _How to use SpecKit as one example of a structured spec workflow_ — usable with different AI coding assistants.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/CVPVPK/>

## 64. [To nest, or not to nest? Nested data types in Polars with big data](https://pretalx.com/pyconde-pydata-2026/talk/7PNT37/)

**Speakers**: [Daniel Finnan](https://pretalx.com/pyconde-pydata-2026/speaker/3US9H9/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Do you find yourself weighing up the pros and cons of using nested types in the Polars library - pondering whether you should encode your variables in structures using lists, arrays or opt for a flat format without complex hierarchy? This talk focuses on the crucial design choices available, the performance implications, and how this impacts the logic of your queries, as well as code readability, when deciding how to implement your big data pipeline in Polars. The methods available for nested types in Polars have seen some significant additions over the last year, with powerful functionality, such as filtering and aggregation, released in the latest versions of the library. These provide much-needed shortcuts for queries interrogating complex nested structures that previously required sophisticated user-defined functions. It makes the use of nested types much easier and intuitive, but does this mean you should nest your data? Through practical examples you’ll learn some guidelines to help you decide.

**Description** (verbatim):

If you’ve ever designed or used SQL databases in your data science projects perhaps you’ve cringed at the lack of relational structure and data duplication in the design of big data storage and processing. On the other hand, if you’ve spent any considerable time getting dirty with Polars’ vectorized and columnar processing, you’ll also know that this can be somewhat of a moot point. So why bother?

Outline of the talk:

5 minutes: Introduction & origin story. What are Polars nested types? How do they work? Why do they matter?
5 minutes: Back to the future. Advanced queries on nested types, past & present.
5 minutes: Query structure - “Group by” forever baby, versus element-wise.
5 minutes: Storage comparison and the gigabyte scrooge - how a miser decides on a nested Polars structure.
5 minutes: Time is money – How performance stacks up.
5 minutes: Q&A

By the end of the talk, participants will have seen several straightforward examples, as well more advanced illustrations of nested structures in Polars using real-world data. They will be able to identify some key considerations informing their use of nested structures, including query logic, storage and performance.

**Links**:

- [Blog post](https://daniel.finnan.fr/2026/05/17/to-nest-or-not-to-nest-nested-data-types-in-polars-with-big-data.html)
- [GitHub repository](https://github.com/daniel-finnan/polars-nested-types-pydata)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/7PNT37/>

## 65. [State of In-Browser ML: WebAssembly, WebGPU, and the Modern Stack](https://pretalx.com/pyconde-pydata-2026/talk/DQDEES/)

**Speakers**: [Oleh Kostromin](https://pretalx.com/pyconde-pydata-2026/speaker/NWAQCX/), [Iryna Kondrashchenko](https://pretalx.com/pyconde-pydata-2026/speaker/EACXYX/)

**When and where**: Wednesday, 2026-04-15, 10:15–10:45, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

What if you could run real data/ML workflows right in your browsers - sandboxed, with no installation or sending your data anywhere? Such an approach would have tons of benefits: it is easy to distribute, safer by default, and can scale almost infinitely with virtually no infrastructure costs.

This talk is a pragmatic overview of the current in-browser ML stack. We’ll cover what workflows are realistic today (from training of traditional ML models to on-device LLM inference), how packaging/loading works, and the constraints one should be aware of. By the end of the talk you will have a clear sense of when in-browser ML is a good fit, and when it isn’t.

**Description** (verbatim):

Over the last few years, the tooling has matured enough to make "ML in a tab" worth taking seriously. Today, you can execute Python code in a sandboxed environment, ship interactive demos as a single URL, and even run LLM inference entirely on-device, without installations, servers, or sending data anywhere. In this talk, we will give a practical overview of the current in-browser ML stack, focusing on what is realistically possible today and the practical limits you still have to design around.

We will start with interactive environments such as JupyterLite and explain how they work under the hood via Pyodide: what it means to run CPython compiled to WebAssembly, how the filesystem and networking model differ from "normal" Python, and what that implies for performance, I/O, and package support.

We will then move from notebooks to applications with PyScript, showing how the same building blocks can be used to create shareable browser-based tools. We will also briefly cover the lower-level approach: using Pyodide directly and orchestrating it with JavaScript for granular control over loading, packaging, and data interchange.

Finally, we will cover in-browser inference workflows for both traditional and deep learning models (via ONNX), and LLMs (via wllama and WebLLM), and discuss how WebGPU can accelerate these pipelines.

By the end of the talk, attendees will have a clear overview of the in-browser ML ecosystem and the practical intuition to decide whether it's the right choice for your next project.

**Target Audience:**
This talk can be relevant for a broad audience. However, at least intermediate knowledge of ML / familiarity with Python ML ecosystem is required.

**Outline:**

- Introduction + Motivating examples [4 min]
- Running Python in WebAssembly [6 min]
  - Overview of Pyodide [2 min]
  - Package management [3 min]
  - Runtime and memory constraints [1 min]
- Overview of interactive dev environments / JupyterLite [4 min]
- Building applications with PyScript and direct Pyodide bindings [7 min]
- On-device ML inference using ONNX, WebGPU, WebLLM, and wllama [5 min]
- Q&A [4 min]

Source: <https://pretalx.com/pyconde-pydata-2026/talk/DQDEES/>

## 66. [Leveraging Hexagonal Architecture When Building Applications](https://pretalx.com/pyconde-pydata-2026/talk/VY3CY7/)

**Speakers**: [Luke Gerstner](https://pretalx.com/pyconde-pydata-2026/speaker/SAGEL8/)

**When and where**: Wednesday, 2026-04-15, 10:55–11:25, room Platinum [2nd Floor]

**Type**: Sponsored Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Hexagonal architecture in software development is a design pattern that has existed for more than 20 years and remains highly applicable today as we enter an era where LLMs are increasingly used as development tools. At a high level, it can be used to create distinct layers within an application, resulting in more maintainable and flexible code. One of the primary benefits of utilizing this architecture is the separation of concerns, allowing different components of software to be swapped as needed - whether that is business logic, database technologies, or external services. In this talk, I will discuss the benefits and practical applications of hexagonal architecture. I will also include a detailed walkthrough of how this pattern is implemented in a real-world application.

**Description** (verbatim):

This talk will cover the following related to hexagonal architecture:

**Introduction**
The hexagonal architecture design pattern, also known as “Ports and Adapters”, was introduced by Alistair Cockburn in the early 2000s. With the increase in usage of LLMs as software development tools, this design pattern can help create clear boundaries within applications and make code more understandable and modifiable by AI tools.

**Core principles and concepts**
In this section, I will discuss the fundamental concepts that make hexagonal architecture effective. This includes, the central application core (business logic/domain), ports (interfaces that define contracts), and adapters (implementations that handle external interactions, for example interaction with a database or external services).

**Benefits and problem-solving capabilities**
The discussion will highlight benefits including enhanced testability, improved maintainability by reducing coupling, and easier technology migration. I'll demonstrate how hexagonal architecture addresses common development pain points such as database lock-in, framework dependencies, and the challenge of writing effective unit tests.

**Implementation and real-world case study**
Included in this presentation will be a real-world case study of how hexagonal architecture is implemented in a production application. This example will demonstrate how to handle common scenarios such as database functionality, external API integration, and user management. The case study will show actual Python code, highlighting patterns for repository implementations, service layers, and adapter configurations.

**Conclusion and Q&A**
The presentation concludes with the key takeaways, resources for further learning, and an interactive Q&A session.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/VY3CY7/>

## 67. [Scaling Data Processing for Training Workloads at DeepL Research with Rust](https://pretalx.com/pyconde-pydata-2026/talk/F79RG9/)

**Speakers**: [Jonas Dedden](https://pretalx.com/pyconde-pydata-2026/speaker/87HSSJ/), [Johanna Goergen](https://pretalx.com/pyconde-pydata-2026/speaker/VBRTYZ/)

**When and where**: Wednesday, 2026-04-15, 15:00–15:45, room Platinum [2nd Floor]

**Type**: Talk (long) — **Track**: General: Rust — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

This talk will detail how we used Rust to solve a number of resource utilization inefficiencies while scaling data pre-processing to a petabyte scale and enable next-generation model training at DeepL. Besides other factors, this was done by developing an internal library for interacting with Parquet files in a memory efficient nature.

Topics include:
• Convincing you to love Rust for its memory safety
• Comparing C++ and Rust ecosystems for Python library development
• Diving into Python-Rust interoperability
• Convincing you to love Rust for its user-friendly (yes, actually!) language features
• Providing a high-level overview of the continuously growing impact that Rust is having on the Arrow and data engineering ecosystem

**Description** (verbatim):

We set out to replace an inefficient internal file format with an industry standard - a seemingly straightforward task. What we got instead was a descent into memory leak hell.

This talk will walk you through our journey of scaling DeepL's data preprocessing and model training pipelines to handle petabyte-scale corpora. When open-source C++-based Python libraries proved too unstable and memory-inefficient, we invested time and resources into developing our own Rust-based tooling and, compared to our previous internal file format, decreased memory load by a factor of 10 and latency until first byte read by a factor of 50.

What we'll cover:
• **Why Rust's memory safety guarantees matter in practice:** We will provide a direct comparison of our results using C++-based vs Rust-based implementations for data processing libraries.
• **The Rust ecosystem advantage for Python interop:** While C++ offers a fragmented landscape of build systems and tooling choices, Rust provides a canonical path with cargo, maturin, and PyO3—providing a clean interface for everything from GIL management to readable, zero-copy conversions between Rust and Python objects
• **Rust's surprisingly friendly features:** Despite its reputation for having a steep learning curve, Rust offers language features that make it genuinely pleasant to work with, even for beginners coming from a Python background: from enums to pattern matching, error handling with Result, and cargo's canonical, ergonomic tooling.
• **Rust's impact on the arrow ecosystem and data engineering with Python in general:** Besides the well-known impact that Rust-based data processing libraries like polars, Daft, and datafusion are having on the engineering ecosystem, we we will show how the Rust implementation of Arrow called arrow-rs is having a growing impact and expanding the data engineering toolkit by powering an increasing number of great and contributor-friendly processing and introspection tools built in Rust.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/F79RG9/>

## 68. [Build a web coding platform with Python, run in WebAssembly](https://pretalx.com/pyconde-pydata-2026/talk/BFYYQG/)

**Speakers**: [Maris Nieuwenhuis](https://pretalx.com/pyconde-pydata-2026/speaker/W3RRQT/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyCon: Python Language & Ecosystem — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Ever wanted to build a website that can run python, but you're worried about running user submitted code on your server?
In this talk I'll show how Holoviz Panel can create an interactive coding environment where students can write functions, solve exercises, and experiment safely, all while their code runs locally via WebAssembly.

**Description** (verbatim):

### The Problem

Building interactive Python learning platforms traditionally requires server infrastructure to execute user code, creating security risks and operational overhead. What if we could run Python entirely in the browser?

### The Solution

This talk presents a coding platform built with Holoviz Panel that executes Python through WebAssembly via Pyodide. The entire application – UI and code execution – runs client-side, eliminating backend complexity while providing safe, isolated Python execution.

### Architecture Overview

The platform combines three key technologies:

- **Holoviz Panel** for building the interactive interface with its built-in code editor component
- **Pyodide** for secure Python execution via WebAssembly in the browser
- **LocalStorage** for persisting student progress without a database

### Key Features

The platform supports multiple learning modalities:

- Coding exercises validated against pre-defined test cases – from simple variable assignments to complete functions with return values or print statement
- Interactive playground that evaluates expressions and captures output
- Single and multiple-choice questions for concept checks

### What You'll Learn

This talk covers the technical integration between Panel's UI framework and Pyodide's execution environment – the critical piece that makes browser-based Python coding work. Attendees will understand:

- How to architect client-side Python applications
- Running Panel components with Pyodide
- Trade-offs between client-side and server-side execution
- Handling code execution, output capture, and state management

### Target Audience

Data scientists, educators, and developers interested in building interactive Python tools without server infrastructure. Basic familiarity with Python web frameworks is helpful but not required.

### Background

This work originated from my bachelor thesis exploring Python education. The resulting platform demonstrates that WebAssembly enables entirely new architectures for Python applications – shifting from traditional server models to fully client-side execution.

The takeaway: You can build sophisticated Python applications that run anywhere there's a browser, with no backend server setup, no security concerns about arbitrary code execution, and no additional infrastructure costs.

**Links**:

- [Talk slides (google slides)](https://docs.google.com/presentation/d/1RQqUNh6MiGLBcnrXRMVsfzBeusHU8aag6_G-Xqc1_1M/edit?usp=sharing)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BFYYQG/>

## 69. [Before You Ship Your Agent: An Agent Builder’s Primer on Jailbreaking Attacks](https://pretalx.com/pyconde-pydata-2026/talk/X3KQMQ/)

**Speakers**: [Simonas Černiauskas](https://pretalx.com/pyconde-pydata-2026/speaker/AZ7FNH/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Platinum [2nd Floor]

**Type**: Talk — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Before you ship an AI agent to production, you need to understand how it can be broken. Jailbreaking and prompt injection attacks are not edge cases—they are an inevitable consequence of deploying real-world, action-taking AI systems.

This talk is a practical primer on the most common ways agents fail under adversarial pressure. We’ll break down how jailbreaking and prompt injection attacks actually work, including techniques such as excessive agency, prompt leakage, and weaknesses in vector search and embeddings. We’ll examine why popular AI guardrails consistently fail in practice, and offer little more than a false sense of protection.

We’ll also address a common misconception: the absence of major AI security incidents does not mean systems are safe. Instead, it reflects limited deployment, constrained agency, and cautious rollout. As organizations adopt browser agents, autonomous tools, and systems that can take real-world actions, these vulnerabilities quickly become critical attack surfaces.

This talk focuses on what organizations should do instead: applying proven security principles—least privilege, isolation, monitoring, and abuse modeling—adapted to the unique properties of AI systems. Attendees will leave with a clear understanding of the real risks, why they matter today, and the concrete steps to take before shipping an AI agent into production.

**Description** (verbatim):

AI agents are rapidly moving from demos and copilots into production systems that browse the web, call APIs, execute workflows, and take real‑world actions. As this transition happens, a critical truth is becoming unavoidable: any agent with meaningful capability will be attacked—and most are easy to break. Jailbreaking and prompt injection attacks are not theoretical research topics or rare edge cases; they are an inevitable outcome of deploying autonomous, instruction‑following systems in adversarial environments.

This talk is a practical, engineering‑focused primer on how AI agents fail under real‑world pressure, and what organizations must understand before shipping an agent into production. Rather than focusing on sensational examples or hypothetical risks, we will examine the concrete mechanisms that attackers use today, why they work, and why many popular defenses provide little real protection.

We begin with a clear, accessible overview of jailbreaking and prompt injection attacks. Attendees will learn how attackers manipulate model instructions, context windows, and tool‑calling behavior to override intended safeguards. We’ll cover both direct prompt injection (explicitly malicious instructions) and indirect prompt injection, where hostile content is embedded in webpages, documents, emails, or user‑generated data that agents are designed to consume. These attacks are especially dangerous because they exploit normal, expected behavior rather than software bugs.

From there, we’ll explore several recurring failure modes that appear across nearly all production agent architectures:

Excessive agency: Agents are often given broader permissions and autonomy than necessary, turning minor instruction hijacks into high‑impact incidents.
Prompt leakage: System prompts, policies, secrets, and internal instructions are frequently exposed or inferable, providing attackers with a roadmap for further exploitation.
Vector and embedding weaknesses: Retrieval‑augmented generation systems can be poisoned or manipulated, allowing malicious content to outrank trusted sources and influence agent decisions.
Tool and browser abuse: Agents that browse the web or execute actions are uniquely vulnerable to hostile environments intentionally crafted to manipulate them.
A key focus of the talk is why AI guardrails don’t work the way many teams expect. We’ll examine common approaches—prompt‑based restrictions, content filters, and policy‑layer defenses—and explain why they are brittle, bypassable, and often fail silently. Rather than stopping attacks, these mechanisms frequently create a false sense of security that masks deeper architectural risks.

We’ll also address a common misconception in the industry: “If these vulnerabilities are so serious, why haven’t we seen major AI security incidents yet?” The answer is not that systems are safe, but that most deployments are still constrained—limited autonomy, limited blast radius, and cautious rollout. As organizations move toward browser agents, long‑running autonomous workflows, and systems with real operational authority, the conditions that have so far prevented large‑scale incidents will disappear. When that happens, these attack classes will move from curiosity to crisis.

The final section of the talk focuses on what actually works. Instead of recommending yet another AI security product or guardrail framework, we will outline practical, proven steps organizations can take today, grounded in decades of security engineering experience:

Applying least privilege and minimizing agent capabilities
Isolating tools, credentials, and execution environments
Designing for failure and containment, not perfect prevention
Monitoring agent behavior for abuse patterns rather than policy violations
Performing threat modeling that treats prompts and context as untrusted input
Attendees will leave with a clear mental model of how AI agents are attacked, why these attacks succeed, and how to reduce risk without relying on ineffective silver bullets. This talk is intended for engineers, security practitioners, and technical leaders building or deploying AI agents who want to understand the real risks—and take responsible action—before putting these systems into production.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/X3KQMQ/>

## 70. [Don’t Let Imposter Syndrome Win: U Can Do Big Things from a Small Place, A 7-Year African AI Journey](https://pretalx.com/pyconde-pydata-2026/talk/V7LQGR/)

**Speakers**: [Gift Ojeabulu](https://pretalx.com/pyconde-pydata-2026/speaker/YET9G9/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Platinum [2nd Floor]

**Type**: Talk — **Track**: General: Community & Diversity — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Imposter syndrome affects engineers everywhere, but underrepresented professionals often face amplified self-doubt due to geography, limited access, and systemic biases. In this talk, I share my 7-year journey as an African AI engineer building global impact from outside major tech hubs. From founding DataFestAfrica and leading remote AI opportunities to getting the attention of organizations like Huawei, MongoDB, McKinsey, and AnyScale, I’ll show how community, mentorship, open source, media presence, and strategic partnerships can create opportunities and influence. Attendees will gain practical strategies to overcome self-doubt, expand their reach, and make a meaningful difference in tech, no matter where they are.

**Description** (verbatim):

Imposter syndrome affects engineers worldwide, but for underrepresented professionals, geographic location, limited access to resources, and systemic biases can amplify its impact. Many talented engineers outside major tech hubs face self-doubt, missed opportunities, and barriers to career growth, even when they have the skills and vision to make meaningful contributions globally. Recognizing and addressing these challenges is crucial for building inclusive and diverse tech ecosystems.

This topic is particularly relevant for early- to mid-career engineers, community builders, and professionals navigating global tech ecosystems. Many in these groups experience self-doubt, uncertainty about career paths, and difficulty gaining visibility and recognition. Understanding how to overcome these challenges can empower them to take bold steps, make an impact beyond their immediate environment, and thrive despite systemic limitations.

In this talk, I share actionable strategies that helped me overcome imposter syndrome and build influence from any location. Drawing on my 7-year journey as an African AI engineer, I highlight how leveraging community building, open source contributions, mentorship, media engagement, and strategic partnerships can create meaningful opportunities. I illustrate these strategies through real-world examples, including founding DataFestAfrica, growing AI and MLOps communities with limited funding in emerging regions and collaborating with global organizations. Attendees will leave with practical insights to overcome self-doubt, expand their reach, and make a global impact from wherever they are.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/V7LQGR/>

## 71. [From Research Models to SLAs: Operationalizing TSFMs with Python](https://pretalx.com/pyconde-pydata-2026/talk/3XDMXS/)

**Speakers**: [Jeyashree Krishnan](https://pretalx.com/pyconde-pydata-2026/speaker/NH38CT/), [Catarina Filipe](https://pretalx.com/pyconde-pydata-2026/speaker/DNYXSR/)

**When and where**: Wednesday, 2026-04-15, 10:15–10:45, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Time series foundation models (TSFMs) such as Chronos, Lag-Llama, TimesFM, and Siemens’ own GTT have shown strong generalization capabilities across diverse forecasting tasks. However, integrating these models into a large organization is primarily a software engineering and MLOps challenge rather than a modeling one.

In this talk, we present a real-world case study based on Siemens KPI Forecast, a Python-based forecasting platform that operationalizes multiple TSFMs as reusable, production-grade services. The platform integrates both open research models and Siemens-developed models behind a unified API, supporting zero-shot inference, fine-tuning jobs, and fine-tuned inference depending on user needs and operational constraints.

We focus on how Python is used to compose heterogeneous components including open and closed-source models, internal data products, APIs, and orchestration layers into a consistent time series specialist user experience. The session also covers challenges operating such services within a B2B environment, including issues related to monitoring, versioning, and governance.

Attendees will gain practical insights into turning TSFMs into reliable Python services that scale across teams and use cases.

**Description** (verbatim):

### Motivation

Time series foundation models promise rapid prototyping and strong performance across domains, but many teams struggle to move beyond notebooks and benchmarks. In practice, the hardest problems are not model accuracy or architecture, but integration, operability, and developer experience.

This talk addresses a common but under-discussed question:

How do you operationalize time series foundation models inside a large organization with real users, real constraints, and real SLAs?

### Case study context

The talk is based on hands-on experience building and operating Siemens KPI Forecast, a Python-based forecasting platform that exposes multiple TSFMs through stable APIs. The platform integrates:

- Chronos ([https://arxiv.org/abs/2308.16103](https://arxiv.org/abs/2403.07815))
- Lag-Llama ([https://arxiv.org/abs/2310.08268](https://arxiv.org/abs/2310.08278))
- TimesFM ([https://arxiv.org/abs/2310.10688](https://arxiv.org/pdf/2310.10688))
- GTT, a Siemens-developed large-scale time series model (https://arxiv.org/pdf/2402.07570.pdf)

Chronos, Lag-Llama, and TimesFM are open-source research models, while GTT is a proprietary Siemens model. The platform is designed to treat both open and closed-source models uniformly from a developer and user perspective.

### Topics covered

- Why TSFMs are easy to prototype but hard to operationalize
- Designing Python APIs that unify multiple foundation models
- Supporting zero-shot inference, fine-tuning jobs, and fine-tuned inference in one system
- Integrating open-source and proprietary models consistently
- Making forecasting services accessible to different user personas
- Challenges related to operating ML services in a B2B environment including monitoring, versioning, and governance considerations

### What attendees will learn

- How to structure Python services around foundation models
- How to avoid fragmentation when supporting multiple models and workflows
- Practical MLOps patterns for operating ML services beyond notebooks
- Lessons learned from running TSFMs at organizational scale

This session focuses on engineering and operational lessons that are broadly applicable to teams building Python-based ML platforms in both enterprise and open-source contexts. Model references are included for transparency; the talk focuses on system design and operational patterns rather than proprietary details.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/3XDMXS/>

## 72. [Demystifying Agentic AI Using Small Language Models](https://pretalx.com/pyconde-pydata-2026/talk/YZM8TA/)

**Speakers**: [Serhii Sokolenko](https://pretalx.com/pyconde-pydata-2026/speaker/ZUECPC/)

**When and where**: Wednesday, 2026-04-15, 10:55–11:25, room Europium [3rd Floor]

**Type**: Talk — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The AI world is buzzing with claims about “agentic intelligence” and autonomous reasoning. Behind the hype, however, a quieter shift is taking place: Small Language Models (SLMs) are proving capable of many reasoning tasks once assumed to require massive LLMs. When paired with fresh business data from modern lakehouses and accessed through tool calling, these models can power surprisingly capable agents.

In this talk, we cut through the noise around “agents” and examine what actually works today. You’ll see how compact models such as Phi-2 or xLAM-2 can reason and invoke tools effectively, and how to run them on development laptops or modest clusters for fast iteration.
By grounding agents in business facts stored in Iceberg tables, hallucinations are reduced, while Iceberg’s read scalability enables thousands of agents to operate in parallel on a shared source of truth.
Attendees will leave with a practical understanding of data agent architectures, SLM capabilities, Iceberg integration, and a realistic path to deploying useful data agents - without a GPU farm.

**Description** (verbatim):

The Agentic Buzz - What’s Real, What’s Marketing

- The explosion of “agentic” frameworks and the confusion it causes
- What an agent really is at its core: planning, acting, and reasoning

Anatomy of an Agent

- The three basic functions: task decomposition, tool use, and code synthesis
- How frameworks like LangChain and Python make it easy to chain these together

Why Small Models Are Catching Up

- Review of research from NVIDIA and Georgia Tech
- Benchmarks showing SLMs matching or exceeding performance of larger LLMs
- Cost, latency, and deployability tradeoffs

Hands-On Demo: Building and Running an Agent on a Laptop

- Using LangChain and Python to orchestrate reasoning, tool calls, and code execution
- Example workflow: “Plan a dataset cleanup pipeline” using an SLM
- Observing resource use, latency, and performance in real time

Key Takeaways and Open Research Directions

- Opportunities for local and edge deployments
- The emerging role of SLMs in allowing everyone to experiment with agents
- Future questions: scaling reasoning vs. scaling models

Source: <https://pretalx.com/pyconde-pydata-2026/talk/YZM8TA/>

## 73. [Building Secure Environments for CLI Code Agents](https://pretalx.com/pyconde-pydata-2026/talk/3BYLZU/)

**Speakers**: [Harald Nezbeda](https://pretalx.com/pyconde-pydata-2026/speaker/VED8E9/)

**When and where**: Wednesday, 2026-04-15, 11:35–12:05, room Europium [3rd Floor]

**Type**: Talk — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI code agents like Claude Code are powerful but require careful isolation. Learn how to run them in secure containers with persistent credentials, API logging, and complete filesystem isolation—protecting your host system while maintaining full functionality.

**Description** (verbatim):

AI-powered code agents like Claude Code can autonomously edit files, run commands, and interact with your development environment. This power comes with risks: unrestricted filesystem access, exposed credentials, and unmonitored API usage. How do you harness this capability safely?

This talk presents a practical containerization approach for running CLI code agents in complete isolation from your host system. You'll learn how to build secure environments that maintain persistent authentication, enable workspace access through volume mounts, and provide full API request logging, all while keeping the agent sandboxed.

I'll demonstrate a production-ready setup using Docker containers that includes credential management, an API proxy for request logging and monitoring, and Datasette integration for analyzing API usage patterns. You'll see how to structure volumes for security, implement network isolation, and maintain developer productivity while enforcing safety boundaries.

**Links**:

- [Slides](https://nezhar.com/slides/pycon-de-26/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/3BYLZU/>

## 74. [Mastering the Hex: A Case Study in Reinforcement Learning for Strategy Games](https://pretalx.com/pyconde-pydata-2026/talk/MJTQEJ/)

**Speakers**: [Simon Hedrich](https://pretalx.com/pyconde-pydata-2026/speaker/VX8JGC/)

**When and where**: Wednesday, 2026-04-15, 14:20–14:50, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

What does it take to build an AI that learns to play strategy games from scratch? Over the past year, I chose to explore this question out of personal fascination with game AI — as a seminar project for college, but really as a hobby. The result was a complete reinforcement learning environment for Antiyoy, a turn-based strategy game played on hexagonal grids.

The journey raised intriguing challenges: How do you represent hexagonal game boards for neural networks? What do you do when your AI has over 4,000 possible actions to choose from? How do you design rewards that teach strategy rather than just reward flailing in the right direction? This talk shares how these problems were approached using Python's modern ML ecosystem—Gymnasium, PyTorch, and PPO training—ultimately producing an agent that wins nine out of ten games against a random opponent. Whether that qualifies as "strategic play" is a question the agent and I still disagree on.

Whether you're curious about building custom RL environments, interested in game AI, or just wondering what reinforcement learning actually looks like when it half-works, you'll leave with practical insights and a healthy dose of realistic expectations.

**Description** (verbatim):

### Context and Motivation

This talk emerged from a year-long journey that began with a simple curiosity: could I teach a computer to play strategy games by itself? It started as a college seminar project, but the topic was chosen purely out of personal interest in reinforcement learning and game AI — this was a hobby from the start. Rather than working with pre-built environments like CartPole or Atari games, the goal was to understand the entire pipeline—from implementing game mechanics to training a neural network that actually learns to win.

The game chosen was Antiyoy, a minimalist turn-based strategy game where players control territories on hexagonal grids, build units and structures, manage resources, and compete for dominance. While the game is simple enough to understand, it presents genuine strategic depth—exactly the kind of challenge that makes reinforcement learning both difficult and rewarding.

The talk walks through the complete development process, focusing not on implementation minutiae but on the fundamental questions and design decisions that anyone building similar systems would encounter. You won't see walls of code or detailed mathematical derivations. Instead, you'll hear about the thinking process, the challenges faced, and the solutions that emerged—all with the goal of demystifying what it actually takes to build a learning agent for complex games.

---

### What Will You Learn?

The talk is structured around three core challenges that define this kind of project, presented as questions that the work had to answer:

**How do you turn a game into something a neural network can understand?**

Strategy games aren't naturally suited for machine learning. Antiyoy is played on hexagonal grids, uses discrete turn-based actions, and involves complex state information—territory ownership, unit positions, economic resources, and more. The talk explores how to bridge this gap: representing hexagonal coordinates in ways that computers can efficiently process, encoding complete game state into multi-channel observations similar to those used in AlphaZero, and designing observation spaces that preserve spatial relationships for convolutional networks. You'll hear about the choice between different coordinate systems, the challenge of maintaining game history for temporal reasoning, and how to normalize diverse information types (positions, money, turn counts) into a coherent input for neural networks.

**How do you handle massive action spaces without overwhelming your AI?**

When your agent has more than 4,000 possible actions at any given moment—moving units to different positions, building various types of units and structures, or ending the turn—training becomes a serious challenge. Most of these actions are illegal at any given time, yet a naive approach would force the agent to learn this the hard way. The talk discusses how action masking solves this problem by dynamically filtering the action space to only legal moves, dramatically improving learning efficiency. You'll understand why this technique is crucial for games with complex rules and how it fundamentally changes the training dynamics compared to environments where every action is always available.

**How do you design rewards that actually teach strategy?**

Perhaps the most subtle challenge in reinforcement learning is reward design. Give an agent only a +1 for winning and -1 for losing, and it may take forever to figure out what behaviors lead to victory. But add too many intermediate rewards, and you risk the agent exploiting shortcuts rather than learning genuine strategy. The talk shares the experimentation process: starting with sparse rewards as a baseline, carefully introducing intermediate signals for meaningful actions like territory expansion and economic development, and ultimately landing on a reward structure that accelerated learning while still encouraging strategic play. You'll see how reward shaping influenced training speed and final performance, and learn to think about reward design as a crucial part of the development process rather than an afterthought.

---

### What Are the Results and Takeaways?

After training over several thousand episodes—which took about eight hours on a consumer-grade GPU—the agent learned to win approximately nine out of ten games against a baseline random opponent. To be precise about what that means: the baseline picks uniformly from legal moves, so the bar is not high. The trained agent makes progress through a game, expands territory, and occasionally does things that look like they could be intentional. It also makes plenty of moves that defy easy explanation. "Strategy" might be a generous word; "learned to flail more purposefully" is closer to the truth.

The talk concludes by reflecting on what worked well and what proved unexpectedly difficult—and what is still unresolved. Action masking emerged as perhaps the single most impactful technique for managing complexity. The choice of observation space design—borrowing ideas from AlphaZero's approach to representing board games—turned out to be well-suited for the problem. Training infrastructure using MLflow provided invaluable insight into the learning process and made experimentation much more manageable. On the challenging side: reward design required multiple iterations and still produced an agent that plays competently but not strategically. The gap between "beats random" and "actually plays well" is humbling and, it turns out, enormous.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/MJTQEJ/>

## 75. [Building Agentic Systems with Python, LangGraph, MCP, and A2A](https://pretalx.com/pyconde-pydata-2026/talk/JBFGCA/)

**Speakers**: [Holger Nösekabel](https://pretalx.com/pyconde-pydata-2026/speaker/K9VNNX/)

**When and where**: Wednesday, 2026-04-15, 15:00–15:45, room Europium [3rd Floor]

**Type**: Talk (long) — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Building an agentic system that collects and evaluates company information in real time—without curated datasets—requires solving difficult challenges in data acquisition, quality control, and agent orchestration.

This talk outlines the solution design for such a system, implemented with Python-based tooling including LangGraph, and emerging protocols such as A2A and MCP, within a multi-agent workflow. Because MCP and A2A are still new and lightly documented, we will share implementation lessons and a practical example of a hub-and-spoke architecture based on a recent real-world system.

Attendees will learn architectural patterns for multi-agent systems, common pitfalls of using MCP/A2A in real-world scenarios, and strategies for maintaining data quality in agent-based workflows.

**Description** (verbatim):

# What we are going to show

- A live demo of a Python-based multi-agent system that retrieves, aggregates, and evaluates company information in real time.
- The overall solution architecture: how LangGraph, MCP, A2A, and custom Python components fit together.
- Key implementation lessons from building the system, covering both technical and business challenges.

# What problem is our talk addressing

AI analysis depends heavily on data. When systems cannot rely on pre-collected or curated datasets, developers must find, collect, and validate data of sufficient quality.

At the same time, emerging technologies such as MCP, A2A, and LangGraph are evolving quickly, with limited documentation, occasional breaking changes, and examples that rarely scale beyond minimal tutorials. Applying these tools to real-world Python applications introduces challenges in design, orchestration, versioning, and error handling that are not yet widely discussed.

# Why is the problem relevant to the audience

Many Python developers and data practitioners will soon need to build systems that combine LLMs, external data sources, and multi-agent logic, without relying on static datasets. This talk provides practical guidance for designing such systems using open-source Python tooling.

The presented solution is designed with a modular, scalable component approach. MCP and A2A protocols facilitate the connection between AI-related solutions, and this design demonstrates re-usable patterns for implementation.

By sharing our approach, design choices, and implementation pitfalls, the talk equips attendees to anticipate challenges early, evaluate whether MCP/A2A are appropriate for their own projects, and build more robust agentic systems.

# What is our solution to the problem

Our solution has split responsibilities in several blocks, though the overall idea is to present with code examples a Python system that combines LangGraph, A2A and MCP:

- Data access via MCP servers
  MCP servers retrieve data from multiple sources (e.g., LinkedIn APIs, web scraping endpoints, Perplexity research). Using MCP makes it easy to plug in new data sources and manage them consistently. We demonstrate how to build and connect MCP servers in Python.
- Data processing via LangGraph agents
  A set of agents implemented in LangGraph handle tasks such as coordinating the workflow, collecting company data, calculating evaluation scores, and validating results. These agents operate in a hub-and-spoke pattern centered around a coordinator agent. We show how this is implemented in Python using LangGraph.
- Inter-agent communication via A2A
  Agents exposes capability “cards,” which the coordinator aggregates into a registry. An intent-detection step determines which agents should be invoked to answer a user's request. We demonstrate how A2A can be applied in Python to orchestrate agents effectively.
- Data validation agent
  A dedicated validation agent checks retrieved data against defined rules to ensure quality. While no internet-sourced data is perfect, this approach significantly increases reliability. We show how validation logic is implemented within the LangGraph flow.
- Scalability through configuration and deployment
  A centralized configuration file and simple Docker-based deployment make the system easy to scale and adapt. We explain how environment variables and shared configuration patterns can coordinate the various Python components.

# What are the main takeaways from our talk

Attendees will learn:

- How to design and implement a practical multi-agent architecture using Python, LangGraph, MCP, and A2A.
- How to acquire and validate external data dynamically without relying on curated datasets.
- Common pitfalls and lessons from using MCP and A2A in larger-scale systems.
- How to structure agent roles, orchestration flows, and validation strategies for scalable, extendable AI systems.

**Links**:

- [GitHub Repository](https://github.com/hnoesekabel/ai_agents_pycon2026)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/JBFGCA/>

## 76. [Tidy Finance in Practice: How Explicit Assumptions Avoid Bad Investment Strategies](https://pretalx.com/pyconde-pydata-2026/talk/XGL37G/)

**Speakers**: [Christoph Frey](https://pretalx.com/pyconde-pydata-2026/speaker/XTMJSZ/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Europium [3rd Floor]

**Type**: Talk — **Track**: General: Others — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Many investment strategies look convincing because they performed well in the past, but these results are often easy to misread and do not always say much about how the strategy would work in the future. In many cases, strong backtest results come not from real skill or insight, but from hidden rules, unclear data choices, or unrealistic assumptions. In this talk, I show how Tidy Finance principles help make these issues visible and easier to examine. Using clear examples from Tidy Finance with Python, I demonstrate that once assumptions are made explicit, many impressive results no longer hold up.

**Description** (verbatim):

Many investment strategies look great because they performed well in the past. However, it is often unclear why they work or whether they would still work in the future. Strong backtest results are frequently driven by hidden assumptions, unclear data handling, or unrealistic rules rather than real skill or insight.

In this talk, I show how Tidy Finance principles help people better understand what is actually happening inside a financial backtest. Tidy Finance has become a popular open-source teaching and learning platform for empirical financial research. Its core idea is simple: financial analyses should be built from clear, well-structured data that makes assumptions easy to see and results easy to reproduce.

Using explicit examples from Tidy Finance with Python during the talk, I go through a real backtesting workflow and show how it changes when assumptions are written down clearly instead of being hidden inside the code. I demonstrate how small, often overlooked choices can have a large impact on results, and how these effects become visible when the analysis is structured cleanly. The focus is on learning how to read and question backtests, not on presenting new models or strategies.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/XGL37G/>

## 77. [Octopus AutoML: Extracting Signal from Small and High-Dimensional Data](https://pretalx.com/pyconde-pydata-2026/talk/8YTYEN/)

**Speakers**: [Nils Haase](https://pretalx.com/pyconde-pydata-2026/speaker/EYAZMY/), [Andreas Wurl](https://pretalx.com/pyconde-pydata-2026/speaker/TLZK97/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Many machine learning tools assume abundant, independent data, rely on a single data split plus cross-validation, and leave test-set separation to the user.

In application-driven domains such as industrial materials science and pharmaceutical development, data are scarce, high-dimensional, and often correlated, creating conditions under which standard ML pipelines frequently fail. Small datasets are highly sensitive to the random seed used for splitting, and common pitfalls such as feature selection before splitting or distributing correlated samples across train and test sets cause data leakage and inflated performance metrics.

Octopus is an open-source Python AutoML library explicitly designed for small-data, high-dimensional regime. It enforces strict nested cross-validation for model and hyperparameter selection, quantifies performance variability across multiple splits, and tightly controls data leakage. Its modular architecture embeds an internal ML engine, several feature selection methods (e.g., MRMR, Boruta), and external AutoML solutions such as AutoGluon into a unified, rigorous validation framework, enabling systematic and fair comparison of methods on limited data. In addition, Octopus supports survival analysis, addressing time-to-event problems common in healthcare and materials science. This talk will use realistic small-scale datasets to illustrate how conventional pipelines can be misleading and how to obtain more reliable models when every sample matters.

**Description** (verbatim):

Many machine learning tools are based on the quiet assumption that data is plentiful, independent, and identically distributed, and that a random training/testing split, plus a little cross-validation, is “good enough”. In application-driven domains such as pharmaceutical development and industrial materials science, however, this is often not the case. Synthesizing a new compound can take months and early phase clinical trials are small, so we often work with fewer than 1,000 samples and several thousands of features. In this context, standard AutoML practice can be dangerously optimistic.

On small datasets, performance can vary significantly depending on the random seed used for splitting the data. Working with a single split exposes us to this randomness: with an unlucky seed we might prematurely abandon promising experiments, while a particularly favorable seed can lead to overestimating the true performance. Another major risk is data leakage, such as performing feature selection before splitting the data, or distributing correlated samples (e.g., repeated measurements from the same patient or material batch) across both training and test sets. Such leakage inflates evaluation metrics and produces models that fail to generalize to new data.

Octopus is an open-source Python AutoML library designed specifically for small and high-dimensional datasets. Its core idea is simple: make statistically honest evaluation the default. Octopus enforces strict nested cross-validation, with an inner loop for model and hyperparameter selection and an outer loop that provides generalization performance estimates. Thanks to this nested setup, users also obtain an estimate of how much performance varies across multiple data splits; low variation increases trust in the reported results. Furthermore, because Octopus handles the entire data-splitting process and is carefully designed to avoid information leakage, the reported metrics are far less likely to be inflated.

Our library provides a robust drop-in replacement for existing machine learning workflows, ensuring a principled implementation of nested cross-validation while leveraging advanced machine learning techniques in the background. Adopting a modular architecture, the library offers a dedicated, internally developed ML module, seamless integration of several feature selection methods (e.g., MRMR, Boruta), and support for external ML solutions such as AutoGluon. This modular design makes Octopus a powerful platform for benchmarking different methods and solutions on specific datasets and use cases, helping users systematically compare and select the most suitable approach for their problem

Octopus also supports time-to-event (survival) problems, which are common healthcare (e.g. time to progression or death) and in materials science (e.g. time to failure or degradation). Survival models are evaluated using appropriate metrics within the same nested cross-validation framework.

This talk will demonstrate, using realistic small-scale datasets, how standard AutoML pipelines can report deceptively strong performance and how these metrics change when proper nested cross-validation and domain-aware splits are applied. Attendees will learn where typical mistakes originate and how Octopus establishes practical safeguards against them. The goal is straightforward: to produce better models and more reliable conclusions when data are scarce and every sample matters.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/8YTYEN/>

## 78. [Heat: scaling the Python scientific stack to HPC systems](https://pretalx.com/pyconde-pydata-2026/talk/K9LCNQ/)

**Speakers**: [Claudia Comito](https://pretalx.com/pyconde-pydata-2026/speaker/JKT3YT/), [Thomas Saupe](https://pretalx.com/pyconde-pydata-2026/speaker/BELFDP/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python’s scientific stack (NumPy/SciPy) is often confined to single-node execution. When datasets exceed local memory, researchers face a steep learning curve, typically choosing between complex manual distribution or the overhead of task-parallel frameworks.

In this talk, we introduce [Heat](https://github.com/helmholtz-analytics/heat), an open-source distributed tensor framework designed to bring high-performance computing (HPC) capabilities to the scientific Python ecosystem. Built on PyTorch and mpi4py, Heat implements a data-parallel model that allows users to process massive datasets across multi-node, multi-GPU clusters (including AMD GPUs) with minimal code changes.

We will discuss the design and architecture enabling "transparent distribution":

- Heat’s distributed n-dimensional array for data partitioning and communication under the hood;
- The synergy of PyTorch as a high-performance compute engine and MPI for efficient, low-latency communication;
- Scaling efficiency, encompassing both strong and weak scaling for memory-intensive operations;
- Fundamental building blocks—from linear algebra to machine learning—re-implemented for distributed memory space.

Attendees will learn how to leverage the cumulative RAM of supercomputers without leaving the familiar NumPy-like interface, effectively removing the "memory wall" for large-scale scientific analytics.

**Description** (verbatim):

**Memory bottleneck in scientific computing (4 minutes)**

- Limitations of single-node libraries
- Complexity of existing workarounds: trade-offs between manual MPI programming (high developer effort) and task-parallel frameworks
- The data-parallel alternative: performing uniform operations on distributed slices of a global tensor.

**Architecture and implementation (8 minutes)**

- The DNDarray structure: Technical breakdown of the distributed n-dimensional array, which provides a global logical view while managing local physical storage across MPI ranks.
- The split axis concept: How data is partitioned along specific dimensions (e.g., rows or columns) to optimize communication for different mathematical operations.
- Backend synergy:
  - PyTorch as the compute engine for high-performance local tensor operations and GPU acceleration.
  - mpi4py for communication in cluster environments.
- Hardware interoperability: Transparent execution across CPUs and GPUs, including NVIDIA (CUDA) and AMD (ROCm) accelerators.

**Algorithmic building blocks for distributed memory (8 minutes)**

- Communication-aware linear algebra: Distributed matrix-matrix multiplication and its communication costs. Advanced matrix decomposition methods, such as hierarchical and randomized SVD (hSVD), for massive datasets.
- Scalable machine learning and statistics: Example: clustering (K-Means) and Principal Component Analysis (PCA) on distributed arrays.
- Temporal analysis using Dynamic Mode Decomposition (DMD) on large-scale scientific data like global wind speeds.

**Performance and scaling efficiency (7 minutes)**

- Scaling methodologies: strong scaling (speedup for a fixed problem size) and weak scaling (efficiency as both problem size and resources grow).
- Memory wall removal: Utilizing the cumulative RAM of many cluster nodes to process datasets that are otherwise impossible to load.
- Case studies: Reviewing performance results from large-scale runs

**Summary and project roadmap (3 minutes)**

- Key takeaways
- Upcoming features
- Open-source community

Source: <https://pretalx.com/pyconde-pydata-2026/talk/K9LCNQ/>

## 79. [From Pixel to Payouts: A Multi-Agent System for Real-Time Insurance Claims Processing](https://pretalx.com/pyconde-pydata-2026/talk/APWGQB/)

**Speakers**: [Claudio Giorgio Giancaterino](https://pretalx.com/pyconde-pydata-2026/speaker/VDZH9N/)

**When and where**: Wednesday, 2026-04-15, 10:15–10:45, room Palladium [2nd Floor]

**Type**: Talk — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The traditional process for auto damage evaluation is relatively slow, subjective, and prone to fraud. With this presentation, the goal is to show a Multi-Agent System designed for the automation and standardization in real-time of the car damage evaluation, disrupting the initial claims workflow. The system is built around an Orchestrator Agent with the role to coordinate specialized AI agents: a Vision Agent (powered by OpenAI GPT-5.2) for damage analysis and severity classification, two Cost Estimation Agents (powered by Perplexity's sonar-pro) to provide comparative quotes (OEM vs. Aftermarket), and a Shop Finder Agent for local repair options. The system produces a report that includes a description of the damage, severity, comparative repair costs in local currency, and recommended repair shops, all embedded into a Gradio/Streamlit interface. The task of this approach is to reduce the processing time, improve transparency for customers, and provide insurers with objective data to enable faster claims resolution.

**Description** (verbatim):

**Project Goal and Business Impact**
Imagine filing an auto insurance claim. Instead of waiting days for a damage evaluation, photograph the car with your phone and, within minutes, receive a detailed assessment.
The primary objective of this project is to drastically improve the efficiency and objectivity of the initial auto insurance claim process. Current methods rely heavily on human adjusters and manual estimates, resulting in delays and potential cost inflation. By deploying a sophisticated Multi-Agent System, the aim is to provide a fastly, data-driven assessment that benefits both the insurer and the customer.
**The Multi-Agent Architecture**
At the heart of this solution, there is an orchestrated system of specialized AI agents, each with a distinct role. The architecture follows a sketch where an Orchestrator Agent works as the brain, creating execution plans, managing agent lifecycle, coordinating the execution, and aggregating results into coherent outputs.
The Vision Agent, powered by OpenAI GPT-5.2, acts as the system's eyes. It analyzes uploaded damage photos with technical precision, identifying specific damaged parts (bumpers, panels, headlights, etc.), classifying severity levels (minor, moderate, severe), categorizing damage types (collision, scratch, dent, paint damage), and generating detailed technical assessments.
Two specialized Cost Estimation Agents run, representing different repair philosophies. The OEM (Original Equipment Manufacturer) Agent focuses on premium repairs using manufacturer-certified parts from authorized dealers, while the Aftermarket Agent explores cost-effective alternatives using quality certified aftermarket parts from independent shops. Both agents are powered by Perplexity's sonar-pro model, which provides access to current market data and pricing information.
The Shop Finder Agent searches for repair facilities near the user's location, provides contact information, ratings, and availability, and adapts its search strategy based on the information retrieved.
**Technical Highlights**
The system is built in Python, leveraging several key technologies. The Gradio/Streamlit framework provides an intuitive web interface for image upload, location input, and real-time results display. OpenAI's GPT-5.2 handles computer vision tasks. Perplexity's sonar-pro model accesses current market data for repair costs and local business information.
A sophisticated state management system provides each agent with memory of past interactions, confidence scores to assess decision quality, performance tracking to optimize the system, and context-aware autonomous decision-making.
At the core of each agent's execution is the ReAct loop: a Reasoning, Action, Observation cycle. Each agent doesn't just call an API and return a result; it first records a thought explaining why it's taking an action, executes the action, and then logs its observations. This trace is accumulated across all agents and surfaced in the UI as a collapsible reasoning log, making every decision in the pipeline fully auditable and transparent.
**Generative AI vs. Manual/Traditional Tools**
While traditional automated tools rely on rigid, rule-based computer vision and static databases, this Multi-Agent System introduces a modular reasoning layer that bridges the gap between raw data and decision-making. According to the industry research from McKinsey (2025) the agentic workflows reduce claim cycle times from days to seconds with consistency in claim evaluations.
Traditional tools are often "black boxes" or monolithic scripts, instead this modular architecture give the opportunity to develop in the future every task as a swappable module for an hybrid framework where every single agent can be replaced by a non Generative AI tool, for flexible, custom and scalable solution.  
**The Future of Insurance Claims**
This multi-agent architecture is a robust, scalable blueprint for automating complex decision-making business processes, such as insurance claims. It leverages the strengths of several large language models (LLMs) and specialized agents to deliver a fast, transparent, and comprehensive output that far exceeds the capabilities of a single model. The project demonstrates practical, real-world applications of multi-agent systems in production environments.

**Links:**
[Article](https://medium.com/@c.giancaterino/from-pixel-to-payouts-a-multi-agent-system-for-real-time-insurance-claims-processing-d647298c4eb8)
[Hugging Face App](https://huggingface.co/spaces/towardsinnovationlab/AI_Car_Damage_Evaluation)
[Repository](https://github.com/claudio1975/AI_Car_Damage_Evaluation)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/APWGQB/>

## 80. [No, you can't 'eval' your way to fairness](https://pretalx.com/pyconde-pydata-2026/talk/S7KYEE/)

**Speakers**: [Laura Summers](https://pretalx.com/pyconde-pydata-2026/speaker/NYBL9E/)

**When and where**: Wednesday, 2026-04-15, 10:55–11:25, room Palladium [2nd Floor]

**Type**: Talk — **Track**: General: Ethics & Privacy — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Fairness is fundamentally not tractable to classic optimisation techniques. It's not a state of the world, it's an experience of it. No technology is fair in a vacuum - fairness can only be understood when a technical system collides with humans.

We're seeing a wave of off-the-shelf libraries measuring bad behaviours in LLM outputs, often simplifications of older fairness metrics. They can catch obvious failure modes like slurs. But this is one failure mode among many. Installing a library and calling the job done is fairness washing. The harder, more fruitful approach is to explore the space of failure modes, consider what an ideal world would look like, and design measures, mitigations, and feedback loops accordingly.

This is a talk for people who suspect we can't optimise our way to human dignity.

**Description** (verbatim):

**Cold open**
Fairness is fundamentally not tractable to classic optimisation techniques.

**The exposition**
Fairness is not a state of the world, it's an experience of it. No technology is fair in a vacuum. Fairness can only be understood when a technical system collides with humans in the world. It is felt as much as it is calculated. We can look at statistical results in aggregate to understand patterns, but these do not tell the story of the individual.

Further, attempting to optimise numerical fairness metrics is fundamentally coercive and technocratic: putting our thumb on the scale globally, injecting "positive bias" into single dimensions, framing fairness as a data problem rather than a problem of human dignity. It's a "one metric to rule them all" approach that fails to acknowledge differences in preference, culture, experience. To build systems that support human agency we must first abandon our idea of a single moral machine which consistently outputs correct answers from inputs and algorithms. Any system treating people as fungible or undifferentiated is structurally unfair.

What might consent-based fairness look like instead? Asking "Do you want extra help?", making sure individual preferences and self-reported disadvantage can add a layer of human respect into the equation. But we rarely see even this. Instead we see universalist design that decides what's good for people without consulting them - the same pattern that Design Justice critiques as erasing those who experience intersectional disadvantage.

What does this have to do with evals? We're seeing a wave of off-the-shelf libraries measuring bad behaviours in LLM outputs, often simplifications of older fairness metrics. And yes, they can catch obvious failure modes like slurs in outputs. But this is one failure mode among many. Installing a library and calling the job done is fairness washing. The harder, more fruitful approach is to explore the space of failure modes, consider what an ideal world would look like, and design measures, mitigations, and feedback loops accordingly. It also means grappling with the fact that we cannot avoid doing harm. What we can do is harm reduction, humility, and striving toward something better while acknowledging the impossibility of the task.

**Third act**
This talk won't offer easy answers. Attend if you want to grapple with the gnarly problems of building systems for humans. We'll borrow ideas from Design Justice and the disability rights movements: nothing about us without us. Let's ask and answer better questions. You'll leave with sharper mental models and tools for the next tricky conversation at work.

**Outline (30 minutes):**
The problem (10 min):

- Fairness as experience, not state.
- Why optimisation fails.
- The individual vs the aggregate.
- Why treating people as fungible is structurally unfair.

The critique (10 min):

- Off-the-shelf fairness evals as fairness washing.
- The temptation to install a library and call it done.
- What these tools can and cannot catch without further analysis.

The alternative (10 min)

- Borrowing from Design Justice and disability rights.
- Exploring failure modes rather than optimising metrics.
- Harm reduction over false perfection.
- Transparency, explanation, empowerment.

**What you'll take home**
You'll leave with sharper mental models for thinking about fairness in technical systems, frameworks borrowed from Design Justice and disability rights movements, and tools for the next tricky conversation at work about what fairness actually means. There are no easy answers here, but there are better questions.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/S7KYEE/>

## 81. [PyTorch and CPU-GPU Synchronizations](https://pretalx.com/pyconde-pydata-2026/talk/RNT9FV/)

**Speakers**: [Tomas Ruiz](https://pretalx.com/pyconde-pydata-2026/speaker/UX7XPD/)

**When and where**: Wednesday, 2026-04-15, 14:20–14:50, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

CPU–GPU synchronizations are a subtle performance killer in PyTorch: they block the host, prevent the CPU from running ahead, and create GPU idle gaps. This talk explains what host-device synchronization is, how it’s triggered by subtle code patterns (dynamic-shapes), and how to diagnose it with NVIDIA Nsight Systems by correlating utilization gaps with long CUDA API calls. We’ll end with practical mitigation patterns, including unit testing for syncs via `torch.cuda.set_sync_debug_mode()` and when a small Triton kernel can help avoid syncs and fuse ops.

**Description** (verbatim):

PyTorch gets its speed from asynchronous execution: the CPU launches operations quickly while the GPU executes them later. CPU–GPU (host-device) synchronizations break this pipeline by blocking the host until the GPU reaches a specific point. The result is often counterintuitive: even if kernels are fast, the GPU develops idle gaps, throughput drops, and latency rises because the CPU can no longer run ahead and keep the GPU fed with work.

This talk builds intuition with a minimal loop that alternates a slow GPU operation with a quick “bookkeeping” operation, a pattern that resembles many inference and training pipelines. By adding a seemingly harmless action—such as printing a CUDA tensor—we’ll see how easily a synchronization can be introduced and why the slowdown can be disproportionate to what the code appears to do.

We’ll then walk through a practical profiling workflow in NVIDIA Nsight Systems. The key technique is to correlate GPU utilization gaps with long CPU-side CUDA API calls (for example cudaStreamSynchronize) that indicate the host thread is waiting. Comparing a healthy trace to a sync-heavy trace makes it clear where the pipeline stalls and which code region triggers it.

Beyond the usual suspects (.item(), printing device tensors, explicit device transfers), the talk highlights dynamic shapes as a common synchronization trigger. Patterns like boolean indexing with a GPU mask or slicing with a GPU-resident index can force PyTorch to fetch information back to the CPU to determine output sizes and allocations. We’ll discuss how to recognize these cases and how to restructure code toward shape-stable alternatives when possible.

Finally, we’ll cover how to prevent regressions. Instead of relying on profiling alone, we’ll use PyTorch’s experimental API `torch.cuda.set_sync_debug_mode()` in unit tests to surface synchronizations early, while keeping production code unchanged. We’ll close with guidance on when a small Triton kernel is worth considering to avoid sync-inducing patterns and to fuse multiple small ops into a single, fully asynchronous kernel.

**Links**:

- [Blog Post](https://tomasruizt.github.io/posts/08_cpu_gpu_synchronization/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/RNT9FV/>

## 82. [Beyond Kafka and S3: Python Data Pipelines with HTTP-Native Bytestreams](https://pretalx.com/pyconde-pydata-2026/talk/HP7DLX/)

**Speakers**: [Johannes Dröge](https://pretalx.com/pyconde-pydata-2026/speaker/ZZWUGV/)

**When and where**: Wednesday, 2026-04-15, 15:00–15:45, room Palladium [2nd Floor]

**Type**: Talk (long) — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Real-time bytestreams between systems in different organizations or secured environments, whether for batch dataset delivery or continuous streaming, are surprisingly hard. Traditional solutions fall short: message brokers like Kafka use discrete messages, file storage like S3 works for batch exchange but lacks streaming and coordination, while HTTP client-server approaches require one side to host and expose server endpoints, introducing security and operational overhead.

This talk introduces the ZebraStream Protocol: an open, HTTP-based bytestream protocol with coordination mechanisms that let you stream data — Parquet files, compressed archives, encrypted content—directly between decoupled systems using Python's file-like interface. No message framing, no server hosting, no exposed endpoints.

We'll explore the design of a bytestream protocol for data sharing and integration that crosses the file-stream boundary, enabling seamless integration with pandas and any Python library expecting file-like objects, supporting use cases from ETL pipelines to IoT data delivery, cross-org collaboration to home network automation.

**Description** (verbatim):

**TL;DR** _Streaming data between systems — whether across organizations, from secured environments, isolated networks, or even home setups — remains a common challenge in modern data engineering and data sharing workflows. This talk introduces the ZebraStream Protocol: an open, HTTP-based bytestream protocol designed specifically for decoupled systems, where both sides act as clients — no server hosting, no exposed endpoints._

### Talk Outline (45 minutes)

**Opening — The Shape of the Solution (3 min)**

The talk opens with a UNIX pipe: opaque, minimal, composable. Any program that reads from stdin and writes to stdout already fits — no negotiation, no shared infrastructure. Two real-world use cases introduce the challenge: a supplier pushing inventory to a buyer's pipeline, and a hospital sharing trial data with a contract research organization. The question the talk sets out to answer: can the pipe's properties work across organizational boundaries, over HTTP?

**Part 1 — Why the Problem Is Hard (8 min)**

Sharing data across organizational boundaries requires sharing infrastructure, trust, protocol, and format. Every crossing is a negotiation, and the cost is ongoing. The coupling spectrum — from function calls to cross-org transfers — sets up a precise vocabulary for what "strong decoupling" actually means. A well-composed protocol owns only transport and access, leaving structure and format to the caller.

**Part 2 — What Already Exists (4 min)**

Kafka, S3, and HTTP APIs each fail at strong decoupling in a specific and diagnosable way. Kafka requires the other side to adopt a platform. S3 is a storage abstraction, not a transfer abstraction — no presence signal, no cleanup. An HTTP API permanently makes one side a server. Reading each failure as a requirement, a named pipe already satisfies all three — within a machine. The open question: can this work over HTTP?

**Part 3 — The ZebraStream Protocol (5 min)**

The basic protocol and its Data API are revealed: a bytestream channel over HTTP where both sides are clients. A stateless relay sits in the middle — exclusive channel, HTTPS outbound only, separate read and write tokens. The difference between a message and a bytestream is made precise: no opinions on size, structure, or format. A raw HTTP example using `requests` shows the Data API in full — producer streams a generator over PUT, consumer reads a streaming GET response.

**Part 4 — Presence and Coordination (5 min)**

HTTP connects immediately, without knowing whether the other side is there. Two failure modes show the consequence: a consumer holding a silent GET with no way to tell if the producer is slow or absent; a producer writing into a PUT with no signal that nobody is reading. The Connect API resolves this with an explicit waiting room — the first client waits, the second triggers the transfer. Push and pull are runtime choices, not architectural ones: whoever arrives first waits.

**Demo 1 — Push and Pull** (3 min): the supplier/buyer inventory use case, both modes shown live; the rendezvous is the point.

**Part 5 — Python Integration (8 min)**

`zebrastream-io` implements `io.IOBase`. Any library that accepts a file — pandas, loguru, tarfile, csv, pickle — works immediately, with no changes to existing code. Because there is no intermediate file, the producer's write and the consumer's read are the same operation: an early disconnect on either side raises immediately. No silent failures, no orphaned files, no copy cascades.

**Demo 2 — Log Streaming** (5 min, notebook): two lines added to a loguru producer; the consumer is the ZebraStream CLI. The application logs normally — transport is invisible.

**Part 6 — Design Decisions and Security (5 min)**

Three deliberate choices — HTTP, bytestream, stateless relay — are named alongside what each costs. The security model follows from the relay design: TLS and scoped tokens require trusting the relay; end-to-end encryption does not. The relay moves ciphertext and has no key. Per-chunk encryption keeps live streams encrypted without buffering the full payload. The hospital/CRO use case from the opening gets its resolution: pull mode, on-demand EHR query, one extra argument — the relay operator sees nothing.

**Closing — Open Protocol (1 min)**

The protocol specification is open and community-focused. The Python client is open source. ZebraStream.io is the managed relay and protocol sponsor. The talk closes where it opened: opaque, minimal, composable — across organizational boundaries.

**Q&A (5–10 min)**

**Links**:

- [GitHub Project](https://github.com/zebrastream/)
- [zebrastream-io Python Package](https://pypi.org/project/zebrastream-io/)
- [Cloud Relay](https://www.zebrastream.io/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/HP7DLX/>

## 83. [Hierarchical Models in MMM: Can Structure beat data size?](https://pretalx.com/pyconde-pydata-2026/talk/EL7X8C/)

**Speakers**: [Mohamed Amine Jebari](https://pretalx.com/pyconde-pydata-2026/speaker/RJBMTK/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

In every marketing project, teams strive to find more data, a longer timeframe, and more detailed splits, just to fix noisy channel attribution.

But what if structure played a bigger role than size and volume?
In this talk, we try to prove this. Using a simple toolkit like Arviz and PyMC, we show you a simple hierarchical mix model, and how, by applying partial pooling, we can stabilize important KPIS like ROAS estimates across sparse channels- without the need for more data.
We will go through the code, transformation, and the real-life practices that allow us to get as close to the truth, to be able to have a meaningful impact in the marketing world.
The approach will be centered around marketing mix models, different transformations, and how useful it will be for the business.

**Description** (verbatim):

## What we are going to show

- Country-specific marketing Data that is, unfortunately, never good.
- Function and Python transform like Adstock and saturation (with the tests so that you can see it in action).
- Differentiation between pooled, unpooled, and partial pooling.
- Meaningful diagnostics.
- Wins and losses of hierarchical modeling.

## Why this is interesting and relevant

How do you model marketing effectiveness when you only have 12 months of data per country, some channels are interrupted for weeks, and your manager wants reliable ROAS estimates yesterday?
Most teams think: "We need more data." But getting more data takes time, costs money, and sometimes isn't even possible (or the quality is bad).

What if you could get better estimates by changing how you model the problem?
This is where hierarchical modeling and partial pooling come in. Instead of treating each market as separate (unpooled) or pretending they're all identical (pooled), we let markets share information through partial pooling. Countries with thin data borrow strength from the group, while markets with strong signals pull away from the mean. You get stability where you need it and flexibility where the data supports it. We show this end-to-end in Python: from building testable transform functions (Adstock, saturation curves, lag effects) to assembling three different model architectures in PyMC, to evaluating which one gives you calibrated intervals and stable ROAS estimates. You'll see the good, the bad, and the ugly.

## Main challenges

- Making transforms reusable and testable_ Marketing transformations like adstock and saturation are usually hidden in modeling code. It is generally very difficult to imagine how they look, how they change the data. We pull them out as pure Python functions with clear signatures, unit tests (pytest), and property-based checks (hypothesis). This makes them composable, debuggable, and easy to understand and even improve.
- Building fair model comparisons: We construct pooled, unpooled, and hierarchical models with identical priors where appropriate so the comparison isolates the effect of structure, not prior choice. We walk through the PyMC code, show how partial pooling works mathematically, and run short MCMC chains that still demonstrate the key differences.
  We go beyond "we reached 90% R2" to actual decision metrics:
  - Posterior predictive checks: Does the model generate realistic data?
  - ROAS stability: how much do channel estimates vary across groups?

We use ArviZ throughout to visualize traces, compare models, and compute these metrics. You'll see exactly when hierarchical structure pays off and when it doesn't.

## Practical lessons and the repo

**We share what we learned building this:**

- Data checks and control using Pydantic, so you catch errors before MCMC runs for hours
- Test your transforms independently: Yes, for unit tests!
- Use synthetic data with known ground truth to validate the whole pipeline
- Calibration metrics matter more than posterior predictive RMSE alone

**The repo will include:**

- Typed transform functions (Adstock, saturation, lag) with unit tests
- Three PyMC models with matching priors
- ArviZ evaluation scripts (calibration, PPC)
- A Typer CLI to run everything on a predefined CSV

**When hierarchical lose (and what to do about it):**
Partial pooling isn't magic. If your groups are genuinely wildly different and you have almost no data per group, hierarchical models can still produce overconfident nonsense. We show a scenario where this happens and discuss alternatives: stronger priors, splitting the hierarchy, or just admitting you don't have enough signal.
The takeaway: structure beats volume in the right conditions. We help you recognize those conditions and build models that respect them.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/EL7X8C/>

## 84. [Metashade: Compilerless Immediate-Mode Shader Generation in Pure Python](https://pretalx.com/pyconde-pydata-2026/talk/B8GQ9Z/)

**Speakers**: [Pavlo Penenko](https://pretalx.com/pyconde-pydata-2026/speaker/KFMB83/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Discover how to build a GPU shader generator in pure Python, without having to write a compiler.

We start by discussing how Pythonic embedded domain-specific languages (EDSLs) can help address the common challenges of shader programming.

We then examine the architectural decisions shared by popular frameworks like Warp and Taichi and outline their limitations. In particular, their reliance on introspection means supporting only a subset of Python - a language within a language - while compiler-like backends necessitate complex implementations in languages like C++.

The talk introduces an alternative architecture making it possible to overcome these limitations. Instead of introspection, we capture the program's logic by tracing execution with proxy objects at Python runtime, similar to JAX and PyTorch. Instead of building an IR, we emit target code eagerly, line-by-line, similar to how PyTorch Eager Mode launches computations. And because we don't implement a compiler, the implementation remains 100% Python.

Attendees will leave with a toolbox of Python metaprogramming patterns empowering them to write a code generator in Python without having to implement a compiler.

**Description** (verbatim):

The area of shader programming offers many tough problems to solve. The range of target platforms is vast: from CPU path-tracers to mobile GPUs - served by a zoo of incompatible languages: from GLSL to HLSL, from OSL to WGSL.

Common challenges include portability, managing specializations, and a lack of abstraction mechanisms. The solutions for these include the archaic C Preprocessor, templates/generics, visual graph frameworks, transpilers and, finally, embedded domain-specific languages (EDSLs).

Python is an ideal host for Embedded Domain-Specific Languages (EDSLs). Warp, Taichi, Numba, and Triton evolved to target GPU compute. All of them share common architectural decisions. They capture the program's logic by inspecting the Python source code, generate an internal representation and compile that IR to the target format.

The above approach comes with significant disadvantages. Only a subset of Python is supported, debugging with standard tools is impossible, integration with external Python code is limited, metaprogramming requires special syntax, and heavy compiler infrastructure needs to be implemented in a language like C++.

This talk proposes an alternative architecture. Instead of introspection, we capture the program's logic by tracing execution with proxy objects at Python runtime, similar to JAX and PyTorch. Instead of building an IR, we emit target code eagerly, line-by-line, similar to how PyTorch Eager Mode launches computations. And because we don't implement a compiler, the implementation remains 100% Python.

We discuss in detail how core elements of Python syntax can be overloaded to implement such an architecture:

- Operator overloading to capture expressions.
- Context managers to simulate C-like scopes.
- `__setattr__`/`__getattr__` to capture variable names.
- Function decorators to capture function signatures.

Attendees will leave with a toolbox of Python mataprogramming patterns empowering them to write a code generator in Python without having to implement a compiler.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/B8GQ9Z/>

## 85. [AI Is Changing the Game: Building Modular, AI-Ready Platforms on Top of Legacy Systems](https://pretalx.com/pyconde-pydata-2026/talk/HRFYVS/)

**Speakers**: [Werner Gothein](https://pretalx.com/pyconde-pydata-2026/speaker/FPMRS9/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI is fundamentally changing how quickly business and domain teams can create new logic, validations, and insights. In regulated environments, this new speed collides head-on with legacy systems, monolithic architectures and IT landscapes that were never designed for continuous AI-driven change.

This talk presents an open, Python-based platform architecture that turns AI-driven pressure into an architectural advantage. Instead of embedding AI into existing monoliths, the platform introduces a central control layer that orchestrates independent, stateless apps—ranging from classical algorithms to AI agents—without binding them to specific infrastructure or legacy constraints.

The control layer, implemented using Python and optionally Django, provides workflow orchestration, security, tenant management, and self-service registration of new components. This allows domain teams to deploy AI agents—such as anomaly detection for regulatory reporting—within days, while IT retains governance, auditability, and operational stability.

The talk argues that AI will amplify architectural weaknesses—and shows why modular orchestration layers will become essential for AI-ready systems far beyond finance.

**Description** (verbatim):

# AI Is Changing the Game: Building Modular, AI-Ready Platforms on Top of Legacy Systems

AI is no longer a future topic—it is actively reshaping expectations inside organizations. Domain and business teams can now prototype new rules, validations, and analytical logic themselves, often within days. While this accelerates innovation, it puts enormous pressure on existing IT architectures, especially in environments dominated by legacy systems and monolithic platforms.

This talk explores how software architecture must evolve to absorb this pressure instead of breaking under it.

Rather than embedding AI capabilities directly into legacy systems, the presented approach introduces a modular, AI-ready platform built around independent, stateless apps orchestrated by a central control layer. These apps can represent classical reporting logic, risk calculations, or AI agents, all treated as first-class architectural components.

The talk is highly relevant for the **PyCon track “Programming, Software Engineering & Testing”**, because it demonstrates how to design, orchestrate, and integrate AI-driven workflows in complex Python-based platforms. The central control layer, implemented using Python and optionally Django, provides workflow orchestration, security, tenant management, and self-service registration of new components. This allows domain teams to deploy AI agents or agents written with the help of AI within days, while IT retains governance, auditability, and operational stability.

By showing how AI-driven pressure can be turned into an architectural advantage, the talk provides patterns and practical lessons that apply far beyond finance, making it relevant for any domain dealing with legacy systems, modular design, and AI integration.

## Architectural Concepts Covered

The talk introduces the key architectural principles behind the platform:

- **Independent, stateless apps** that declare their data needs and outputs but remain unaware of infrastructure, environments, or other apps
- **Strict separation of concerns** between domain logic, orchestration, persistence, and presentation
- **Technology-indifferent design**, allowing apps to run on different databases, reporting tools, or compute backends
- **Parallel and distributed execution** as a default, not an optimization

This architecture allows legacy systems to coexist with modern components instead of blocking innovation.

## The Control Layer as an Enabler for AI

A central part of the talk is the control layer that orchestrates all components. Implemented using Python and optionally Django, this layer is responsible for:

- workflow orchestration and dependency management
- authentication, authorization, and tenant isolation
- self-service registration of apps and AI agents
- resource allocation, monitoring, and auditability

Django is not used as a traditional CRUD backend, but as governance infrastructure: providing APIs, admin and self-service portals, and security mechanisms that allow fast innovation without losing control.

## Example: Integrating an AI Agent into a Regulated Platform

A concrete example demonstrates the architecture in action: integrating an AI agent for e.g. anomaly detection in regulatory reporting.

The example walks through:

- developing the agent as an independent, containerized app
- registering it via standardized APIs
- declaring required data and produced results
- orchestrating it within existing workflows
- testing, monitoring, and scaling it without touching legacy systems

This shows how new AI capabilities can be deployed within days while maintaining stability and compliance.

## Why This Matters Beyond Finance

While the example comes from regulatory reporting, the patterns discussed apply to many domains facing similar challenges: data-heavy systems, long-lived platforms, and increasing pressure to integrate AI safely.

The talk concludes with lessons learned and architectural patterns that help future-proof systems as AI continues to raise the bar for flexibility, speed, and modularity.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/HRFYVS/>

## 86. [Getting Career Clarity in Uncertain Times](https://pretalx.com/pyconde-pydata-2026/talk/DDVW3W/)

**Speakers**: [Tereza Iofciu](https://pretalx.com/pyconde-pydata-2026/speaker/NMACLQ/)

**When and where**: Wednesday, 2026-04-15, 10:15–11:45, room Ferrum [2nd Floor]

**Type**: Tutorial — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Feeling unsure about your next step in your career?

The data & AI field is evolving faster than ever. New tools, new roles, and constant “next big things” can make even experienced professionals feel unsure about where they are heading, and how to make intentional career decisions in the middle of all this change.

You might be doing well, feeling comfortable. Interesting work, steady progress, recognition.
And still, there’s that question in the background: Where is this actually going?

This interactive workshop helps you explore different future paths, understand trade-offs, and gain clarity about what kind of work and influence you want next.

**Description** (verbatim):

The data & AI field is evolving faster than ever. New tools, new roles, and constant “next big things” can make even experienced professionals feel unsure about where they are heading, and how to make intentional career decisions in the middle of all this change.

You might be doing well, feeling comfortable. Interesting work, steady progress, recognition.
And still, there’s that question in the background: Where is this actually going?

A lot of career advice in tech assumes there is a clear path to follow. In reality, most data & AI careers don’t work that way. Roles shift, organisations change, and what used to feel like a logical next step often isn’t anymore.

In this workshop, we’ll slow things down and focus on direction rather than decisions. The goal is not to figure out “the next job”, but to get clearer on the kind of work you want to do.

This is a practical, hands-on session.

We’ll use exercises such as odyssey planning to explore a few possible future paths you could take from here.

You’ll work through:
• Different ways your career could evolve
• The trade-offs each direction comes with
• What feels worth exploring further, and what doesn’t

And, just as importantly, how you feel about these plausible futures.

You’ll leave with a clearer sense of what matters to you now, and a stronger sense of direction

By the end of the session, you will:
• Have more clarity about the kind of work and influence you want going forward
• See more than one possible future, instead of feeling stuck with a single “right” option
• Feel more confident navigating uncertainty without rushing into decisions

Who this session is for
• Data & AI professionals with a few years of experience or more
• People who feel “in between” stages, roles, or directions
• Individual contributors and leaders alike
• Anyone who wants more intentionality in their work

Source: <https://pretalx.com/pyconde-pydata-2026/talk/DDVW3W/>

## 87. [Accelerate FastAPI Development with OpenAPI Generator](https://pretalx.com/pyconde-pydata-2026/talk/N8QVT8/)

**Speakers**: [Dr. Evelyne Groen](https://pretalx.com/pyconde-pydata-2026/speaker/NUFKS8/), [Kateryna Budzyak](https://pretalx.com/pyconde-pydata-2026/speaker/93VSJ9/)

**When and where**: Wednesday, 2026-04-15, 14:20–15:50, room Ferrum [2nd Floor]

**Type**: Tutorial — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Develop FastAPI applications faster with the contract-first approach using the OpenAPI Generator, no GenAI required.

**To attend this workshop, please install the openapi generator.**
For details, please visit the README.md of https://gitlab.com/Eeffee/pycon26

Machine learning models are often deployed as APIs, but the "agreement" between the consumer and the service is often fragile. How does the consuming app know if a parameter is optional or required? When the code diverges from the documentation, integration breaks.
In this tutorial you will learn to define an API contract using OpenAPI specification. We will use the OpenAPI Generator to automatically generate API endpoints and strictly typed Pydantic data models. Following this approach for all applications supports standardization, consistency, and maintainability across all projects.

The session will cover three key areas:
**Design**: We will define an OpenAPI specification as our single source of truth for the API and end consumer.
**Generate**: We will use the OpenAPI Generator to create a FastAPI skeleton and show possibilities for customization to fit specific project needs.
**Implement**: We will connect our generated app to a ML model where we will create Mystic Creatures for Real Life Problems

**Description** (verbatim):

Machine learning models are often deployed as APIs, where we have an endpoint that generates predictions given some input. For example, we can send a POST request specifying a color, a length, and a number of legs, and the endpoint predicts the best fitting animal. The description of the endpoint, the schema of the request, and the response acts as a form agreement between the consumer and the service. In practice, the restrictions on the API are not well defined. How does the consuming app know if a parameter is optional or required?
In this tutorial you will learn to define an API contract as an OpenAPI specification (OAS). OAS is a standardized description of the API endpoints and data models. We will demonstrate how to use the OpenAPI Generator to automatically generate the API endpoints and strictly typed Pydantic data models, by only designing the OAS in YAML format, without GenAI. OpenAPI Generator utilizes mustache templates to translate the specification into actual code. We will demonstrate use cases for customizing the template for specific needs of the resulting API stubs.  
By generating code from the contract, you ensure that the deployed application always reflects the agreed-upon specification. It automates the writing of repetitive code, such as Pydantic models and endpoint definitions, allowing developers to focus on the implementation logic. It enforces standard patterns and structures, ensuring consistency and maintainability across different projects.

Expect fun mystic creatures after deploying the resulting API in your local environment.

#### Target Audience

Engineers and data scientists looking to standardize their FastAPI development workflow. We expect you to have basic knowledge in Python, virtualenv, Pydantic data models and FastAPI.

**To attend this workshop, please install the openapi generator v7.20.**
For details, please visit the README.md of https://gitlab.com/Eeffee/pycon26

#### Technical Setup

- _Operating system:_ We recommend using Unix OS (Mac or Linux)
- _Python:_ Version 3.10+
- _OpenAPI Generator:_ Version 7.20
  - Installation Guide: https://openapi-generator.tech/docs/installation/

For details, please visit the README.md of https://gitlab.com/Eeffee/pycon26

#### Outline

1. Introduction (10 min)

- The philosophy of Contract-First development
- Overview of the OpenAPI specification and Pydantic data models
- Introduction to the OpenAPI generator tool

2. Design (20 min)

- Introduction to the unicorn service logic (Input: Real Life Problems, Output: Mystic Creatures)
- Definition of the openapi specification, focusing on the Request and Response schemas

3. Generate (30 min)

- Running the standard vanilla OpenAPI generator
- Introduction to mustache templates
- Customization of the default mustache to inject our specific dependencies

4. Implementing (15 min)

- We will connect the generated API stubs to a predict() function that calls our unicorn generation service.

5. Demo & QA (15m)

- Running the server via u**v**icorn and testing our u**n**icorn service endpoint using the Swagger UI.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/N8QVT8/>

## 88. [Practical Refactoring with Syntax Trees](https://pretalx.com/pyconde-pydata-2026/talk/N98BQT/)

**Speakers**: [Laurent Direr](https://pretalx.com/pyconde-pydata-2026/speaker/WRXLGJ/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Ferrum [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The Python Abstract Syntax Tree powers tools like pytest, linters, and automatic refactoring.
In this talk, we'll approach syntax trees from first principles and see how Python code can be treated as structured data.

We'll then explore how syntax trees can be used to automate refactoring across large codebases.
Using a real-world example and the libCST library, we'll build a small refactoring tool and share practical advice for writing and applying automated refactorings.

You'll leave with a clear mental model of syntax trees and a solid starting point for writing your own refactoring tools.

**Description** (verbatim):

Modern Python tooling relies heavily on syntax trees. In this talk, we take a practical look at Python's Abstract Syntax Tree (AST) and how Python code can be treated as structured data rather than plain text.

We'll start from first principles: how Python source code is parsed, what an AST represents, and how to reason about code as a tree. This builds a clear mental model that makes syntax-tree-based tooling easier to understand and work with.

From there, we'll explore how syntax trees enable automated refactoring across large codebases using scripts to rewrite code (sometimes called codemods).
Using a realistic refactoring scenario, we'll implement a small refactoring tool using libCST.

The talk also shares practical tips from writing codemods. This includes how to use test-driven development when writing refactoring tools, where AI can help in refactoring tasks, and strategies for dealing with formatting.

Attendees will leave with a solid understanding of how syntax trees work in Python and a concrete starting point for writing their own automated refactoring tools.

Outline:

Minutes 0-5: Primer on Python syntax trees and the AST mental model
Minutes 5-12: From syntax trees to codemods and automated refactoring
Minutes 12-22: Implementing a refactoring codemod with libCST
Minutes 22-27: Test-driven codemods, formatting strategies, and AI assistance
Minutes 27-30: Conclusion

EDIT:

- [Slides](https://ldirer.github.io/talk_pycon_de_2026_libcst/)
- [Code for example](https://github.com/ldirer/codemod-rename-pytest-fixtures)

**Links**:

- [Code for example](https://github.com/ldirer/codemod-rename-pytest-fixtures)
- [Slides](https://ldirer.github.io/talk_pycon_de_2026_libcst/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/N98BQT/>

## 89. [Simplifying RAG Document Pipelines with Multimodal Embeddings](https://pretalx.com/pyconde-pydata-2026/talk/R7TT3E/)

**Speakers**: [Arne Grobrügge](https://pretalx.com/pyconde-pydata-2026/speaker/LDZFAV/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Ferrum [2nd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

In RAG-based systems, the main challenge is often not tuning the LLM itself, but making documents available in a form that can be retrieved reliably. In enterprise settings, the dominant input format is still PDF, ranging from text-heavy reports to slide decks, scanned documents, and visually dense presentations.

Traditional document processing pipelines rely on OCR and layout analysis to extract text, followed by chunking and embedding. While this works well for text-heavy documents, much of the original structure is often lost—especially for presentations, multi-column layouts, and visually driven content. Images, charts, and diagrams typically require separate processing, increasing pipeline complexity and fragility.

Recent multi-modal embedding models enable a different approach: embedding entire PDF pages directly as images. This preserves layout, visual hierarchy, and embedded graphics in a single representation and significantly simplifies document ingestion.

This talk compares classical OCR-based document processing pipelines with multi-modal page embeddings, drawing on benchmarks conducted on real-world enterprise documents across different models. It highlights where this approach performs well, where its limitations lie, and how to design practical, cost-aware retrieval systems in Python.

**Description** (verbatim):

This talk provides an overview of how document processing for RAG systems can be simplified using multimodal embeddings, grounded in benchmarks on real-world enterprise documents.

What the talk covers

1. **Motivation: Why RAG Is Still Hard**  
   Why PDFs remain challenging in enterprise RAG systems, and where current document processing approaches break down—especially for presentations and visually structured documents.

2. **The Classical Approach: PDF → Text → Chunks**  
   An overview of traditional OCR- and layout-based pipelines, including their strengths, typical failure modes, and why they tend to grow into complex and fragile systems over time.

3. **A New Paradigm: Multimodal Page Embeddings**  
   How embedding entire PDF pages as images changes the ingestion model, what information is preserved compared to text-only approaches, and what this means for retrieval quality and system simplicity.

4. **Benchmark Setup**  
   How the benchmark comparing classical pipelines and multimodal page embeddings was designed, using anonymized, real-world enterprise documents across multiple document types. Different models and vendors are referenced only as examples, not as the focus.

5. **Results and Key Findings**  
   Where multimodal page embeddings outperform text-based pipelines, where they do not, and how hybrid approaches can emerge as a practical solution.

6. **Production Best Practices**  
   Practical guidance for deploying these approaches in real systems, including index design, quality monitoring, cost control, and how to integrate multimodal retrieval cleanly into Python-based RAG architectures.

Attendees will leave with a clear understanding of when multimodal embeddings are a strong replacement for classical PDF pipelines, and how to reason about the trade-offs involved.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/R7TT3E/>

## 90. [The Day the Agent Started Lying (Politely)](https://pretalx.com/pyconde-pydata-2026/talk/P8Y9TD/)

**Speakers**: [Asya Melnik](https://pretalx.com/pyconde-pydata-2026/speaker/XG9398/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Ferrum [2nd Floor]

**Type**: Talk — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

You deploy an agent to automatically route incoming customer support tickets. At first, it is a clear win: response times improve, customers are happier, and support teams finally get some rest.

Then time passes.

Nothing crashes. Dashboards stay green. No alerts fire. Yet the agent’s decisions slowly degrade first slightly, then inconsistently, and eventually becoming confidently wrong.

This is data drift.

LLM-based agents in production operate in constantly changing environments. Products launch, outages happen, terminology evolves, and priorities shift. Unlike traditional ML models, LLMs can produce plausible, well-phrased outputs even when they are incorrect, making these failures difficult to detect.

In this talk, we focus on practical techniques for continuously evaluating and monitoring LLM-based agents after deployment. Using a support-ticket routing agent as an example, we examine drift signals such as increasing classification uncertainty, spikes in fallback categories, shifts in embedding distributions, and growing disagreement with historical or human decisions.

The emphasis is not on training or prompt tuning, but on operating agents safely over time: detecting silent failures early and knowing when intervention, retraining, or retirement is required before users notice.

**Description** (verbatim):

In this talk, we will walk through a concrete production-style example of an LLM-based agent that automatically classifies and routes incoming customer support tickets. The agent takes raw ticket text as input, predicts a priority label, and routes the ticket to the appropriate support queue. A human override is possible but expected to be rare.

At deployment time, the system performs well. Classification confidence is high, fallback usage is low, and manual corrections are infrequent. Over time, however, the environment changes: new products are launched, outages introduce new failure modes, terminology evolves, and internal definitions of ticket priorities shift. Nothing crashes, latency remains stable, and traditional service-level metrics stay green; yet the agent’s decisions slowly degrade.

This talk focuses on how to observe, measure, and act on that degradation.

Using recorded ticket data and a demo, I will show how to instrument an LLM-based agent with continuous evaluation signals, including:

- Tracking class-probability entropy over time to detect increasing uncertainty
- Monitoring the rate of “unknown” or fallback predictions as an early warning signal
- Measuring embedding distribution drift between historical and recent tickets
- Quantifying disagreement between current agent decisions and historical routing outcomes or human corrections

I will demonstrate how these signals can be computed in rolling time windows, visualised on simple dashboards, and connected to alert thresholds. Rather than relying on a single accuracy number, the talk shows how multiple weak signals together reveal silent failure modes that would otherwise go unnoticed.

The focus is deliberately not on training new models or tuning prompts. Instead, we concentrate on operating LLM-based agents safely after deployment. You will see how to build a continuous evaluation pipeline, how to distinguish normal variation from meaningful drift, and how to decide when intervention is required whether that means retraining, prompt changes, label redefinition, or temporary rollback to human routing.

By the end of the talk, attendees will have a clear, practical blueprint for monitoring LLM-based agents in production and for detecting quiet, confident failure modes before they affect users or business operations.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/P8Y9TD/>

## 91. [Process, Analyze, and Transform Python Code with ASTs](https://pretalx.com/pyconde-pydata-2026/talk/VWCZXS/)

**Speakers**: [Stefanie Molin](https://pretalx.com/pyconde-pydata-2026/speaker/9WJJPL/)

**When and where**: Wednesday, 2026-04-15, 10:15–11:45, room Dynamicum [Ground Floor]

**Type**: Tutorial — **Track**: PyCon: Python Language & Ecosystem — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

You’ve likely used a tool like `black`, `flake8`, or `ruff` to lint or format your code, or a tool like `sphinx` to document it, but you probably do not know how they accomplish their tasks. These tools and many more use **Abstract Syntax Trees (ASTs)** to analyze and extract information from Python code. An AST is a representation of your code's structure that enables you to access and manipulate its different components, which is what makes it possible to automate tasks like code migrations, linting, and docstring extraction.

In this workshop, you’ll learn how to use the Python standard library’s `ast` module to parse and analyze code. Using just the standard library, we will implement a couple of common checks from scratch, which will give you an idea of how these tools work and help you build the skills and confidence to use ASTs in your own projects.

**Description** (verbatim):

This tutorial will be a roughly 50/50 split of lecture and exercises. Attendees will get hands-on experience working with ASTs in Python, using only the standard library. By recreating common code-quality checks from scratch, attendees will both learn how common tools work under the hood and how to work with the AST in an easy-to-understand fashion.

Topics covered:

- Introduction to the term and concept of Abstract Syntax Trees (ASTs)
- Some of the ways ASTs are used by Python itself and by popular tools
- Parsing code into an AST and inspecting it
- Walking the tree: `ast.iter_fields()`, `ast.iter_child_nodes()`, `ast.walk()`
- Modifying the code before running it
- Converting an AST into source code again with `ast.unparse()` and its caveats
- Finding missing docstrings
- `ast.NodeVisitor` and `ast.NodeTransformer`
- `generic_visit()` method — what it does and why we need it using animation
- 4 exercise breaks spread throughout accounting for ~45 minutes

**Links**:

- [Setup instructions](https://github.com/stefmolin/ast-workshop?tab=readme-ov-file#setup-instructions)
- [Slides](https://stefaniemolin.com/ast-workshop/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/VWCZXS/>

## 92. [Array-Oriented Programming in Python: Libraries, Techniques, and Trade-offs](https://pretalx.com/pyconde-pydata-2026/talk/AGYLTV/)

**Speakers**: [Iason Krommydas](https://pretalx.com/pyconde-pydata-2026/speaker/3E3SVE/)

**When and where**: Wednesday, 2026-04-15, 14:20–15:50, room Dynamicum [Ground Floor]

**Type**: Tutorial — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python has become the dominant language for scientific computing and data science, largely due to powerful array libraries that enable high-performance numerical computation. This tutorial introduces array-oriented programming as a paradigm and surveys the modern Python array ecosystem.

We'll explore when and how to use different array libraries: NumPy for general-purpose array operations, JAX for automatic differentiation, just-in-time compilation of array-oriented code, and GPU acceleration, Numba for just-in-time compilation of imperative code, and Awkward Array for nested and irregular data structures. Through live demos, we'll show how to think in arrays, discuss the limitations of array-oriented programming, and demonstrate how JIT compilation addresses these challenges.

Whether you're analyzing data, building machine learning models, or doing scientific simulations, understanding the strengths and trade-offs of each library will help you choose the right tool for your problem.

**Description** (verbatim):

## Material

https://github.com/ikrommyd/2026-04-15-pyconde-and-pydata-2026-tutorial-array-oriented-programming
What you need: Your laptop, and the repository cloned and the environment set up as explained in the README. Alternatively, an internet connection during the tutorial to set up the environment live or follow along on MyBinder.
The setup is needed to do the problems/puzzles which are part of the tutorial.

## Overview

Python's dominance in scientific computing and data science stems from its powerful array libraries that enable high-performance numerical computation. This 90-minute tutorial introduces array-oriented programming as a paradigm and surveys the modern Python array ecosystem, helping you understand which tools to use and when.

## What is Array-Oriented Programming?

Array-oriented programming is a paradigm that separates problems into lightweight Python bookkeeping and heavy numerical computation handled by vectorized operations in fast, precompiled libraries. We'll demonstrate how this approach combines Python's ease of use with near-compiled-language performance.

Through live examples, you'll see how array operations can be orders of magnitude faster than explicit loops. This mindset shift—thinking about operations on entire arrays rather than individual elements—is fundamental to effective scientific Python programming.

## The Array Library Landscape

We'll survey the modern Python array ecosystem and when to use each tool:

- **NumPy**: The foundation for general-purpose array operations
- **Numba & JAX**: JIT compilation approaches—when and why to use each
- **Awkward Array**: Handling nested and ragged data structures
- **Large dataset tools**: Brief overview of Dask, Xarray, Zarr, and Blosc2 for distributed computing, labeled arrays, and compression

We'll demonstrate the strengths and limitations of each through live coding examples, showing trade-offs between different approaches.

## Understanding Limitations and Trade-offs

A critical part of choosing the right tool is understanding when array-oriented programming has limitations. We'll discuss challenges like intermediate array overhead and algorithms that don't naturally vectorize, and show how different libraries address these problems.

## What You'll Learn

By the end of this tutorial, you will:

1. **Understand array-oriented programming** as a paradigm and how it differs from imperative programming
2. **Know which library to choose** for different problems: NumPy vs. Numba vs. JAX vs. specialized tools
3. **Recognize when array-oriented approaches have limitations** and how to address them with JIT compilation
4. **Handle non-rectilinear data** using libraries like Awkward Array
5. **Work with large datasets** using chunking, compression, and labeled arrays
6. **Write more performant Python code** by applying array-oriented thinking to your own problems

## Prerequisites

Familiarity with Python (loops, functions, if statements) and basic NumPy exposure (what an array is and how to use it). No deep expertise required.

## Target Audience

Data scientists, researchers, and engineers who want to write more efficient Python code, understand the modern array ecosystem, or choose the right tools for their problems.

## Outline

- **0:00‒0:10 (10 min)** Lecture 1: Array-oriented programming and its benefits. Simple and complex (3 body problem) examples of imperative, functional, and array-oriented styles. Speed and memory advantages in Python. What the array-oriented paradigm emphasizes/is good for: interactive analyses of distributions. Path length as a worked example.
- **0:10‒0:25 (15 min)** NumPy puzzles and solutions. Alternating between hands-on puzzles and walkthrough of solutions: array slicing, consecutive differences, curve length, and image downscaling with reshape.
- **0:25‒0:35 (10 min)** Lecture 2: Disadvantages of array-oriented programming. (1) The problem of intermediate arrays, shown using the quadratic formula, with timing, compared to pre-compiled C code. (2) The “iterate until converged” problem, shown using a one-dimensional minimizer (Newton’s method) for an array of initial states; talk about epochs in ML.
- **0:35‒0:45 (10 min)** Lecture 3: JIT-compilation with Numba and JAX. Describe JIT-compilation as the solution to the intermediate array problem (1). First Numba then JAX on the quadratic formula. Show that Numba only accelerates if you write imperative code, unlike JAX, and show that JAX can’t follow if-branches or loops of unknown length.
- **0:45‒0:55 (10 min)** Project 3: JIT-compilation of the Mandelbrot set. Walk through imperative Python, array-oriented NumPy, Numba, and JAX implementations with timings. Note that array-oriented programming is advantageous for GPU programming, even beyond Python.
- **0:55‒1:05 (10 min)** Lecture 4: Ragged and deeply nested arrays. Show examples of ragged, nested, missing, and heterogeneous data, and how it can still make sense to treat them as arrays. Conversion to and from “tidy” data (tabular with references) to compare and contrast.
- **1:05‒1:20 (15 min)** Lecture 5: Working with large datasets. Overview of tools for chunking, compression, and labeled arrays: Dask, Zarr, Blosc2, and xarray.
- **1:20‒1:30 (10 min)** Wrap-up and Q&A.

**Links**:

- [GitHub Repository](https://github.com/ikrommyd/2026-04-15-pyconde-and-pydata-2026-tutorial-array-oriented-programming)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AGYLTV/>

## 93. [Roll for Architecture: DungeonPy – A D&D Companion as Server + Thin Clients](https://pretalx.com/pyconde-pydata-2026/talk/S9VSCV/)

**Speakers**: [Francesco Conte](https://pretalx.com/pyconde-pydata-2026/speaker/RCRAQE/)

**When and where**: Wednesday, 2026-04-15, 16:15–16:45, room Dynamicum [Ground Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

### **DungeonPy** – an interactive Dungeon&Dragons app for remote campaigns

As a matter of fact, tabletop RPGs are secretly distributed systems: one canonical world state, many clients, lossy links (players), and strict access control (“no peeking at the DM notes”). This talk introduces **DungeonPy**, which evolves a Python D&D companion from two local app – a Pygame battle map and a PySimpleGUI initiative/condition tracker – connected by lightweight TCP messages, into an authoritative server with multiple role-aware clients. The result is a fully real-time interactive setup, where the DM controls the full state and can reveal information selectively – under the hood it’s all about client intents, server validation, state updates, event broadcasting and periodic snapshots. We will cover protocol design (deltas vs snapshots, ordering/idempotency), server-side view projections (DM omniscience vs per-player truth and fog-of-war), UI-safe concurrency, and testing your homemade message bus without summoning race conditions. Expect patterns you can reuse in any stateful client/server app – just with more goblins.

**Description** (verbatim):

## **Roll for Architecture: DungeonPy – A D&D Companion as Server + Thin Clients**

Many tiny, personal projects reach a point where “it works on my machine” is no longer the interesting part, and it becomes more about making it _scale in structure_: clean boundaries, explicit state, testable behaviour and room for new features. This session is a case study of that journey using a D&D assistant for remote playing written in Python, that turned into something completely off-scale.
The starting point is a few desktop clients:

- a **Pygame** (battle) _map_ (grid, tokens, map objects, movement), and
- a **PySimpleGUI** _tracker_ for initiative, HP and conditions, with a clear “active combatant” concept,

initially synchronized with lightweight TCP messages.
This already exposes real engineering questions: avoiding GUI thread violations, preventing feedback loops, and deciding what the “source of truth” is when both ends can initiate updates.
The evolved version introduces an **authoritative server**. Players connect as clients and can interact in real time – moving tokens and manipulating shared objects – while the DM client keeps full visibility and control. Clients do not share state with each other: they submit _intents_ (move here, end turn, toggle condition), the server validates, updates state, and broadcasts events plus periodic snapshots. The key architectural move is _role-scoped state_: the server owns the full truth and projects different “views” to each client (DM omniscience vs per-player information), so fog-of-war and hidden details are enforced by design. In other words:

- **DM client**: full map + all combatants + hidden details.
- **Player client**: a filtered view (only the player’s character sheet details, their token, and whatever the DM has revealed).

The authoritative server runs on a small VPS with a public endpoint. Clients connect over secure WebSockets (wss://) on port 443, so players can join from anywhere without port forwarding. TLS is terminated by a standard reverse proxy, and the server speaks a small JSON message protocol (snapshots + events) over WebSocket frames.

### **Open source software used**

- `Pygame` (map rendering + input)
- `PySimpleGUI` (initiative/conditions UI)
- `asyncio` (multi-connection handling)
- `websocket` (client/server transport)
- (non-python) `NGINX` (reverse proxy, TLS)

### **Detailed talk outline**

1. - **Intro: D&D, remote play, and why am I doing this?**
2. - **Setting up the table**
     - PyGame
     - PySimpleGUI
3. - **State model and serialisation**
     - Turning GUI objects into explicit data (combatants, map, doors, initiative order).
     - JSON snapshots and versioning.
4. - **Protocol design: events vs snapshots**
     - Event messages for responsiveness (“token moved”, “condition added”).
     - Snapshot sync for recovery and late joiners.
     - Idempotency and ordering: simple sequence numbers, replay safety and conflict avoidance.
5. - **Role-based filtering (the privacy boundary)**
     - A single canonical server state.
     - Server-side “view projection”: DM view vs per-player view.
     - Practical examples: hidden enemies, secret doors, private notes, fog-of-war style reveals.
6. - **Concurrency and UI integration**
     - Socket threads feeding GUI event loops safely (posting events into the GUI thread rather than touching widgets directly).
     - Keeping the map smooth under network jitter: optimistic UI vs confirmed updates (and when not to).
7. - **Testing strategy for a networked hobby project**
     - Unit tests for pure state transitions (“apply damage”, “advance turn”, “illegal move rejected”).
     - Protocol tests with simulated clients.
     - Logging that helps during live play without drowning you in noise.
8. - **Extensibility hooks**
     - Adding new client types (spectator screen, mobile character sheet).
     - Plug-in style rules (different systems, homebrew conditions).
     - Future improvements: authentication for remote play, persistence, and reconnection.

### **Takeaways**

Attendees will leave with a practical blueprint for:

- Designing a tiny, testable message protocol in Python.
- Updating GUIs safely from background network threads.
- Enforcing “who can see what” without duplicating logic everywhere.
- More importantly, they’ll be given an example on how python can be used for highly non-standard tasks (like allowing remote role-playing gaming).

### **Intended audience**

Basic and intermediate Python developers comfortable with basic classes and modules, and curious about architecture and networking. This talk will be as much about _Python_ as it will be about _nerd culture_: the goal is learning something while keeping a light heart.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/S9VSCV/>

## 94. [Django-Q2: Async Tasks Made Simple](https://pretalx.com/pyconde-pydata-2026/talk/BHJERV/)

**Speakers**: [Moin Uddin](https://pretalx.com/pyconde-pydata-2026/speaker/EDNBNV/)

**When and where**: Wednesday, 2026-04-15, 16:55–17:25, room Dynamicum [Ground Floor]

**Type**: Talk — **Track**: PyCon: Django & Web — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Managing asynchronous task queues in Django with tools like Celery can be overkill for many projects. Django-Q2 is a lightweight alternative that integrates natively with the Django admin. In this talk, you will learn how to streamline your background tasks and cron jobs, featuring a practical demo to get you started immediately.

**Description** (verbatim):

Handling asynchronous tasks and cron jobs in Django is essential for features like sending emails or generating periodic reports. However, the industry standard Celery often comes with significant configuration overhead and infrastructure dependencies like Redis or RabbitMQ.

If you have ever struggled with that complexity or looked for a more intuitive way to manage background processes, Django-Q2 is the answer. It is a lightweight solution that leverages your existing database, eliminating the need for complex brokers. Its native integration makes it perfect for small to medium-sized projects that need to move fast.

This talk will guide you through integrating Django-Q2 to simplify your workflow:

- Problem Solving: We will look at how to use Django-Q2 to solve real-world task management issues.

- Feature Deep Dive: We will explore key features, such as using the database as a backend and monitoring tasks directly from the Django Admin interface.

- Live Demo: We will configure Django-Q2 from scratch to handle asynchronous email sending and schedule a recurring maintenance job

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BHJERV/>

## 95. [Holistic Optimization: Implementing "Pipeline-as-a-Trial" HPO with Ray and Cloud Infra](https://pretalx.com/pyconde-pydata-2026/talk/GPV9SM/)

**Speakers**: [Abdullah Taha](https://pretalx.com/pyconde-pydata-2026/speaker/H39TUV/)

**When and where**: Wednesday, 2026-04-15, 17:35–18:05, room Dynamicum [Ground Floor]

**Type**: Talk — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Most hyperparameter optimization (HPO) stops at the model boundary. But what happens when your system relies on a complex chain of steps, a short-horizon model, a long-horizon model, ensembles, postprocesses etc? Tuning one piece in isolation often leads to sub-optimal global results.

In this talk, we explore how we used Ray to move beyond simple model tuning. We’ll dive into a "Pipeline-as-a-Trial" architecture where Ray acts as the brain, triggering independent, scalable cloud workflows ( SageMaker Pipelines or Databricks Workflows) for every hyperparameter set.

We will discuss:

- The architectural shift from tuning models to tuning pipelines
- How to build the DAG/pipeline on Sagemaker/Databricks using declarative configs
- How to use Ray to orchestrate heavyweight remote jobs without bottlenecks.

Attendees will learn how to optimize entire pipelines (in a scalable manner on cloud) to minimize global metrics like WAPE, rather than just local model loss.

**Description** (verbatim):

Have you ever tuned a model to perfection, only to have it fail once integrated into your production pipeline? This is the "local optimization" trap: fixing a component while unintentionally breaking the complex system around it.
At Zalando, where we manage hundreds of forecasting models across 25 countries, local wins often lead to global failures.In this talk, we move beyond single-model tuning to explore Holistic Optimization.
We will detail how our team implemented a "Pipeline-as-a-Trial" architecture,

What We’ll Cover:

- An explanation of what "local optimization" problem is, and how it appears everywhere from tech products to day-to-day life.
- How we leveraged Ray’s distributed capabilities to manage high-concurrency Machine Learning workloads.
- Infrastructure Comparison: A candid, battle-tested breakdown of running HPO across AWS SageMaker, Databricks, and Internal EC2/Metaflow clusters.
- Operational Trade-offs: Real-world insights into the performance, cost, and traceability of different cloud implementations.
  *Configuration Driven Development: How an abstract library layer allows us to scale experimentation across hundreds of production models.

Stop chasing local solutions. Join me to learn how to build a distributed HPO framework that optimizes for your global business objectives.

PS: if you are a "Rick and Morty" fan, definitely join to see how Rick fell into the local optimization problem!

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GPV9SM/>

## 96. [Innovation Day: Startup Lounge [no-video]](https://pretalx.com/pyconde-pydata-2026/talk/KBNKAP/)

**Speakers**: Not listed in the source data

**When and where**: Wednesday, 2026-04-15, 10:00–12:00, room Lounge [1st Floor]

**Type**: Open Space — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

**Presented by hessian.AI**

PyCon DE & PyData has always been about building bridges — between disciplines, between communities, between ideas and implementation. And today, the worlds of startups, open source, and AI are more connected than ever.

That's why this year we're opening a dedicated space for exactly these conversations: real discussions, no hype, no fluff — just founders, engineers, and curious minds talking honestly about what it takes to build.

The **Startup Lounge** is a new, **unrecorded format** — which means you can speak freely, think out loud, and have the kind of conversation that doesn't happen on stage.

**Description** (verbatim):

## What to expect

This is not a talk. There are no slides.

The Startup Lounge is an interactive, participatory format built around open conversations and peer exchange. Whether you're actively building a company, thinking about it, or just want to understand how open source and AI actually connect to real business — this is your space.

You'll be in a room with 2,000+ Python developers, engineers, and data scientists. That's a rare concentration of technical depth and practical experience. Use it.

The session combines short impulse talks, guided table discussions, and open networking.

## Program

### 10:00 – 10:15 — Welcome & Introduction

An introduction to the format and an overview of the session.

### 10:15 – 10:30 — Impulse Talks

Three short talks to spark discussion, including topics such as:

- Open source & business models
- Developer tools and coding with AI
- Additional community-driven topics

### 10:30 – 11:30 — Table Discussions

The core of the session — three parallel discussion tables:

- **"Hair on Fire"** — urgent founder challenges (product, hiring, funding, tech)
- **Startup Curious** — for future founders and those exploring the startup world
- **Tech Stuff** — where Python meets product: scaling, architecture, AI/ML in production

Participants are free to move between tables and join different conversations.

### 11:30 – 12:00 — Open Networking

Unstructured time to continue conversations, connect, and follow up.

## Why join

Because the best conversations at a conference never happen on stage.

The Startup Lounge is intentionally small, intentionally unrecorded, and intentionally unscripted. You'll meet founders, engineers, and domain experts — and actually talk to them. Share a challenge, get direct input, form your own picture.

If you're building something, thinking about building something, or just want to understand how open source and AI are reshaping what's possible — come find out for yourself.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/KBNKAP/>

## 97. [Workshop: What do we still need to learn? [no-video]](https://pretalx.com/pyconde-pydata-2026/talk/7YA98N/)

**Speakers**: [Paula Gonzalez Avalos](https://pretalx.com/pyconde-pydata-2026/speaker/S3DXCY/), [Sebastian Neubauer](https://pretalx.com/pyconde-pydata-2026/speaker/NEBKEY/), [Dr. Kristian Rother](https://pretalx.com/pyconde-pydata-2026/speaker/MGXCCP/)

**When and where**: Wednesday, 2026-04-15, 14:20–15:50, room Lounge [1st Floor]

**Type**: Open Space — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI agents are reshaping how we work, how we code, how we search — and quietly, how we think about ourselves as practitioners. The ground is shifting. And nobody has all the answers yet. That is exactly why we are doing this. We invite you into an open, interactive workshop in the community space: no slides, no frontal talk, no recording. Just honest conversations about what skills still matter, what is becoming obsolete, and what we need to build to navigate what is coming.

**Description** (verbatim):

These are troubling times. Interesting times. Exciting times. Times that challenge us to reflect on where we should be focusing our energy.

In this interactive workshop, we will start by collectively answering four thought-provoking questions on shared boards — every voice, every perspective, visible in the room. Then we vote with dots on the topics that matter most to us. The winning topics go straight into a fishbowl: short, focused five-minute discussions where a small circle talks while everyone else listens, reacts, and rotates in.

The insights and themes from this session will flow directly into the panel discussion on Thursday afternoon, so your voice carries further than this room.
Come in, participate, find a seat, and let us figure this out together.

_Open community space · Non-recorded · All experience levels welcome_

Source: <https://pretalx.com/pyconde-pydata-2026/talk/7YA98N/>

## 98. [A View of Sovereignty from The Cloud](https://pretalx.com/pyconde-pydata-2026/talk/LSJ3CN/)

**Speakers**: [Aaron Glenn](https://pretalx.com/pyconde-pydata-2026/speaker/QZ3QRG/)

**When and where**: Thursday, 2026-04-16, 09:05–09:50, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Keynote — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

While The Cloud is just someone elses computer, those computers come together from many places and many, many someone elses. The constituent parts to connect, power, house, and ultimately operate those computers are from many more places and someones still! We explore what these infrastructure pieces of The Cloud are explicitly; and how the many definitions of digital sovereignty can be viewed from the viewpoint high up in The Cloud.

**Description** (verbatim):

While The Cloud is just someone elses computer, those computers come together from many places and many, many someone elses. The constituent parts to connect, power, house, and ultimately operate those computers are from many more places and someones still! We explore what these infrastructure pieces of The Cloud are explicitly; and how the many definitions of digital sovereignty can be viewed from the viewpoint high up in The Cloud.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/LSJ3CN/>

## 99. [Building MCP at the Speed of Hype: Principles That Outlast the Trends](https://pretalx.com/pyconde-pydata-2026/talk/EPASS8/)

**Speakers**: [Rahkakavee Baskaran](https://pretalx.com/pyconde-pydata-2026/speaker/YPZZ3S/), [Friederike Bauer](https://pretalx.com/pyconde-pydata-2026/speaker/UUB9SM/)

**When and where**: Thursday, 2026-04-16, 10:15–10:45, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Every week, development in AI brings us another groundbreaking release, another model version, another must-have integration. In this rapidly shifting landscape, how does one build production systems that won’t be obsolete by the time you deploy them?

We'll explain how trusting in proven engineering principles from software development and machine learning, like separation of concerns and evaluation practices, became our anchor in an ever-changing landscape of AI development. We share lessons learned from building two MCP applications using FastMCP and PydanticAI. Against these challenges, we found that fundamental engineering principles provided the foundation we needed.

Participants in the process of developing AI tools will leave with practical strategies for building AI-powered systems that are flexible enough to adapt, yet stable enough to trust.

**Description** (verbatim):

Every week, AI brings us another groundbreaking release, another model version, another must-have integration. Among these developments, agentic systems have emerged as a key component. Introduced at the end of 2024, the Model Context Protocol (MCP) has become an important enabler of this change and has established itself as the standard for connecting AI agents with external data sources and tools. In this rapidly shifting landscape, how does one build production systems that won't be obsolete by the time you deploy them?

This talk shares practical lessons from building two real-world MCP applications with FastMCP and PydanticAI: JobmonitorMCP, which leverages the jobmonitor.de API to create intelligent regional labor market reports, and a tool for an international non-profit combining multiple agents into a powerful question and answer application.

During development, we faced multiple challenges: MCP clients and models that interpret the same protocol differently, emerging features with limited documentation and trying to evaluate non-deterministic outputs. Stakeholders repeatedly asked "Why does it behave differently today?" and "Are we using the newest model yet?"

What we learned: The antidote to AI hype isn't avoiding new technology, it's anchoring development in trusted engineering principles. Separation of concerns and focused components helped us design for the protocol rather than specific clients. Rigorous evaluation approaches combined LLM-as-Judge with manual review and user feedback. Transparent communication helped us manage expectations around AI capabilities without undermining confidence.

This session targets intermediate Python developers building or planning to build AI-powered applications. You'll leave with concrete strategies for building AI systems that adapt to new models while maintaining production stability, reflection questions for your own projects, and perhaps a little more confidence in your existing knowledge.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/EPASS8/>

## 100. [In Praise of Documentation: Tools, Tips & Techniques for Literate Programming in the AI Age](https://pretalx.com/pyconde-pydata-2026/talk/37AESH/)

**Speakers**: [Stephen](https://pretalx.com/pyconde-pydata-2026/speaker/UBWSCP/)

**When and where**: Thursday, 2026-04-16, 10:55–11:25, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

This talk has one simple message: _please document your code_. If you attend my talk, you'll hear me explain why I praise documentation, and why you should too.

While writing documentation is generally acknowledged to be a "good thing", most engineers do not document their work. I'll offer my optionated lament on the life and death of literate programming. A lament is a poetic discourse, expressing sadness, or feeling sorry about something. I'll give some examples of the _bad things_ that can happen when people don't write documentation.

Then, after making you feel bad, I'll give examples of how you can _feel good_. I'll explain why writing documentation is a "good" edifying activity, which helps you to be a better person, and make a better world.

I'll review types of open source documentation (Python and Unix), documentation frameworks (Diátaxis), and Python tools (Sphinx, Jupyter, Quarto) you can try out as soon as my talk is finished.

Then, I'll get "cool n' futuristic" by talking about AI. I'll emphasise the importance of text to AI-assisted coding and agentic workflows for "spec-driven development" (e.g. Agent-OS with Claude Code), before tempering your excitement by giving you some old-fashioned advice on "good" writing style by George Orwell.

In summary, if you come to my talk, you might experience an unusual mixture of sadness combined with hope. To conclude, I'll tell you to "please document your code". You'll laugh, go to the next talk, and forget my advice.

**Description** (verbatim):

# Introduction

# In Praise of Documentation

- The Promise of "Literate Programming"
- A Lamentation on the Death of Literate Programming
- Bad things that happen when you don't document

# Why You Should Document

- Code is Communication
- Accessible, Maintainable, Sustainable Code
- Version Control (e.g. GitHub)

# Examples

## Examples of Open Source Documentation:

- Python `help`
- Docstrings
- Unix `man` pages
- `README.md`
- `Readthedocs.com`

## Documentation Framework Example:

- Diátaxis

## Python Documentation Tool Examples:

- Sphinx
- `cookiecutter`

## Scientific Publishing Tool Examples:

- Jupyter
- Quarto

# The Bit About AI (yes, I know, and I'm sorry)

- The importance of text for AI Code Assistant and Agentic Coding workflows

## Documentation in "Spec-Driven" Development:

- `AGENTS.md`
- Agent-OS with Claude Code

# Calls to Action:

- Writing Tips by George Orwell
- Please Document Your Code!

Source: <https://pretalx.com/pyconde-pydata-2026/talk/37AESH/>

## 101. [7 Anti-Lessons from Building a PydanticAI Agent: Mistakes We Made So You Don't Have To](https://pretalx.com/pyconde-pydata-2026/talk/RUSUYF/)

**Speakers**: [Joshua Görner](https://pretalx.com/pyconde-pydata-2026/speaker/GUUWH3/)

**When and where**: Thursday, 2026-04-16, 11:35–12:20, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Talk (long) — **Track**: General: Autonomous Systems & AI Agents — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Life sciences compliance isn't forgiving. When your software helps companies navigate FDA regulations, ISO 13485, and EU MDR, "move fast and break things" isn't an option. Audit trails matter. Documentation is mandatory. Getting it wrong means regulatory findings, delayed product launches, or worse — patient safety risks.

During the development of our AI Assistant we made every mistake in the most unforgiving environment possible. After more than a year building with PydanticAI, pydantic-evals, and Claude — nearly 3,000 commits and 20+ contributors — here are 7 anti-lessons so you don't have to repeat them:

1. **"We need a multi-agent system"** — We built one. Then deleted it.
2. **"Agents need sophisticated planning"** — A todo list beat our workflow engine.
3. **"Give the agent lots of specific tools"** — Two high-level tools replaced dozens.
4. **"Encode workflows in code"** — Markdown files the agent reads at runtime won.
5. **"It works when I test it"** — Simple tests ≠ real user journeys. Realistic evals or you're blind.
6. **"Automate everything"** — Human stays in the driver's seat, not the trunk.
7. **"Apply what made you successful before"** — Your engineering instincts might hurt you here.

Real code, real git commits, real mistakes from a domain where mistakes are expensive.

**Come for the mistakes. Leave with shortcuts.**

**Description** (verbatim):

## The Domain: Where Mistakes Are Expensive

[Qualio](https://www.qualio.com/) builds quality management software for life sciences companies — the ones making medical devices, pharmaceuticals, and biotech products. Our customers navigate FDA 21 CFR Part 11, ISO 13485, EU MDR, and SOC 2. In this world, compliance isn't optional. Audit trails are mandatory. Documentation gaps mean warning letters, import bans, or product recalls.

When we decided to build an AI agent to help users manage compliance gaps, create remediation plans, and handle documentation — we knew the stakes. An agent that hallucinates a regulatory requirement or skips an approval step isn't just annoying. It's a liability.

So we built carefully with PydanticAI and Claude. And we still made every mistake possible. Here are 7 anti-lessons from the trenches.

---

### Anti-Lesson 1: "We need a multi-agent system"

It seemed obvious: separate agents for documents, compliance, and events. Clean architecture. We built it, shipped it, and spent weeks debugging coordination failures and inconsistent responses. In a domain where consistency matters, multi-agent chaos was unacceptable. The fix? Delete it. One agent with dynamic capabilities. Simpler, faster, and — according to our evals — more accurate.

### Anti-Lesson 2: "Agents need sophisticated planning"

Compliance workflows are complex. Surely the agent needs workflow graphs, state machines, planning frameworks? We tried. The agent got confused, skipped steps, invented procedures. The fix? A todo list. Add a task, check it off, see what's next. In a regulated environment, simple and auditable beats clever and opaque.

### Anti-Lesson 3: "Give the agent lots of specific tools"

We built dozens of tools using PydanticAI's tool registration: `create_document`, `update_control`, `get_gap_details`, `list_frameworks`, `submit_for_review`... The tool descriptions bloated the context. The agent picked wrong tools. The fix? Two high-level tools: `call API` (with OpenAPI specs for the details) and `read instruction` (load a markdown file). Fewer tools, better results, easier to audit.

### Anti-Lesson 4: "Encode workflows in code"

How does the agent know how to remediate a compliance gap? How to create a controlled document? At first, it was buried in prompts and Python. The fix? Markdown files — like Claude's skills system. The agent reads them at runtime. Engineers can review them. Knowledge belongs in documents your compliance team can actually read.

### Anti-Lesson 5: "It works when I test it"

Our early tests passed. The agent handled every case we threw at it. Then real users arrived — and everything broke. The problem? Our test cases were simple, synthetic, and predictable. Real user journeys are messy, multi-step, and full of context we didn't anticipate. The fix? Realistic evaluation data. We capture actual user sessions, anonymize them, and run them through pydantic-evals with LLM-as-judge rubrics. Does the agent follow the procedure? Does it hallucinate requirements? Does it handle the weird tangents users take? A 95% pass threshold in CI means nothing if your test data doesn't reflect reality.

### Anti-Lesson 6: "Automate everything"

We built a fully automated feedback loop: user feedback creates a Jira ticket, a dev triages it, a Claude instance picks it up, raises a PR, responds to review comments. The dream? The fix: keep the human in the driver's seat. PydanticAI's `DeferredToolRequests` pattern lets our agent propose actions and pause for approval — the same principle applies to our dev workflow. In compliance software, someone is always accountable. The automation handles grunt work. Humans make decisions. Assisted development, not autopilot.

### Anti-Lesson 7: "Apply what made you successful before"

This is the meta anti-lesson. Good engineering habits — upfront design, comprehensive APIs, handling every edge case — _can_ slow you down with agents. The LLM will surprise you. Your assumptions will be wrong. The fix? Start scrappy, iterate fast, let evals tell you what's working. The hardest part isn't code. It's unlearning.

---

### Bonus: Scaling Agent Development with tmux

How to run multiple agent experiments in parallel. Low-tech, high-leverage.

---

## Who Should Attend

Developers building AI agents, especially in domains where accuracy and auditability matter. Familiarity with PydanticAI is helpful but not required — you'll see enough code to get started.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/RUSUYF/>

## 102. [Open Source as a Business — Models, Paths, and Practice](https://pretalx.com/pyconde-pydata-2026/talk/AKGUAC/)

**Speakers**: [Yann Lechelle](https://pretalx.com/pyconde-pydata-2026/speaker/TRD78B/), [Ines Montani](https://pretalx.com/pyconde-pydata-2026/speaker/FZKG9N/), [Sylvain Corlay](https://pretalx.com/pyconde-pydata-2026/speaker/FDGPYL/), [Alexander CS Hendorf](https://pretalx.com/pyconde-pydata-2026/speaker/K9DZKF/)

**When and where**: Thursday, 2026-04-16, 13:20–14:20, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Panel — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Open source powers the world's digital infrastructure — from AI research to enterprise data pipelines. But how do you build a sustainable business on it? This panel brings together three figures from the heart of the global open source ecosystem: Yann Lechelle (Probabl), who made the deliberate switch from infrastructure CEO to open source; Sylvain Corlay (QuantStack), whose consulting business is built from and around the core of the Jupyter ecosystem and its maintainers; and Ines Montani (Explosion / spaCy), one of the most influential voices in NLP tooling. Three founders. Three paths. Real answers on what it takes to build — or switch to building — a business in open source.

**Description** (verbatim):

The discussion centres on concrete experience — different starting points, different ecosystems, different business models — with the shared thread being open source as a deliberate professional and commercial choice.

**Key Questions:**

1. _Different entry points:_ You each came to building a business on open source from a different direction. What drove that decision — and what did you not expect?

2. _Where the business actually starts:_ Open source is the foundation, not the product. How do you define what you sell, and to whom?

3. _Community and commerce:_ How do you maintain trust and credibility in an open source community while running a commercial operation around it?

4. _Open source and AI:_ The AI landscape is consolidating fast around closed systems. What does that mean for open source projects and the businesses built on them?

5. _European perspective:_ Is there something specifically European about the way you think about open source as a business — around sustainability, sovereignty, or independence?

6. _Advice:_ What would you tell someone who wants to build a business on open source — or switch to doing so — and has not yet started?

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AKGUAC/>

## 103. [Panel What Do We Still Need to Learn?](https://pretalx.com/pyconde-pydata-2026/talk/KFPNUA/)

**Speakers**: [Paula Gonzalez Avalos](https://pretalx.com/pyconde-pydata-2026/speaker/S3DXCY/), [Sebastian Unterreitmeier](https://pretalx.com/pyconde-pydata-2026/speaker/DT3MJ3/), [Silvia Hänig](https://pretalx.com/pyconde-pydata-2026/speaker/N7PU9Q/), [Dr. Kristian Rother](https://pretalx.com/pyconde-pydata-2026/speaker/MGXCCP/)

**When and where**: Thursday, 2026-04-16, 15:05–16:05, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Panel — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI is no longer just a technical tool. It is fundamentally rewriting how we approach every professional task and we are now seeing a shift that impacts every role in every industry. In this panel discussion we will discuss the question no one can answer too confidently: in a world where AI writes the code, drafts the report, and automates the pipeline, what exactly are we still supposed to be learning?

**Description** (verbatim):

If AI can handle the code, the writing, the routine data processing, and complete automation frameworks with agents, what exactly are we supposed to be learning? This panel brings together the Python community for an honest and likely heated conversation about the skills that actually provide a human edge in an automated world. We are moving past the hype to look at the hard realities of 2026:

**The Educational Pivot:** When the doing is automated, does technical mastery still matter? A developer and Data Science education expert debates whether we still need to learn the how, or whether the focus should shift entirely to the why.
**The Global Reality**: A consultant's view on how AI is transforming non-technical industries. It is no longer just about code; AI is reshaping the very tasks that define professional roles across the board. And how do you spot real talent in a world of AI-assisted portfolios?
**The Future Framework:** The Head of an AI Academy asks: how do we upskill an entire workforce when the tools are changing faster than any curriculum can be written? And which future skills matter most, beyond AI skills themselves?

No consensus guaranteed. These are the very questions we all need to answer, right now.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/KFPNUA/>

## 104. [Closing Session](https://pretalx.com/pyconde-pydata-2026/talk/9ZEFTR/)

**Speakers**: Not listed in the source data

**When and where**: Thursday, 2026-04-16, 16:20–16:40, room Merck Plenary (Spectrum) [1st Floor]

**Type**: Plenary — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Closing Session

**Description** (verbatim):

Closing Session

Source: <https://pretalx.com/pyconde-pydata-2026/talk/9ZEFTR/>

## 105. [5 Years of NiceGUI: What We Learned About Designing Pythonic UIs](https://pretalx.com/pyconde-pydata-2026/talk/TZYGTL/)

**Speakers**: [Falko Schindler](https://pretalx.com/pyconde-pydata-2026/speaker/RPP37L/)

**When and where**: Thursday, 2026-04-16, 10:15–10:45, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

NiceGUI has grown from a small experiment into a widely used framework for building modern web-based user interfaces entirely in Python. After five years of development, thousands of users, and countless design iterations, we have gathered a rich set of insights into what makes a UI framework feel truly “Pythonic” while still leveraging the power of the web platform.
This talk presents the key lessons learned while evolving NiceGUI, with a focus on how Python’s own language features can meaningfully improve the developer experience. We explore how context managers, method chaining, decorators, async/await, type hints, dataclasses, and even well-chosen default arguments contribute to a clean, expressive, and maintainable UI API. Attendees will walk away with a deeper understanding of how to design Python-first interfaces—whether for web apps, dashboards, or internal tools—without needing to write JavaScript, CSS, or frontend boilerplate.

**Description** (verbatim):

Five years ago, the NiceGUI project set out to answer a simple question: Can we build modern, interactive web UIs entirely in Python without giving up power or flexibility? Since then, the framework has evolved into a production-ready, community-driven tool that builds on top of proven technologies such as HTML, CSS, JavaScript, Vue.js, Quasar, Tailwind, and FastAPI—while exposing a Pythonic interface that feels natural to Python developers.
This talk traces that journey and distills the design principles that worked, those that didn’t, and the patterns that ultimately enabled NiceGUI to provide a smooth developer experience.
We begin with a short demonstration of NiceGUI’s “3-line Hello World,” highlighting how familiar Python code can generate dynamic web interfaces. From there, we examine the technical foundations that allow the framework to stand on the shoulders of major frontend and backend ecosystems.
The core of the talk focuses on Python language features and how they shape API design:

- **Context managers** to express hierarchy and UI composition intuitively.
- **Method chaining** inspired by the builder pattern for concise, readable configuration.
- **Decorators** (such as @page and @refreshable) to define routing and reactive behaviour without ceremony.
- **Async/await** for event handlers, background tasks, and page functions.
- **Type hints** to support static analysis, IDE completion, and clearer API intent.
- **Dataclasses** as bindable, structured state containers.
- **Default arguments and sentinel patterns** to allow powerful yet discoverable APIs.

Attendees will gain practical insights useful beyond NiceGUI itself: how to design Python APIs for GUI frameworks, dashboards, developer tools, or any domain where clarity, maintainability, and expressiveness matter. The talk is aimed at Python developers interested in web interfaces, framework design, or improving the ergonomics of their own libraries.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/TZYGTL/>

## 106. [Surviving AI Fatigue: Staying Sane and Relevant in a Fast Moving Field](https://pretalx.com/pyconde-pydata-2026/talk/GATMPP/)

**Speakers**: [Ajay](https://pretalx.com/pyconde-pydata-2026/speaker/TJMBFL/), [Jeyashree Krishnan](https://pretalx.com/pyconde-pydata-2026/speaker/NH38CT/)

**When and where**: Thursday, 2026-04-16, 10:55–11:25, room Titanium [2nd Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

In an era where new AI models, benchmarks, and frameworks emerge daily, many of us feel caught in a relentless cycle of catching up, what is called "AI fatigue". This talk dives into the causes and consequences of that fatigue, from information overload and social media hype to the constant pressure to stay relevant. Drawing on personal experience and community insights, we explore why chasing every new paper or trend often leads to burnout rather than mastery.

More importantly, we share practical, evidence-backed strategies to stay informed without losing balance: curating a focused “information diet,” setting clear boundaries, using summarization tools intelligently, maintaining a personal knowledge base, and embracing “JOMO”—the joy of missing out. We also discuss how organizations can combat fatigue structurally by promoting focus, curiosity, and psychological safety.

This session is for anyone, from beginners to seasoned professionals, seeking to rediscover genuine curiosity in AI while preserving mental well-being. Attendees will leave with concrete tools, actionable habits, and a renewed sense that it is not only acceptable but healthy to not know everything.

**Description** (verbatim):

The world of AI and machine learning is moving at breakneck speed, with new papers, models, benchmarks, and frameworks announced daily. If you have ever felt overwhelmed, behind, or simply exhausted trying to keep up, you are not alone. In this talk, we share our own journey grappling with AI fatigue, what it feels like, why it happens, and what we have learned about staying informed without burning out.

We will start by defining AI fatigue and reflecting on why it is such a pervasive experience in our community, from social media hype to the sheer pace of real innovation. We highlight some of the common pitfalls, like chasing every trend, consuming too much noise, or neglecting mental health, and show why these approaches are counterproductive.

Then, we focus on actionable strategies and habits that actually work. We share concrete tips and techniques we personally use to manage our learning and maintain our enthusiasm for the field, including:

- Crafting an intentional information diet with trusted sources
- Setting clear boundaries and time boxing your learning
- Building a personal knowledge base for long term retention
- Using summarization tools to cut through dense papers and blogs
- Practicing “JOMO,” the joy of missing out, by focusing on depth over breadth
- Learning in public by teaching, blogging, or pairing with others
- Designing small, achievable experiments to stay engaged and motivated

Finally, we will suggest how organizations and teams can help prevent fatigue at a structural level by fostering focus, psychological safety, and curiosity instead of always on urgency.

This talk is for anyone, from beginner to expert, who wants to stay relevant and curious about AI without losing sight of their well being. You will leave with a set of practical tools, a fresh perspective on learning in a chaotic environment, and hopefully the reassurance that it is okay to not know everything.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GATMPP/>

## 107. [Open Table Formats in the Wild™ - Reloaded: Vortexing Ducks over Floating Icebergs](https://pretalx.com/pyconde-pydata-2026/talk/TRGQTL/)

**Speakers**: [Franz Wöllert](https://pretalx.com/pyconde-pydata-2026/speaker/3CXHP7/)

**When and where**: Thursday, 2026-04-16, 11:35–12:20, room Titanium [2nd Floor]

**Type**: Talk (long) — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Open table formats have _almost_ freed us from vendor lock-in. They form a critical building block of the modern, composable data stack. The most prominent open table format is Apache Iceberg - not only because of its storage layout, but also due to its REST catalog specification. Iceberg has gained significant traction through a recent stream of feature announcements from the community itself, major cloud providers like AWS, and data platform leaders such as Snowflake and Databricks.

But cutting through the hype: how does Iceberg actually perform in the real world if you are _not_ Netflix or Apple which are capable of _Building Your Own Snowflake_ (BYOS)? Can you realistically migrate from legacy solutions to Iceberg and enjoy all its promises without tradeoffs?

That, of course, is a rhetorical question. Some even argue that Iceberg got parts of the specification fundamentally wrong!?!

Curious? Join me for another episode of Open Table Formats in the Wild™. Expect a practical look at the current state of Apache Iceberg and Apache Parquet, alongside a gentle introduction to DuckLake and Vortex as promising contenders for table and file formats, respectively.

**Description** (verbatim):

### Description

The core promise of open table formats is engine interoperability with ACID guarantees, mutability, and schema evolution for massive datasets stored on cheap, reliable cloud object storage. Modern data platforms demand far more than _just_ interoperable, analytical batch processing. Engineers now require native support for CDC, incremental processing, streaming workloads, low-latency access, and point lookups - especially for AI-driven applications. Ideally, all of this would be covered by a single, unified solution.

However, Parquet - the foundational format for physically storing much of today’s data - predates both the AI boom and the era of unified batch and streaming systems. Likewise, Iceberg’s original design DNA was firmly rooted in large-scale, batch-oriented analytical workloads. This raises an uncomfortable question: are Parquet and Iceberg truly up to the task?

This talk explores that question through real-world use cases and architectural constraints. While the focus is on conveying key ideas and practical insights, the session is aimed at an intermediate to advanced audience. If you are new to the topic, you may want to watch last year’s [episode](https://youtu.be/YdFeHj5lRP4?si=NxO0Ot2-S_kYOokV) on Apache Parquet and Delta Lake, which provides a gentle introduction to the fundamentals of open table formats.

### Takeaways

After this talk, attendees will:

- Understand why incremental processing is not a native concept in Apache Iceberg
- Recognize how Iceberg’s metadata model creates hard limits for low-latency streaming workloads
- Learn why Parquet’s physical layout becomes a bottleneck for point lookups and AI-driven access patterns
- Get an early look at DuckLake and Vortex as emerging alternatives

### Agenda

**The Past (10 min)**

- Rationale - **The Idealized Model**
- Implications - **The Engineering Trade-offs**

**The Present (15 min)**

- Incremental Processing - **The Missing Primitive**
- Streaming Workloads - **The Batch Inheritance**
- AI Applications & Point Lookups - **The Access Wall**

**The Future (15 min)**

- DuckLake - **The Return of Relational Databases**
- Vortex - **The Parquet of Tomorrow**

Source: <https://pretalx.com/pyconde-pydata-2026/talk/TRGQTL/>

## 108. [Making Tech Tutorials Accessible: Practical Techniques for Educators](https://pretalx.com/pyconde-pydata-2026/talk/GYBRVN/)

**Speakers**: [Tamara Badikyan](https://pretalx.com/pyconde-pydata-2026/speaker/UVGDHP/)

**When and where**: Thursday, 2026-04-16, 13:20–13:50, room Titanium [2nd Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Want to make your tech tutorials accessible but don't know where to start? This talk shares practical techniques anyone can use.
In June 2025, I started creating tutorials for deaf and hard-of-hearing learners because my partner is hard of hearing. I learned that accessible content helps everyone: international learners, people on noisy trains, junior developers and tired seniors at the end of the day.
In this talk, I will share practical techniques for creating accessible tech tutorials:
• Creating videos with meaningful subtitles (manual timing, simple language)
• Principles of simple language for technical content
• Structuring content so everyone can navigate it easily
I am a content creator who learned these techniques through experimentation while teaching Excel. The talk presents my actual workflow with examples from creating tutorials for deaf/hard-of-hearing learners.
Whether you're creating video tutorials, writing documentation, or teaching workshops, you'll leave with actionable steps to make your content more accessible.

Why it matters: Tech education is growing globally. Making our content accessible isn't just good ethics—it makes our teaching better for everyone.

**Description** (verbatim):

Accessible content isn't just for people with disabilities—it makes tech education better by design for everyone. International learners, people on noisy trains junior developers and tired seniors at the end of the day—they all benefit from subtitles, simple language, and clear structure. Yet most developers who become educators have never learned how to make their content accessible.
This talk shares practical techniques I use creating tech tutorials for deaf and hard-of-hearing learners. Since June 2025, I've been creating Excel tutorial videos with manual subtitles in simple language for a YouTube community (~400 subscribers). My partner is hard of hearing, which taught me that accessibility isn't optional—it's essential. The techniques could be applied to any tech content: Python tutorials, data science courses, documentation, or workshops.
The talk follows this structure:

1. Understanding Barriers (5 minutes) Who benefits from accessible content? People with permanent, temporary, and situational limitations.
2. Creating Accessible Videos (15 minutes) My core workflow: manual subtitles in DaVinci Resolve with timing based on text length, using AI tools to simplify technical language, visual clarity with arrows and highlights, and the insight that you can't be accessible to everyone—focus on your target audience.
3. Clear Structure for any Content (8 minutes) Applying video principles to any format: logical heading hierarchy for navigation, alternative text for images, using built-in accessibility checkers, and simple language techniques.
4. Getting Started (2 minutes) One action to take this week, free tools to use, and resources for continued learning.
   I completed the W3C "Introduction to Web Accessibility" course and will be conducting a guest lecture on accessible learning materials at MSB Medical School Berlin (January 2026). As a non-native German speaker, I understand language barriers firsthand.
   Attendees will leave with practical techniques they can implement immediately and the confidence that accessibility is achievable without being an expert. No prior knowledge on accessibility is required.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GYBRVN/>

## 109. [How to compare apples with oranges: Proper evaluation of article-level demand forecasts](https://pretalx.com/pyconde-pydata-2026/talk/TB9WYZ/)

**Speakers**: [Stefan Birr](https://pretalx.com/pyconde-pydata-2026/speaker/BSV8LH/), [Mones Raslan](https://pretalx.com/pyconde-pydata-2026/speaker/LHFSUL/)

**When and where**: Thursday, 2026-04-16, 14:00–14:30, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

How do you evaluate performance when you predict more than 10 million time series each day? While a good plot can be worth more than a thousand metrics for a single time series, with large-scale machine learning models implemented with _LightGBM_ and _PyTorch_ we have to resort to meaningful aggregations. We will share insights and learnings from the past 2 years of deploying and operating our article-level demand forecasting models at the pricing department of Zalando.
This talk moves beyond basic metrics to showcase the pitfalls of aggregated error measures and the best practices we’ve developed to keep our stakeholders informed and our models accurate.

**Description** (verbatim):

At the pricing department in Zalando, we are predicting future demand for millions of articles on a daily basis by large-scale machine-learning models. These forecasts are key for discount decisions taken downstream. As evaluating every forecast on its own becomes infeasible at this scale and frequency we created a set of aggregated metrics that help us make informed statements about the performance of our models. On the one hand these metrics are being used by us to further improve our forecasting models, on the other hand they are used by our stakeholders to make informed decisions.

To handle this volume, we use _PySpark_ for data processing and scaling our evaluations across the entire assortment. Furthermore, evaluating forecast performance in this context is crucial in two different scenarios, namely when analysing past forecast performance and when creating and comparing alternative models. In both cases we look at different time ranges and possible different subsets of the forecasted articles and calculate aggregated performance measures to compare them. We want to answer questions like

- “Is this forecast performing better in low-discount periods than during sales events?”
- “Did we make a higher error on highly discounted articles during last week?”
- “Is this model well-suited to predict high (or low) selling articles?”
- “Did our model perform well for sneakers during the last voucher event?”

Evaluating aggregated metrics like a relative mean squared error (MSE) or an mean absolute percentage error (MAPE) over different sets of articles has lots of pitfalls. Comparing different parts of the assortments leads to an "Apples vs. Oranges" problem that we want to elaborate on based on examples we experienced in our daily work.

To answer the questions above we developed a set of aggregated metrics that we monitor on a daily basis using _plotly_ and _streamlit_ for clear, interactive visualization. We want to present these metrics and explain how they are useful for the questions and tasks mentioned above. We will highlight the techniques and best practices to draw meaningful insights from evaluating forecast performance and how we are able to compare apples with oranges using meaningful lower bounds for our aggregated metrics.

We also want to share how observations from our monitoring influenced the evolution of our _LightGBM_ and _PyTorch_ models and how it shaped important parts like feature engineering, hyperparameter tuning and the choice of our loss functions. Lastly we will touch on how to communicate these sometimes very technical numbers with stakeholders so that they can make informed decisions without being overwhelmed by details.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/TB9WYZ/>

## 110. [Simulating the World using SimPy: A practical Example](https://pretalx.com/pyconde-pydata-2026/talk/WDHTQR/)

**Speakers**: [Niklas](https://pretalx.com/pyconde-pydata-2026/speaker/VRJLJE/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Titanium [2nd Floor]

**Type**: Talk — **Track**: PyData: PyData & Scientific Libraries Stack — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Modern systems are complex - and testing them in real environments is often expensive, risky, or simply not reproducible. Simulation is a practical way to explore behavior under controlled conditions: run scenarios, validate assumptions, inject failures on purpose, and repeat experiments without touching production.

In this talk, I build a concrete event-based simulation with `SimPy` to compare `load-balancing algorithms` under different conditions. I’ll show how `SimPy`’s processes and events fit together, how to structure the simulation cleanly, and how to move beyond a one-off demo by making runs reproducible and configurable - using `configuration files` and a simple `command-line interface`.

**Description** (verbatim):

Real-world systems are often too complex to test reliably, in the same environment and under the same conditions. Changes are hard to measure, edge cases are difficult to reproduce, and external influences can hide the real behavior of a system. Simulation offers a way to abstract from reality while staying close enough to produce meaningful results. It allows full control over system components, timing, and disruptions, and makes it possible to test many scenarios in a repeatable way.

The practical example of this talk focuses on simulating `load-balancing algorithms`. Load-balancers are a good example of systems that are hard to evaluate in real environments. Some tested algorithms have no existing implementation, others differ across platforms, and cloud environments introduce many uncontrollable factors such as network latency, cloud noise, and reoccurring background workloads. These factors make fair and consistent testing almost impossible.

The problem is addressed by building an event-based simulation using `SimPy`. The session explains how `SimPy` works by using `Generators` to create the events, and how time and processes interact inside a simulation. An architecture for a practical example for a load-balancer simulation is presented, showing how different components interact and how algorithms can be swapped and compared.

The talk also covers improvements made to the simulation, including a `command-line interface` for easier execution and a `YAML` configuration file for flexible setup. It concludes with practical tips and lessons learned when working with `SimPy`, helping to avoid common pitfalls and improve simulation design.

Overall, the session provides an introduction to simulation as a testing tool, a hands-on example using `SimPy`, and a realistic architecture for building and evolving simulations in Python.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/WDHTQR/>

## 111. [Why Did The Model Do That? Debugging the Ghost in the Machine](https://pretalx.com/pyconde-pydata-2026/talk/MLUK9M/)

**Speakers**: [Cosima Meyer](https://pretalx.com/pyconde-pydata-2026/speaker/7GY7XH/)

**When and where**: Thursday, 2026-04-16, 15:45–16:15, room Titanium [2nd Floor]

**Type**: Talk — **Track**: General: Ethics & Privacy — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Why did the model say "No"? In an era where machine learning models increasingly influence high-stake decisions, "trust me" isn't a sufficient explanation. Yet, the logic behind many model decisions remains a black box, often hiding bias and making it difficult to establish trust.

In this talk, we move beyond the mystery of the "ghost in the machine" and into practical debugging using a structured _XAI Decision Tree_. Instead of guessing which method to use, we will walk through a logical framework that narrows down the field based on a few critical questions: the type of data you have, the level of model access available, and whether you need to explain a single prediction or the entire system.

The audience will leave with a clear path to choosing the right explainable AI (XAI) method - such as SHAP, LIME, or Integrated Gradients - and the corresponding Python framework for their specific use case.

This session will cover:

- Importance of XAI: Understanding why XAI is crucial using a real-world example
- XAI Landscape: An overview of existing XAI methods and how they are related
- XAI Decision Tree: How to use the structured XAI decision tree to choose the right explanation method for your use case
- Local vs global: A common understanding of local vs global explainability
- XAI in Practice: XAI in practice as well as corresponding Python frameworks to use

**Description** (verbatim):

My planned outline for the talk is as follows:

- **Intro and opening hook** (4 mins): A look at a clearly biased model and why "black box" decisions fail to establish trust
- **The XAI Decision Tree** (17 mins):

  - A practical overview of the landscape and walking through the tree: Selecting the right method based on your model and data
  - Mapping these methods to specific Python libraries and frameworks (e.g., `shap`, `lime`, `captum`, `transformers-interpret`, `alibi`, `dalex`, ...)

- **Closing and Take-away** (4 mins)
- **Q&A and Buffer** (5 mins)

**Links**:

- [Why Did The Model Do That? Debugging the Ghost in the Machine (Presentation)](https://bit.ly/xai-talk)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/MLUK9M/>

## 112. [Embedding Data Science in IoT devices with MicroPython and emlearn](https://pretalx.com/pyconde-pydata-2026/talk/3U3BZH/)

**Speakers**: [Jon Nordby](https://pretalx.com/pyconde-pydata-2026/speaker/CVFFNV/)

**When and where**: Thursday, 2026-04-16, 10:15–10:45, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyCon: Embedded Systems & Robotics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python is the standard solution for many machine learning and data science applications,
from large cloud systems, to workstations, and even on larger embedded or robotics systems.
But as we move down into more constrained environments regular (C)Python starts to be a less good fit.
The MicroPython project provides a Python implementation that is tailored for such environments,
and this makes it possible scale down to microcontrollers with just a few megabytes of RAM (or less!).
As a bonus, MicroPython with WebAssembly also makes lightweight browser applications possible.
In this talk, we will discuss how to combine Internet of Things (IoT) hardware, MicroPython and browser to build stand-alone smart sensor systems and laboratory gear for physical data science.

**Description** (verbatim):

Typical Internet of Things devices send off most of the data to an external cloud service for analysis.
This causes challenges both in terms privacy, poor reliability under poor connectivity, and loss-of-availability when the service is discontinued.

We would like to show that it is possible to achieve the majority of functionality using a local-first approach, including machine-learning based sensor-data analysis.
And that this can done on low-cost microcontrollers such as ESP32.

This talk will cover how to build stand-alone devices for measuring and analying physical sensor data, using MicroPython. This includes these aspects:

- Measuring the surroundings using sensors
- Connectivity using WiFi
- Data storage using on-board filesystem
- Serving a webui for configuration/control, using Microdot
- Automated data processing/analysis using DSP and ML, with emlearn-micropython
- Enabling interactive data analysis via webui
- Managing concurrency on microcontroller, using asyncio
- Optional integration. Pull using HTTP, and/or push using Webhooks/MQTT

The sensor data will either be accelerometer, sound or images/video (To be Decided).

### About MicroPython

MicroPython is an implementation of Python that runs on practically all microcontrollers with 128kB+ RAM. It provides access to the microcontroller hardware, functions for interacting with sensors and external pheripherals, as well as connectivity options such as WiFi, Ethernet, Bluetooth Low Energy, etc.

While MicroPython can target a very wide range of hardware, we will focus on the Espressif ESP32 family of devices. These are very powerful and affordable, with good WiFi+BLE connectivity support, good open-source toolchains, are very popular both among hobbyist and companies, and have many good ready-to-use hardware development kits.

### About emlearn-micropython

emlearn-micropython is Machine Learning and Digital Signal Processing package for MicroPython, built on top of the emlearn C library. It provides convenient and efficient MicroPython modules, and enables application developers to run efficient Machine Learning models on microcontroller, without having to touch any C code. Compared to pure-Python approaches, the emlearn-micropython models are typically 10-100x faster and smaller.

### Intended audience and expected background

Intended audience: Any developer or data scientist curious about sensor data processing, IoT, and how Python scales down to the smallest of devices.

The audience is expected to have a basic literacy in Python and proficiency in programming.
Familiarity with microcontrollers and embedded systems is of course an advantage, but the talk should be approachable to those who are new to this area. Familiarity with basic networking and web/browser concepts is an advantage.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/3U3BZH/>

## 113. [How We Built an Inclusive Data Organization: Careers, Community & 50% Women](https://pretalx.com/pyconde-pydata-2026/talk/RQTJFS/)

**Speakers**: [Xia He-Bleinagel](https://pretalx.com/pyconde-pydata-2026/speaker/UC7VCN/)

**When and where**: Thursday, 2026-04-16, 10:55–11:25, room Helium [3rd Floor]

**Type**: Talk — **Track**: General: Community & Diversity — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Building inclusive data teams and sustainable career paths is a challenge many organizations struggle with—especially in fast-growing, highly technical environments. Data careers are often portrayed as linear, while diversity initiatives remain abstract or ineffective in practice.

This talk shares concrete, experience-based lessons from building an inclusive data organization that supports career growth, fosters an internal data science community, and achieved more than 50% women representation in data roles. Rather than focusing on theory, the session highlights practical decisions, structural changes, and leadership behaviors that made inclusion measurable and sustainable.

Attendees will gain actionable insights into designing career paths that support non-linear journeys, creating internal data communities that encourage learning and collaboration, and implementing diversity practices that strengthen—rather than dilute—technical excellence. The talk is relevant for data scientists, engineers, team leads, and managers who want to build better teams and healthier data cultures.

**Description** (verbatim):

Many organizations aim to grow strong data teams, yet struggle with three connected challenges: unclear career paths, weak internal data communities, and a lack of diversity—especially in senior and technical roles. These challenges are often treated separately, even though they strongly influence one another.

This talk presents a holistic approach to building an inclusive data organization by aligning career development, community building, and diversity goals. The focus is on practical actions and structural choices that can be applied in real-world settings, regardless of company size or industry.

Talk Outline

1. The problem: why data organizations struggle

- Common myths about data careers (linear paths, constant availability, narrow profiles)
- Why diversity efforts often fail in technical teams
- The cost of ignoring community and inclusion: attrition, silos, burnout, and missed talent

2. Career growth beyond linear paths

- Designing career paths that support different life phases and backgrounds
- Recognizing and valuing transferable skills in data roles
- Making progression criteria transparent and fair
- Supporting growth from individual contributor to leadership without forcing a single model

3. Building an internal data science community

- Why internal communities matter for learning, retention, and impact
- Creating spaces for knowledge sharing without gatekeeping
- Encouraging collaboration across roles (data science, engineering, analytics)
- Aligning community activities with business value and technical standards

4. Achieving diversity with intention

- What “50% women in data” actually requires in practice
- Hiring processes that reduce bias while maintaining technical excellence
- Inclusive team structures and ways of working
- Leadership behaviors that support inclusion without tokenism

5. What worked—and what didn’t

- Trade-offs, challenges, and lessons learned
- Why inclusion is a continuous process, not a one-time initiative

6. Actionable takeaways

- Practical steps attendees can apply in their own teams
- Signals to look for when inclusion efforts are working—or failing
- How to start small and scale impact over time

Source: <https://pretalx.com/pyconde-pydata-2026/talk/RQTJFS/>

## 114. [Securing AI Agentic Systems: Enforcing Safety Constraints in AI Agent](https://pretalx.com/pyconde-pydata-2026/talk/9PBYAP/)

**Speakers**: [John Robert](https://pretalx.com/pyconde-pydata-2026/speaker/3VHXXW/)

**When and where**: Thursday, 2026-04-16, 11:35–12:20, room Helium [3rd Floor]

**Type**: Talk (long) — **Track**: PyCon: Security — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI agents are increasingly deployed with autonomy: calling tools, accessing data, modifying systems, and making decisions without human supervision. While prompts and guardrails are often presented as safety solutions, they break down quickly in real-world agentic systems.

In this talk, we explore how to enforce safety constraints in AI agents beyond prompting, using engineering techniques familiar to Python developers and data engineers. We will examine common failure modes in agentic systems such as tool misuse, goal drift, and over-permissioning and show how to mitigate them using policy layers, capability boundaries, and execution-time validation.

**Description** (verbatim):

AI agents are increasingly used as autonomous systems that can call tools, access data, and take actions in real environments. As these systems gain more autonomy, ensuring their safe and predictable behavior becomes an engineering challenge rather than a prompting problem.

This talk examines how safety constraints can be explicitly enforced in agentic AI systems, instead of relying solely on natural language instructions or model alignment. We will discuss typical safety and security issues that arise in agent based architectures, including over permissioned tools, unintended action chains, goal drift, and unsafe retries.

Using practical Python examples, the talk introduces architectural patterns for constraining agent behavior, such as policy layers, capability based tool access, action budgets, and runtime validation of agent decisions before execution. We will also explore how human in the loop checkpoints and audit logging can be integrated into agent workflows to support safer operation in production environments.

The focus of this session is on practical design and implementation techniques that help developers build AI agents with clearly defined boundaries, making their behavior more controllable, observable, and secure

Through practical Python examples, we will demonstrate how to:

- Design constrained agent architectures
- Enforce tool level permissions and action budgets
- Validate and block unsafe agent actions at runtime
- Combine human-in-the-loop checkpoints with automated controls

Source: <https://pretalx.com/pyconde-pydata-2026/talk/9PBYAP/>

## 115. [Escape the Hype: Teaching LLM Concepts Through an Interactive AI Factory Game](https://pretalx.com/pyconde-pydata-2026/talk/MS7AWK/)

**Speakers**: [Vadim Vlasov](https://pretalx.com/pyconde-pydata-2026/speaker/VNDGHR/), [Eric Glaser](https://pretalx.com/pyconde-pydata-2026/speaker/FKLVKJ/), [Lisa Amrhein](https://pretalx.com/pyconde-pydata-2026/speaker/KN3MLY/)

**When and where**: Thursday, 2026-04-16, 13:20–13:50, room Helium [3rd Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Everyone talks about LLMs, RAG, and AI agents - but who truly understands them? Marketing promises magic while documentation assumes expertise. Recent research from Gartner reveals the consequences: only 8% of HR leaders believe their managers possess adequate AI competency, while companies that restructure work around AI achieve revenue goals twice as often as those who merely train employees. The problem isn't lack of information; it's the lack of genuine understanding through experience.

We took a different approach. Instead of slides or tutorials, we built "AI Factory" - a non-profit educational platform in the form of escape room game where players learn by doing. Craft prompts under budget pressure. Watch guardrails fail in real-time. Break their own RAG pipeline. Each mistake teaches more than any documentation ever could.

In this talk, we'll share what we discovered while building and testing this game with real users: why failure-driven learning outperforms tutorials, how game mechanics create memorable "aha moments," and the surprising concepts that clicked only through play.

**Description** (verbatim):

The gap between AI adoption and AI understanding keeps growing. Teams copy-paste prompts without understanding why they work, vendor materials highlight capabilities over limitations, and the EU AI Act now requires organizations to ensure "a sufficient level of AI literacy among their staff." Traditional training — documentation, tutorials, talks — isn't closing this gap. What's missing is embodied learning: touching the parameters, breaking the system, feeling the consequences.

**Our Approach**

We built "AI Factory" — a Python-based educational game where players learn LLM concepts through hands-on challenges. Set in a magical potion factory, players master prompt engineering, guardrails, RAG pipelines, MCP tool orchestration, and multi-agent coordination.

What makes it different from typical AI tutorials:

- Real API calls, not simulations. Players interact with actual LLMs — when they misconfigure guardrails or adjust temperature, they see real consequences that transfer directly to production.
- Budget-driven decisions. Every API call costs in-game currency, forcing the same quality-cost-speed tradeoffs faced in real deployments.
- Progressive disclosure over information dumps. Each game stage reveals one missing piece. The full picture only clicks at the end — and that revelation is the reward.
- Immediate, specific, actionable feedback. Players see results the moment they submit — not just "incorrect," but a diagnostic breakdown of exactly what went wrong, clear enough to act on and retry.

**What This Talk Covers**

We share concrete design decisions and their outcomes — what worked, what didn't, and what surprised us:

- Narrative vs. jargon. How story-driven framing changed the way players understood complex concepts like RAG — without a single slide of theory.
- Constraints as a teaching tool. Why our first budget system backfired, and how a small redesign turned frustration into strategic thinking.
- When to simulate instead of build. Where we replaced real infrastructure with controlled illusions — and why the learning outcome didn't suffer.
- One game, many audiences. How players from different backgrounds found completely different entry points into the same levels.
- Scoring on top of non-deterministic AI. How we built a reliable evaluation engine for a system that never gives the same answer twice.

**Who Should Attend this Talk**

This talk is designed for multiple audiences:

- Educators and trainers looking for new approaches to teaching AI concepts
- Team leads responsible for upskilling teams on AI fundamentals — take away a tested approach, not just theory
- Anyone interested in gamification as an approach to technical education

Source: <https://pretalx.com/pyconde-pydata-2026/talk/MS7AWK/>

## 116. [Dynamic Knowledge Graphs](https://pretalx.com/pyconde-pydata-2026/talk/TST9LF/)

**Speakers**: [Jakob Leander Müller](https://pretalx.com/pyconde-pydata-2026/speaker/FYA7P8/)

**When and where**: Thursday, 2026-04-16, 14:00–14:30, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Traditional RAG systems struggle to understand holistic connections in distributed, constantly changing knowledge sources that characterize real-world organizations. While document-based approaches using vector embeddings provide basic retrieval, they fail to capture relationships and answer complex questions about interconnected information. Graph-based RAG offers a solution, but existing implementations like Microsoft's GraphRAG explicitly avoid dynamic operations due to complexity, requiring costly rebuilds when knowledge changes.

This talk introduces a production-ready dynamic knowledge graph system that supports real-time insertion, querying, and deletion of information. Through practical implementation details you will learn to build maintainable knowledge graphs that evolve with data, handle ambiguous entities and preserve information lineage.

**Description** (verbatim):

Like many organizations, we at VisualVest face the challenge of distributed and constantly evolving knowledge sources. Documentation lives across repositories, internal wikis, JIRA tickets, and various file formats in cloud storage. With ~250 employees making daily changes, our source of truth is highly dynamic. While traditional document-based RAG using semantic embeddings solved some of these pain points, it couldn't answer holistic questions or understand relationships between sources, leading us to explore graph-based approaches.

The challenge? Real-world knowledge sources are inherently dynamic. When thinking about information management and retrieval, we cannot ignore this reality if we want to create powerful, machine-readable and actually useful products. Microsoft's popular [GraphRAG](https://microsoft.github.io/graphrag/) library [explicitly rejected dynamic features](https://github.com/microsoft/graphrag/issues/429) (like deletion) due to complexity concerns. However, we believe that constantly rebuilding entire graphs isn't feasible for production systems.

This talk presents our solution: a truly dynamic knowledge graph with full insertion, query and deletion capabilities. We are also working on reducing the high computational cost of building knowledge graphs. Through caching strategies and small language model fine-tuning, we are trying to minimized both computational effort and strengthen our independence from cloud providers.

What you'll learn:

- An industry perspective on the challenges of distributed knowledge sources
- Formal definition and properties of dynamic knowledge graphs
- Our transformation pipeline
  - Experiments with fine-tuned small-language models
- Implementation details:
  - Inserting nodes and edges while preventing ambiguity through similarity matching
  - Tracking information origin across sources
  - Safely deleting documents from the graph without breaking relationships
  - Graph inference strategies

By the end of this talk, you'll understand why real-world knowledge graphs should be dynamic, how to build one yourself as well as the limitations and future directions of our approach.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/TST9LF/>

## 117. [(Autism and) The Predictive Brain Theory (in Tech)](https://pretalx.com/pyconde-pydata-2026/talk/BRCNB7/)

**Speakers**: [Dennie Declercq](https://pretalx.com/pyconde-pydata-2026/speaker/LUKY9J/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Helium [3rd Floor]

**Type**: Talk — **Track**: General: Education, Career & Life — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

New studies showed how the brain is not a passive receiver of stimuli but an active predictor of stimuli. People with autism have more difficulties when the predicted and received stimuli doe not match. How do we create a tech workforce where autistic individuals can work more comfortable due to predictability?

**Description** (verbatim):

What does new autism, AI and quantum computing research have in common? We need to stop following the well known 'input - process - output' model. Let's escape this model and embrace the predictive brain theory to understand autism and how people on the spectrum interact with technology and at the workplace.

Recent brain research shows that the brain is not a passive receiver of stimuli, but an active predictor of what will happen next. The brain is constantly building a big model of the world based on past experiences and using this model to predict what will happen next. When we have a big model of the world we know what to expect. If something unexpected happens, the brain receives this as an error and needs to update its model to accommodate the new information. This is not autism or tech specific, this is how the brain works for everyone according to the latest brain research.

A recent hypothesis suggests that people on the autism spectrum often have a harder time building the big model of the world and the stimuli-response system of people on the spectrum is often more sensitive, adding context blindness and the higher energy cost of executive functioning to the mix, it is harder for people on the spectrum to predict what will happen next and to deal with unexpected situations. This can lead to anxiety, stress and burnout.

If your tech job is constantly causing errors in the predictive model of the world, it will be hard to do your job and to be happy at work. In this talk I will explain how the predictive brain theory can help us understand autism and how we can build better technology and workplaces for people on the spectrum.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BRCNB7/>

## 118. [Rediscovering single-node processing: When does it make sense to move from Spark to Polars?](https://pretalx.com/pyconde-pydata-2026/talk/HQBC7R/)

**Speakers**: [Jonas Böer](https://pretalx.com/pyconde-pydata-2026/speaker/TP9MH3/)

**When and where**: Thursday, 2026-04-16, 15:45–16:15, room Helium [3rd Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

As data engineers, we are used to spinning up a Spark Cluster every time we want to do data processing and handle the overhead that comes with using such a mighty framework. But is this really necessary? In this talk I will argue that single-node processing with Polars is in many cases easier and cheaper. I will compare a typical ETL & Feature Engineering task in Spark and in Polars and offer a pragmatic opinion on when to use one or the other.

**Description** (verbatim):

Apache Spark is the industry standard for big data processing, rightfully so. But for many data processing applications, a more light-weight solution will work just as well, avoiding Spark's compute and configuration overhead. Polars offers such a solution, with a fast single-node processing engine and a syntax that will pose no problems for experienced Spark developers.
I will give a short comparison of Spark and Polars, where they have similarities and differences and show an implementation of a typical ETL and Feature Engineering task in both. I will compare the deployment, performance and cost of the two and, while giving my opinion on the topic, hope to enable you to also make an informed decision on when you want to use Polars and when to use Spark.

**Links**:

- [Slides on GitHub](https://github.com/morgil/pycon26-talk-rediscovering-single-node-processing)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/HQBC7R/>

## 119. [Tracking Knowledge Diversity in LLM-Generated Responses.](https://pretalx.com/pyconde-pydata-2026/talk/P7NYXB/)

**Speakers**: [Sarah Masud](https://pretalx.com/pyconde-pydata-2026/speaker/EKABAA/)

**When and where**: Thursday, 2026-04-16, 10:15–10:45, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

As large language models (LLMs)-powered “AI highlights” become the first information people see on the Web, a key question arises: how much variety and perspective do these systems actually deliver for information-seeking queries? Do LLMs offer broader viewpoints than traditional search or Wikipedia pages? Do larger models really produce more diverse answers—or are they all converging on the same language, and framing, raising concerns about “knowledge collapse”?

Drawing insights from experiments across LLM families, real-world topics, and hundreds of user-style prompts, this talk introduces an open-source framework for benchmarking and tracking epistemic diversity in LLMs. We focus on practical lessons for data scientists building and evaluating LLM-powered search, summaries, and knowledge systems—where diversity of information actually matters.

**Description** (verbatim):

This talk summarizes our research on how LLMs generate narratives and recurring tropes in real-world information-seeking setups via prompting.

**Talk outline:**

- Knowledge collapse and epistemic diversity: What they mean and why they matter for real-world information access (5 mins).
- Framework overview: How we measure epistemic diversity across LLM outputs (5 mins).
- Experimental design, results: Curating dataset for comparisons across model families, search results, and Wikipedia pages (7 mins).
- Implications for designing LLM-powered systems that preserve information diversity (10 mins)

**Key takeaways for AI practitioners:**

- When can retrieval-augmented generation (RAG) increase diversity?
- Can expanding Wikipedia via translation improve epistemic diversity or reinforce existing tropes?
- What are some open challenges in measuring cultural and contextual diversity in LLM outputs?
- Where are we headed in terms of model sizes, fluency, and breadth of knowledge?

**Useful links:**

- [Our open source framework](https://github.com/dwright37/llm-knowledge)
- [Reproducible Data Hugging Face](https://huggingface.co/datasets/dwright37/llm-knowledge-collapse)
- [Our Research paper](https://arxiv.org/abs/2510.04226)

**Links**:

- [Research Paper](https://arxiv.org/abs/2510.04226)
- [Github Repo](https://github.com/dwright37/llm-knowledge)
- [Full Dataset](https://huggingface.co/datasets/dwright37/llm-knowledge-collapse)
- [Slides for the Pycon DE talk on Speaker Deck](https://speakerdeck.com/_themessier/tracking-knowledge-diversity-in-llm-generated-responses)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/P7NYXB/>

## 120. [Are we free-threaded ready? Looking at where free-threaded Python fails](https://pretalx.com/pyconde-pydata-2026/talk/FP7YN7/)

**Speakers**: [Cheuk Ting Ho](https://pretalx.com/pyconde-pydata-2026/speaker/8EGVC9/)

**When and where**: Thursday, 2026-04-16, 10:55–11:25, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyCon: Python Language & Ecosystem — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Free-threaded Python aims to significantly improve performance, allowing multiple native threads to execute Python bytecode concurrently. In this talk, we will explore the current state of Python's free-threading initiative and assess its practical readiness for widespread adoption.

**Description** (verbatim):

We begin by exploring the background of free-threaded Python, summarising its origins, current status, and the technical differences distinguishing it from standard Python implementations. A key focus will be examining the compatibility landscape, specifically investigating how many popular third-party libraries are currently prepared for free-threading. We will distinguish between generic pure Python wheels and explicitly free-threaded wheels and I’ll explain how the community can contribute to compatibility verification.

We then critically discuss free-threaded Python's necessity, weighing the disadvantage of increased thread safety concerns (and verification methods) against the promised advantage of speed (including multithreaded profiling).Will free-threaded Python become a critical future direction for the language? How can you contribute? If and how specific projects can immediately benefit from it? Let’s find out together!

**Links**:

- [Slides](https://canva.link/free-threaded-py)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/FP7YN7/>

## 121. [Designing and Scaling a Python Library in the Open: Architecture, Automation and Community](https://pretalx.com/pyconde-pydata-2026/talk/VBPRQR/)

**Speakers**: [Camila Maia](https://pretalx.com/pyconde-pydata-2026/speaker/GXBKTT/)

**When and where**: Thursday, 2026-04-16, 11:35–12:20, room Platinum [2nd Floor]

**Type**: Talk (long) — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Designing a Python library that scales over time requires more than clean code. In this talk, we present ScanAPI, an open-source Python library for automated API integration testing and live documentation, as a case study in sustainable library design.

We explore how architectural decisions, Python features, and automation pipelines help reduce maintenance costs while improving developer experience. We also share how open collaboration and community practices turn a Python library into a long-term, scalable project.

Attendees will leave with practical patterns to apply when building or evolving Python libraries in the open.

**Description** (verbatim):

Building a Python library that remains reliable, maintainable, and welcoming to contributors is a challenge many projects face as they grow. This session presents ScanAPI as a real-world case study of how thoughtful engineering and automation can support both technical scalability and open source sustainability.

ScanAPI is an open-source Python library that enables automated API integration testing and live documentation using declarative specifications. Distributed via PyPI and actively maintained, the project has been adopted by developers across different contexts and was recognized by GitHub as part of initiatives focused on securing the open source supply chain.

Rather than focusing on abstract best practices, this talk dives into concrete engineering decisions made while designing and maintaining the library.

What we will cover:

1. Designing a Python Library for Growth

- How the codebase is structured to separate configuration, execution, and reporting
- Organizing modules and public APIs to remain stable over time
- Packaging decisions and CLI design for ease of use

2. Using Python Features Effectively

- Configuration-driven workflows with YAML and JSON
- Validation, error handling, and predictable failures
- Type hints and interfaces to improve readability and contributor confidence

3. Automation as a First-Class Concern

- Continuous integration with GitHub Actions
- Unit and integration testing strategies
- Automated releases, versioning, and dependency management

4. Developer Experience and Adoption

- Documentation and live reports as part of the product, not an afterthought
- Lowering the barrier for new users and contributors
- Tooling choices that reduce cognitive load

5. Community and Sustainability

- Contribution guidelines and governance models
- How open collaboration scales better than individual ownership
- The role of the Cumbuca Dev open source community in sustaining the project

By the end of the talk, attendees will have a clear mental model for designing Python libraries that can scale technically and socially. The lessons shared are applicable to anyone maintaining or planning to publish Python libraries, whether in personal projects, companies, or community-driven initiatives.

**Links**:

- [Canva link](https://canva.link/696vllybljnpl4c)
- [SpeakerDeck PDF file](https://speakerdeck.com/cumbucadev/2026-pycon-de-designing-and-scaling-a-python-library-in-the-open-architecture-automation-and-community)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/VBPRQR/>

## 122. [Increase productivity of CNC-machining of aerospace engine parts with Python](https://pretalx.com/pyconde-pydata-2026/talk/FJQXEQ/)

**Speakers**: [Nico Buhl](https://pretalx.com/pyconde-pydata-2026/speaker/APWPGK/)

**When and where**: Thursday, 2026-04-16, 13:20–13:50, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Increasing unit labour costs and the imperative need to reduce energy consumption raises the necessity to enhance productivity in industrial production. Python is an excellent tool for GKN Aerospace, as the world’s leading tier one aerospace supplier, to address the needs for higher utilization and unmanned operation on the shopfloor on its site in Kongsberg, Norway.

As an example, the presentation shares insight into the in-house developed “Production Execution System”, consisting of a Python backend and a REACT frontend. The application orchestrates all necessary data on cell-level, like NC-programs and additional digital services of the company’s IT environment during unmanned production. Furthermore, it supports the operator with necessary information to ensure highest quality of engine parts in a work environment of increasing digitalization and workload.

**Description** (verbatim):

Python is not exclusively a powerful tool for datascience and web-development. It gains in importance on the shopfloor in industrial production, too. Increasing unit labour costs and the imperative need to reduce energy consumption raises the need to enhance productivity in industrial production in general.

For GKN Aerospace, as the world’s leading tier one aerospace supplier of systems and components, this leads to higher utilization and unmanned operation of a high variety of production processes and CNC-machining tools. On its site in Kongsberg, Norway, GKN produces mainly turbine shafts and casings for civil and military engines, which are used for up to 100.000 flights every day around the globe.

The programming language Python enables fast and forward-thinking development of powerful applications which supports the operators and increases the degree of automation in the next years by concurrent assurance to fulfill demanding quality requirements and to cope the workload.

Standardization of applications is a key factor for increasing robustness of the automated production and reduce maintenance effort. Therefore a standardized interface to NC-controller and PLC’s from the “pre ASCII era” in the 70ies to up-to-date systems had to be found and suitable gateway services had to be developed.

As an example for the usage of Python on the GKN shopfloor in Norway, a standardized in-house developed “Production Execution System”, consisting of a Python backend and a REACT frontend is presented. Connected to more than 25 different machining tools on the shopfloor and additional digital services of the company’s IT environment, the application orchestrates all necessary data on cell-level. It provides data, like NC-programs and part meta-data to the machining tools and additional process information to the operators, necessary to produce a high variety of different engine components.

It enables unmanned production by selecting the next part for machining and commanding part changes to the machine to maximize utilization of the means of production. Furthermore, it reports back collected data for usage by other processes downstream in production.

Cloud-based and due to its restart capability in running production, bugfixes and implementation of new features can be carried out “on-the-fly”. Thereby automated unit- and integration testing for the core functionalities ensure robustness for the high variety of used machining tools.

The development and usage of the “Production Execution System” on GKN Aerospace’s shopfloor are an excellent example for the increasing importance of the programming language Python to ensures highest quality of engine parts in a work environment of increasing digitalization and workload.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/FJQXEQ/>

## 123. [Making bad CLIs fun with Small Language Models](https://pretalx.com/pyconde-pydata-2026/talk/GMNE3E/)

**Speakers**: [Moritz Bauer](https://pretalx.com/pyconde-pydata-2026/speaker/UUVSCB/)

**When and where**: Thursday, 2026-04-16, 14:00–14:30, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Command Line Interfaces (CLIs) offer an efficient and powerful way to interact with software, but poorly designed interfaces can be incredibly frustrating. Complicated parameter names and unconventional formats can turn using a great tool into a burdensome experience.

Large Language Models (LLMs) seem like a great solution to this problem as they can easily add a natural-language interface to any CLI. However, LLMs can introduce their own challenges, such as requiring API keys or high-performance GPUs. In this talk, I'll demonstrate a method for creating natural-language interfaces for any CLI using fine-tuned Small Language Models. These models are lightweight enough to be run directly on laptops or even smartphones.

We'll explore the process of generating synthetic data, fine-tuning models, and evaluating their performance using both an in-house CLI and a well-known open-source package as examples.

**Description** (verbatim):

I've often had to rely on a poorly designed home-grown CLI, leading to frustration due to constantly forgetting argument names and allowable values. While Large Language Models (LLMs) initially appeared to be an ideal fix, their limitations quickly became evident, suggesting the need for a more efficient approach.

To begin, we'll have a look at what makes CLIs hard to use and articulate why LLMs fall short in addressing them. Following this, we'll examine the process of generating synthetic data tailored for any CLI, whether it's proprietary or open-source. Then, I'll show you how to use this synthetic dataset to fine-tune a Small Language Model on your laptop or in the cloud. We will use the smallest variant of Google's Gemma 3 models, which boasts a lean 270 million parameters, to transform natural language instructions into actionable CLI commands.

Lastly, I'll share benchmark results to illustrate that these models can operate smoothly on various machines without needing API keys or GPUs, showcasing their robust capability and practical deployment potential.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GMNE3E/>

## 124. [AI Evals Done Right: From Vibes to Confident Decisions](https://pretalx.com/pyconde-pydata-2026/talk/MQJVFU/)

**Speakers**: [Martin Seeler](https://pretalx.com/pyconde-pydata-2026/speaker/9FLCR9/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyData: Generative AI & Synthetic Data — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Testing traditional software is "simple"... same input, same output. LLMs? Not so much. Same prompt, different result every time. So how do you actually know if your AI product is good?

Most teams struggle with this. Generic metrics like "Helpfulness: 4.2" sound scientific but don't drive real decisions. And when a new model releases, it's weeks of debates instead of data.

This talk introduces Error Analysis: a methodology to discover the concrete failure modes of your AI product and turn them into measurable evals. You'll learn how to build a failure taxonomy that enables real prioritization. Which issues are critical? Which are frequent? What should developers fix next, and how do you measure success?

The payoff: A real quality number for stakeholders. Concrete improvement tasks for developers. And when a new model drops, a ship-or-skip decision within 24 hours based on actual data.

Expect a meme-powered walkthrough, real-world examples from production, and a clear path to implement this yourself starting with just 20 traces.

**Description** (verbatim):

Testing traditional software is "simple"... same input, same output. LLMs? Not so much. Same prompt, different result every time. So how do you actually know if your AI product is good?

Spoiler: Most teams don't. They ship on vibes and hope for the best.

This talk takes you through our real journey at Blue Yonder, where we built an LLM-powered analytics system and needed a way to actually measure its quality. You'll see how we went from "feels okay-ish" to concrete numbers that let us make real decisions - with actual examples from production along the way.

The methodology is called Error Analysis: collect traces, annotate them from the user's perspective, group similar issues into failure modes, and turn those into automated evals. Along the way, we'll share practical best practices like why binary Pass/Fail beats rating scales, and why 100% pass rate means your evals are broken.

The payoff? When a new model drops, we run our pipeline and know within hours - not weeks - whether it's better or worse for our specific use case. Real percentages. Real trade-offs. Real decisions.

Expect a meme-powered walkthrough and a clear path to implement this yourself starting with just 20 traces.

Outline:

- Introduction: The challenge of testing stochastic systems, why we needed a better approach
- Collecting and Annotating Traces: Every trace is a user experiencing your product, Open Coding from the user perspective, real examples of failure modes we discovered
- Building the Failure Taxonomy: Grouping observations into categories, Axial Coding, turning scattered comments into actionable failure modes
- Writing Evals That Work: LLM-as-judge setup, binary scores vs rating scales, validating against human judgment
- From Vibes to Decisions: Prioritizing what to fix, measuring improvement, 24-hour model benchmarking
- Wrap-up: Your action plan, start with 20 traces

Source: <https://pretalx.com/pyconde-pydata-2026/talk/MQJVFU/>

## 125. [Restaurants around train stations are bad and I can prove it](https://pretalx.com/pyconde-pydata-2026/talk/NAHX3L/)

**Speakers**: [Dennis Schulz](https://pretalx.com/pyconde-pydata-2026/speaker/GKF8H3/)

**When and where**: Thursday, 2026-04-16, 15:45–16:15, room Platinum [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Have you ever asked yourself: Why is there no good food option close to this main station? This talk tries to find out if this is a systematic problem - using publicly available data and Google APIs.

After this talk, you will know about the best- and worst-rated restaurants close to main stations in Germany, if kebabs or pizza places are systematically a better choice, and which station is the worst to eat in all of Germany.

**Description** (verbatim):

Does the quality of restaurants degrade with your proximity to a train station? And which German town is worst for the hungry traveller? In this culinary data exploration, we used publicly accessible data to assess whether busy train stations correlate with lower restaurant ratings - and which towns are actually the worst. Using the Google Maps API and the hottest framework for data manipulation, polars, we give an overview over publicly available data resources and show how far you can get with them.

Of course, this talk will also deliver all the cold hard food facts: Analyzing the data of over 10,000 restaurants in Germany and worldwide, we will present the best and worst dining options available at train stations. We compare urban and rural environments, examine the impact of chain stores, and provide practical advice for you, the hungry traveler.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/NAHX3L/>

## 126. [Don’t call your LLM too often! How to build your dialog graph with confidence and sleep at night.](https://pretalx.com/pyconde-pydata-2026/talk/EWZMJK/)

**Speakers**: [Evgeniya Ovchinnikova](https://pretalx.com/pyconde-pydata-2026/speaker/DNKUXX/), [Andrei Beliankou](https://pretalx.com/pyconde-pydata-2026/speaker/NYYQSC/)

**When and where**: Thursday, 2026-04-16, 10:15–10:45, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Keywords: **Explainable AI, enhanced RAG, GraphRAG, LLMOps, dialog system evaluation.**

Designing reliable dialog flows for LLM-based systems remains challenging once conversations require branching, correction, or multi-step reasoning. Dialog graphs often evolve organically and accumulate structural issues: endless correction loops, dead subpaths, redundant validation steps, overly generic catch-all branches, or linear sequences that should be collapsed. Such phenomena raise operational costs, significantly increase TTFT and make the system answer less predictable and explainable.

Many solutions try to introduce an all-fit generalized RAG retrieval solution. Contrary to this, we present our empirical learnings on how to enhance system speed, lower overall costs and offer a better dialog graph explainability through enhanced LLM call tracing and iterative enhancements for common dialog paths.

We also show that more elaborated knowledge retrieval strategies like GraphRAG may drastically enhance overall response quality and shorten the dialog graph. We evaluate several approaches and give recommendations on how to leverage more complex document indexing phases for inference time benefits.

Overall, the session argues that scalable conversational systems require not only better prompts, but explicit graph structures paired with rigorous tracing and data-driven optimization.

**Description** (verbatim):

Building reliable dialog flows for LLM-based conversational systems remains difficult once interactions move beyond linear question–answer patterns. While early prototypes often rely on prompt chains, real-world systems quickly require branching, correction, clarification, and multi-step reasoning. At this stage, dialog logic implicitly turns into a graph, yet is still implemented and reasoned about as a sequence. This mismatch leads to structural problems that are hard to detect without explicit modeling and observability.

Complex document retrieval systems are not born out of theoretical itch. We’ll exemplify practical problems framing them around the following practical use case from the area of electricity/power production.

_Use Case: Aladdin and the Case of the Almost-Exploding Power Plant_

Rick and Morty are operations engineers at a large electrical power plant. Every single day, they face the same heroic challenge: too many documents, too little clarity.

The technical staff produces a constant stream of operational reports: free-text summaries describing the health and performance of steam generators. These reports are rich in knowledge, but poor in structure. Rick’s daily ritual is to read, compare, and summarize them, trying to predict which units will soon need maintenance. If he gets it right, the plant saves money by avoiding unnecessary service routines which are prescribed by regular maintenance guidelines. If he gets it wrong… well, let’s just say steam generators have a dramatic way of expressing dissatisfaction.

But unstructured reports are only one part of the story. Alongside them exists a well-behaved, structured world: databases containing results of regular, non-invasive ultrasonic inspections of pipelines, used to track corrosion development over time. Morty has built a quantitative model that predicts the probability (and timing out of this probability) of a pipeline rupture based on these corrosion measurements.

Naturally, Rick and Morty want everything. They want one system that can: 1) Understand messy human-written reports, 2) Reason over numerical corrosion models, and 2) Answer simple document questions without investing into unnecessary intelligence.

Thus, the system Aladdin is born.

Aladdin combines three very different subsystems:

- An agentic indexing component, which dynamically builds a search index for a GraphRAG over heterogeneous documents, given a pre-defined graph structure.
- An autonomous analytical agent, which evaluates pipeline failure probabilities using Morty’s quantitative corrosion model.
- A lightweight text-based RAG, backed by a vector index, for fast and simple document retrieval.

But what is the challenge? Once these components start talking to each other, the dialog graph becomes unpredictable. Execution paths depend heavily on what information is actually present in the documents. And this is something that cannot be fully reasoned about in advance. Loops appear, branches explode, and theoretically “clean” dialog designs fail in practice.

This use case illustrates why observability, tracing, and empirical optimization of dialog graphs are essential when building real-world document retrieval systems for industrial environments. Especially when Rick just wants a straight answer and Morty really doesn’t want another pipeline incident on his watch.

Given this use case we will exemplify several structural pathologic cases in the dialog graph which we observed in the practice and for which we found curative approaches.

**Non-ending loops in the dialog graph**
A frequent failure mode is the emergence of endless circular dialog graphs. Typical examples include:

- correction loops (“Please rephrase your input” → user rephrases → validation fails again → same prompt),
- clarification cycles (“What do you mean by X?” → partial answer → same clarification),
- fallback loops where a generic catch-all path routes the conversation back to an earlier state without introducing new information.

Such cycles are rarely intentional; they arise from local fixes applied over time and are difficult to identify by prompt inspection alone. In production, they manifest as stalled conversations, increased latency, rising token costs, and user frustration.

Beyond circularity, several other structural pathologies commonly appear in document retrieval systems.

**Dead subpaths after non-matching branching conditions**

Dialog graphs often include branches guarded by semantic or data-dependent conditions, but changes in document structure, embeddings, or preprocessing can make these conditions unsatisfiable, creating dead subpaths that are never executed. These paths are dangerous because they give a false sense of coverage, increase maintenance and reasoning complexity, and in production often manifest as mysterious fallback behavior where the system always takes a default route instead of a specialized one.

**Redundant validation and re-validation steps**

Another common issue is redundant validation, where the same or equivalent checks are performed multiple times along a single dialog path. This often happens when validation logic is added defensively at multiple layers: once at input parsing, again before retrieval, and again before response generation. While each validation step may seem harmless in isolation, their combination leads to inflated dialog depth, unnecessary latency, and increased cognitive load when analyzing traces. Worse, slight inconsistencies between validation prompts can produce contradictory outcomes, for example, an input being accepted in one step and rejected in the next.

**Overly generic catch-all branches**

Catch-all branches are often introduced as a safety mechanism: a “default” path that handles unexpected input or retrieval failure. Over time, however, these branches tend to grow in scope and responsibility, eventually becoming overly generic handlers that do everything. Such branches blur the distinction between genuinely exceptional situations and routine cases. As more logic is added to the catch-all path, it becomes harder to reason about what the system is actually responding to. Specialized logic may be silently bypassed, while unrelated scenarios are forced through the same generic response strategy.

**Linear sequences that should be collapsed**

Many dialog graphs contain long linear chains of nodes with no branching, no state changes, and no observable side effects between steps. These sequences often originate from iterative prompt development, where small transformations are added one by one (“extract entities” → “normalize entities” → “rephrase query” → “check relevance”). While conceptually clean, such linear chains are rarely optimal. They increase token usage, latency, and the number of failure points, without adding expressive power. More importantly, they obscure the true logical structure of the system: what could be a single semantic transformation is spread across multiple opaque steps.

An additional aspect of an overcomplicated dialog graph - especially baked by an autonomous agent - are barely predictable costs. Autonomous parts of the system need a very tight observability net to stay under control and not to burst cost prediction by an order of magnitude.

Working within a specifically regulated environment of a power plant posts additional restrictions on the explainability of the results. Every fact must be trackable to the source of the information and model hallucinations must be recognized in the very early step.

All the above requirements result in a setup which is heavily based on an LLM Operating Platform like Langfuse.

When combined with dialog-oriented orchestration frameworks such as Langflow, experiment tracking extends from single calls to full conversational trajectories. Complete dialog traces expose path stability, node utilization, dead branches, fallback prevalence, and user-facing metrics such as turns to resolution or correction-loop repetition.

Over time, this empirical evidence replaces design-time assumptions. Dialog paths are merged or removed based on observed execution rather than theoretical intent, with unreachable branches, redundant validations, and unstable loops revealed directly through trace analysis. Dialog graph optimization thus becomes a continuous, reproducible process grounded in measured behavior.

This talk proposes an engineering-oriented approach that models conversational logic as explicit dialog graphs and treats execution traces as first-class data. Using Langfuse instrumentation, developers can analyze concrete execution paths—branch frequency, loop formation, latency hotspots—and compare alternative graph designs through aggregated metrics and A/B testing, enabling systematic optimization based on evidence rather than intuition.

**To sum up:** using concrete production-oriented examples, the talk shows how graph-based dialog design improves multi-step retrieval, explainability, and robustness across languages. Endless correction loops are detected and eliminated, dead branches are pruned, and overly generic catch-all paths are replaced with targeted recovery strategies. The overall message is that scalable conversational systems require not just better prompts or larger models, but explicit dialog graphs combined with rigorous tracing and data-driven optimization.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/EWZMJK/>

## 127. [Vibe NLP for Applied NLP](https://pretalx.com/pyconde-pydata-2026/talk/AWMRFD/)

**Speakers**: [Ines Montani](https://pretalx.com/pyconde-pydata-2026/speaker/FZKG9N/)

**When and where**: Thursday, 2026-04-16, 10:55–11:25, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

One of the hardest parts of applied NLP has always been breaking down complex business problems into machine learning components. It's so hard because it requires domain expertise and reasoning about the specific use case, and it's the one thing technology couldn't fix. But what if we could take some of the learnings from AI-powered coding assistants and apply them to solving real-world NLP problems? In this talk, I'll show how we've built powerful assistants and tools to help developers solve NLP tasks using open-source software, and create modular solutions that are small, fast and fully data-private.

**Description** (verbatim):

One of the hardest parts of applied NLP has always been breaking down complex business problems into machine learning components. It's so hard because it requires domain expertise and reasoning about the specific use case, and it's the one thing technology couldn't fix. But what if we could take some of the learnings from AI-powered coding assistants and apply them to solving real-world NLP problems? In this talk, I'll show how we've built powerful assistants and tools to help developers solve NLP tasks using open-source software, and create modular solutions that are small, fast and fully data-private.

At the core of it is an often overlooked idea: using LLMs to _build systems_ instead of _as systems_. AI-powered coding assistants have transformed the way we build software – and they can be even more impactful for AI development itself and bridge the experience gap that's often holding teams back and causing projects to fail. In the talk, I will show you a new way of using generative models for AI development, and some practical examples of how to make "Vibe NLP" work for real-world problems

**Links**:

- [Slides](https://speakerdeck.com/inesmontani/vibe-nlp-for-applied-nlp)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AWMRFD/>

## 128. [From Row-Wise to Columnar: Speeding Up PySpark UDFs with Arrow and Polars](https://pretalx.com/pyconde-pydata-2026/talk/FT7V39/)

**Speakers**: [Aimilios Tsouvelekakis](https://pretalx.com/pyconde-pydata-2026/speaker/CD8CLV/)

**When and where**: Thursday, 2026-04-16, 11:35–12:20, room Europium [3rd Floor]

**Type**: Talk (long) — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python UDFs often become the slowest part of PySpark pipelines because they run row-by-row and pay a high cost crossing the JVM↔Python boundary. Spark’s Arrow-backed execution changes that cost model by moving data in columnar batches, which can reduce overhead and enable efficient, vectorized processing in Python.

In this session, we’ll cover practical patterns for writing Arrow-friendly UDF logic and integrating it with fast Python execution engines that operate on Arrow data. We’ll compare common approaches—scalar UDFs, Pandas UDFs, Arrow-native UDFs, and table-shaped Arrow transforms—then translate the results into a decision guide you can apply to production pipelines. Attendees will leave knowing when Arrow helps, when it doesn’t, and how to design UDF-heavy transformations that scale.

**Description** (verbatim):

Objective
Demonstrate how to accelerate UDF-heavy PySpark workloads by switching from row-wise execution to Arrow-backed columnar execution, using Polars for fast, maintainable column transformations and table transformations.

Key Takeways

- How Arrow is being used in PySpark for batched, columnar data exchange
- Why Polars helps: a higher-level DataFrame API plus Arrow interoperability that can often reuse Arrow buffers
- How to design fast column transformations (column in → column out) and fast table transformations (batch/table in → batch/table out).
- Benchmarks and tradeoffs across scalar UDFs, Pandas UDFs, Arrow-native UDFs, and Polars-based Arrow table transforms on real-world examples.

Audience

- Data engineers and data scientists working with PySpark at scale
- Engineers seeking concrete strategies to optimize spark pipelines that rely on Python UDFs

Knowledge Expected

- Familiarity with PySpark DataFrames and UDFs
- Basic understanding of Spark execution helps but is not required
- Exposure to Polars/Arrow is not required but might be beneficial

Source: <https://pretalx.com/pyconde-pydata-2026/talk/FT7V39/>

## 129. [Simplicity Scales: Rewriting to a Django Monolith and Monorepo](https://pretalx.com/pyconde-pydata-2026/talk/AAY8KQ/)

**Speakers**: [Bruno Vollmer](https://pretalx.com/pyconde-pydata-2026/speaker/LCXWWK/)

**When and where**: Thursday, 2026-04-16, 13:20–13:50, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Simplicity scales better than complexity. In this talk we share what we learned from a year-long refactor of our Python-based infrastructure where we majorly improved developer velocity and overall developer happiness with two choices: moving everything into a monorepo and replacing our microservices architecture with a Django monolith.
Instead of going deep on any single technology, we offer a holistic view of how these decisions enabled a multi-disciplinary team to move faster on a shared codebase. We'll introduce a blueprint for a uv-based Python monorepo, discuss why we chose "boring" tools over custom solutions, and share the metrics we used to measure success. The metrics dashboard will be open-sourced as part of this talk.

**Description** (verbatim):

When working on older codebases most developers encounter the question of "Should we fix this or rewrite it completely?". Weeklong releases, multi-day bug hunts and a very obvious impact of tech debt on developer happiness and development velocity led us to ask that question in a very general way. We were wondering how a better approach to a Python-based infrastructure could look when working in a multi-disciplinary startup environment. We believe that many developers have been in a similar situation and we would like to introduce our holistic take on a when and how to refactor older codebases.

Our solution to these problems consists of two main changes: moving the entire code of various teams in a uv-based monorepo and questioning a lot of technical decisions of the past under the paradigm of "Can this be done simpler or can we rephrase the problem to solve it with an existing technical solution?". We will share our insights into how a multi-language monorepo approach can work at a startup where full-stack and ML practitioners work on the same code base. This includes going over standardized procedures (e.g. code quality) that are shared between all teams.

Furthermore we will discuss some of the high-level decisions and introduce our reasoning within the available options of the python ecosystem. This includes for example why for us a monolithic approach based on Django works better than a Flask based microservice solution.

The goal of this talk is to give the listener an introduction to our solutions and make it easy to draw parallels to their own situation or problems. Attendees will leave with an insight into our decision framework and we will show what metrics we used to validate the success of our refactoring and technical choices.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/AAY8KQ/>

## 130. [Using Sensor Fusion and ML to Navigate Underground When GPS Fails](https://pretalx.com/pyconde-pydata-2026/talk/LVJXK3/)

**Speakers**: [Étienne Tremblay](https://pretalx.com/pyconde-pydata-2026/speaker/QXFCVA/)

**When and where**: Thursday, 2026-04-16, 14:00–14:30, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

In the twisting vaults of a subway, metro, or U-Bahn, there’s often no reliable cell service, wifi, or GPS. Which means riders had no good way of keeping track of their stops or ETA when underground.
After collecting extensive ground truth data, we trained a motion classifier using the phone's accelerometer to identify a moving train. This prediction is fed into a location model that combines it with the train schedule to estimate a location, even when GPS fails. We cover our unique data pipeline, feature engineering, and the optimization for high-scale, offline edge deployment to millions of users.

**Description** (verbatim):

In the twisting vaults of a subway, metro, or U-Bahn, there’s often no reliable cell service, wifi, or GPS. Which means riders had no good way of keeping track of their stops or ETA when underground.
After collecting extensive ground truth data, we trained a motion classifier using the phone's accelerometer to identify a moving train. This prediction is fed into a location model that combines it with the train schedule to estimate a location, even when GPS fails. We cover our unique data pipeline, feature engineering, and the optimization for high-scale, offline edge deployment to millions of users.

Attendees will gain from the lessons learned developing a sensor fusion ML system for offline use in smartphones

##### Data Collection & Annotation

Strategies for gathering high-quality, labeled "ground truth", especially in cases where the labels can't be inferred by human annotators after the fact

##### The ML Pipeline

Hyperparameter tuning of a convolutional neural network (CNN)
Building a multi-stage training regimen, to leverage different datasets

##### UX

Presenting predictions to users in a way that expresses uncertainty when necessary, and inspires confidence when justified. We want users to forget GPS doesn't work underground.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/LVJXK3/>

## 131. [Is my AI Recruiting biased? - How to evaluate these systems](https://pretalx.com/pyconde-pydata-2026/talk/3C9P9V/)

**Speakers**: [Sebastian Krauss](https://pretalx.com/pyconde-pydata-2026/speaker/SPBCU3/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Europium [3rd Floor]

**Type**: Talk — **Track**: General: Ethics & Privacy — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI recruiting systems are increasingly used to filter, rank, and select applicants at scale. Yet their deployment raises essential questions: How reliable are these models in real hiring environments, and how do we ensure fairness and safety across diverse applicant profiles? This talk presents a structured approach to testing and validating AI-driven recruiting pipelines. It highlights the role of synthetic test data, data augmentation, and fairness metrics in uncovering systemic risks and mitigating bias. Attendees will walk through a complete evaluation workflow. The session also incorporates insights from real-world testing practices, demonstrating how rigorous validation can increase trust and transparency in recruitment AI.

**Description** (verbatim):

AI recruiting systems are rapidly reshaping talent acquisition by automating candidate filtering, ranking, and selection. However, their growing influence raises critical concerns around fairness, robustness, and decision transparency. This talk introduces a practical testing methodology for evaluating AI recruiting pipelines beyond traditional accuracy metrics.

We will examine how synthetic data and augmentation techniques can expose hidden weaknesses, improve coverage, and stress-test edge cases. The talk will address the role of proxy variables, why they matter, and how they can help uncover unintended model behavior. We will also explore fairness measurement strategies, including individual and group fairness metrics, and discuss how these approaches reveal structural bias in ranking and scoring outcomes.

Because parts of the evaluation process can be automated, the session will demonstrate how Python-based agents and LLM “referees” can assist in generating and augmenting CVs and certificates, validating predictions, and assessing explanation quality. This automation can accelerate workflows, increase reproducibility, and reduce human error.

Participants will walk through a complete testing pipeline, supported by insights from real-world projects that illustrate how different tools and strategies expose systemic risks and guide mitigation. Attendees will leave with practical techniques to make recruiting systems more reliable, transparent, and trustworthy in real deployment contexts.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/3C9P9V/>

## 132. [Post-Processing and Visualization of Astrophysical Data with PyPLUTO](https://pretalx.com/pyconde-pydata-2026/talk/NN7CVP/)

**Speakers**: [Giancarlo Mattia](https://pretalx.com/pyconde-pydata-2026/speaker/YSUFD3/)

**When and where**: Thursday, 2026-04-16, 15:45–16:15, room Europium [3rd Floor]

**Type**: Talk — **Track**: PyData: Visualisation & Notebooks — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Modern scientific workflows increasingly rely on interactive analysis, reproducibility, and high-quality visualisation. **PyPLUTO** is a Python package designed to explore, analyse, and visualise numerical simulations produced by the **PLUTO** code for computational astrophysics. This talk shows how _PyPLUTO_ leverages the Python ecosystem to transform raw simulation outputs into clear, flexible analysis and visualization workflows.

The session demonstrates how domain-specific simulation data can be integrated with tools such as `NumPy` and `Matplotlib` to support efficient post-processing, rapid exploration, and production of publication-quality figures. Attendees will see how structured Python workflows can replace fragmented, ad-hoc scripts, how visualisation accelerates scientific insight, and how Python lowers the barrier between simulation output and interpretation.

Although examples are drawn from computational astrophysics, the approach is broadly applicable to any field working with structured simulation data. The talk highlights how lightweight, Python-based post-processing tools can improve clarity, reproducibility, and productivity without imposing heavy frameworks or tightly coupled visualisation pipelines.

**Description** (verbatim):

Numerical simulations often generate vast amounts of structured data; yet, extracting insights from these outputs remains a major challenge. Analysis is frequently performed through fragmented, ad-hoc scripts that are difficult to maintain, reuse, or reproduce. **PyPLUTO** is a Python package designed to address this gap by providing a clear and flexible interface for post-processing, analyzing, and visualizing simulation data produced by the **PLUTO** code for computational astrophysics.

This talk presents **PyPLUTO** as a case study in building lightweight, domain-specific scientific tools on top of the Python scientific ecosystem. The emphasis is on offline analysis and visualisation workflows that operate on completed simulation outputs, enabling efficient exploration, comparison, and communication of results. Rather than coupling visualisation to simulation runtime, **PyPLUTO** focuses on clarity, composability, and integration with established PyData libraries.

Through concrete examples, the session demonstrates how structured simulation data can be processed and visualised using tools such as NumPy and Matplotlib. Attendees will learn how Python-based workflows can replace scattered analysis scripts, how visualization supports rapid scientific insight, and how a clean separation between simulation and analysis enhances reproducibility and productivity.

## Outline

#### 1. **From Simulation Output to Insight**

- Common challenges in post-processing large numerical simulations
- The gap between raw data and scientific interpretation
- Why offline analysis and visualisation remain essential

#### 2. **PyPLUTO: Scope and Design**

- What PyPLUTO does and the problems it targets
- Design goals: simplicity, flexibility, and interoperability
- Clear separation between simulation execution and analysis

#### 3. **Working with Simulation Data**

- Loading and organising structured simulation outputs
- Handling scalar and vector fields across space and time
- Typical post-processing tasks and analysis patterns

#### 4. **Visualisation Workflows**

- Exploratory plots and diagnostic views
- Time evolution and comparison between simulations
- Producing publication-quality figures with Matplotlib

#### 5. **Interactive GUI for Post-Processing**

- Lightweight graphical interfaces for exploring simulation data
- Interactive selection of fields, slices, and time steps
- GUI as a complement to scripting, not a replacement

#### 6. **Integration with the Python Ecosystem**

- Efficient data handling with NumPy
- Interoperability with existing scientific Python tools
- Benefits of building on established libraries

#### 7. **Software Design Lessons**

- Building user-friendly scientific APIs
- Balancing usability, transparency, and performance

#### 8. **Broader Applicability and Outlook**

- Relevance to other simulation-heavy fields
- Reusable patterns for Python-based post-processing
- Future directions and potential extensions

The talk is aimed at scientists, data practitioners, and Python developers interested in scientific visualisation and simulation data analysis. No background in astrophysics or PLUTO is required; the focus is on workflows, tools, and design principles applicable across the PyData community.

**Links**:

- [Presentation (made with google slides)](https://docs.google.com/presentation/d/1XNoe_t-PG9tju9ib1VoB33cGj_IJZP8_SHU6lm4ZIRo/edit?usp=sharing)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/NN7CVP/>

## 133. [Schema-Driven Lambdaliths in Python with AWS Lambda Powertools and Pydantic](https://pretalx.com/pyconde-pydata-2026/talk/Q9HMT3/)

**Speakers**: [Tanio Toranosuke](https://pretalx.com/pyconde-pydata-2026/speaker/SF3WYV/), [Haruto Mori](https://pretalx.com/pyconde-pydata-2026/speaker/N9LBTH/)

**When and where**: Thursday, 2026-04-16, 10:55–11:25, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Django & Web — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Modern web frameworks such as Hono have renewed interest in schema-driven development and the “Lambdalith” architecture, where an application is delivered as a single AWS Lambda function. While this model provides a predictable developer experience, Python-based serverless systems often struggle to achieve the same consistency, validation, and maintainability in production.

Deploying Python web frameworks to AWS Lambda frequently requires additional execution layers—such as ASGI adapters or container-based runtimes—which add complexity and blur data boundaries. For teams that prefer clear, minimal Lambda handlers, these abstractions can hinder both development and operations.

This session shares production-proven patterns for building schema-driven Lambdalith applications in Python using AWS Lambda Powertools and Pydantic, without relying on heavy framework abstractions. Through real-world examples, we show how these tools simplify handler logic, standardize request and response validation, and improve observability and error handling.

Attendees will leave with practical techniques for building reliable and maintainable Python Lambdalith systems, and insights they can immediately apply to modernizing existing serverless codebases or delivering new production services with confidence.

**Description** (verbatim):

The rise of modern web frameworks such as Hono has brought increased attention to schema-driven development and the “Lambdalith” architecture, where an application is delivered through a single Lambda function. These approaches offer a highly streamlined developer experience, but many existing Python-based systems struggle to achieve the same level of consistency, validation, and maintainability.

In Python, closing this gap often means introducing additional execution layers outside the language itself. When frameworks designed around web servers and request lifecycles are deployed on AWS Lambda, they typically require ASGI adapters, web adapters, or container-based runtimes. While powerful, these layers can make it harder to focus on what many teams actually want: writing clear, minimal Python handlers with explicit data boundaries.

This talk explores how combining AWS Lambda Powertools and Pydantic can close that gap and enable a modern, predictable development workflow—even in established Python ecosystems. Drawing from real-world product use cases, we will examine how these tools can simplify handler-level logic, standardize request and response validation, and improve observability and error handling.

Lambda Powertools provides far more than logging and metrics: it includes utilities for structured tracing, data parsing, idempotency, typed configuration, and other features that bring Python serverless development closer to the ergonomics of newer frameworks. When paired with Pydantic, developers can enforce clear data contracts, reduce boilerplate, and achieve stronger guarantees around application behavior.

Attendees will learn practical patterns for improving quality and productivity in Lambda-based applications, including how to:

- Validate event payloads and responses using Pydantic models
- Implement consistent error handling strategies
- Structure a Lambdalith-style architecture in Python
- Leverage Powertools utilities to enhance reliability and developer experience

This session will be valuable for Python developers who want to apply schema-driven design principles, modernize existing serverless codebases, or build more maintainable Lambda applications with confidence.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/Q9HMT3/>

## 134. [When LLMs Are Too Big: Building Cost-Efficient High-Throughput ML Systems for E-Commerce Cataloging](https://pretalx.com/pyconde-pydata-2026/talk/GAUNKM/)

**Speakers**: [Tobias Senst](https://pretalx.com/pyconde-pydata-2026/speaker/UXME8R/), [Bastian Wandt](https://pretalx.com/pyconde-pydata-2026/speaker/LGQXA9/)

**When and where**: Thursday, 2026-04-16, 11:35–12:20, room Palladium [2nd Floor]

**Type**: Talk (long) — **Track**: PyCon: MLOps & DevOps — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

E-commerce cataloging at idealo operates at extreme scale: 4.5 billion offers from 50,000+ shops across six countries, with peak ingestion rates of 4.8 million offers per minute. While large language models (LLMs) provide strong classification accuracy, they are too slow and costly for billion-scale real-time processing. This talk shows how idealo builds a cost-efficient, high-throughput machine learning system that leverages LLM knowledge without deploying full models in production.

We present how knowledge distillation from a large e5 instruction model enables a compact multilingual MiniLM encoder to achieve high accuracy, and how optimized inference runtimes and specialized hardware such as AWS Neuron help meet strict latency and cost requirements. Beyond modeling, we highlight key operational challenges: constructing training datasets from massively imbalanced data, selecting the right encoder architecture from today’s model landscape, and designing a robust MLOps lifecycle with automated data sampling, training, deployment, and monitoring.

Attendees will learn practical techniques for scaling ML systems under real-world constraints, how to extract value from LLMs when they are too large to serve directly, and how to transition research prototypes into reliable, high-volume production pipelines.

**Description** (verbatim):

## When LLMs Are Too Big: Building Cost-Efficient High-Throughput Machine Learning for Cataloging in E-Commerce

idealo.de offers a price comparison service for over 5.7 million products from a wide variety of over thousands of categories. It navigates a dynamic, constantly changing billion-scale landscape with **over 2 billion offers from 50,000+ shops in 6 countries**. Our central challenge is cataloging this huge amount of offers automatically at scale, with a peak throughput of **processing 4.8 million offers per minute.**

While modern large language models (LLMs) excel in such tasks, they do not scale well to huge amounts of data. To fulfill business needs, we need to strike a balance between processing speed and offer cataloging quality. By employing modern machine learning techniques to extract specialist knowledge from downscaled state-of-the-art LLMs and a multitude of performance enhancing techniques we speed up idealo’s processing while massively improving cataloging performance. This talk presents how these solutions find the balance between cost and performance and how they integrate into idealo’s offer cataloging pipelines.

### What makes this approach unique?

Our solution and practical experiences in the area of high-throughput classification are presented. This includes the operational aspects of our system, in particular the design of a stable and high-performance MLOps lifecycle integrated into our CI/CD and continuous Training pipelines. Where we automate continuous data sampling, model training, model deployments, and monitoring.

Concrete solutions and best practices are discussed that demonstrate how our model accuracy of the multilingual MiniLM transformer encoder model is improved through knowledge distillation by a large e5 instruction transformer. Additionally, we show how the integration of these models on specialized hardware like AWS Neuron enables strict runtime and latency requirements to be met in a cost-efficient manner.

In detail we will discuss the following topics:

- Machine Learning Operation Lifecyle for a high-throughput category classification system.
- Challenges when creating training and testing datasets from the huge amount of existing massively unbalanced data efficiently.
- Selecting the right model in presence of the current encoder language model zoo.
- Using knowledge distillation via student-teacher models to balance required compute and classification performance.
- Integrating quantization techniques for speed improvements.
- Selecting ideal compute instances for our production environment.
- How to compile the model on custom designed machine learning accelerators using the neuron package.

### Key takeaways for attendees:

- An overview of months of research and exploration for massive throughput environments including their practical integration in live systems.
- Modern machine learning systems in production, especially with billion-scale data, need to carefully balance business needs in terms of cost and quality.
- State-of-the-art LLMs are often not feasible for large-scale tasks. However, new machine learning techniques can extract their knowledge for specific applications.
- How to transition research findings to production.

The talk will be aligned along our tech stack, which includes PyTorch, PyTorch Lightning, Huggingface, AWS Sagemaker, AWS Neuron SDK, Grafana Loki, Docker and GitHub Actions.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GAUNKM/>

## 135. [Free T(h)r(e)ading: A Trading Systems Journey Beyond the GIL](https://pretalx.com/pyconde-pydata-2026/talk/NDZSSB/)

**Speakers**: [Tim Kreitner](https://pretalx.com/pyconde-pydata-2026/speaker/BPNG3K/)

**When and where**: Thursday, 2026-04-16, 13:20–13:50, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Python 3.13's free-threaded mode opens new territory for Python concurrency. We embarked on an experiment: could a trading algorithm benefit from true parallelism, and what would it take to get there? This talk documents our research journey from async/await to free threading—the hypotheses we tested, the benchmarks we designed, the unexpected behaviours we discovered, and the systematic approach we took to validating whether GIL-free Python could handle real-time market data. You'll see our experimental methodology, the data we collected, surprising findings about thread scheduling and memory patterns, and what our results suggest about Python's concurrent future.

**Description** (verbatim):

The release of Python 3.13 with experimental free-threaded mode (PEP 703) represents a fundamental shift in Python's concurrency model. For decades, the Global Interpreter Lock has dictated how we write concurrent Python code, pushing developers toward async/await patterns for I/O-bound workloads and multiprocessing for CPU-bound tasks. But what happens when we remove that constraint?

We designed a research experiment to answer this question empirically: take a production trading algorithm built on asyncio, migrate it to free threading, and measure everything. Trading systems make ideal subjects for this research—they're latency-sensitive, handle multiple concurrent data streams, perform both I/O and CPU-bound operations, and have clear, quantifiable performance metrics.

This talk presents our complete research journey, from initial hypothesis to validated conclusions, sharing both our methodology and findings.

Detailed Outline:

1. Research Question & Motivation (3 minutes)

The research question: can a trading algorithm benefit from true parallelism?
Why trading systems make ideal experimental subjects
Initial hypotheses about performance characteristics
Baseline system: async architecture and performance profile

2. Experimental Design (4 minutes)

Migration approach
Benchmarking framework
Workload simulation
Control variables and isolation of I/O vs. CPU-bound operations

3. Migration Journey (5 minutes)

Architectural transformation
Key refactoring patterns and synchronization strategies
Thread safety challenges
Library ecosystem compatibility findings

4. Results & Discoveries (8 minutes)

Performance data: latency, throughput, and resource utilization
Workload analysis: where free threading won, where async remained competitive
Visual data presentation: charts and comparative analysis

5. Practical Implications (4 minutes)

Decision framework: when to choose free threading over async
Migration best practices and lessons learned
Production readiness assessment
What this means for Python's concurrent future

6. Q&A (5 minutes)

Prerequisites - This talk assumes attendees have:

- Strong understanding of Python's concurrency models (asyncio, threading, multiprocessing)
- Familiarity with the GIL and its implications
- Basic understanding of systems programming concepts (thread safety, synchronization)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/NDZSSB/>

## 136. [Letting AI Move: Robotics Demos Powered by Python](https://pretalx.com/pyconde-pydata-2026/talk/VUHSG9/)

**Speakers**: [Larissa Haas](https://pretalx.com/pyconde-pydata-2026/speaker/HVSNHD/), [Annika Herbert](https://pretalx.com/pyconde-pydata-2026/speaker/HPJTAP/)

**When and where**: Thursday, 2026-04-16, 14:00–14:30, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyCon: Embedded Systems & Robotics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI is sometimes hard to explain, especially for people outside of tech. With robots, AI becomes visible and tangible. In this talk we want to show how we can use Python and the huggingface reachy mini as an example to make AI more concrete, interactive, and engaging for beginners and non-experts.

**Description** (verbatim):

Artificial intelligence can be difficult to explain, especially to people outside of tech. We often rely on slides, diagrams, or on-screen demos, but the real impact does not always stick. For people encountering AI for the first time—such as students or non-technical audiences—AI terminology and concepts can remain abstract and disconnected from real-world experience.

Robots can help change that. When AI controls a physical system, its behavior becomes visible, tangible, and easier to reason about. In this talk, we explore how Python and playful robotics experiments can be used to make AI more concrete, interactive, and engaging. Using the Hugging Face Reachy Mini robot as a case study, we show how physical interaction can turn abstract AI concepts into intuitive, memorable experiences.

The perspective of this talk is intentionally non-traditional: we started with no prior knowledge of robotics or mechanics and approached the problem purely from a Python developer’s point of view. This journey strongly shapes the talk. Rather than focusing on advanced robotics engineering, the emphasis is on accessibility, experimentation, and learning by doing. The goal is to show that robotics can be an approachable medium for explaining AI, even for people without a hardware or engineering background.

During the talk, we walk through basic building blocks such as movement, gestures, and simple interaction patterns, and show how AI-driven behavior can be layered on top of them using familiar Python tools. We share examples from real experiments and demos, including what worked well, what failed, and what we learned from unexpected behavior in live settings.

Importantly, this is not a product demo or a hardware-specific tutorial. While Reachy Mini is used as a concrete example, the focus is on transferable ideas and design patterns:

How physical interaction changes the way people perceive AI

How Python lowers the barrier to experimenting with robotics

How to design demos that invite curiosity rather than intimidation

How to make AI systems easier to explain in educational and outreach contexts

Attendees do not need access to a robot to benefit from this talk. The lessons and patterns discussed can be applied to a wide range of settings, including classrooms, workshops, meetups, and public demonstrations.

This talk is aimed at Python beginners and intermediate developers, especially educators and anyone who regularly needs to explain or demonstrate AI to others. Attendees will leave with new ideas, inspiration, and practical approaches for making AI more tangible, engaging, and human-centered.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/VUHSG9/>

## 137. [Is digital sovereignty a new buzzword in AI development?](https://pretalx.com/pyconde-pydata-2026/talk/QMBEZX/)

**Speakers**: [Dr. Maria Börner](https://pretalx.com/pyconde-pydata-2026/speaker/LT7LHM/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Palladium [2nd Floor]

**Type**: Talk — **Track**: General: Ethics & Privacy — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

AI development usually focuses on feasibility and implementation, but a new buzzword is now being used: 'sovereignty'. While customers are excited about it, what does it mean for them and for AI developers? In this presentation, we analyse different aspects of sovereignty and explore how it can be used to build trustworthy AI solutions.
We will also discuss current examples from politics and development to identify the best practices for secure data processing.

**Description** (verbatim):

AI development typically prioritises feasibility and implementation. While solutions should be efficient, high-performing and scalable, sovereignty and data security are often overlooked. These issues tend to be overlooked when solutions are being found, even though we don't use AI as an end in itself, but rather to benefit or support our customers. Customers operate within a regulatory framework and rely on responsible technology.
Rather than seeing regulation as a hindrance, we should view it as an opportunity to drive innovation and create sustainable, trustworthy solutions. However, this is only possible if we understand the full meaning of sovereignty.
This presentation will explore the various aspects of the term 'sovereignty' and its potential impact on AI projects. We will discuss current examples from politics and development to identify best practices for secure data processing.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/QMBEZX/>

## 138. [On Interventional Generalisation](https://pretalx.com/pyconde-pydata-2026/talk/BRRHGY/)

**Speakers**: [Andy Kitchen](https://pretalx.com/pyconde-pydata-2026/speaker/Y3GHEB/)

**When and where**: Thursday, 2026-04-16, 15:45–16:15, room Palladium [2nd Floor]

**Type**: Talk — **Track**: PyData: Machine Learning & Deep Learning & Statistics — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

If I do X instead of Y, will I get the outcome I want? What about in a new unseen situation? Making predictions alone is pointless, one wants to act in the world. Furthermore one must act in situations that are similar but different to all past experience. The real underlying goal of all decision making is really interventional generalisation: the ability to evaluate hypothetical choices in new unseen situations. Unfortunately data science and statistics has a inordinate focus on observation and statistical significance instead of intervention, counter-factuals and generalisation. Improve your modelling both practically and conceptually with the mental tools presented in this talk.

**Description** (verbatim):

If I do X instead of Y, will I get the outcome I want (in a novel situation)? Making predictions alone is pointless, one wants to act in the world. Furthermore one must act in situations that are similar but different to all past situations. The real underlying goal of all decision making is interventional generalisation: the ability to evaluate hypothetical choices in new unseen situations.

This talk covers this history and problems of null hypothesis significance testing, the benefits (and limitations) of Bayesian reasoning. Introduces the basics of Pearl-ian causality theory and its treatment of interventions and counter-factuals (things that hypothetically could have happened, but didn't), finally we discuss the next step, interventional generalisation, that is being able to compare the value of hypothetical interventions in new unseen situations. Decisively improve your modelling practically and conceptually with the mental tools in this talk.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/BRRHGY/>

## 139. [Building reliable data pipelines with polars and dataframely](https://pretalx.com/pyconde-pydata-2026/talk/GPJGH3/)

**Speakers**: [Oliver Borchert](https://pretalx.com/pyconde-pydata-2026/speaker/Y3BGJB/), [Andreas Albert](https://pretalx.com/pyconde-pydata-2026/speaker/D93SYG/)

**When and where**: Thursday, 2026-04-16, 10:15–11:45, room Ferrum [2nd Floor]

**Type**: Tutorial — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

If you have worked with real-world data before, you know that processing it can be challenging. Data often comes scattered across tables, in inconsistent encodings, with duplicated rows and is generally dirty. In this tutorial, you will learn how to process large amounts of data reliably and quickly using `polars` and `dataframely`.

What we love about `polars` is that it's easy to use, fast and elegant — it allows us to build and compose complex transformations with ease. On this basis, we built `dataframely`: a library for defining and validating contents of polars data frames. With `dataframely`, we can build pipelines without ever getting confused about what's in our data frames. We document and validate our expectations and assumptions clearly, which makes our pipeline code simpler and easier to understand. "Is this join correct?", and "where did this column come from?" are questions you will not have to worry about anymore.

In this tutorial, you will become familiar with `polars` basics by writing a simple pipeline: you will read data, transform it to make it ready for use, and you will learn how to do that fast. With `dataframely` schemas, you will upgrade your code from "it works" to "it's beautiful!", and along the way, `dataframely` will help you eliminate entire classes of bugs you will never have to think about again. After the tutorial, you will be all set to use these tools in your own work.

**Description** (verbatim):

**Note for attendees: Please check out the [git repository](https://github.com/Quantco/tutorial-pycon26-polars-dataframely) and follow the simple setup steps in the `README`, ideally before the tutorial.**

In this tutorial, you will become familiar with `polars` basics by writing a simple pipeline: you will read data, transform it to make it ready for use, and you will learn how to do that fast. With `dataframely` schemas, you will upgrade your code from "it works" to "it's beautiful!", and along the way, `dataframely` will help you eliminate entire classes of bugs you will never have to think about again. After the tutorial, you will be all set to use these tools in your own work.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GPJGH3/>

## 140. [pytest tips and tricks for a better testsuite](https://pretalx.com/pyconde-pydata-2026/talk/GCGLPN/)

**Speakers**: [Freya Bruhin](https://pretalx.com/pyconde-pydata-2026/speaker/BPA78X/)

**When and where**: Thursday, 2026-04-16, 13:10–14:40, room Ferrum [2nd Floor]

**Type**: Tutorial — **Track**: PyCon: Programming & Software Engineering & Testing — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

pytest lets you write simple tests fast - but also scales to very complex scenarios: Beyond the basics of no-boilerplate test functions, this training will show various intermediate/advanced features, as well as gems and tricks.

To attend this training, you should already be familiar with the pytest basics (e.g. writing test functions, parametrize, or what a fixture is) and want to learn how to take the next step to improve your test suites.

If you're already familiar with things like fixture caching scopes, autouse, or using the built-in `tmp_path`/`monkeypatch`/... fixtures: There will probably be some slides about concepts you already know, but there are also various little hidden tricks and gems I'll be showing.

**Description** (verbatim):

We'll cover things like:

- Recommended pytest settings for more strictness
- What's xfail and why is it useful?
- How to mark an entire test file or single parameters
- Ways to deal with parametrize IDs and syntax
- Useful built-in pytest fixtures
- Caching for fixtures
- Using fixtures implicitly
- Advanced fixture and parametrization topics
- How to customize fixtures behavior based on markers or custom CLI arguments
- If time permits: Short intro to writing pytest plugin and to property-based testing with Hypothesis

**To prepare, please clone the [GitHub repository](https://github.com/The-Compiler/pytest-tips-and-tricks) and follow the setup steps in the README.**

Source: <https://pretalx.com/pyconde-pydata-2026/talk/GCGLPN/>

## 141. [Foundation Models in Forecasting: Are We There Yet? Lessons from the Trenches](https://pretalx.com/pyconde-pydata-2026/talk/KQM8JJ/)

**Speakers**: [Dr. Irena Bojarovska](https://pretalx.com/pyconde-pydata-2026/speaker/UGLH8C/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Ferrum [2nd Floor]

**Type**: Talk — **Track**: PyData: Generative AI & Synthetic Data — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

The rise of time-series foundation models like Chronos-2 and TimesFM has sparked a debate: can a single pre-trained model replace the specialized "local" models we have tuned for years? We moved beyond the hype to test these models in production-like environments, from high-level market trends to granular article-level demand. In this talk, we share a transparent look at our journey: the zero-shot capabilities of these models, the reality of fine-tuning with exogenous business drivers, and a comparison between generative models and state-of-the-art classical methods. We categorize what is currently possible, what remains a challenge, and provide a roadmap for teams looking to integrate foundation models into their forecasting stack without sacrificing reliability.

**Description** (verbatim):

The landscape of time-series forecasting is undergoing a seismic shift. With the emergence of foundation models like Chronos 2 and TimesFM, the industry is at a crossroads: can a large-scale pre-trained model truly replace the specialized, "local" models that practitioners have spent years tuning?

In this talk, we move beyond theoretical benchmarks to provide a transparent look at testing time-series foundation models in production-like environments. We explore the transition from traditional statistical and machine learning methods to generative architectures, focusing on the practical challenges that arise when "zero-shot" capabilities meet the messy reality of business data.

### What you will learn:

- **The Foundation Model Landscape:** A high-level mapping of the current state-of-the-art and how these architectures differ from classical statistical and ML approaches.
- **Zero-Shot vs. Reality:** How pre-trained models handle domain-specific context and exogenous business drivers—such as promotions, seasonality, and market shocks—without explicit training.
- **The Operational Shift:** How moving toward foundation models changes the MLOps lifecycle,from data preparation to running inference at scale
- **Predictive Stability & Trust:** A framework for evaluating whether a model is "production-ready," focusing on forecast stability and consistency of predictions over time.
- **A Decision Roadmap:** A practical checklist for teams looking to integrate these models into their stack without sacrificing reliability.

Whether you are a data scientist looking to upgrade your forecasting pipeline or a lead evaluating the impact of Foundation Models on time-series workflows, this session offers a grounded, hype-free perspective from the front lines of implementation.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/KQM8JJ/>

## 142. [Your Data Is Leaking: A Hands-On Introduction to Differential Privacy with OpenDP](https://pretalx.com/pyconde-pydata-2026/talk/VJPQCR/)

**Speakers**: [Shlomi Hod](https://pretalx.com/pyconde-pydata-2026/speaker/USEYXD/), [Marcel Neunhoeffer](https://pretalx.com/pyconde-pydata-2026/speaker/8HYLHH/)

**When and where**: Thursday, 2026-04-16, 10:15–11:45, room Dynamicum [Ground Floor]

**Type**: Tutorial — **Track**: General: Ethics & Privacy — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Data analysis and machine learning often involve sensitive information. But how can we ensure that our analyses and releases do not inadvertently reveal information about the individuals in our data? Traditional approaches such as anonymization or releasing only aggregate statistics have repeatedly proven insufficient.

Differential privacy is a mathematical framework that offers provable privacy guarantees while still enabling useful data analysis. In this tutorial, we provide a hands-on introduction to differential privacy, covering key concepts relevant to understanding and applying it in practice. The focus will be on practical implementation rather than underlying theory.

Using interactive examples in Python, we will explore the core ideas of differential privacy, highlight its attractive properties and limitations, and demonstrate how to build privacy-preserving analyses using OpenDP, an open-source Python library for differential privacy. Participants will leave equipped to continue exploring differential privacy on their own. Familiarity with the basics of Python programming is helpful, but no prior knowledge of differential privacy is required.

**Description** (verbatim):

Aggregate statistics feel safe to release - just counts, means, and totals, no individual records. But a long history of privacy failures has shown otherwise. From the AOL search data leak to the Netflix Prize re-identification attack to LLM memorization, "anonymized" data has repeatedly revealed more than intended.

Differential privacy offers a different approach: a mathematical framework that quantifies and bounds the information any release reveals about any individual. It has moved from theory to practice in recent years, with deployments at the US Census, Wikimedia, Israel’s national birth registry, Google, Apple, Linkedin and more.

In this tutorial, we provide a hands-on introduction to differential privacy. We'll start by making the problem concrete - executing an attack on aggregate statistics - and then explore how differential privacy addresses it. The focus will be on practical implementation rather than underlying theory.

## What You'll Learn

1. Why traditional anonymization and aggregation fail to protect privacy
1. The core ideas of differential privacy: what it guarantees, what epsilon means, and when DP is a suitable solution
1. How to use OpenDP's building blocks
1. How to build differentially private data analyses using OpenDP's Polars integration
1. Where to go next: resources for AI/ML with DP, synthetic data, and further learning

## Tutorial Outline

### Part 1 - The Privacy Problem (20 minutes)

- Real-world privacy failures (such as AOL search data, Netflix Prize, LLM memorization)
- Hands-on: execute a reconstruction attack on aggregate statistics
- Discussion: why traditional approaches fail

### Part 2 - Introduction to Differential Privacy (20 minutes)

- Core ideas: masking the contribution of a single individual through calibrated noise; protection against membership inference attack
- Learning by doing: exploring DP with OpenDP's building blocks
- Tuning privacy protection with f-DP; the privacy-utility tradeoff
- Real-world deployments (such as US Census, Israel birth registry, LinkedIn API)

### Part 3 - Data Analysis with OpenDP (40 minutes)

- OpenDP fundamentals: domains, transformations, measurements, chaining
- Working with tabular data using OpenDP's Polars integration
- Building a complete DP data analysis pipeline
- Revisiting the attack: does it still work?

### Part 4 - What's Next (10 minutes)

- Beyond the basics: AI/ML with differential privacy, synthetic data generation
- Resources and community
- Q&A

## Prerequisites

- Python: Comfortable writing functions and working with notebooks
- Statistics: Basic familiarity with mean, counts, histograms
- Differential privacy: No prior knowledge required

## Materials

Participants will have access to interactive Jupyter notebooks with all code and exercises. Materials will be publicly available after the tutorial.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/VJPQCR/>

## 143. [Do you know how well your model is doing? Evaluate your LLMs](https://pretalx.com/pyconde-pydata-2026/talk/QX8DDJ/)

**Speakers**: [Cheuk Ting Ho](https://pretalx.com/pyconde-pydata-2026/speaker/8EGVC9/)

**When and where**: Thursday, 2026-04-16, 13:10–14:40, room Dynamicum [Ground Floor]

**Type**: Tutorial — **Track**: PyData: Natural Language Processing & Audio (incl. Generative AI NLP) — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

Large Language Models (LLMs) are becoming central to modern applications, yet effectively evaluating their performance remains a significant challenge. How do you objectively compare different models, benchmark the impact of fine-tuning, or ensure your LLM responses adhere to safety guidelines (guard-railing)? This hands-on workshop addresses these critical questions.

**Description** (verbatim):

We will begin with an essential revision of the Hugging Face Transformers library, covering basic LLM inference and fine-tuning. The core of the workshop will introduce and provide deep practice with Lighteval, an efficient and powerful LLM evaluation framework. Participants will learn how to leverage Lighteval to compare various LLMs available on the Hugging Face Hub using a range of pre-built tasks and metrics.

Finally, we will delve into advanced evaluation techniques, focusing on creating custom tasks and metrics tailored to unique, real-world application requirements. Participants will learn how to prepare custom datasets on the Hugging Face Hub and integrate them into Lighteval for precise, domain-specific evaluation. By the end of this workshop, you will possess the practical skills to rigorously evaluate, benchmark, and fine-tune your LLMs with confidence.

Prerequisites:

    - Have experience coding in Python (with Python installed in the local machine)
    - Basic understand of machine learning and LLMs
    - Experience with Hugging Face Transformers preferred but not necessary
    - A Hugging Face Hub account (sign up for free)
    - A modern computer that can fine-turn small LLMs locally

Preparation:

Clone and follow setup [here](https://github.com/Cheukting/lighteval-exercises/)

**Links**:

- [Slides](https://canva.link/lighteval-workshop)
- [Exercises](https://github.com/Cheukting/lighteval-exercises)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/QX8DDJ/>

## 144. [Zero-Copy or Zero-Speed? The hidden overhead of PySpark, Arrow & SynapseML for inference](https://pretalx.com/pyconde-pydata-2026/talk/TPNBRN/)

**Speakers**: [Petar Ilijevski](https://pretalx.com/pyconde-pydata-2026/speaker/JNR9GB/)

**When and where**: Thursday, 2026-04-16, 15:05–15:35, room Dynamicum [Ground Floor]

**Type**: Talk — **Track**: PyData: Data Handling & Data Engineering — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

"Zero-copy" data transfer promises free communication between Spark's JVM and Python workers, but at 6 billion rows daily, the reality is far more complex. This session explores the low-level mechanics of distributed inference, focusing on the serialization bottlenecks.

We will conduct an analysis of execution plans generated by `pandas_udf`, `mapInPandas`, and SynapseML. We visualize the true cost of pickling, Arrow record batching, and JNI context switching. Join this deep dive to understand the physics of distributed inference and learn how to tune `spark.sql.execution.arrow.maxRecordsPerBatch` to prevent OOMs without starving the CPU.

**Description** (verbatim):

This talk is a technical deep dive into the "physics" of distributed machine learning inference. While high-level APIs promise seamless integration between Spark (JVM) and Python, the underlying data transfer mechanisms often become the primary bottleneck for high-throughput systems. We start by reality-checking the "Zero-Copy" promise of Apache Arrow in a PySpark context, identifying exactly where the abstraction leaks and where "Zero-Copy" isn't actually free.

The session concludes with a focus on tuning for throughput. We will explore the delicate balance of configuring `spark.sql.execution.arrow.maxRecordsPerBatch`, demonstrating how to find the "Goldilocks" zone that maximizes CPU saturation without causing JVM off-heap memory crashes. Attendees will gain a deep understanding of the memory hierarchy involved in distributed inference and practical strategies for profiling serialization overhead in production.

Key Takeaways:

- Internals knowledge: Understand exactly how data moves from JVM heap to Python worker memory.
- Which method to use depending on your use-case
- Tuning skills: Learn how to configure Apache Arrow batch sizes to optimize CPU saturation.

Source: <https://pretalx.com/pyconde-pydata-2026/talk/TPNBRN/>

## 145. [Problem Clinic: Python in Regulated Environments --- What Works, What Doesn't](https://pretalx.com/pyconde-pydata-2026/talk/U7QDCH/)

**Speakers**: [Alexander CS Hendorf](https://pretalx.com/pyconde-pydata-2026/speaker/K9DZKF/)

**When and where**: Thursday, 2026-04-16, 10:15–11:15, room Lounge [1st Floor]

**Type**: Open Space — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pyconde-pydata-2026/schedule/export/schedule.json)):

_Open Space / Problem Clinic_

A moderated hour under Chatham House Rule with 20 practitioners from five regulated industries (banking, pharma, medical-product development, healthcare IT providers, critical infrastructure).

**Description** (verbatim):

A moderated hour under Chatham House Rule with 20 practitioners from five regulated industries (banking, pharma, medical-product development, healthcare IT providers, critical infrastructure).

The session covered the operational bottlenecks AI programmes inside regulated corporates actually run into in 2026: SBOM and sub-dependencies, model validation, the perception of open source, communication between engineering, QA and compliance, and the handling of AI-generated code in review.

The format ran deliberately without recording and without slides, so that participants could speak openly about the real bottlenecks their programmes face.

An extensive write-up of the discussion, distilled to three core bottlenecks (language, threshold, mandate) and concrete recommendations for decision-makers, is published as a blog post: [Regulated, Interconnected, Stalled: What's Blocking AI Projects in Five Industries](https://hendorf.com/en/blog/problem-clinic-pyconde-2026/).

**Links**:

- [Summary on Alexander CS Hendorf's blog](https://hendorf.com/en/blog/problem-clinic-pyconde-2026/)

Source: <https://pretalx.com/pyconde-pydata-2026/talk/U7QDCH/>
