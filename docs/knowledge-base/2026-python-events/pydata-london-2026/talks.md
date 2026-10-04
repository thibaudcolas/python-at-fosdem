# PyData London 2026 talks

Collected from the official PyData London 2026 schedule via its Pretalx frab JSON export at <https://pretalx.com/pydata-london-2026/schedule/export/schedule.json> (schedule version **0.33, a draft revision**, fetched 2026-09-20). The schedule page is at <https://pretalx.com/pydata-london-2026/schedule/>.

Talks and tutorials are both included. The export's only break-like rows (organizer luncheons) live in the unconference room excerpt and are noted here rather than extracted as talks. Every talk record carries its canonical Pretalx talk URL and the export as source. Speaker names come from the export's person records; profile URLs are included where the export provides them (verified live for a sample).

Machine-readable version of this data: [`talks.json`](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/2026-python-events/pydata-london-2026/talks.json) in this directory.

## Talks

Machine-readable version of this data: [`talks.json`](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/2026-python-events/pydata-london-2026/talks.json) in this directory.

## Talks

## 1. [Making Databases LLM-Ready: Building Production Semantic Layers with Semantido](https://pretalx.com/pydata-london-2026/talk/YFYXAC/)

**Speakers**: [Dragos Crintea](https://pretalx.com/pydata-london-2026/speaker/UATLWR/)

**When and where**: Friday, 2026-06-05, 09:00–10:30, room Grand Hall 1

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

We'll explore the architecture of production-grade semantic layers, demonstrating how Semantido enables reliable text-to-SQL applications by providing LLMs with rich contextual understanding of database schemas, relationships, and business logic. Attendees will learn practical patterns for implementing semantic layers that bridge the gap between user intent and database queries by building a semantic layer for a fictional company.

The repos for this tutorial:
https://github.com/hikarilabs/pydata-london-2026-ui.git
https://github.com/hikarilabs/pydata-london-2026-sql.git

The deck:
https://docs.google.com/presentation/d/1uyN-xblr6d6cKb9HgHcgfd4ZafnN3mLRcVTuiKsYL-E/edit?usp=sharing

**Description** (verbatim):

Learning Objectives

By the end of this tutorial, participants will be able to:

- Design and implement semantic models that capture business logic and domain knowledge alongside database schema definitions
- Build LLM integrations that leverage semantic metadata for accurate query generation and validation
- Deploy scalable semantic APIs that abstract database complexity from LLM applications
- Use PydanticAI for an agentic analytics harness
- Implement observability patterns for monitoring and debugging
- How to evaluate semantic layer quality

**Desired Tutorial Structure (90 minutes)**

**Part 1: Foundations (~20 minutes)**

- The Text2SQL Challenge: Why naive approaches fail
- Semantic Layer Architecture: Core concepts, design patterns, and the role of metadata in LLM reliability
- Semantido Quick Start: Installation, project setup, and connecting to the playground database
- _Hands-on Exercise_: Participants will set up their development environment and connect semantido to a provided database.

**Part 2: Building Your First Semantic Layer (~25 minutes - 35 mins)**

- Declarative Model Definition: Extending SQLAlchemy models with business metadata, descriptions, and constraints
- Relationship Semantics: Annotating foreign keys, joins, and cross-table business rules
- Domain Knowledge Injection: Adding enums, validation logic, and computed fields with business meaning
- _Hands-on Exercise_: Participants will build a semantic layer for a given database, adding rich metadata that describes the tables and columns both in application and business terms.

**Part 3: LLM Integration Patterns (~20 minutes)**

- Context aware Query Generation: Using semantic layers exposed via a FastAPI endpoint
- _Hands-on Exercise_: Participants build a simple chatbot that answers natural language questions using the generated semantic layer. Participants will implement query validation and test it with ambiguous questions.

**Part 4: Production Considerations (~20 minutes)**

- Observability and Debugging (6 min): Logging semantic context, tracing query generation, and monitoring LLM-database interactions
- Evaluation Framework (5 min): Testing semantic layer quality with automated benchmarks and business logic validation
- Deployment Patterns (4 min): Docker, FastAPI integration, and scaling considerations
- _Hands-on Exercise_: Participants will add observability instrumentation to their semantic layer and run an evaluation suite that tests query accuracy against known business questions.

**Part 5: Production Considerations (15 minutes)**

- Q&A: Open discussion and troubleshooting

Source: <https://pretalx.com/pydata-london-2026/talk/YFYXAC/>

## 2. [GPU Algorithm Authoring with CUDA Tile](https://pretalx.com/pydata-london-2026/talk/DBGAND/)

**Speakers**: [Katrina Riehl](https://pretalx.com/pydata-london-2026/speaker/Z9ENP8/)

**When and where**: Friday, 2026-06-05, 10:50–12:20, room Grand Hall 1

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Want to write your own GPU algorithms, but not sure how to get started or keep them portable? Come to this hands-on session to learn tile programming with CUDA Tile and cuTile Python: you will build an accurate mental model of tiles and thread groups, write and debug real GPU kernels in a browser-based JupyterLab (no installation), profile and tune performance with NVIDIA Nsight, and see how the same tile code applies across DL and HPC examples like LLM inference and conjugate gradient, including when to use tiles vs SIMT and how to mix both.

**Description** (verbatim):

CUDA Tile is NVIDIA's new programming model for writing GPU kernels in an array-centric style that is portable across NVIDIA GPU architectures. Instead of orchestrating thousands of threads directly, you express computation over small local arrays (tiles) and let the system manage the parallel execution details: synchronization, data movement, and coordination across the GPU.

This interactive session introduces the core mental model behind tile programming and how it is realized in cuTile Python on top of the Tile IR compiler stack. You will write tile code, see how it maps onto real GPU execution, and learn how to evaluate and tune performance with NVIDIA's Nsight profilers. We'll explore examples from both DL and HPC, such as large language model inference and conjugate gradient solvers.

This session is hands-on with no installation required, just a web browser. We'll use Brev, NVIDIA's developer cloud, to get access to GPUs, and all work will be done in a JupyterLab environment.

By the end of this session, you will:

- Build an accurate mental model of tiles, thread groups, and how tile code executes on GPUs.
- Write and debug tile-based GPU kernels in Python for real workloads.
- Use profiling traces to identify bottlenecks and guide optimizations inside a notebook workflow.
- Decide when tile programming is the right tool versus SIMT, and how to mix the two when needed.

Links:

- Accelerated Computing Hub: https://github.com/NVIDIA/accelerated-computing-hub
- cuTile Python: https://github.com/NVIDIA/cutile-python
- Tile IR: https://github.com/NVIDIA/cuda-tile
- TileGym examples: https://github.com/NVIDIA/TileGym

Source: <https://pretalx.com/pydata-london-2026/talk/DBGAND/>

## 3. [Keynote: Samuel Colvin: Pydantic Monty & Logfire: Wild LLMs, from tool calling to computer use](https://pretalx.com/pydata-london-2026/talk/TAWYHU/)

**Speakers**: [Samuel Colvin](https://pretalx.com/pydata-london-2026/speaker/CDSDTD/)

**When and where**: Friday, 2026-06-05, 13:20–14:05, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

LLMs are increasingly being used to take actions, call APIs, and write code. But giving AI agents the ability to run code opens up a surprisingly tricky question: how much control do you actually hand over?

There's a full continuum here, from structured tool calling at one end to full computer use at the other, but most developers don't realise how many interesting options live in between. That gap matters, because the extremes both have serious trade-offs: pure tool calling is safe but sequential and limiting, while full sandboxes or computer use are powerful but complex, slow, and often a hard sell to enterprise security teams.

This talk introduces Monty, a minimal Python interpreter written in Rust, purpose-built for running AI-generated code safely. Unlike traditional sandboxing approaches that start with full access and try to lock things down, Monty starts from zero and requires you to explicitly grant each capability — meaning the LLM can only interact with the outside world through functions you wrote, control, and can audit. It's a new paradigm: not AI using your tools, but AI writing its own programs to coordinate your tools.

In this talk, you will learn how to think about the control-capability trade-off when building AI agents, where Monty sits on that spectrum and why, and how to use it with Pydantic AI to replace sequential tool calls with expressive Python — complete with a live demo traced through Logfire.

Basic familiarity with Python and LLM tool use is helpful but not required. No prior knowledge of Rust or sandboxing concepts needed.

Source: <https://pretalx.com/pydata-london-2026/talk/TAWYHU/>

## 4. [Flexible Statistical Modeling with Bayesian Additive Regression Trees](https://pretalx.com/pydata-london-2026/talk/M8TE3Q/)

**Speakers**: [Chris Fonnesbeck](https://pretalx.com/pydata-london-2026/speaker/MZZ8YC/)

**When and where**: Friday, 2026-06-05, 14:10–15:40, room Grand Hall 1

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Most machine learning methods give you a prediction but not a measure of how much to trust it. Bayesian Additive Regression Trees (BART) combine the flexibility of tree ensembles (e.g. random forests, boosting) with full uncertainty quantification—every prediction comes with a probability interval, not just a point estimate. This hands-on tutorial introduces BART for regression and classification. Using `pymc-bart`, participants will learn to fit flexible models that automatically capture non-linear relationships while providing honest uncertainty estimates. We emphasize practical interpretation throughout: visualizing predictions with uncertainty bands, understanding variable importance, and interpreting model output.

**Description** (verbatim):

Machine learning models are often evaluated on predictive accuracy alone, but accuracy without uncertainty can be misleading. Classical tree ensemble methods like random forests and gradient boosting provide point predictions, and while techniques like conformal inference or bootstrap aggregation can add uncertainty estimates, these are often poorly calibrated or computationally expensive.

Bayesian Additive Regression Trees (BART) offer a different approach: uncertainty quantification is built into the model, not ignored or bolted on afterward. BART models the response as a sum of small trees, with regularization priors that keep each tree weak. Posterior inference over the tree structures yields a full distribution over predictions—every fitted value comes with a credible interval that reflects genuine uncertainty about the underlying function.

This tutorial introduces BART through three applications, each demonstrating how uncertainty changes the way we interpret results:

**Regression:** We begin with continuous outcomes, fitting BART models and visualizing posterior predictive distributions. Rather than a single fitted curve, participants will see HDI bands that widen where data is sparse and narrow where evidence is strong. We'll explore variable importance—which comes with its own uncertainty—and partial dependence plots that reveal non-linear effects.

**Classification:** For binary outcomes, BART produces predicted probabilities with uncertainty, not just class labels. We'll examine how this uncertainty propagates through decision-making and compare calibration against standard classifiers.

### Target audience

Data scientists and analysts looking to add useful statistical methods to their toolkit.

## Takeaways

Participants will leave able to fit BART models for continuous, binary, and time-to-event outcomes; interpret predictions with full posterior uncertainty; use variable importance and partial dependence plots appropriately; and decide when BART's uncertainty quantification justifies its computational cost over simpler alternatives.

## Materials

GitHub repository with marimo notebooks, real-world datasets from sports, psychology, and other domains, environment files, and a one-page BART reference guide. Participants should clone the repository and verify their setup before the session.

Source: <https://pretalx.com/pydata-london-2026/talk/M8TE3Q/>

## 5. [Do you know how well your model is doing? Evaluate your LLMs](https://pretalx.com/pydata-london-2026/talk/SUJZCA/)

**Speakers**: [Cheuk Ting Ho](https://pretalx.com/pydata-london-2026/speaker/8EGVC9/)

**When and where**: Friday, 2026-06-05, 16:00–17:30, room Grand Hall 1

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

[Preflight check]: You may want to have a look at the repo and pre-download some libraries or models in advance: https://github.com/Cheukting/lighteval-exercises

Large Language Models (LLMs) are becoming central to modern applications, yet effectively evaluating their performance remains a significant challenge. How do you objectively compare different models, benchmark the impact of fine-tuning, or ensure your LLM responses adhere to safety guidelines (guard-railing)? This hands-on workshop addresses these critical questions.

**Description** (verbatim):

Prerequisites:

- Have experience coding in Python (with Python installed in the local machine)
- Basic understanding of machine learning and LLMs
- Experience with Hugging Face Transformers is preferred but not necessary
- A Hugging Face Hub account (sign up for free)
- A modern computer that can fine-turn small LLMs locally

Description:

We will begin with an essential revision of the Hugging Face Transformers library, covering basic LLM inference and fine-tuning. The core of the workshop will introduce and provide deep practice with Lighteval, an efficient and powerful LLM evaluation framework. Participants will learn how to leverage Lighteval to compare various LLMs available on the Hugging Face Hub using a range of pre-built tasks and metrics.

Finally, we will delve into advanced evaluation techniques, focusing on creating custom tasks and metrics tailored to unique, real-world application requirements. Participants will learn how to prepare custom datasets on the Hugging Face Hub and integrate them into Lighteval for precise, domain-specific evaluation. By the end of this workshop, you will possess the practical skills to rigorously evaluate, benchmark, and fine-tune your LLMs with confidence.

Source: <https://pretalx.com/pydata-london-2026/talk/SUJZCA/>

## 6. [After Conference Social- Fleets- Sponsored by PDFTA & Coefficient](https://pretalx.com/pydata-london-2026/talk/3RBSQM/)

**Speakers**: Not listed in the source data

**When and where**: Friday, 2026-06-05, 18:00–21:00, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Join us after Day 1 of PyData London for an evening of drinks, conversation, and community at Fleets • Bar & Kitchen, a stylish bar and social space just steps from St Paul’s Cathedral. It’s the perfect opportunity to unwind after a full day of talks, connect with fellow attendees, speakers, and organizers, and keep the PyData conversations going in a relaxed setting. Whether you’re looking to network, catch up with colleagues, or simply enjoy a great London evening with the community, we’d love to see you there.

Thank you to our sponsor PDFTA & Coefficient, find John Carney and John Sandall and give them a big thank you!

Venue: 44–46 Ludgate Hill, London EC4M 7DE
Learn more: [Fleets website](https://www.urbanpubsandbars.com/city-by-urban/venues/fleets#)

Source: <https://pretalx.com/pydata-london-2026/talk/3RBSQM/>

## 7. [Learn to Unlock Document Intelligence with Open-Source AI](https://pretalx.com/pydata-london-2026/talk/9PPVRK/)

**Speakers**: [Mingxuan Zhao](https://pretalx.com/pydata-london-2026/speaker/HRNV7T/), [Abby Tse](https://pretalx.com/pydata-london-2026/speaker/XS7A7F/), [Carol Chen](https://pretalx.com/pydata-london-2026/speaker/W97P3X/)

**When and where**: Friday, 2026-06-05, 09:00–10:30, room Doddington Forum

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Unlocking the full potential of AI starts with your data, but real-world documents come in countless formats and levels of complexity. This session will give you hands-on experience with Docling, an open-source Python library designed to convert complex documents into AI-ready formats. Learn how Docling simplifies document processing, enabling you to efficiently harness all your data for downstream AI and analytics applications.

**Description** (verbatim):

Most organizational knowledge is still locked inside complex documents, making it difficult to extract and use the information effectively. Traditional tools often fail when working with real-world document formats, particularly PDFs. Tables lose their structure, figures get separated from captions, and multi-column layouts become unreadable text. These failures make it difficult to bring AI to document-heavy workflows.

This workshop will give you hands on experience with Docling, an open-source project that takes a different approach, using deep learning models to parse documents the way humans read them. It preserves hierarchy, extracts structured data through a consistent API, and supports 15+ file formats out of the box. All of Docling is MIT-licensed, enabling fully local execution, allowing you to keep sensitive data on-premise while delivering low-latency processing and ingestion.

You'll be building a complete document intelligence pipeline from the ground up. We'll work through three progressive modules: first, converting documents and exploring Docling's enrichment features like table detection and image classification; second, chunking strategies that preserve document semantics for retrieval; and finally, building on all our other components using Docling, we will build a multimodal RAG pipeline with visual grounding, creating an application that can cite the exact page and location where it found an answer.

No prior experience with Docling is required. Colab notebooks with hosted model endpoints will be provided, so you can follow along with just a browser. Attendees who prefer local execution should have Jupyter Notebook installed and the ability to download models from Hugging Face. Bring your own documents to experiment with, or use the samples provided.

Link to workshop, project resources, and more: https://red.ht/pydataLON

Source: <https://pretalx.com/pydata-london-2026/talk/9PPVRK/>

## 8. [Observing Agentic AI in Production: MCP Server Tracing with OpenTelemetry and Animal Crossing](https://pretalx.com/pydata-london-2026/talk/APYSNR/)

**Speakers**: [Tun Shwe](https://pretalx.com/pydata-london-2026/speaker/KBN889/), [Fei Phoon](https://pretalx.com/pydata-london-2026/speaker/WTUCWT/)

**When and where**: Friday, 2026-06-05, 10:50–12:20, room Doddington Forum

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

AI agents are moving into production in 2026, but when something goes wrong (a tool call fails silently, an LLM takes 13 seconds to respond, token costs spike overnight) teams struggle to diagnose issues across multi-step agentic workflows. In this hands-on tutorial you will solve a real problem on the island in Animal Crossing with a FastMCP Model Context Protocol (MCP) server in Python, instrumenting it with OpenTelemetry following the emerging GenAI and MCP semantic conventions and visualising end-to-end traces in a local Jaeger instance. Did I mention that events on the island occur in real time and are collected and processed using Apache Kafka?

You will learn how distributed tracing captures the hierarchical relationship between agent conversations, tool executions and MCP protocol messages, and how to use that visibility for debugging, cost analysis and performance optimisation (including picking the right model and checking if you’re drowning in serialisation overhead). You will leave with a fully instrumented MCP server, a Docker Compose real-time observability stack and the knowledge to bring production-grade observability to your own agentic AI systems.

**Description** (verbatim):

### Why this matters

OpenTelemetry is rapidly becoming the standard telemetry backbone for AI agents, just as it is already for microservices. It is one of the most active CNCF projects after Kubernetes, with native support from 30+ observability vendors. Its GenAI Special Interest Group declared 2025 the "year of AI agents" and has since published purpose-built semantic conventions for LLM calls, agent orchestration, and MCP tool calls. The industry has followed: Amazon launched Bedrock AgentCore Observability built entirely on OTel and GenAI semantic conventions; Grafana Labs demonstrated production tracing of the OpenAI Agents SDK and AWS Bedrock AgentCore.

However, most teams building agents today have none of this. The reason is a “developer experience gap”: many agent builders come from data science and ML research backgrounds, not distributed systems, and have never configured a tracing pipeline. Traditional monitoring tools don't capture the signals that matter for agents: token usage, cost per invocation, tool selection, multi-agent handoffs. Since agentic architecture is interaction-centric (98% of wall-clock time is spent in LLM API calls and tool executions, not your code), this means distributed tracing, not traditional metrics, is the primary observability signal. Without it, failures are invisible: one fintech company's agent ran in a loop for 11 hours accumulating $47,000 in costs before anyone noticed.

### What we will do

We will instrument a FastMCP server that exposes tools for a fun real-time data engineering scenario, instrument it with OpenTelemetry and visualise the resulting traces.

- Check out a FastMCP server (understand the MCP request/response lifecycle).
- OpenTelemetry for agentic AI (traces, metrics, logs and why they're the primary signal for agents).
- Instrument the MCP server (OpenTelemetry instrumentation, see how errors are automatically recorded with stack traces).
- From traces to dashboards (build a dashboard that answers which tools are slowest, showing error rates and token costs).
- Production patterns and case studies (patterns for sensitive data handling, sampling strategies for high-throughput agent workflows).
- Connecting auth and observability (auth attributes appearing in traces when OAuth is enabled, giving per-user visibility).

### Target audience

Data engineers, data scientists, ML/AI engineers and SRE/platform engineers who are building or operating AI agents and need production visibility into agentic workflows. This is relevant to anyone deploying LLM-powered tools, multi-agent orchestration or MCP servers. Or you’re just a fan of Animal Crossing and social simulation gaming.

### Prerequisites

- Basic to Intermediate Python (comfortable with decorators, async/await basics and uv).
- No prior knowledge of MCP, OpenTelemetry or FastMCP is required.

### Tutorial requirements

- MacOS/Linux laptop or Windows with PowerShell.
- Docker, Colima or OrbStack (to run Docker Compose for the local observability stack).
- uv for package management.
- A code editor (VS Code, Cursor, Kiro or similar).
- LLM access, either via a vendor (Anthropic, OpenAI, etc) or local Ollama. We will be serving a local 1B model, so you’ll need enough RAM and disk space ~4 GB.
- Visit the GitHub repo <https://tinyurl.com/anteaters26> and follow the `SETUP.md` to install all the tools prior to arrival.

### Key takeaways

1. Understand why distributed tracing (rather than traditional metrics) is the primary observability signal for agentic AI systems.
2. Be able to build an MCP server with custom tools using FastMCP and instrument it with OpenTelemetry.
3. Know the OpenTelemetry GenAI and MCP semantic conventions and how they standardise telemetry across agent frameworks.
4. Be able to visualise, query and dashboard agent traces using Jaeger.
5. Understand the production observability landscape: auto-instrumentation libraries, sensitive data handling and compliance considerations.

Source: <https://pretalx.com/pydata-london-2026/talk/APYSNR/>

## 9. [Building a Browser Agent from Scratch: Teach an LLM to Navigate the Web](https://pretalx.com/pydata-london-2026/talk/ZAR8AG/)

**Speakers**: [Richard](https://pretalx.com/pydata-london-2026/speaker/QRKADD/), [Oreolorun Olu-Ipinlaye](https://pretalx.com/pydata-london-2026/speaker/DV9CMN/)

**When and where**: Friday, 2026-06-05, 14:10–15:40, room Doddington Forum

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

AI systems that can autonomously navigate websites, fill forms, extract data, and complete multi-step workflows; are one of the most exciting and practical applications of large language models in 2026. Libraries like browser-use (60k+ GitHub stars) and Skyvern have demonstrated their potential, but their abstractions can obscure the surprisingly approachable fundamentals underneath.

In this 90-minute hands-on tutorial, attendees will build a browser agent entirely from scratch using only Python, Playwright, and an LLM API. No agent frameworks, no magic; just the core building blocks: extracting and structuring the DOM into an LLM-friendly representation, capturing screenshots for vision-based reasoning, building the observe-think-act agent loop, and handling real-world challenges like dynamic content, multi-tab navigation, and error recovery.

By building from first principles, attendees will gain a deep understanding of how browser agents actually work; knowledge that transfers directly to using, debugging, and extending any browser agent framework. Every participant will leave with a working agent that can autonomously complete tasks on live websites.

This tutorial is aimed at Python developers and data scientists who are curious about AI-driven browser automation. Basic Python proficiency and familiarity with async/await are expected. No prior experience with Playwright, browser automation, or agent frameworks is required.

**Description** (verbatim):

The web is the world’s largest API, but it was designed for humans, not machines. Traditional browser automation tools like Selenium and Playwright require developers to write brittle scripts with hardcoded selectors that break whenever a website changes its layout. Browser agents flip this model: instead of telling the browser exactly what to click, you describe what you want to accomplish, and an LLM figures out how to do it; reading the page like a human would, reasoning about what to do next, and adapting when things don’t go as expected.

This approach has seen explosive growth. The open-source browser-use library surpassed 60,000 GitHub stars within months of release, and its creators raised $17M in seed funding. Skyvern, Browserbase, and others have built commercial platforms around the same idea. Under the hood, these tools all share a remarkably similar architecture: a perception layer that converts web pages into LLM-readable context, a reasoning layer where the LLM decides what action to take, and an execution layer that carries out the action via browser automation.

This tutorial strips away the abstraction layers and builds each component from scratch. The “from scratch” approach is deliberate: by understanding how the DOM is parsed, how screenshots are fed to vision models, and how the agent loop manages state, attendees gain transferable knowledge that applies to any browser agent tool or framework. When something breaks in production (and it will), this understanding is what separates debugging from guessing.

Source: <https://pretalx.com/pydata-london-2026/talk/ZAR8AG/>

## 10. [From Synthetic Examples to Production Signals: Multimodal Training Data Pipelines with Privacy-Safe Feedback](https://pretalx.com/pydata-london-2026/talk/HC3SLQ/)

**Speakers**: [Nabin Mulepati](https://pretalx.com/pydata-london-2026/speaker/ADXQZR/), [Lipika Ramaswamy](https://pretalx.com/pydata-london-2026/speaker/DGZM9L/)

**When and where**: Friday, 2026-06-05, 16:00–17:30, room Doddington Forum

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Production AI systems improve through a data flywheel: teams create training examples from curated source material, those examples shape model behavior, production usage reveals what the model still needs, and those usage signals become the next round of improvement. This hands-on tutorial focuses on the data pipelines behind that flywheel: how to generate, validate, and anonymize training data without relying on one-off prompt scripts.

Participants will build a reproducible training-data pipeline using NVIDIA NeMo Data Designer and NeMo Anonymizer. We'll start by working through text-based examples that introduce the basics of Data Designer: defining the shape of a dataset, connecting generation to source records, creating structured outputs, and filtering generated rows with judge-based quality checks. Then we'll extend the same pattern to multimodal document understanding with rich synthetic business document images, VLM-classified visual focus areas, and VLM-generated visual QA examples.

Finally, we'll shift from workshop-generated data to production-style usage data. Using Anonymizer, participants will detect and transform sensitive fields so usage logs can safely become source material for the next training iteration.

By the end, participants will understand a practical pattern for multimodal training data with privacy-safe feedback: **source data -> generate -> validate -> anonymize feedback -> improve**.

**Description** (verbatim):

This tutorial is for AI builders who want more discipline around training-data creation. The central premise is simple: the data models consume deserves the same engineering rigor as the models themselves.

Across three progressive Jupyter notebooks, participants will:

- Learn the Data Designer workflow through a text QA example, using explicit controls for the mix of examples, seed datasets, templated LLM generation, structured outputs, and LLM-as-a-judge quality checks.

- Apply the same pipeline shape to multimodal document data, using rich synthetic business document images as source records, VLM-classified visual focus areas, VLM-generated question-answer pairs, and a judge step to filter for correctness and visual grounding.

- Anonymize production-style usage data from a fine-tuned model, comparing privacy strategies that reduce sensitive-data risk while preserving useful training signal.

Participants leave with a working repo, runnable notebooks, and a reusable mental model for building training-data pipelines across text and images.

**Takeaways**

- A reproducible pattern for multimodal training-data generation.
- Practical use of source datasets, example-mix controls, dependency-aware columns, structured LLM outputs, and judge-based validation.
- A privacy workflow for turning production usage logs into safer source data for future training iterations.
- Hands-on experience with NeMo Data Designer and NeMo Anonymizer.
- A clear view of how synthetic generation, quality validation, and anonymized production feedback support a training-data lifecycle.

**Why Attend This Session?**
Most synthetic-data tutorials stop after generation. This session follows the full lifecycle: define the source material and the kinds of examples you want, generate text and multimodal training data, validate quality, anonymize production feedback, and prepare the anonymized data to be transformed into the next set of training examples.

**Prerequisites**
This is a hands-on notebook workshop. To follow along, please bring:

- A laptop where you can run Python and Jupyter notebooks.
- Basic comfort with Python, pandas-style dataframes, and editing notebook cells.
- Ability to clone a GitHub repository and run simple terminal commands. Setup instructions will include installing uv if you do not already have it.
- One hosted model API key configured in your environment or .env file. You can create a free `NVIDIA_API_KEY` at `build.nvidia.com`, or use `OPENROUTER_API_KEY` / `OPENAI_API_KEY`; if you use OpenRouter or OpenAI, any cost incurred during the session should be very minimal.
- Internet access for calling hosted LLM APIs during the exercises.

The workshop repository URL (https://github.com/nabinchha/pydata-london-2026-data-designer-anonymizer) will be made public before the session. You do not need prior experience with NeMo Data Designer, or NeMo Anonymizer.

Source: <https://pretalx.com/pydata-london-2026/talk/HC3SLQ/>

## 11. [Beyond ML Model Calibration: Hands-On Multicalibration with MCGrad](https://pretalx.com/pydata-london-2026/talk/SKBDNF/)

**Speakers**: [Niek Tax](https://pretalx.com/pydata-london-2026/speaker/MPS8BR/)

**When and where**: Friday, 2026-06-05, 09:00–10:30, room Hardwick Hub

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Your model is well-calibrated on average, but is it calibrated for _every subgroup_ of your users? In this hands-on tutorial you will learn what multicalibration is, why standard calibration methods leave systematic errors hidden in subpopulations, why this matters for ML models in production, and how to fix it in a few lines of code using MCGrad, an open-source Python library that has been battle-tested on hundreds of production models at a large tech company. Attendees will leave with a working notebook they can immediately apply to their own projects.

**Description** (verbatim):

A globally well-calibrated model can still be systematically overconfident for one subgroup and underconfident for another, these errors cancel out in aggregate, passing standard checks while silently degrading decisions for specific populations. Multicalibration fixes this by ensuring predictions are calibrated across all subgroups simultaneously, while improving other notions of model performance.

This tutorial introduces multicalibration from scratch using **MCGrad**, an open-source library (`pip install mcgrad`) that has been deployed on hundreds of production ML models at a major tech company, and the methodology was recently accepted at KDD 2026. Attendees train a classifier on a public dataset, discover hidden subgroup miscalibration, then fix it with MCGrad in a few lines of code, all inside a ready-to-run Colab notebook. We also cover hyperparameter tuning, safety mechanisms, and when not to apply multicalibration.

OUTLINE:

- **Welcome & Setup** (5 min)
  Goals, format, open Colab notebook, pip install mcgrad.
- **The Calibration Gap** (15 min)
  What is calibration? And why should ML practitioners care about it? Train a logistic regression on the dataset. Apply isotonic regression -- global calibration looks perfect. Reveal: the model is still badly miscalibrated for specific subgroups.
- **From Calibration to Multicalibration** (15 min)
  Define multicalibration and the MCE metric. Why practitioners need it: you rarely know which subgroups matter in advance. Deployment lessons from a major tech company (hundreds of production models).
- **MCGrad in Action -- Hands-On** (30 min)
  Walk through the MCGrad API (`fit`/`predict`). Fit MCGrad on the dataset, inspect the learning curve, compare base model vs. isotonic regression vs. MCGrad. Visualise segment-level error reduction. Mini-exercise: change segment features, observe impact on MCE.
- **Advanced Features & Production Tips** (15 min)
  Hyperparameter tuning, safety mechanisms (no-op failsafe), regression multicalibration, model serialization, when not to use multicalibration.
- **Wrap-Up & Q&A** (10 min)
  Recap the three-step workflow (measure MCE, fit MCGrad, verify). Pointers to docs and tutorials. Open Q&A.

Attendees leave with a working notebook, a new metric _multicalibration error_ (MCE) for auditing their own models, and a pip-installable tool to act on the results.

Source: <https://pretalx.com/pydata-london-2026/talk/SKBDNF/>

## 12. [Hands-On with Tabular Foundation Models: From Zero to Strong Baselines](https://pretalx.com/pydata-london-2026/talk/WDQZLR/)

**Speakers**: [Nicolas Makaroff](https://pretalx.com/pydata-london-2026/speaker/RBHKHH/)

**When and where**: Friday, 2026-06-05, 10:50–12:20, room Hardwick Hub

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

This hands-on tutorial takes participants from zero to confident use of tabular foundation models. Using real datasets, we will run TabICL-style models, benchmark them rigorously against XGBoost and Random Forest, diagnose their behavior, and build intuition for when they help and when they don't.

**Description** (verbatim):

Tabular foundation models are generating excitement, but most practitioners haven't used them yet. This **90-minute hands-on tutorial** bridges that gap.

Participants will work through **four progressive notebooks** on real-world datasets of varying difficulty. By the end, they won't just know _about_ tabular FMs — they'll have **run them, broken them, and compared them** against familiar baselines.

### Who is this for?

Data scientists and ML engineers who:

- Use sklearn / XGBoost / LightGBM regularly
- Are curious about tabular FMs but haven't tried them
- Want to build informed opinions grounded in hands-on experience

### What we'll use

- **Models:** Any TFMs (TabICL, TabPFN or Neuralk proprietary model with free credits), XGBoost, Random Forest
- **Datasets:** 3 curated real-world datasets chosen to expose different behaviors:
  - A small medical dataset (~500 rows, 12 features) — where TFMs tend to shine
  - A medium e-commerce dataset (~5K rows, 40+ features with mixed types) — a realistic "grey zone"
  - A large, noisy dataset (~50K rows) — where trees typically dominate
- **Stack:** Python 3.9+, sklearn, tabicl, xgboost, matplotlib, pandas

### Detailed outline (90 min)

| Time  | Phase                                        | What participants do                                                                                                                                                                            | Expected output                                                    |
| ----- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 0–15  | **Conceptual grounding**                     | Short lecture: what tabular FMs are, how they differ from fitted models, what to expect. No code yet.                                                                                           | Shared mental model before touching code                           |
| 15–30 | **Notebook 1: First predictions**            | Install a TFM, load the small medical dataset, generate predictions. Compare API with sklearn's `.fit()/.predict()` pattern.                                                                    | Working predictions; comfort with the API                          |
| 30–45 | **Notebook 2: Rigorous benchmarking**        | Run XGBoost and Random Forest on all 3 datasets with proper cross-validation. Compare with TFMs using the same splits. Discuss evaluation pitfalls (leakage, metric choice).                    | A comparison table with confidence intervals across 3 datasets     |
| 45–60 | **Notebook 3: When things break**            | Deliberately stress-test the TFMs: add noisy features, increase dataset size, introduce heavy cardinality categoricals. Observe where performance degrades relative to trees.                   | Intuition for failure modes, backed by their own experiments       |
| 60–75 | **Notebook 4: Diagnostics & interpretation** | Apply SHAP to both TFMs and XGBoost on the same dataset. Compare explanations. Discuss: are these explanations trustworthy? What can we still learn? Calibration plots and confidence analysis. | Practical diagnostic skills; awareness of interpretability caveats |
| 75–85 | **Wrap-up: Decision framework**              | Collaborative exercise: given 3 new dataset descriptions, participants vote on which model they'd choose and why. We discuss as a group.                                                        | Internalized decision criteria                                     |
| 85–90 | **Q&A and next steps**                       | Open discussion. Pointers to further resources, papers, and community.                                                                                                                          |                                                                    |

### Requirements

- Laptop with Python 3.9+
- Familiarity with sklearn (fit/predict/cross_val_score)
- No deep learning experience needed
- All materials (notebooks + datasets + environment setup) will be distributed via a **public GitHub repository** at least 2 weeks before the event

> **Note on materials:** The repository is currently being prepared and will contain all notebooks, datasets, and a `requirements.txt` for easy setup. A link will be shared with organizers as soon as it is live. <!-- TODO: replace with actual link once repo is created -->

### What attendees will be able to do after this tutorial

- **Run** tabular foundation models on their own datasets using a familiar sklearn-compatible API
- **Benchmark** TFMs against tree-based baselines with proper cross-validation and meaningful metrics
- **Diagnose** model behavior: identify when a TFM is failing, why, and what to do about it
- **Interpret** TFM outputs using SHAP while understanding the limitations of post-hoc explanations on learned priors
- **Decide** whether to adopt a tabular FM for a new project based on concrete, experience-backed criteria

### Key takeaways

- A working local environment with tabular FM tooling ready to use
- Four completed notebooks they can reuse as templates on their own data
- Confidence to try (or deliberately skip) tabular FMs on their next project

Source: <https://pretalx.com/pydata-london-2026/talk/WDQZLR/>

## 13. [Test-Driven Data Analysis](https://pretalx.com/pydata-london-2026/talk/MRKKWJ/)

**Speakers**: [Nick Radcliffe](https://pretalx.com/pydata-london-2026/speaker/R89Z7R/)

**When and where**: Friday, 2026-06-05, 14:10–15:40, room Hardwick Hub

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Test-Driven Data Analysis is a methodology for reducing errors in data and data analy. It is also an open-source Python package for supporting key aspects of the methodology. This tutorial will provide hands-on experience using the library to validate data and write tests (manually or automatically) for analytical processes. It will also highlight approaches to avoiding errors in specific areas not amenable to software support.

**Description** (verbatim):

Test-Driven Data Analysis is a methodology for reducing errors in data and data analysis, and also a an open-source Python package (tdda) for supporting key aspects of the methodology. This tutorial will provide hands-on experience using the library to

- generate constraints characterising data in data frames automatically;
- validate data using previously generated constraints;
- test structured data resulting from analyses in data frames;
- test unstructured date from analyses, typically in text files and graphical form,

as well as highlighting other libraries that can be used for similar purposes.

It will also discuss a taxonomy of errors arising during analysis and highlight approaches to reducing those errors, including through the use of 22 TDDA-focused checklists.

This major error categories that will be considered are

- errors of interpretation (of formulation and of communication),
- errors of implementation,
- errors of process,
- errors of applicability, and
- errors of judgement.

**ATTENDEES**

No prior experience is required, but it would be helpful to have the tdda library installed and to have some familiarity with DataFrames in polars or pandas. If you want to develop hands-on experience during the tutorial follow the instructions to install tdda at [tdda.readthedocs.io](https://tdda.readthedocs.io/en/latest/installation.html).

If this works, you should be able to use the tdda command. If you change to a directory you are happy to put data in, the command

     tdda examples all

will download all the data that will be used in the tutorial in subdirectories.

There is wifi available at the conference, but if you do this ahead the tutorial, you will fight fewer people for bandwidth and will have more chance to check it works before you need the library.

Source: <https://pretalx.com/pydata-london-2026/talk/MRKKWJ/>

## 14. [Model criticism through posterior predictive checks](https://pretalx.com/pydata-london-2026/talk/JL7YAJ/)

**Speakers**: [Oriol Abril Pla](https://pretalx.com/pydata-london-2026/speaker/MKEJ7N/)

**When and where**: Friday, 2026-06-05, 16:00–17:30, room Hardwick Hub

**Type**: Tutorial — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Posterior predictive checks are a key step within Bayesian modeling workflows where we compare model predictions with the data used to fit the model. By focusing on distributional comparisons instead of point estimates, they offer valuable insights about our models, where they fail and inform model improvements. _Knowing a model is not completely right is relatively easy_, knowing **why** that is the case and **how to fix it** are a whole other question which will be the focus of the tutorial. This tutorial will provide data scientists and researchers with multiple strategies for posterior predictive checks to allow their use in continuous, discrete or categorical data, and for homogeneous or heterogeneous data.

**Description** (verbatim):

The main expected audience of this tutorial are practitioners, either in academia or industry, working with probabilistic models, and it will also include multiple elements of interest to anyone working with any kind of statistical model or fitting data through simulations.

The material for the tutorial will be published on [GitHub](https://github.com/OriolAbril/pydata2026-ppc) beforehand so attendees can download the data and prepare their environments. The tutorial will assume attendees are familiar with Python, Jupyter notebooks and basic statistical concepts. Knowledge about Bayesian inference and posterior predictive sampling will be helpful but they are not required.

The tutorial will have an initial introductory section of ~40 minutes. The introduction will cover posterior predictive checks conceptually as well as usage examples using ArviZ. This will be followed by multiple hands-on exercises on provided example datasets to practice model criticism through posterior predictive checks. The main topics covered will be:

- Understanding the need for distributional comparisons
- Understanding how to adapt model criticism to the type of data
- Diagnosing models of heterogeneous data at both the population and group level
- Translating model criticism visualizations to model issues
- Multiple uncertainty visualization designs
- How to use ArviZ for predefined and custom posterior predictive checks

Source: <https://pretalx.com/pydata-london-2026/talk/JL7YAJ/>

## 15. [Keynote- Rachel Lee Nabors- The Community Is the Boat](https://pretalx.com/pydata-london-2026/talk/PUL99Q/)

**Speakers**: [Rachel Lee Nabors](https://pretalx.com/pydata-london-2026/speaker/EUJQRL/)

**When and where**: Saturday, 2026-06-06, 09:10–09:55, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

The tech industry rises and falls in cycles, like the tide follows the moon. Every few years, the ground shifts and we all have to learn to walk again. It happened to me twice, when I moved from being an award-winning cartoonist to an underemployed web developer during the Recession, and again as a React Core engineer who washed up in AI after layoffs. I went from peak influence to the absolute bottom rung each time. Both times, what saved me wasn't genius or a special gift. It was embracing and being embraced by my new community.

This is a keynote about which skills travel across every shift, what we owe each other as the waves keep coming, and how, in a rising tide era, to find your boat and row with the crew. Whether you've been here a while, have just arrived, or are watching the water rise from the shore, there's a place in this boat.

Source: <https://pretalx.com/pydata-london-2026/talk/PUL99Q/>

## 16. [The Rules Nobody Writes Down: Decoding and Shifting Team Culture From Any Seat](https://pretalx.com/pydata-london-2026/talk/V3D3LS/)

**Speakers**: [Margaritha Groenendijk](https://pretalx.com/pydata-london-2026/speaker/VBMDQR/)

**When and where**: Saturday, 2026-06-06, 10:20–11:05, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Every team runs on unwritten rules. Habits that shape how decisions get made, how failure is handled, and what is safe to say. This talk provides a framework for reading those rules, understanding the collective self-image that drives team behaviour, and influencing culture from any position. With a look at how AI adoption is forming new rules in real-time, you will leave knowing how to decode the system you are in and start shifting it.

**Description** (verbatim):

Most talks on culture are aimed at managers, the people with formal authority to change things. But data scientists, engineers, and ML practitioners navigate team dynamics every day, often without that authority. This talk is for you: how to read the unwritten rules, understand what drives them, and shift them from any position.

The central idea is simple. Team culture isn't what is on the company wiki. It is a paradigm or a system of habits that shapes behaviour more powerfully than any stated policy. Beneath those habits sits the team's collective self-image: the shared belief about "who we are" and "what's possible." That self-image sets the upper limit of performance. A team that sees itself as "always firefighting" will keep firefighting, even when the fires are out.

The good news: you can influence this from any seat. Not through announcements, but through consistent action.

I will cover how to read the paradigm, the signals that reveal real culture. How failure is handled. Who speaks first. What gets celebrated versus quietly ignored. The stories that get repeated. These are data points that tell you what the team actually believes.

I will also share specific questions you can use in interviews to decode culture before you join. Questions about past failures, who thrives versus struggles, how disagreement is managed. The answers matter less than how people respond: the hesitation, the energy, the discomfort.

There is a trap worth knowing about. The longer you stay, the less you see. What felt strange in week one feels normal by month three. Your first weeks are a window of clarity. I will cover how to use it before it closes.

The core of the talk is about influence. Three ways are available to anyone: modelling the behaviour you want to see, naming what others leave unspoken, and holding a different picture of what's possible. This isn't positive thinking. It is praxis, which is integrating belief with behaviour through consistent action.

Finally, I will use AI adoption as an example. AI tools are shifting work toward individual tasks while new unwritten rules form around their use. Who is using AI openly? Who is hiding it? What is the unspoken agreement about quality and trust? This is a chance to watch a paradigm form in real-time and shape it before it solidifies.

This is a practical talk, not a tutorial. The target audience is data scientists, data engineers, and ML practitioners at any level and especially if you'] have recently joined a team, are navigating a tricky dynamic, or want more impact without moving into management.

You will leave with a framework for reading team culture, understanding what drives it, and influencing it through consistent behaviour starting the day you get back to work.

Source: <https://pretalx.com/pydata-london-2026/talk/V3D3LS/>

## 17. [Columnar Thinking - Designing for high-performance execution with Arrow and Polars](https://pretalx.com/pydata-london-2026/talk/WGJMXV/)

**Speakers**: [Kamlesh Shah](https://pretalx.com/pydata-london-2026/speaker/CDTEL8/)

**When and where**: Saturday, 2026-06-06, 11:05–11:50, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

When building high-performance systems for analytical workload, we often focus on the efficiency of the algorithm, like reducing Big-O complexity or optimising numerical routines. Yet in real world workloads, the decisive factor is not just the algorithm but the shape of how the data is laid out, traversed, and distributed across processes.

This talk will cover aspects of mechanical sympathy, focussing on how structures in memory can benefit from cache-sensitive, SIMD-enabled (vector instructions) CPUs, constrained by memory bandwidth and optimised for predictable, contiguous access.

We will use real-world examples to show how minimising serialisation overhead and enabling efficient cross-process and cross-language data exchange reduces the cost of data movement across systems. Beyond single-system performance, we will examine why Arrow’s standardised, zero-copy columnar format is a critical enabler of distributed execution. We will see how columnar formats support scalable computation across threads, processes, and distributed nodes.

**Description** (verbatim):

Everyday production-scale data and systems engineering still reflects a row-oriented mental model. Loops, iterations, mutations are seen as easy to read and are understandable. While these work for small datasets and toy models during explorations in notebooks, they fail to perform when workloads scale - be it for rolling analytics, high-throughput pipelines or multi-million row aggregations. This mismatch between row-wise thinking and modern CPU architecture becomes a structural bottleneck that becomes very costly to fix.

We’ll explore the shift from row-oriented design to columnar thinking, designing and developing high-performance workloads right from the onset. Using Arrow’s columnar memory format and Polars’ execution engine, armed with concrete examples from real-life quantitative calculations, we will examine how contiguous buffers, SIMD-compatible layouts, and lazy query planning are a natural combination for performant analytical workloads.

You’ll leave with:

1. A clear understanding of how columnar memory impacts execution, in contrast to row-oriented or traditional vectorised approaches.
2. Practical patterns for structuring column-first transformations.
3. Insights into how Arrow reduces data movement overhead in distributed systems.
4. Guidance on when lazy execution and query optimisation matters.
5. Ideal design principles for building scalable calculation pipelines with Polars and Arrow tools.

Source: <https://pretalx.com/pydata-london-2026/talk/WGJMXV/>

## 18. [JupyterLite: run all your code in a web browser using WebAssembly](https://pretalx.com/pydata-london-2026/talk/NVXBEM/)

**Speakers**: [Ian Thomas](https://pretalx.com/pydata-london-2026/speaker/NKXZDM/)

**When and where**: Saturday, 2026-06-06, 11:50–12:35, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

JupyterLite is a JupyterLab distribution that runs entirely in the web browser, backed by in-browser language kernels. Using it you can run Python, R and C++ in your browser via WebAssembly, use `git` and `vim` in a terminal, and access AI agents in a safe, sandboxed environment.

This talk will present a comprehensive summary of all things JupyterLite, and provide live demonstrations of many of its key features and how easy it is to deploy.

The talk assumes basic familiarity with JupyterLab but not necessarily JupyterLite. It will be of benefit to anyone who wishes to learn about this emerging technology and its potential for scalable, accessible interactive computing.

**Description** (verbatim):

JupyterLite is a JupyterLab distribution that runs entirely in the web browser, backed by in-browser language kernels. Standard JupyterLab uses kernels run in separate processes and communicate with the client by message passing, whereas JupyterLite uses kernels that run entirely in the browser, based on JavaScript and WebAssembly, such as pyodide and xeus-python.

This means that JupyterLite deployments can be scaled to millions of users without the need for individual containers for each user session, only static files need to be served which can be done with a simple web server like GitHub pages.

This talk will present a comprehensive summary of all things JupyterLite, and demonstrate key features. Highlights include the wide variety of language kernels supported, a terminal for those who wish to run `git` or `vim` at a command line in the browser, and access to AI agents in a safe sandboxed browser environment. It will explain the technology behind JupyerLite and how your favourite packages are built to run in the browser.

JupyterLite sites are easy to deploy and there will be a live demonstration of a deployment to illustrate this.

Talk outline:

- Overview
- Comparison of JupyterLab and JupyterLite
- Live demonstration of basic functionality
- How it works
- Kernels, including why are there two different python kernels (pyodide and xeus-python) and how to choose between them
- Emscripten-forge package building
- Key features such as shared in-browser filesystem
- More detailed demos such as installing packages on the fly
- What it is good and bad at
- Terminal for `vim`, `git`, etc
- Jupyterlite AI
- Use in project documentation using jupyterlite-sphinx
- Deployment, including live demo
- Making it easier to deploy and share using notebook.link
- Where JupyterLite is going

Source: <https://pretalx.com/pydata-london-2026/talk/NVXBEM/>

## 19. [Keynote- Jeremiah Lowin- Build Reasonable Software](https://pretalx.com/pydata-london-2026/talk/QU33NS/)

**Speakers**: [Jeremiah Lowin](https://pretalx.com/pydata-london-2026/speaker/NNKJNL/)

**When and where**: Saturday, 2026-06-06, 13:35–14:20, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Python became the language of data science because it made hard work feel possible. It gave scientists, analysts, engineers, and researchers a shared way to express ideas without forcing them to become software specialists first. The result was a style of software that made powerful systems easier to learn, easier to combine, and easier to trust.

In this keynote, Jeremiah Lowin explores what it means for software to be Pythonic: simple, composable, readable, and easy to reason about. Those qualities helped Python become the default language for data science, and they matter even more now that software is beginning to build software.

The next generation of agentic systems will be judged by whether people can understand them, change them, and trust them. This talk argues that the lesson of PyData is also the challenge for AI: build systems that remain easy to reason about as they become more powerful, and use emerging interfaces like MCP to make data easier to communicate, explore, and act on.

Source: <https://pretalx.com/pydata-london-2026/talk/QU33NS/>

## 20. [Reading the Mind of an LLM](https://pretalx.com/pydata-london-2026/talk/AYDUBL/)

**Speakers**: [Luca Baggi](https://pretalx.com/pydata-london-2026/speaker/LCEK33/)

**When and where**: Saturday, 2026-06-06, 14:45–15:30, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

What if you could watch an AI’s thought take shape? For years, LLMs have been impenetrable "black boxes," but we are finally beginning to find ways to see how the ghost in the machine actually works.

This talk explores **mechanistic interpretability**, a subfield of AI that aims to understand the internal workings of neural networks. Mapping these internal "circuits" is not only just a philosophical curiosity - or duty: it is a high-stakes engineering necessity for safety, debugging, and trust.

**Description** (verbatim):

What if we could step inside an LLM and watch it think in real time?

This talk distills the latest research from Anthropic, DeepMind, and OpenAI to present the current state of the art in **LLM interpretability**.

We’ll start with the modern interpretation of **embeddings** as sparse, monosemantic features living in high-dimensional space. From there, we’ll explore emerging techniques such as **circuit tracing** and **attribution graphs**, and see how researchers reconstruct the computational pathways behind behaviors like multilingual reasoning, refusals, and hallucinations.

We’ll also look at new evidence suggesting that models may have limited forms of introspection—clarifying what they can, and crucially cannot, reliably report about their internal processes.

Finally, we’ll connect these “microscopic” insights to **real engineering practice**: how feature-level understanding can improve debugging, safety, and robustness in deployed AI systems, and where current methods still fall short.

Source: <https://pretalx.com/pydata-london-2026/talk/AYDUBL/>

## 21. [SELECT instance FROM cloud WHERE workload = ? ORDER BY cost_efficiency](https://pretalx.com/pydata-london-2026/talk/ABYV3J/)

**Speakers**: [Gergely Daroczi](https://pretalx.com/pydata-london-2026/speaker/H9DKCZ/)

**When and where**: Saturday, 2026-06-06, 15:30–16:15, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Choosing a cloud instance type for a DS/ML/AI workload is still largely a heuristic exercise. While public pricing and hardware specifications are available, they are fragmented, inconsistently structured, and challenging to compare across cloud providers -- especially once real workload performance is taken into account.

In this talk, we present Spare Cores Navigator, a Python-queryable benchmark dataset that covers thousands of cloud server types from multiple vendors, with standardized performance and cost-efficiency metrics. We demonstrate how instance selection can be expressed as a simple data query, e.g. filtering by workload characteristics, hardware or compliance constraints, and budget, then ranking candidates by price-performance.

**Description** (verbatim):

Selecting a cloud instance for DS/ML/AI workloads is typically done using heuristics, vendor guidance, or trial-and-error. While cloud providers publish pricing tables and hardware specifications, this information is fragmented, inconsistently structured, and challenging to compare across vendors – especially once real workload performance is considered.

This talk introduces Spare Cores Navigator, a vendor-independent, open-source, Python-based ecosystem that treats cloud instance selection as a data problem. The project maintains a continuously updated benchmark dataset covering thousands of server types across multiple cloud providers, with standardized hardware metadata, performance measurements, and cost-efficiency metrics across over 500 workloads.

We describe how the dataset is built by automatically discovering and provisioning cloud instances at scale using public GitHub Actions to run hardware inspection tools and a diverse benchmark suite. This includes general CPU performance, memory bandwidth, compression algorithms, cryptographic workloads, web serving, and data store performance, as well as DS/ML-specific benchmarks such as gradient-boosted model training and LLM inference on CPUs and GPUs.

The main focus of the talk is demonstrating practical use cases for server type selection by querying the dataset under different workload characteristics, compliance and budget constraints, and optimization goals – such as minimizing cost-efficiency trade-offs or reducing environmental impact.

Source: <https://pretalx.com/pydata-london-2026/talk/ABYV3J/>

## 22. [Building a Scientific Taxonomy at Scale with Graph Clustering, Embeddings, and LLMs](https://pretalx.com/pydata-london-2026/talk/ZFR8VH/)

**Speakers**: [Daniele Raimondi](https://pretalx.com/pydata-london-2026/speaker/3U8HLG/), [Feichi Lu](https://pretalx.com/pydata-london-2026/speaker/3QSYBS/)

**When and where**: Saturday, 2026-06-06, 16:15–17:00, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Scientific publishers tag **millions of articles** with author-provided keywords, but these keywords are noisy, inconsistent, and semantically ambiguous. _"Machine learning," "ML," and "machine-learning"_ all mean the same thing, while other terms shift meaning across disciplines.

This talk presents a **production pipeline** that extends [OpenAlex](https://openalex.org/)'s 4-level hierarchy with a fifth in-house **Concept** layer, producing a **115K-concept scientific taxonomy**.

**SPECTER2** embeddings model semantic similarity, and per-field **Leiden clustering with CPM resolution** groups 100K+ concepts via mutual kNN graphs — with hyperparameters selected through **grid search** and **custom pair-based evaluation**. **Qdrant** enables vector-based hierarchical attachment.

**LLMs are deployed at five targeted stages** — granularity filtering, field classification, cluster renaming, explanation generation, and topic-assignment validation — while **deterministic methods handle everything else**, ensuring scalability and reproducibility.

The resulting taxonomy powers a **paper-tagging pipeline** where SPECTER2 retrieves ~150 candidates per paper across multiple text-splitting strategies, deterministic filters prune by field/subfield distribution and near-synonym merging, and an **LLM reranker selects the final 5–8 concepts**. These assignments enable applications such as **temporal trend detection** over emerging research topics and more.

**Attendees will learn** when to integrate LLMs in large-scale NLP pipelines, how to scale graph clustering to 100K+ nodes, and how to design hybrid embedding–LLM systems that turn noisy metadata into reliable scientific intelligence.

**Description** (verbatim):

### The problem

If you've ever tried to make sense of author-provided keywords across millions of papers, you know the pain. _"Machine learning"_, _"ML"_, _"machine-learning"_: same thing, three entries. Other terms look identical but mean completely different things depending on the field. Manual cleanup? Doesn't scale. Regex and string matching? Misses the semantics entirely.

### What we built

We took OpenAlex's 4-level hierarchy (**Domain → Field → Subfield → Topic**) and added a fifth in-house **Concept** layer: 115K+ fine-grained concepts, each with a clear position in the tree.

The core idea: embed all candidate concepts with **SPECTER2**, build a mutual kNN similarity graph per field, and cluster it with **Leiden (CPM resolution)** at 100K+ node scale. We tuned hyperparameters via grid search, scored against hand-curated concept pairs - things like _"Cryptocurrency"_ and _"Crypto Currency"_ must land together, while _"Decision Trees"_ and _"Random Forest"_ must stay apart.

LLMs come in at **five specific points** where embeddings alone aren't enough: filtering concept granularity, classifying into fields, renaming clusters, generating explanations, and validating topic assignments. Everything else is deterministic: no LLM in the loop means reproducible and cheap.

### Paper tagging

Once the taxonomy exists, we use it to tag papers. With SPECTER2 embeddings, we retrieve an initial pool of ~150 candidate concepts per paper (eight different text-splitting strategies over title, abstract, and keywords). Deterministic filters prune by field/subfield distribution and merge near-synonyms with Jaccard + union-find. Then an LLM reranker picks the final **5–8 concepts** with domain verification and keyword mapping, ranked.

### What comes next

With millions of papers tagged consistently, the obvious next step is **trend detection**: tracking how concept frequency and co-occurrence shift over time to spot emerging research areas. We'll sketch out the approach.

### Tech stack

**SPECTER2** (embeddings) · **igraph + leidenalg** (Leiden/CPM clustering) · **hnswlib** (ANN for kNN graphs) · **Qdrant** (vector search for hierarchical attachment) · **Azure OpenAI** (structured LLM inference) · human + automated validation framework

### You'll walk away knowing

- When LLMs actually help in large-scale NLP pipelines and when they're overkill
- How to scale graph clustering to 100K+ nodes in Python
- How to evaluate clustering with custom pair-based constraints
- Practical trade-offs between embeddings, graph methods, and LLMs

Source: <https://pretalx.com/pydata-london-2026/talk/ZFR8VH/>

## 23. [Conference Social](https://pretalx.com/pydata-london-2026/talk/PGFXAR/)

**Speakers**: Not listed in the source data

**When and where**: Saturday, 2026-06-06, 17:00–18:00, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Keep the PyData London energy going as we wrap up an incredible two days of talks, learning, and connection. Join us for our closing social immediately following the final sessions on Saturday from 5:00–6:00 PM, right at the conference venue. This is a great chance to continue conversations sparked during the day, connect with speakers and fellow attendees, and celebrate another fantastic PyData London with the community. Grab a drink, mingle, and enjoy one last opportunity to network and reflect on the ideas and insights shared throughout the conference before heading out for the evening.

Source: <https://pretalx.com/pydata-london-2026/talk/PGFXAR/>

## 24. [Building Production Multi-Agent RAG Systems on Serverless AWS](https://pretalx.com/pydata-london-2026/talk/RQ3FJQ/)

**Speakers**: [Samuel Jaja](https://pretalx.com/pydata-london-2026/speaker/UK3RCM/)

**When and where**: Saturday, 2026-06-06, 10:20–11:05, room Grand Hall 2

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Multi-agent AI systems promise autonomous reasoning, but most tutorials stop at prototypes. This talk shares hard-won lessons from deploying a production multi-agent RAG platform on serverless AWS , covering agent orchestration patterns, cross-region LLM routing, vector search cost optimisation, and the observability strategies that keep it all running reliably.

You'll learn concrete patterns for coordinating multiple RAG-enabled agents via SQS and Lambda, the cost/latency trade-offs between managed and self-managed vector search (including how to achieve 90% storage savings), and practical observability strategies using Langfuse and dead-letter queues. Whether you're scaling your first RAG system or architecting multi-agent workflows, you'll leave with actionable patterns you can apply immediately.

**Description** (verbatim):

Modern AI applications increasingly require multiple specialised agents working together, but orchestrating them reliably at scale is challenging. This talk walks through the architecture and lessons learned from building a production multi-agent financial analysis platform.

Outline:

- Minutes 0-5: Why single-agent RAG hits limits — the case for multi-agent orchestration
- Minutes 5-15: Architecture deep-dive — SQS-based agent coordination, Lambda handlers, and how RAG retrieval integrates across agents
- Minutes 15-22: Cross-region Bedrock routing and why latency geography matters
- Minutes 22-30: Cost lessons — achieving 90% vector storage savings with S3 Vector Search vs managed alternatives
- Minutes 30-37: Observability and failure handling — Langfuse tracing, DLQs, and debugging distributed agent calls
- Minutes 37-40: Key takeaways and Q&A

Target audience: ML engineers, data scientists, and developers building production AI systems. Familiarity with RAG concepts and basic AWS services assumed; no multi-agent experience required.

Source: <https://pretalx.com/pydata-london-2026/talk/RQ3FJQ/>

## 25. [Production-Ready AI Agents: From LLMs to Small Language Models](https://pretalx.com/pydata-london-2026/talk/3JJHZF/)

**Speakers**: [Prattyush Mangal](https://pretalx.com/pydata-london-2026/speaker/M7JYHY/)

**When and where**: Saturday, 2026-06-06, 11:05–11:50, room Grand Hall 2

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Building a demo agent with hundred billion parameters and beyond can be easy. Deploying reliable, cost-effective agents in production is hard. This talk provides a comprehensive roadmap for taking AI agents from prototype to production, with a focus on migrating from expensive frontier LLMs to efficient small language models (SLMs).

We'll explore the entire lifecycle of production agent development: test-driven development practices adapted for non-deterministic AI systems, agent architectures and migration strategies from large to small models, CI/CD considerations for agents, and observability frameworks which capture what matters and assist in remediating failures.

Whether you're running agents at scale or planning your first deployment, you'll leave with actionable strategies and concrete tools to build reliable, maintainable agent systems with small language models.

**Description** (verbatim):

In this talk we will cover the complete Agent Development Lifecycle from Prototype to a scalable and robust Production agent with cost effective Small Language Models. The talk will present the following topics, gathered from real engagements with product teams:

1. **The Production Agent Problem (3 min)**
   The prototype-to-production gap, why closed, frontier LLMs don't scale, and the agent development lifecycle.

2. **Small Models, Big Impact (2 min)**
   The case for small open language models, the current model landscape and pursuing an iterative migration pattern.

3. **Test-Driven Agent Development (5 min)**
   Starting with clear use cases and adapting testing practices for non-deterministic systems. Covering evaluation patterns and practical examples of testing agent behavior for different types of agents.

4. **Techniques for migrating to Small Language Models (7 min)**
   Introducing task decomposition patterns, use of multi-model approaches and agent architectures better suited to Small Language Model utilisation.

5. **CI/CD for Agents** (7 min)
   Treating models and prompts as config rather than code. Building deployment pipelines that handle model and prompt versioning, integration and end-to-end testing for agents with MCP and A2A considerations, and agent packaging for production rollout.

6. **Observability and Monitoring** (4 min)
   Instrumenting agents with structured logging, tracking key metrics beyond traditional monitoring, and building dashboards and alerts that surface quality issues. Monitoring non-functional metrics such as cost, latency and concurrency.

7. **Continuous Improvement Loops** (4 min)
   Creating feedback pipelines from production data, triaging failures and automating analysis. Strategies for iterative improvement, and methods for measuring progress through A/B testing.

As part of this talk, we will reference some Jupyter Notebooks and reusable code snippets with the PyData stack to enable attendees to begin their own Agentic journeys to production with Small Language Models.

**Links**:

- [Useful Code Snippets and Blogs on working with SLMs for Agentic Applications](https://github.com/ibm-granite-community/granite-agent-cookbook)

Source: <https://pretalx.com/pydata-london-2026/talk/3JJHZF/>

## 26. [Evaluating multi-turn conversations: A practical guide to AI Agent evals](https://pretalx.com/pydata-london-2026/talk/8Y9GRD/)

**Speakers**: [Lena Shakurova](https://pretalx.com/pydata-london-2026/speaker/WXBHAE/)

**When and where**: Saturday, 2026-06-06, 11:50–12:35, room Grand Hall 2

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

As AI agents become more popular, one question becomes increasingly important: how do you actually know if your agent is performing well? Multi-turn conversations are hard to evaluate because because there is rarely one right answer and at any given turn multiple responses can be correct. In this talk, we'll walk through a structured approach to evaluating complex conversations. We'll cover what makes a good conversation, techniques for evaluating multi-turn conversations where multiple outcomes are simultaneously valid, and how to scale evaluation pipelines. Finally, we'll discuss practical frameworks for continuous improvement and building confidence in your agent's real-world behaviour.

**Description** (verbatim):

As AI agents move from demos to production, evaluating their performance becomes one of the most important challenges for teams shipping them. Unlike single-turn LLM calls, conversations are messy. You can't evaluate a response in isolation, each turn depends on prior context and a perfectly correct answer in one conversation might be wrong in another.

In this talk we'll discuss a systematic approach to evaluating complex multi-turn conversations.

We'll talk about:

- Defining what makes a "good" conversation
- The unique challenges of multi-turn evaluation
- Metrics for assessing conversation quality
- Constructing evaluation datasets for conversational AI agents
- Automated pipelines for continuous agent evaluation in production

We'll show practical implementations using Python, with real-world examples from production agent systems across different domains.

Attendees will leave with:

- A structured framework for defining and measuring conversation quality in their domain
- Practical techniques for evaluating multi-turn interactions at scale

The session will provide actionable insights for AI engineers, data scientists, and product managers looking to evaluate AI agents rigorously and build stakeholder trust.

Source: <https://pretalx.com/pydata-london-2026/talk/8Y9GRD/>

## 27. [Fast-Forward(ing) Models: Accelerating High-Dimensional Inference with AI Emulators](https://pretalx.com/pydata-london-2026/talk/J99JNR/)

**Speakers**: [Austen Wallis](https://pretalx.com/pydata-london-2026/speaker/LJMHYX/)

**When and where**: Saturday, 2026-06-06, 14:45–15:30, room Grand Hall 2

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

In science and engineering, we are frequently challenged by the inability to manipulate environmental variables—a key component of the scientific method. For example, we cannot simply stop a hurricane in its tracks or change the temperature of the Sun. Instead, we heavily rely on "Forward Models"—numerical simulations that predict data from physical parameters. However, these models are often massively computationally expensive.

Emulators (or surrogate models) present a solution. Whether solving a single time-sensitive equation or searching a high-dimensional inference space, emulators can accelerate simulation results by orders of magnitude. In this talk, we show how these machine-learning tools are revolutionising research across STEM disciplines, from inferring input parameters to developing digital twins and augmenting foundational models.

**Description** (verbatim):

This talk aims to show how we can accelerate the solving of complex, imperfect, high-dimensional physical models using machine learning. We will be discussing:

- The motivation for accelerating models (3 mins)
- An introduction to emulation (5 mins)
- The most common emulation architectures (4 mins)
- Effective sampling and parameter selection for training data (4 mins)
- Model dimensionality reduction techniques and optimisation (4 mins)
- Emulator uncertainty quantification and inference techniques (4 mins)
- Designing an emulator workflow (2 mins)
- Data augmentation for existing datasets (5 mins)
- Use case examples (9 mins)

Attendees will gain a deep understanding of how to architect surrogate models and the libraries typically used to create them, enabling users to "fast-forward" their own computationally intensive numerical models.

Prerequisites: Basic familiarity with Python and regression concepts. No physics background required.

Source: <https://pretalx.com/pydata-london-2026/talk/J99JNR/>

## 28. [Bridging Pandas and Polars: The Hidden Costs of Dataframe Interoperability](https://pretalx.com/pydata-london-2026/talk/YYTLFF/)

**Speakers**: [Ivo Dilov](https://pretalx.com/pydata-london-2026/speaker/ACWZ7K/)

**When and where**: Saturday, 2026-06-06, 15:30–16:15, room Grand Hall 2

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

The Python data ecosystem is migrating from NumPy-based arrays toward Apache Arrow. Polars is built entirely on Arrow, and Pandas is heading in the same direction. Yet differences in string encoding, missing values, schemas, and index metadata make interoperability between the two formats surprisingly costly and error-prone. This talk examines these challenges through a case study of how ArcticDB, the open-source client-side dataframe database, navigated this same migration.

**Description** (verbatim):

As organisations adopt Polars alongside Pandas, a critical question emerges: how do you move data between the two without silent data loss, performance regressions, or broken round-trips? The answer is more complex than calling `polars.from_pandas`.

Pandas stores data in NumPy arrays by default, though as of 3.0 it uses Arrow for strings. Polars is built entirely on Apache Arrow's columnar format. For each area where these formats diverge, this talk will explain the problem and show how ArcticDB, a dataframe database that must serialize, store, and reconstruct both formats, solves it in practice:

- **Memory layout**: How NumPy and Arrow represent the same logical data differently, and how a dataframe database can bridge the two
- **Strings**: NumPy object arrays vs. Arrow's offset-based binary buffers -- why Arrow is dramatically more efficient and the cost of conversion
- **Missing values**: NaN/NaT/None sentinels vs. Arrow's validity bitmask -- why a Pandas NaN behaves differently from a Polars null and what breaks during conversion
- **Schema differences**: Different supported data types and different allowed column names -- e.g. Pandas allows mixed-type columns that Arrow cannot represent
- **Pandas-specific metadata** that has no Arrow equivalent: Index and RangeIndex semantics, and MultiIndex which uses an entirely different memory layout with its own performance implications

Together, these issues make conversion between Pandas and Polars far from trivial. This is especially challenging for a dataframe database like ArcticDB, where petabytes of Pandas DataFrames are stored and users increasingly want to read them back as Arrow. The talk will include benchmarks comparing native format reads against conversion-based approaches, and practical takeaways for anyone migrating a codebase, building a library that supports both formats, or choosing a dataframe database. The talk will include benchmarks comparing native format reads against conversion-based approaches, and practical takeaways for anyone migrating a codebase, building a library that supports both formats, or choosing a dataframe database.

Source: <https://pretalx.com/pydata-london-2026/talk/YYTLFF/>

## 29. [Using coding agents with open models](https://pretalx.com/pydata-london-2026/talk/HBPSDS/)

**Speakers**: [Sujee Maniyam](https://pretalx.com/pydata-london-2026/speaker/A9KFMS/)

**When and where**: Saturday, 2026-06-06, 16:15–17:00, room Grand Hall 2

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Coding agents such as Cursor and Claude Code are fundamentally changing software development workflows. Most teams, however, still rely primarily on proprietary frontier models.
In this demo-driven session, I will show how to pair modern coding agents with high-performance open models running on Nebius Token Factory, with a focus on developer experience, model behavior, considerations relevant to production use.

Attendees will receive platform credits for getting started immediately with open-model-powered coding agents.

Source: <https://pretalx.com/pydata-london-2026/talk/HBPSDS/>

## 30. [Kafka Streaming, the Pythonic Way](https://pretalx.com/pydata-london-2026/talk/BPJEKV/)

**Speakers**: [Arthur Andres](https://pretalx.com/pydata-london-2026/speaker/TSF8WA/)

**When and where**: Saturday, 2026-06-06, 10:20–11:05, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Adopting a streaming architecture as a Python developer often means abandoning the tools and abstractions you know: DataFrames, batch processing, familiar data workflows, in favour of an entirely different mental model. After ten years of tackling this problem across multiple companies, I've learned it doesn't have to be that way.

In this talk, I'll show how to treat Kafka not as a stream of individual messages but as a source of micro-batches, and how to deserialize those messages, whether JSON or Protobuf, into Arrow-backed DataFrames. The result: your processing code looks the same whether the data comes from a Parquet file or a Kafka topic.

No heavy framework required. Using confluent-kafka and Apache Arrow, I'll walk through how to build this from the ground up, so you understand every layer of the stack.

**Description** (verbatim):

The talk opens with a concrete example of stream processing. We have data flowing in, and a clear task to perform on it. No theory, no definitions, just a practical scenario the audience can immediately relate to.

From there, we step back and look at how Kafka works. Topics, consumers, partitions, message formats. Just enough to understand the architecture behind the example, and to appreciate why Kafka has become the standard backbone for streaming systems.

Then comes the friction. When you consume from Kafka, you get one message at a time. Each message is serialized as JSON or Protobuf. If you're a Python developer used to working with DataFrames, this feels like going back to writing for loops over rows. We'll look at what the naive approach looks like in code, and why it quickly becomes painful as processing logic gets more complex.

With the problem clearly felt, we introduce the solution: treating Kafka not as a stream of individual messages but as a source of micro-batches, and deserializing those batches directly into Arrow-backed DataFrames using confluent-kafka and Apache Arrow. The processing code that follows looks identical to what you'd write against a Parquet file. We'll see both versions side by side to make this concrete.

We close with lessons learned from applying this pattern in production over ten years. What breaks, what surprises you, and what trade-offs you should be aware of before adopting this approach in your own systems.

The talk assumes familiarity with Python and basic data processing with DataFrames. No prior knowledge of Kafka or streaming is required.

Source: <https://pretalx.com/pydata-london-2026/talk/BPJEKV/>

## 31. [Beyond Spark MLlib: Deduplicating Common Crawl at Scale](https://pretalx.com/pydata-london-2026/talk/T7GMEL/)

**Speakers**: [Ken Obata](https://pretalx.com/pydata-london-2026/speaker/RUXK7W/)

**When and where**: Saturday, 2026-06-06, 11:05–11:50, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Training large language models requires massive, high-quality text corpora—but web-scale datasets like Common Crawl contain significant near-duplicate content that degrades model performance and wastes compute. Existing solutions like Spark MLlib's MinHashLSH suffer from UDF serialization overhead and shuffle explosion, causing out-of-memory failures at scale.

We present a partition-aware MinHash LSH system that co-locates similar documents within Spark partitions, dramatically reducing cross-partition shuffles during similarity computation. Our approach combines vectorized MinHash generation using mathematical permutation tricks, band-based candidate filtering with configurable collision limits to handle edge cases like boilerplate false positives, and GraphFrames-based connected components for transitive deduplication.

Benchmarks on Common Crawl 253.4 million documents, generating 2.1 billion candidate pair
completed in under five hours on a 9-node r5d.8xlarge EMR cluster. We discuss key optimizations including partition-aware MinHash LSH and band collision filtering for common boilerplate content.
Attendees will learn partition-aware LSH design patterns, strategies for handling boilerplate-induced false positives, and how to integrate deduplication into existing Spark ETL pipelines. The system will be open-sourced, enabling practitioners to deploy production-ready deduplication pipelines for their own LLM training workflows.

**Description** (verbatim):

<Why This Matters for LLM Practitioners>
Training data quality is the bottleneck for LLM performance. Research shows duplicate content causes memorization, reduced generalization, and wasted compute (Lee et al., 2022). Yet existing tools fail at web scale: Spark MLlib's MinHashLSH suffers shuffle explosion causing OOM errors, while Google's deduplicate-text-datasets requires 600GB+ RAM on a single machine.

<What You'll Learn>
This talk introduces a partition-aware MinHash LSH system built with PySpark and NumPy that scales horizontally on commodity clusters. The key innovation: using LSH band hashes to drive Spark's partitioning, co-locating similar documents before comparison and eliminating cross-partition shuffles entirely.

<Target Audience>
Data engineers and ML practitioners working with large text corpora for NLP/LLM applications. Familiarity with PySpark basics and general understanding of similarity matching is helpful but not required.

<Talk Outline>
Minutes 0-5: The deduplication challenge - why LLM training data needs deduplication, why O(N²) comparisons are infeasible, why you can't split into independent batches
Minutes 5-10: Why existing tools fail - MLlib shuffle explosion, Google's memory requirements
Minutes 10-18: Our solution - partition-aware MinHash LSH architecture, code walkthrough showing pandas_udf vectorization and band-based partitioning
Minutes 18-25: Worked example - following two documents through the pipeline: hashing → band assignment → partition co-location → local candidate generation → connected components
Minutes 25-30: Benchmarks and practical lessons - 253M documents, 2.1B candidate pairs, under 5 hours, under $100. boilerplate filtering with MAX_BAND_SIZE
Minutes 30-40: Q&A

<Key Takeaways>
How to use LSH band hashes to drive Spark partitioning for local similarity computation
Vectorized MinHash generation with NumPy and pandas_udf to avoid Python UDF overhead
Strategies for handling boilerplate-induced false positives at scale
A production-ready architecture that will be open-sourced

<Background Knowledge>
Basic PySpark familiarity (DataFrames, partitions). No prior knowledge of MinHash or LSH required — these concepts will be explained.

Source: <https://pretalx.com/pydata-london-2026/talk/T7GMEL/>

## 32. [Governance-as-Code for the Lakehouse: Zero Trust with Iceberg REST Catalog and Policy Engines](https://pretalx.com/pydata-london-2026/talk/8JJUKQ/)

**Speakers**: [Viktor Kessler](https://pretalx.com/pydata-london-2026/speaker/P8BGN9/)

**When and where**: Saturday, 2026-06-06, 11:50–12:35, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Modern lakehouse architectures promise flexibility and scale — but governance is often an afterthought. While we version data and evolve schemas, we rarely version or test access policies.

This talk explores how to implement governance-as-code in a lakehouse using the REST Catalog from Apache Iceberg, applying Zero Trust principles and enforcing fine-grained policies with Open Policy Agent (OPA) and Cedar.

Attendees will learn how to move from static IAM and implicit trust to centralized, engine-agnostic, policy-driven governance.

**Description** (verbatim):

Lakehouse architectures unify data lakes and warehouses, but governance models often lag behind the architectural innovation. Access control is frequently engine-specific, policies are fragmented, and trust is implicit.

This talk argues that the missing layer in many lakehouse implementations is governance-as-code enforced at the catalog boundary.

**We explore:**

- How the Iceberg REST Catalog introduces a centralized enforcement point decoupled from compute engines
- Why Zero Trust principles apply to data platforms (no implicit trust between engines, users, or services)
- How policy-as-code systems such as OPA and Cedar enable versioned, testable, auditable access control
- Patterns for implementing fine-grained authorization (row/column-level policies, environment isolation, service-to-service trust)
- How governance becomes reproducible and portable across Spark, Flink, Trino, and other engines

The session focuses on architectural patterns rather than vendor-specific tooling and highlights practical trade-offs when implementing policy enforcement in production lakehouses.

**Key Takeaways**

1. Understand why traditional RBAC is insufficient for modern lakehouses
2. Learn how REST-based catalog architectures enable centralized governance
3. See how Zero Trust can be applied to data access workflows
4. Discover how to implement policy-as-code using OPA or Cedar
5. Gain a reference architecture for governance-first lakehouse design

Source: <https://pretalx.com/pydata-london-2026/talk/8JJUKQ/>

## 33. [MCP, or not MCP](https://pretalx.com/pydata-london-2026/talk/QMGS7U/)

**Speakers**: [Neal Richardson](https://pretalx.com/pydata-london-2026/speaker/TLHZQ3/)

**When and where**: Saturday, 2026-06-06, 14:45–15:30, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Model Context Protocol is a standard for defining tools that can be made available to LLMs and AI applications. There’s a lot of noise out there about what you should use to get the best results from AI, so in this talk, I will provide some guidance on when you should use MCP, and when you should reach for some other tool. I will describe cases where MCP is the right tool for the job, and when other things, like skills or other context files, are better. I will also devote attention to questions of security and authentication, which are important for MCP, and provide concrete examples of how MCP servers can be used to unlock agentic workflows while also strengthening data governance. This talk is intended for those who are interested in using LLMs for workflows involving data. No prior experience with MCP is required.

**Description** (verbatim):

Outline:

- Intro: how can I get data from this API into my Claude Code session?
- What is MCP? When should you use it, when should you use other tools
- Work through an example
- Sharing and deploying MCP servers, alternatives and best practices
- Optimizing your tools for best results

Source: <https://pretalx.com/pydata-london-2026/talk/QMGS7U/>

## 34. [Build your castle, dig your moat: AI sovereignty, provenance and compliance](https://pretalx.com/pydata-london-2026/talk/T7BQTG/)

**Speakers**: [Daina Bouquin](https://pretalx.com/pydata-london-2026/speaker/PZEMN7/)

**When and where**: Saturday, 2026-06-06, 15:30–16:15, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Your intelligent application is your castle, and your security practices are the moat that protects it. Inside your castle, you must aim for full visibility into what you’re running and why, with freedom to iterate. Your moat creates your security perimeter, ensuring no proprietary data leaves your castle and enforcing best practices including data provenance, cryptographically signed models, evaluation tools, build pipelines and reproducible environments.

Build on your infrastructure, answer to your requirements, scale on your terms.

**Description** (verbatim):

In this talk you’ll learn…

• What AI sovereignty actually means for your stack and your business
• How to evaluate self-hosted, local LLMs
• Overview of supply chain security controls for data and code artifacts – provenance, signatures and compliance measures, opacity and trust signals

Source: <https://pretalx.com/pydata-london-2026/talk/T7BQTG/>

## 35. [Documenting your open source projects for machines](https://pretalx.com/pydata-london-2026/talk/3MAU9W/)

**Speakers**: [Jacob Tomlinson](https://pretalx.com/pydata-london-2026/speaker/EE7H7J/)

**When and where**: Saturday, 2026-06-06, 16:15–17:00, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

As coding agents grow in popularity, open source project documentation is increasingly consumed by LLMs. When people build things with your open source library their agent will read your documentation and write code based on what it discovers there. To ensure your users have a good experience we need to start thinking about how to write and publish our documentation to make sure agents produce the best code possible.

Coding agents are now on the critical path for making decisions around which libraries to use. For open source developers it’s important to market your projects to LLMs as well as humans. Publishing material about the project in a way that is easy to discover and parse for models is key to increasing adoption.

This talk will cover key things you need to know to make your project successful in a coding agent world:

- SEO for the LLM age
- Publishing your docs in context efficient formats like markdown
- Providing plentiful examples that ensure agents produce idiomatic code for your library
- Adding LLM specific information to the documentation to help shape behaviour

**Description** (verbatim):

Introduction (5 mins)
How LLM tools consume documentation pages (5 mins)
Quick steps you can take to improve things (5 mins)
Build markdown pages with sphinx-llm or mkdocs-llmstxt
Helping LLMs write idiomatic code for your library (5 mins)
Constraining how your code is used (5 mins)
Conclusions (5 mins)

Source: <https://pretalx.com/pydata-london-2026/talk/3MAU9W/>

## 36. [From Noisy Sensors to Events: Event Detection in Sensor data with Kalman Filters and Hidden Markov Models](https://pretalx.com/pydata-london-2026/talk/EQZ7VK/)

**Speakers**: [Ono Gantsog](https://pretalx.com/pydata-london-2026/speaker/NUPWSA/)

**When and where**: Saturday, 2026-06-06, 10:20–11:05, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Sensors operating in complex environments produce noisy data. Determining exactly when a system transitions between states — and what values it is recording — is surprisingly hard: vibrations, environmental changes, and gradual shifts all conspire against simple threshold approaches. This talk walks through a real-world Python pipeline that solves this problem, starting with classical signal processing, exposing its failure modes, and then building a principled solution using a Kalman filter for noise reduction coupled with a Hidden Markov Model (HMM) for state inference. Attendees will leave understanding how to frame sensor problems as state estimation tasks and how to apply these techniques in Python using necessary libraries.

**Description** (verbatim):

Objective
Many operations depend on accurate data from continuous sensor streams. Knowing when a system transitions between states, when a process cycle completes, and how much change occurred per cycle drives scheduling, monitoring, and operational reporting. This talk presents a complete data science pipeline — built entirely in Python — that automates event detection and value estimation from noisy sensor streams. The goal is to give attendees both a worked real-world case study and a transferable toolkit for tackling noisy, event-driven sensor data in any domain.

The Problem
Sensors record measurements continuously, but the raw signal is far from clean. Vibrations, speed changes, and environmental shifts all create noise that masks the true underlying state of the system (for example: wake, light sleep, deep sleep, REM sleep). A naive threshold-based approach — the initial "traditional method" — is brittle: it misfires on transient spikes, misses gradual transitions, and cannot estimate values reliably. This section sets up the problem visually with annotated sensor traces and shows concretely where simple methods break down.

Why Kalman Filter + Hidden Markov Model?
The key insight is that the system operates as a latent state machine: at any moment it is in one of a small number of discrete states (idle, transitioning, active, completing), and what we observe is a noisy function of that state. This framing motivates a two-stage approach: Kalman Filter — smooths the raw signal, handles sensor noise, and provides a principled estimate of the true instantaneous value with an associated uncertainty. Hidden Markov Model — takes the smoothed signal and infers the sequence of hidden states, including the timing of transitions and the most probable value estimate at peak. The talk explains the intuition behind both models without heavy mathematics, and then shows how to implement them in Python with filterpy (Kalman) and hmmlearn (HMM).

Source: <https://pretalx.com/pydata-london-2026/talk/EQZ7VK/>

## 37. [Mapping the local heat transition: from large-scale geospatial data to real-world impact](https://pretalx.com/pydata-london-2026/talk/CKV8PH/)

**Speakers**: [Sofia Pinto](https://pretalx.com/pydata-london-2026/speaker/7HMSUV/), [Simran Dave](https://pretalx.com/pydata-london-2026/speaker/UM38T7/)

**When and where**: Saturday, 2026-06-06, 11:05–11:50, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Decarbonising UK’s home heating is one of the greatest challenges of the Net Zero transition, yet it currently relies on individual household decisions supported by government incentives. To help accelerate the local delivery, we are building a tool that maps the most suitable low-carbon heating for clusters of properties at a neighbourhood level.

In this talk we will walk through our end-to-end data science pipeline, covering processing of large-scale geospatial data, the nuances of modelling where ground truth data does not yet exist, and how to translated local authorities needs into a functional product. We will present our Python tech stack and will conclude with a showcase of the user interface.

Whether you're interested in geospatial data engineering, machine learning for social good, or how to work within a multidisciplinary team, this talk offers a blueprint for building data products with real-world impact.

**Description** (verbatim):

Decarbonising UK’s home heating is one of the greatest challenges of the Net Zero transition, yet it currently relies on individual household decisions supported by government incentives. To help accelerate the local delivery, we are building a tool that maps the most suitable low-carbon heating for clusters of properties at a neighbourhood level.

We will walk through the end-to-end journey of building a data product, from handling open data (such Ordnance Survey products and EPC) to designing a user interface that empowers non-technical decision-makers.

What we will cover:

- Our data science pipeline: Processing large-scale geospatial data, deployment of classification models and clustering algorithms, evaluating pipelines where ground truth data does not yet exist, etc
- Our Python tech stack
- A walkthrough of the user interface
- The process of translating the needs of local authorities into a functional and intuitive product

Who should attend?
No prior technical knowledge is required. Whether you are a data science newcomer or a seasoned professional with a decade of experience, this talk is designed to be accessible to all. We welcome:

- Data scientist, engineers, academics, machine learning engineers curious about how data science operates within a mission-driven, not-for-profit context.
- Project and product managers looking for a roadmap to steer complex data products from concept to delivery.

Key takeaways:
By the end of this session, you will gain a deeper understanding of:

- Data science in practice: data science techniques and libraries used
- Applying data science for impact: How to bridge the gap between complex modelling and the practical needs of external stakeholders
- Multidisciplinary collaboration: lessons earned from a team of data scientists, full-stack developers, designers, and domain experts working toward a common goal.

Source: <https://pretalx.com/pydata-london-2026/talk/CKV8PH/>

## 38. [Hazards on the Causal Path: Bayesian Time-Varying Survival Analysis with PyMC](https://pretalx.com/pydata-london-2026/talk/A38MW7/)

**Speakers**: [Nathaniel Forde](https://pretalx.com/pydata-london-2026/speaker/GB9KHE/)

**When and where**: Saturday, 2026-06-06, 11:50–12:35, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Dynamic Path Analysis (DPA) extends survival analysis with a causal, time-varying perspective. This allows causal effects to be decomposed into direct and indirect pathways that evolve over time. The perspective is particularly valuable when interventions (exercise) act through mediators (weight loss) whose influence changes dynamically in time, because we get to distil when each driver of our survival probabilities are active and whether their combined effects are harmful or positive.

Despite its conceptual appeal, DPA remains niche, with existing implementations limited to frequentist R packages and no Bayesian or Python-native alternatives. In this talk, I present a Bayesian, generative implementation of Dynamic Path Analysis using PyMC. By discretising time and modelling cumulative hazard effects with smooth spline priors, we obtain interpretable time-varying causal effects with coherent uncertainty quantification. I benchmark the approach against canonical dpasurv examples and discuss why DPA focuses on hazards rather than survival curves.

This talk is aimed at Python users interested in survival analysis, causal inference, and Bayesian modelling.

**Description** (verbatim):

Survival analysis is often used to answer when an event occurs, but in many real-world settings we also care about how and through which mechanisms interventions exert their effects over time. Dynamic Path Analysis (DPA), introduced by Aalen and colleagues, addresses this by decomposing time-varying effects on the hazard into direct and mediated causal pathways, allowing these relationships to evolve dynamically.

In this talk, I present a Bayesian, generative reinterpretation of Dynamic Path Analysis implemented in PyMC. The model discretises time into intervals and represents cumulative hazard effects using smooth spline-based priors, enabling stable estimation of time-varying direct and indirect effects with full posterior uncertainty. I show how this approach recovers the qualitative behaviour of canonical dpasurv examples while extending them to a fully probabilistic framework.

The emphasis is on the causal decomposition of hazards, clarifying why DPA is well suited to reasoning about evolving mediation structures and intervention planning. The talk highlights how generative Bayesian models make these ideas more flexible, interpretable, and extensible within the Python ecosystem. We end with practical recipes for using g-computation to derive non-parametric estimates of direct, indirect and survival-curve-differences from the fitted DPA model.

Target audience: data scientists and researchers with some familiarity with survival analysis or Bayesian modelling.

Takeaway: attendees will understand when and why to use dynamic causal hazard models, and how to implement them in practice using PyMC.

Source: <https://pretalx.com/pydata-london-2026/talk/A38MW7/>

## 39. [Did Your Rollout Actually Work? Measuring Phased Launches with Staggered DiD in Python](https://pretalx.com/pydata-london-2026/talk/H7PFXK/)

**Speakers**: [Benjamin Vincent](https://pretalx.com/pydata-london-2026/speaker/JH9SPA/)

**When and where**: Saturday, 2026-06-06, 14:45–15:30, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Your company launches a loyalty program — but not everywhere at once. Ten stores get it in January, another ten in March, the rest later. Leadership asks: "Did it work? By how much?" You compare before and after... and get a number that's wrong. Phased rollouts break naive pre/post comparisons, and standard regression quietly gives misleading answers.

This talk shows a practical Python workflow for getting it right. Using a realistic store-rollout example and CausalPy (an open-source library), I'll demonstrate how to produce event-study plots that show _when_ and _how much_ an intervention takes effect — with uncertainty estimates your stakeholders can actually act on. Whether you're measuring feature flags, marketing campaigns, or policy changes, you'll leave with a reproducible notebook and a step-by-step workflow you can apply tomorrow.

**Description** (verbatim):

### Who this is for

Data scientists, analysts, and applied ML/measurement practitioners who evaluate interventions using observational or quasi-experimental data (e.g., feature flags, phased launches, regional changes). Familiarity with pandas and basic regression is helpful; no prior Bayesian experience required.

### What attendees will learn (takeaways)

- How staggered adoption differs from "textbook" two-period Difference-in-Differences, and why the difference matters in production measurement.
- How the imputation-based estimator (Borusyak, Jaravel & Spiess, 2024) works: fit on untreated observations, predict counterfactuals, aggregate by event time.
- How to turn model output into stakeholder-friendly language: probability of positive effect, expected uplift, decision thresholds — no Bayesian background needed.
- The parameter recovery pattern: validate your method on simulated data with known truth before trusting it on real data.
- Practical diagnostics and red flags: parallel trends, anticipation effects, spillovers, and when _not_ to use this method.

### Outline and time plan (30 min talk + 10 min Q&A)

- 0–4 min: The real-world problem — phased rollouts and why naive pre/post comparisons fail
- 4–10 min: DiD refresher, then what breaks under staggered adoption (timing heterogeneity, negative weighting in TWFE)
- 10–17 min: The staggered DiD solution (event-time framing, imputation intuition, key assumptions)
- 17–25 min: Worked example in Python with CausalPy
  - A loyalty program rolled out to 60 stores in 3 waves over 30 weeks
  - Visualise adoption timing and check pre-trends
  - Fit the model and produce event-study plots
  - Parameter recovery: compare estimated effects to known ground truth
- 25–28 min: Diagnostics — pre-treatment placebo checks, counterfactual inspection, "when not to use this" decision checklist
- 28–30 min: Summary — three takeaways and the six-step workflow
- 30–40 min: Q&A

### Background knowledge needed

- Comfortable with tidy data, grouping/aggregating, and reading a regression coefficient.
- Basic causal inference vocabulary (treatment/control, confounding) is helpful but not required.

### What I will provide

A public GitHub repository containing:

- a reproducible Quarto notebook (the slides themselves, with all code),
- a synthetic dataset simulating a realistic store loyalty program rollout,
- and environment setup instructions (conda environment file).

Source: <https://pretalx.com/pydata-london-2026/talk/H7PFXK/>

## 40. [Do Multilingual Embeddings Really Share a Semantic Space? Practical Lessons Across Scripts and Languages](https://pretalx.com/pydata-london-2026/talk/JWNWFQ/)

**Speakers**: [Kavit Tolia](https://pretalx.com/pydata-london-2026/speaker/PZW3NB/)

**When and where**: Saturday, 2026-06-06, 15:30–16:15, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Multilingual embeddings are often assumed to place different languages into a shared semantic space. In practice, that alignment breaks down in systematic ways.

This talk explores where multilingual embeddings work, where they fail, and why. Using examples across multiple languages, I show how tokenisation, training data imbalance, and semantic ambiguity shape embedding behaviour in practice, along with practical diagnostics for evaluating multilingual embeddings.

**Description** (verbatim):

Multilingual embedding models are widely used in retrieval, search, recommendation, and RAG pipelines under the assumption that semantically similar text across languages occupies a shared embedding space.

This talk examines how true that assumption is in practice.

Using pre-trained multilingual embedding models, I explore examples where multilingual alignment works extremely well, and others where it breaks down unexpectedly. Across multiple languages, we will look at how tokenisation, training data imbalance, and semantic ambiguity shape embedding geometry and retrieval behaviour.

Rather than focusing on benchmark performance, the talk emphasises intuition and failure analysis:

- Why do some languages align much more reliably than others?
- Why do averages often hide important multilingual failures?
- What happens when semantic ambiguity enters the embedding space?

Through UMAP projections, nearest-neighbour analyses, tokenisation patterns, and translation similarity distributions, we will build a practical mental model for understanding multilingual embeddings beyond the assumption of “one shared semantic space.”

The talk concludes with concrete diagnostics practitioners can use, along with common failure modes to watch for in applications.

Source: <https://pretalx.com/pydata-london-2026/talk/JWNWFQ/>

## 41. [Designing Semantic Memory for Multi-Agent Systems with Python](https://pretalx.com/pydata-london-2026/talk/JFJFQX/)

**Speakers**: [Theo van Kraay](https://pretalx.com/pydata-london-2026/speaker/JNRLGN/)

**When and where**: Saturday, 2026-06-06, 16:15–17:00, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Multi-agent GenAI systems don’t fail because models lack intelligence, they fail because they lack memory.

As LLM applications move from demos to production, semantic memory becomes the defining systems challenge. Agents must remember user preferences, share context across roles, preserve conversational state across sessions, and evolve over time, all without exploding token costs or losing observability.

In this talk, I’ll explore semantic memory as a data engineering problem rather than a prompt engineering trick. Drawing on real-world experience from the Azure Cosmos DB engineering team, we’ll examine how to design layered memory for multi-agent systems in Python: short-term conversational state, episodic event logs, declarative and procedural memory, and retrieval-driven personalization.

Using a practical multi-agent travel planner built with LangGraph, we’ll implement patterns such as session-level versus per-turn persistence, hybrid retrieval design (structured filters plus semantic signals), memory lifecycle management (write, retrieve, summarize, supersede, expire), and checkpointed workflows for reproducibility and debugging.

You’ll leave with practical design heuristics for building agent systems that become more reliable, more efficient, and more explainable over time.

All demonstrations will be in Python and applicable to production-scale systems.

**Description** (verbatim):

This session focuses specifically on semantic memory architecture as the critical systems layer in production-grade multi-agent AI applications.

From my role on the Azure Cosmos DB engineering team, I’ve worked with teams building large-scale agentic systems that must support multi-tenancy, personalization, long-lived conversational state, and operational observability. A consistent lesson is that orchestration frameworks coordinate agents, but memory design determines whether the system behaves coherently over time.

The talk will cover:

- A practical taxonomy of agent memory: short-term state, episodic logs, declarative knowledge, and procedural memory
- Modeling conversations as append-only event streams versus mutable session documents
- Designing retrieval-aware memory stores that combine structured filtering with semantic signals
- Memory lifecycle management: summarization spans, supersession flags, retention windows, and TTL-based compaction
- Checkpointed agent workflows for traceability and debugging
- Multi-tenant memory partitioning strategies
- Cost tradeoffs between growing context windows and durable storage

A live Python-based multi-agent travel planner (built with LangGraph and backed by Azure Cosmos DB) will demonstrate these patterns in practice, including MCP-based memory tools that separate reasoning from storage concerns.

The goal is to provide PyData attendees with a concrete systems framework for thinking about semantic memory, not as an afterthought to prompting, but as a first-class data architecture problem at the intersection of distributed systems and applied AI.

Source: <https://pretalx.com/pydata-london-2026/talk/JFJFQX/>

## 42. [PyMC Code Sprint](https://pretalx.com/pydata-london-2026/talk/BUEZSA/)

**Speakers**: [Chris Fonnesbeck](https://pretalx.com/pydata-london-2026/speaker/MZZ8YC/), [Oriol Abril Pla](https://pretalx.com/pydata-london-2026/speaker/MKEJ7N/)

**When and where**: Saturday, 2026-06-06, 10:25–12:25, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Come build something with the PyMC development team.

Code sprints are collaborative working sessions where contributors of all experience levels tackle meaningful open issues side by side. Whether you want to squash a long-standing bug, sharpen the documentation, build a worked example, or simply understand how a major open-source project operates from the inside — there's a place for you here.
PyMC is the most widely used probabilistic programming library in Python, and the people who build it will be in the room. Bring your laptop; we'll handle the rest.

Source: <https://pretalx.com/pydata-london-2026/talk/BUEZSA/>

## 43. [Diversity Scholar Luncheon](https://pretalx.com/pydata-london-2026/talk/RZPMEY/)

**Speakers**: [NumFOCUS](https://pretalx.com/pydata-london-2026/speaker/88WGFJ/)

**When and where**: Saturday, 2026-06-06, 12:35–13:35, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

"Join us for a relaxed lunch gathering to meet this year's handpicked scholars - a group of exceptional people bringing fresh perspectives to our community.

This is a chill bring-your-plate space to meet some of the PyData 2026 diversity team and welcome some fine folks with diverse interests & experiences. Let's find conversation over lunch and a shared table.

Space permitting, all are welcome, and speakers and allies are encouraged to squeeze in!"

Source: <https://pretalx.com/pydata-london-2026/talk/RZPMEY/>

## 44. [Unconference- Feminist AI](https://pretalx.com/pydata-london-2026/talk/8SWJS9/)

**Speakers**: [Cheuk Ting Ho](https://pretalx.com/pydata-london-2026/speaker/8EGVC9/)

**When and where**: Saturday, 2026-06-06, 14:45–15:30, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Join our chill space, unwind, chat about Feminist AI and contribute to the PyData London DIY collage zine.

Source: <https://pretalx.com/pydata-london-2026/talk/8SWJS9/>

## 45. [Lightning Talks](https://pretalx.com/pydata-london-2026/talk/YPFBTB/)

**Speakers**: [NumFOCUS](https://pretalx.com/pydata-london-2026/speaker/88WGFJ/)

**When and where**: Sunday, 2026-06-07, 09:00–09:45, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Lightning talk sign up will take place at the NumFOCUS booth all day Saturday.

Source: <https://pretalx.com/pydata-london-2026/talk/YPFBTB/>

## 46. [Your ML Pipeline Meets the EU AI Act](https://pretalx.com/pydata-london-2026/talk/NMFNQJ/)

**Speakers**: [Gabriel Lipnik](https://pretalx.com/pydata-london-2026/speaker/8GMGYR/)

**When and where**: Sunday, 2026-06-07, 10:15–11:00, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

The EU AI Act is often seen as a legal concern, but many of its requirements directly affect everyday ML workflows. This talk shows data scientists and ML engineers where the regulation impacts the machine learning lifecycle and presents concrete, low-overhead patterns to make ML systems more AI Act–ready, without slowing down development.

**Description** (verbatim):

Resources with slides and interactive checklist: anx.io/SI1ja

The EU AI Act introduces new obligations that will directly affect how machine learning systems are designed, evaluated, and operated. While the regulation is often discussed from a legal perspective, many of its practical consequences fall squarely into the domain of data scientists and ML engineers.

This talk provides an engineering-focused walkthrough of where the EU AI Act intersects with the modern ML lifecycle. We map key regulatory expectations to familiar technical stages such as data collection, model training, evaluation, deployment, and monitoring. Rather than diving into legal detail, the session focuses on concrete implementation patterns and common failure modes observed in real-world ML workflows.

Attendees will learn how to perform lightweight risk classification, identify typical compliance gaps in existing pipelines, and apply design patterns that improve traceability, documentation, and monitoring without significantly slowing down development. The talk concludes with a practical readiness checklist that teams can immediately apply to their own systems.

Target audience: data scientists, ML engineers, and MLOps practitioners working with production ML systems.

Expected background: familiarity with the basic ML lifecycle and model deployment concepts. No prior knowledge of the EU AI Act is required.

Key takeaways:

- Understand where the EU AI Act impacts ML pipelines
- Learn practical patterns for AI Act readiness
- Avoid common compliance pitfalls in production ML
- Leave with a concrete checklist for next steps

Source: <https://pretalx.com/pydata-london-2026/talk/NMFNQJ/>

## 47. [The Silent Crash: Why Your RAG Evaluation Metrics Are Lying to You](https://pretalx.com/pydata-london-2026/talk/MMS9WY/)

**Speakers**: [Hitendri Bomble](https://pretalx.com/pydata-london-2026/speaker/87KSCF/), [Arghyadeep Sarkar](https://pretalx.com/pydata-london-2026/speaker/TN73JB/)

**When and where**: Sunday, 2026-06-07, 11:00–11:45, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

We rely on dashboards to tell us if our RAG system is working. But most standard metrics, Cosine Similarity, BLEU, and even BERTScore, are fundamentally broken for measuring factual correctness. They measure text overlap or semantic drift, not truth.

This means you can have a "90% Accurate" system on paper that hallucinates dangerous misinformation in production. This talk dismantles the current state of RAG evaluation. We will look at why "Golden Datasets" are often contaminated, why "LLM-as-a-Judge" is biased towards its own output, and how to build a robust, adversarial evaluation pipeline that actually catches failures before your users do.

**Description** (verbatim):

Picture this: You’ve just finished your RAG pipeline. The test dashboard is all green, Context Recall is 85%, Answer Relevance is 92%. You deploy with confidence. Ten minutes later, a user asks a simple question, and the bot confidently gives the wrong answer.

Why did the metrics pass? Because **similarity is not correctness**. To a vector database, "The treatment is safe" and "The treatment is not safe" look nearly identical, they share the same words and sentence structure. But logically, they are opposites. Standard metrics like Cosine Similarity or BLEU often completely miss these critical negations.

In this talk, we are going to stop relying on "vibe checks" and start treating Evaluation as a software testing problem. We’ll look at why traditional NLP metrics are useless for RAG and move toward the new standard: **LLM-as-a-Judge**. We will discuss the messy reality of using GPT-4 to grade Llama-3, how to catch "Self-Preference Bias" (where models just like their own writing style), and how to do all of this without bankrupting your API budget.

**Outline**

- **Real-world examples** where high metrics hid major failures, and why "Finding the doc" (Retrieval) is different from "Answering the question" (Generation).
- Why Your Metrics Are Broken: Why **Cosine Similarity is good for search but bad for truth**, and why BLEU scores punish correct answers just for using different synonyms.
- Using models (like G-Eval) to grade logic and tone, and solving the "Judge Paradox" by swapping options to remove Position Bias.
- Building a "Hard" Test Set: How to stop testing on easy questions and generate adversarial "Trick Questions" that specifically target your retrieval gaps.
- Key Takeaways: A practical strategy for using metrics, plus a look at tools like Ragas and DeepEval.

Source: <https://pretalx.com/pydata-london-2026/talk/MMS9WY/>

## 48. [Vibe NLP for Applied NLP](https://pretalx.com/pydata-london-2026/talk/CJGBGV/)

**Speakers**: [Ines Montani](https://pretalx.com/pydata-london-2026/speaker/FZKG9N/)

**When and where**: Sunday, 2026-06-07, 11:45–12:30, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

One of the hardest parts of applied NLP has always been breaking down complex business problems into machine learning components. It's so hard because it requires domain expertise and reasoning about the specific use case, and it's the one thing technology couldn't fix. But what if we could take some of the learnings from AI-powered coding assistants and apply them to solving real-world NLP problems? In this talk, I'll show how we've built powerful assistants and tools to help developers solve NLP tasks using open-source software, and create modular solutions that are small, fast and fully data-private.

**Description** (verbatim):

At the core of it is an often overlooked idea: using LLMs to _build systems_ instead of _as systems_. AI-powered coding assistants have transformed the way we build software – and they can be even more impactful for AI development itself and bridge the experience gap that's often holding teams back and causing projects to fail. In the talk, I will show you a new way of using generative models for AI development, and some practical examples of how to make "Vibe NLP" work for real-world problems.

Source: <https://pretalx.com/pydata-london-2026/talk/CJGBGV/>

## 49. [Keynote- Martin O'Reilly- LLMs and AI agents demystified](https://pretalx.com/pydata-london-2026/talk/XQXNVK/)

**Speakers**: [Martin O'Reilly](https://pretalx.com/pydata-london-2026/speaker/CS8QA9/)

**When and where**: Sunday, 2026-06-07, 13:30–14:15, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Large language models (LLMs) have taken the world by storm since the public launch of ChatGPT 3 in November 2022, sparking a huge number of LLM-powered tools, products and start-ups. Since then LLMs have gained reasoning and tool use capabilities, and have been integrated into more autonomous agentic workflows, leading to significant increases in their usefulness for software engineering work. However, despite being readily accessible to us all, these models and their agentic wrappers remain black boxes to many of us using them in our daily work.

Martin will demysitify LLMs by providing an intuitive understanding of how they build upon key prior advances to successfully cross the "uncanny valley" of text generation and achieve almost flawless fluency. He will explain what makes these models "foundational", illustrating how this "one weird trick" of next word prediction results in models that can be easily fine-tuned for conversation, coding and reasoning, and we'll take a peek under the hood of how LLMs have been extended to integrate private data sets, call external tools and support more autonomous agentic workflows.

This talk won't make you an expert on deep neural networks, transformers, fine-tuning or agentic workflows, but it will give you a peek behind the curtain of how these seemingly magical models work and hopefully give you enough intuitive understanding to explain them to friends and family.

Source: <https://pretalx.com/pydata-london-2026/talk/XQXNVK/>

## 50. [AI-Assisted Creative for Automated Marketing using Python](https://pretalx.com/pydata-london-2026/talk/GBGB9X/)

**Speakers**: [Matt Crooks](https://pretalx.com/pydata-london-2026/speaker/ESQ8WB/)

**When and where**: Sunday, 2026-06-07, 14:45–15:30, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Our video streaming service hosts vast catalogue of content, but producing tailored marketing assets is slow, manual, and costly and therefore limited to the most popular shows with the biggest budgets. This talk describes how we’re using python to automate the creation of thousands of marketing assets to promote our full catalogue on and off-platform. The system combines audience data, programme metadata, machine learning, and automated rendering in Adobe After Effects. For editorial safety, we’ve built AI-assisted QA layers, automated Slack messaging, and plotly dash apps to allow controlled human review and intervention. All using python (mostly!)

**Description** (verbatim):

Large content catalogues create a classic long-tail problem: while a small number of titles receive heavy promotion, a large proportion of overall consumption comes from many programmes with relatively small individual audiences. Producing bespoke marketing assets for this long tail is usually impractical, as traditional workflows rely on manual design and editing.

This talk presents a real-world Python-based system that automates marketing asset production at scale by combining audience data, asset metadata, machine learning models and automated rendering through Adobe After Effects. The pipeline generates thousands of platform-specific video and image assets, including multi-title creatives populated dynamically using recommendation outputs. We’ve even gone a step further by tapping into catalogue ads in paid social marketing and we’re able to deploy direct to audience-facing without any human intervention using python’s Dropbox API.

A key focus of the talk is how we made automation safe for audience-facing outputs without compromising editorial standards. We will cover the design of automated QA layers that utilise python’s OpenAI API, rule-based validation, and alerting mechanisms using python’s Slack API that trigger human intervention when necessary. Plotly dash apps allow review and controlled interventions such as blacklisting problematic shows.

While the domain is media, the architectural challenges can be applied to other data-driven workflows: orchestration, quality assurance, risk management and human-in-the-loop design. The session is aimed at data scientists, ML engineers and data engineers interested in automation and production pipelines. The talk will aim to be accessible to all and focus on the application and output interspersed with relevant python code snippets.

Rough timings:
0–5 min — The long-tail problem in large content catalogues
5-10 min — Examples of marketing creative
10 - 15 min — Demo of running Adobe After Effects through python
15 - 25 min — System overview: data sources, models, and orchestration
25–30 min — Making automation safe: QA layers, rules, tooling, and alerting
30–35 min — Multi-title assets and recommendation-driven content selection
35–40 min — Key lessons, design principles, and audience Q&A

Source: <https://pretalx.com/pydata-london-2026/talk/GBGB9X/>

## 51. [LLM-Based Recommendation Systems: From Embeddings to Real Personalization](https://pretalx.com/pydata-london-2026/talk/HAYANG/)

**Speakers**: [Özge Çinko](https://pretalx.com/pydata-london-2026/speaker/RZSNJL/)

**When and where**: Sunday, 2026-06-07, 15:30–16:15, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Large Language Models are rapidly changing how we think about recommendation systems. Traditional pipelines based on collaborative filtering or matrix factorization are being complemented and sometimes replaced by embedding-based and LLM-driven approaches.

In this talk, we explore how modern recommendation systems can be built using LLM embeddings, vector databases, and hybrid architectures that combine classical ML with generative models. We will discuss practical design patterns for personalization, retrieval, ranking, and user modeling, focusing on real-world constraints such as latency, cost, and evaluation.

The session emphasizes hands-on insights from production systems and highlights where LLMs add real value and where they don’t. Attendees will leave with a clear mental model for designing scalable, LLM-powered recommendation systems beyond toy examples.

**Description** (verbatim):

Recommendation systems are a core component of many data-driven products, yet most practitioners are still navigating how and when to incorporate Large Language Models into these systems effectively.

This talk presents a practical, end-to-end view of LLM-based recommendation systems. We start by revisiting classical recommendation architectures and then move into modern approaches built around embeddings, vector similarity search, and retrieval-augmented generation (RAG).

Topics covered include:
Using LLM embeddings for user and item representation
Hybrid retrieval pipelines combining vector search and traditional ranking models
Prompt-driven personalization and context-aware recommendations
Offline and online evaluation strategies for LLM-based recommenders
Trade-offs around latency, cost, and system complexity

The focus is on real-world applicability rather than theoretical novelty. Examples and design patterns are drawn from production-like systems and practical experimentation. This session is aimed at data scientists, ML engineers, and practitioners who want to move beyond hype and build recommendation systems that deliver meaningful personalization using LLMs.

Source: <https://pretalx.com/pydata-london-2026/talk/HAYANG/>

## 52. [The Future of Notebooks in a Claude Code World**](https://pretalx.com/pydata-london-2026/talk/KDWRYR/)

**Speakers**: [Paddy Mullen](https://pretalx.com/pydata-london-2026/speaker/EFFTBK/)

**When and where**: Sunday, 2026-06-07, 16:15–17:00, room Grand Hall 1

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

AI coding agents are changing how data professionals work. But an AI agent chat session is a stream, a long conversation that scrolls on and on. A good notebook is something different: a sequence of distinct, well-structured transformations, each with an explanation and a visible result. How do you get from the chat stream to that? And how do you see the visualizations, the tables, charts, and diffs that make data work legible?

We'll trace the historical reasons why the programming notebook style developed, what problems it solves, and what problems it creates. Notebooks intermingle three valuable concepts: a live execution environment, a long-running process that caches state in memory, and a narrative log of exploration steps. The long-running process is the key. It's why data scientists use notebooks instead of Python scripts. But this coupling is also why notebooks are fragile, unreproducible, and impossible to productionize. And the kernel's implicit mutable state is a poor fit for AI agents. Unlike databases (explicit state, declarative interface, introspectable), a notebook kernel degrades as implicit state accumulates across cells.

This talk introduces the Deconstructed Notebook: a system that gives AI-agent-driven data work the structure and visualization of a notebook without the notebook's baggage. Claude writes the instructions in the terminal. The PyData Arrow stack, driven by Ibis and xorq, handles the compute. A browser companion renders tables, charts, diffs, and lineage live as the work iterates, organized into distinct steps, not a scrolling chat log. The key architectural insight is that automatic caching of expression results to disk replaces the notebook kernel's in-memory state, letting each step execute as a self-contained script while preserving the interactive, incremental workflow data scientists depend on. The system is built on xorq, an open-source library built on Ibis and Apache Arrow, but the design principles generalize. We'll demo the full workflow live and share what we learned about building post-notebook tooling for the age of AI agents.

**Description** (verbatim):

1. **The notebook's hidden contract** — Jupyter intermingles three valuable things: interactive execution, a long-running process that caches state in memory, and a narrative log of exploration steps. The coupling has real benefits — edit-in-place re-execution captures a clean story, not a noisy shell log, and the persistent kernel means you never have to reload expensive state. But the coupling is also why notebooks are fragile, unreproducible, and can't go to production. AI agents are fine with long-running stateful processes like databases (explicit state, declarative interface, introspectable). A notebook kernel is the opposite — implicit mutable state, imperative, execution-order-dependent — and the agent's model of it degrades as state accumulates. Self-contained steps with explicit inputs and cached outputs have much better failure modes.

2. **The display surface gap** — How data professionals actually use Claude Code today: saving PNGs, dumping ASCII tables, switching back and forth to Jupyter. The terminal is a fantastic interface for intent but a terrible interface for output.

3. **Prior art and adjacent solutions** — MCP Apps (renders UI inside Claude Desktop's chat window), chart-canvas (browser dashboard for Claude Desktop), Data Formulator (Microsoft's standalone viz tool). What each gets right, and why none of them solve the CLI agent case.

4. **The deconstructed notebook (live demo)** — Separate the three concerns. Terminal for intent. The PyData Arrow stack driven by Ibis/xorq for compute, with instructions written by Claude. Browser for display. Live walkthrough of the working system: the audience sees the browser update in real time as Claude iterates, with tables, charts, and diffs appearing in structured blocks, not a scrolling chat log. The default view shows the current result at each step — preserving the notebook's narrative quality — with iteration history available but not in your face.

5. **Iteration and diffing (live demo)** — Exploratory data analysis through model evaluation, driven by conversation. The audience watches the full loop live: prompt, compute, result, diff, refine. Interactive tables with sort/filter, Vega-Lite charts, side-by-side diffs showing exactly what changed between iterations, and expression lineage tracing the full dependency graph from raw data to final result.

6. **What the compute substrate needs to get right** — Why "just render HTML" isn't enough. The notebook kernel's real job is caching — keeping expensive intermediate results in memory so you can build on them. To decouple the notebook, you need a substrate that handles caching automatically: expression results stored as Parquet on local disk, streamed to the next step, no long-running process needed. Plus: content-addressing (so every iteration is retrievable), typed schemas (so composition errors are caught early), and separation of transform logic from visualization. Brief introduction of xorq's expression model as one approach to these requirements.

7. **Design principles for post-notebook tooling** — Expressions are append-only and immutable — every iteration is preserved. But the workflow and the final view are structured like a notebook: blocks that are iterated on, each showing its current result, with history accessible underneath. These blocks can be arranged into a traditional notebook-style narrative or a dashboard. The human controls the intent and reviews the display. Diffing is a first-class operation. Every intermediate result is addressable.

Source: <https://pretalx.com/pydata-london-2026/talk/KDWRYR/>

## 53. [Tesco AI & Data Science: From Recipes to Reality](https://pretalx.com/pydata-london-2026/talk/BGNZLQ/)

**Speakers**: [Julie Huang](https://pretalx.com/pydata-london-2026/speaker/VVKTDR/), [Kareem Hussein](https://pretalx.com/pydata-london-2026/speaker/FGG7CG/)

**When and where**: Sunday, 2026-06-07, 10:15–11:00, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Tesco is applying AI and Data Science at scale to solve some of the most complex problems in retail. From personalisation to optimisation and decision support, our systems power millions of customer interactions and operational decisions every day. In this talk, we highlight how these capabilities come together in modern AI-driven customer experiences, and why Tesco is at the forefront of applying AI in real-world, high-impact settings.

We briefly introduce Tesco’s Meal Planner to highlight the technical challenges behind AI-driven customer experiences. A key challenge behind the scenes is translating recipes into products that customers can actually buy. We approach this by connecting recipes, ingredients, and products in a way that enables the system to move from meal ideas to a ready-to-shop basket. This requires balancing richer reasoning over customer needs and preferences with the practical realities of a live retail environment, such as a constantly changing product catalogue, cost, and availability.

We then turn to one of the most important aspects of deploying AI systems at scale: Evaluation and how it helps to ensure that the system behaves reliably. When AI assistants support customer journeys, even small errors can degrade the experience or lead to incorrect outcomes. We present our evaluation framework, which combines multiple techniques to assess both system behaviour and response quality. This allows us to identify issues early, enforce consistent standards, and continuously improve performance.

Overall, this talk offers a practical view of how Tesco applies AI and Data Science to real-world problems, combining strong technical foundations with robust evaluation to deliver reliable and impactful customer experiences.

Source: <https://pretalx.com/pydata-london-2026/talk/BGNZLQ/>

## 54. [Querying the queries: SQL Metaprogramming in Python](https://pretalx.com/pydata-london-2026/talk/KQDKTE/)

**Speakers**: [Michel Semaan](https://pretalx.com/pydata-london-2026/speaker/ZZA7AP/)

**When and where**: Sunday, 2026-06-07, 11:00–11:45, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Large SQL codebases inevitably accumulate duplication, inconsistency, deep nesting, and subtle logic errors, making refactoring slow, risky, and often unrealistic to do by hand. This talk shows how Python metaprogramming can turn SQL itself into data that can be analyzed and transformed safely and automatically.

Instead of relying on fragile regex patterns or manual inspection, we use Python to parse queries into Abstract Syntax Trees (represented as nested dictionaries) using libraries such as sqloxide. Once SQL itself is encoded as data, entirely new workflows become possible.

The session walks through practical examples of treating SQL programmatically via tree operations in Python: computing subquery depth for linting, wrapping all denominators in NULLIF() with a simple AST rewrite, auto‑aliasing aggregate expressions, and generating dependency graphs of temporary tables used across pipelines, among others. Each example highlights how metaprogramming enables precise, automatable refactors that would be error‑prone or impossible through text manipulation alone. This talk is designed for analytics and data engineers who work with large SQL codebases.

**Description** (verbatim):

SQL sits at the heart of most analytics and data engineering work, yet the way we maintain SQL rarely scales with the complexity of our pipelines. As codebases grow, SQL tends to accumulate structural debt: duplicated logic, subtle inconsistencies, deeply nested subqueries, and transformations that are difficult to apply reliably. Teams often end up relying on manual pattern‑matching, ad‑hoc scripts, or one‑off rewrites, approaches that are fragile and nearly impossible to generalise.

This talk presents a more systematic solution: treat queries as manipulable data through metaprogramming in Python. Instead of working with SQL as raw text, we use Python to parse queries into Abstract Syntax Trees (ASTs), unlocking the ability to inspect, analyze, and modify SQL with precision at scale.

After introducing the intuition behind SQL ASTs, we walk through what they look like in practice using Python libraries such as sqloxide. With queries represented as nested dictionaries, we can traverse them, detect patterns, and apply targeted modifications without breaking syntactic structure. The session demonstrates several real examples that highlight the power of this approach: evaluating subquery depth for complexity diagnostics, adding defensive transformations such as wrapping denominators in NULLIF(), generating consistent aliases for aggregation expressions, and extracting table references to infer dependency graphs across staging or temporary‑table‑heavy pipelines.

Rather than offering a single tool or framework, this talk focuses on the underlying metaprogramming techniques that empower engineers to build their own SQL analysis and refactoring utilities. Attendees will leave with a clear mental model of how SQL parsing works, how ASTs can be manipulated in Python, and how these patterns can be applied to enforce standards, build linters, or automate large‑scale refactors.

Background required:

- Intermediate familiarity with Python (nested dictionaries, basic tree algorithms).
- Intermediate familiarity with SQL (CTEs, subqueries, aggregates)
- No prior knowledge of compiler theory or ASTs is assumed

Outline:

- 0–3 min — Motivation: Why SQL Refactoring Is Hard
  -- Structural debt in real SQL codebases: duplication, inconsistencies, nested logic
  -- Why regex and manual review fail at scale

3–8 min — Key Idea: Treat SQL as Data
-- What is an Abstract Syntax Tree (AST)?
-- Using Python libraries (e.g., sqloxide) to parse SQL into manipulable structures

8–15 min — Demo: Exploring Real SQL ASTs in Python
-- Show nested dictionaries representing SQL structure
-- Simple tree traversal patterns

15–25 min — Practical Refactoring Examples
-- Computing subquery depth (complexity linting)
-- Auto‑aliasing aggregate expressions
-- Wrapping denominators with NULLIF()
-- Extracting table references for dependency graphs

25–32 min — Building Custom SQL Tooling
-- How these patterns generalize
-- Enforcing standards, writing linters, automating bulk rewrites
-- When AST‑based tooling is worth it

32–40 min — Lessons Learned & Limits + Q&A
-- Homoiconicity (Python vs Lisp for AST manipulation)

Source: <https://pretalx.com/pydata-london-2026/talk/KQDKTE/>

## 55. [Making tech boring to keep data exciting](https://pretalx.com/pydata-london-2026/talk/AMGUEK/)

**Speakers**: [Fred O'Loughlin](https://pretalx.com/pydata-london-2026/speaker/PRTTM8/), [Kerry Parker](https://pretalx.com/pydata-london-2026/speaker/Y3ZRSN/), [Mark Cottam](https://pretalx.com/pydata-london-2026/speaker/3NBVAH/)

**When and where**: Sunday, 2026-06-07, 11:45–12:30, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Data work often gets blocked by the unglamorous parts: brittle pipelines, unclear ownership, slow deployments, and systems that are hard to trust. This talk is about deliberately making data infrastructure “boring” — predictable, observable, and easy to change — so that the data itself can be used in lots of exciting ways.

Climate Policy Radar is a non-profit building open, credible databases and AI powered tools to support informed climate, nature, and development action.

Using a real-world journey from an unreliable ingest to a steadier, federated platform, this talk will walk through the principles and trade-offs that matter most: resilience over heroics, incremental delivery over big-bang rewrites, and transparency over intuition. The focus is not on specific tools, but on the engineering moves that turn data pipelines into dependable systems: orchestration that supports recovery, interfaces that unblock downstream teams, quality signals that can be acted on, and a shared layer (data lake/warehouse) that aligns definitions and reduces duplication.

Attendees will leave with a practical mental model for taking maturing data flows and making them boring — in a good way.

**Description** (verbatim):

Data engineering succeeds when it disappears into the background. Not because it’s unimportant, but because it becomes reliable enough that other teams can build on it without thinking about it. In many organisations, the opposite happens: pipelines are fragile, changes are risky, and operational work consumes the roadmap.

This talk tells the story of moving from that state to one where the pipeline becomes a platform:

- Predictable runs and recovery: designing for frequent ingest, safe execution windows, and fast time-to-recover when things fail.
- Incremental modernisation: migrating orchestration and execution in a way that avoids running parallel “shadow pipelines” and reduces blast radius.
- System transparency: turning a black box into something teams can interrogate — what ran, what it produced, what failed, what changed, and why.
- Data quality as a product feature: creating actionable quality signals (not just logs), so improvements to text quality and search relevance can ship quickly and be measured.
- Federation and alignment via a shared layer: using a data lake/warehouse layer to consolidate outputs, align metrics across teams, and remove ad hoc transforms at the edges.
- Unblocking downstream users: improving interfaces and handoffs so application, policy, and data science teams can self-serve, iterate, and trust the numbers.

The emphasis is on the big picture: how to set goals that matter (scale, resilience, extendability), how to define “done” in operational terms, and how to deliver tangible improvements sprint by sprint while still laying foundations for the future. The takeaway is a repeatable approach for making data infrastructure boring — so the work built on top of it can be exciting.

Source: <https://pretalx.com/pydata-london-2026/talk/AMGUEK/>

## 56. [The Polars vs SQL differences nobody is talking about](https://pretalx.com/pydata-london-2026/talk/HPJR9B/)

**Speakers**: [Marco Gorelli](https://pretalx.com/pydata-london-2026/speaker/KEUJ9U/)

**When and where**: Sunday, 2026-06-07, 14:45–15:30, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Polars is a dataframe library which has taken the world by storm over the last 4-5 years. Because people love benchmarks, people often compare it with SQL-like engines such as DuckDB, PySpark, Daft, and others. But what if, instead of comparing performance, we compared semantics?

This talk will make no mention whatsoever of performance differences. Instead, it will focus entirely on the semantic differences - which don't get nearly enough attention - of Polars vs SQL. Attendees will leave with a heightened appreciation for the differences between the Polars and SQL models, and an understanding of the consequences this has on their code.

**Description** (verbatim):

Polars is a dataframe library that started gaining significant traction in the data science community around 2022/2023. It is now generally regarded as a safer and more performant alternative to its extremely popular counterpart pandas. As such, it has attracted several performance comparisons with SQL-like engines such as DuckDB, PySpark, Daft, and more. What's typically missing from these comparisons is an explanation of the semantic differences.

For example:

- Why does Polars let me do `pl.col('price') - pl.col('price').mean()`, but SQL doesn't?
- Why does Polars let me filter using window functions, and how can I get SQL to?
- Are there operations that are more dangerous in Polars than in SQL?
- How do they differ when working with time zones?
- Why did SQL reorder my rows when Polars didn't?

Outline of the talk:

- Motivation: why care about Polars or about SQL?
- Relational model background, row order
- Polars model, how it differs from the relational model, and what this means for you
- Abstracting the Polars and SQL differences away in Narwhals, and advice for non-Narwhals users
- Q&A

This is a technical but accessible talk aimed at data practitioners. Data engineers, data scientists, data analysts, and anyone else working with data will leave the talk with stronger theoretical foundations regarding the Polars and SQL data models. Most importantly, they will learn what this means for them, and what they can do about it.

Source: <https://pretalx.com/pydata-london-2026/talk/HPJR9B/>

## 57. [From Chat-with-PDF to Quiz-Master: Live-Grading RAG with LLM-as-Judge in Python](https://pretalx.com/pydata-london-2026/talk/QQWDVQ/)

**Speakers**: [Adam Hill](https://pretalx.com/pydata-london-2026/speaker/P98FWZ/)

**When and where**: Sunday, 2026-06-07, 15:30–16:15, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Most RAG demos stop at retrieval and summarisation. In practice, we also need to measure the understanding of users, models, and the source material. This talk introduces a reusable evaluation pattern that turns any document into a live-graded “exam engine” using Python tools including Docling, DeepEval, and Marimo.

We will build a stateful application that generates multiple-choice and free-text questions from complex documents, creates realistic distractors, and scores answers in real time using an LLM-as-judge pipeline. The demo is intentionally playful, but each component maps to a production concern: layout-aware ingestion (tables and figures), synthetic QA dataset creation, semantic grading, and interactive evaluation loops.

Attendees will learn how to move beyond passive RAG towards systems that benchmark knowledge, support training workflows, and enable human-in-the-loop evaluation.

**Description** (verbatim):

RAG systems typically answer questions but rarely evaluate whether the answer, or the user, actually demonstrates understanding. That requires structured datasets, grading logic, and application state, not just retrieval.

In this talk, we build a live-graded “knowledge arena”: a Python application that converts a dense technical document into an interactive quiz with two modes:

- Easy mode - automatically generated multiple-choice questions with plausible distractors
- Expert mode - free-text answers scored in real time using semantic LLM metrics

The implementation illustrates several reusable production patterns:

- **Document ingestion (Docling)**: Extracting layout, tables, and figures so evaluation covers the full source rather than plain text only.
- **Synthetic dataset generation (DeepEval)**: Creating “golden” QA pairs and automated distractors for benchmarking and training.
- **LLM-as-judge grading**: Scoring free-text answers with semantic metrics instead of brittle string matching.
- **Stateful Python UI (Marimo)**: Managing interaction and evaluation loops without custom JavaScript.

Although the interface is playful, the architecture generalises to production RAG and agentic knowledge systems for benchmarking, training, and human-in-the-loop evaluation.

This talk presents a reusable LLM-as-judge architecture for evaluating understanding in RAG systems using synthetic QA generation and real-time semantic grading in Python. All demo components are pre-built and run locally with cached models and datasets.

**Audience / Prerequisites**

- Intermediate Python users familiar with basic LLM and RAG concepts (embeddings, retrieval).
- No prior experience with Docling, DeepEval, or Marimo required.

**Key Takeaways**

- A reusable LLM-as-judge evaluation pattern for RAG
- How to generate QA benchmarks from documents automatically
- Techniques for handling tables and figures in ingestion
- Where live grading fits into production workflows

Full code example available here: https://github.com/Cadarn/PyData-AI-Generated-Quiz

Source: <https://pretalx.com/pydata-london-2026/talk/QQWDVQ/>

## 58. [When Your Dataset Has Blind Spots: Practical LLM-Based Data Augmentation](https://pretalx.com/pydata-london-2026/talk/CHQLFU/)

**Speakers**: [Ophelie Bleu](https://pretalx.com/pydata-london-2026/speaker/NNQHFT/)

**When and where**: Sunday, 2026-06-07, 16:15–17:00, room Doddington Forum

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Learn practical techniques for using LLMs to solve the data scarcity problem that plagues real-world ML projects. This talk demonstrates three production-ready approaches: synthetic generation, LoRA fine-tuning, and LLM-powered annotation to augment training datasets when you have abundant data for common cases but almost nothing for edge cases or emerging categories. Using a food review classification scenario, you'll see how to generate high-quality training data, when each technique works best, and critically, how to validate synthetic data to avoid amplifying errors. Perfect for practitioners facing the "we have 10k examples of X but zero for Y" problem.

Target Audience: Data scientists and ML engineers working on classification, NLP, or content moderation tasks who struggle with imbalanced or incomplete training datasets.

Takeaway: A decision framework for choosing between synthetic generation, fine-tuning, and LLM annotation, plus validation strategies to ensure data quality before retraining models.

**Description** (verbatim):

## Objective

Many machine learning teams struggle not because of model limitations, but because their datasets fail to cover rare classes, niche domains, or emerging user behavior. Traditional data augmentation techniques offer limited help for text, often producing surface-level variations without meaningful semantic diversity. This talk presents a practical framework for using large language models to augment NLP datasets.

## Outline

- The Data Bottleneck: Why models trained on "standard" food language fail to generalize to "Molecular Gastronomy" or niche culinary terms.
- Three Complementary Techniques:
  1. Synthetic Generation: Creating fully labeled examples for missing classes.
  2. LoRA Adapters: Fine-tuning LLMs to control style and label consistency (e.g., matching a "Professional Critic" tone).
  3. LLM Annotation: Labeling large volumes of messy, real-world text from social media or external scrapes.
- Validation Strategies: Addressing error amplification and bias through human agreement checks, self-consistency, and "LLM-as-a-judge" approaches.
- Measuring Impact: Evaluating downstream model performance via rare-class recall, calibration, and error distribution.

## Central Thesis and Takeaways

The session provides a decision framework for choosing between generation, fine-tuning, and annotation based on data availability and the need for style or tone. Attendees will walk away with strategies to ensure synthetic data quality before retraining their models.

## Background Knowledge Expected

Basic knowledge of Python and familiarity with machine learning workflows (training, labelling, and evaluation) is recommended.

Source: <https://pretalx.com/pydata-london-2026/talk/CHQLFU/>

## 59. [From SQL to Python: Building Data Context for Agents and People](https://pretalx.com/pydata-london-2026/talk/BAFKCL/)

**Speakers**: [Dmitry Petrov](https://pretalx.com/pydata-london-2026/speaker/WYJRPW/)

**When and where**: Sunday, 2026-06-07, 10:15–11:00, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Text-to-SQL makes great demos, but in real systems generating queries is rarely the hard part - understanding data is. Modern data is increasingly S3-first and multimodal, where meaning is defined by Python workflows, not table schemas.

To work reliably, both agents and people need data context across multiple layers: storage context (what exists and where), metadata context (what’s inside files), dataset context (how files are grouped and versioned), and code context (the transformations that define semantics).

In this talk, I’ll share a practical framework for building these context layers in Python-first systems, and show how DataChain makes multimodal workflows agent-ready in domains like Physical AI and biotech.

**Description** (verbatim):

Text-to-SQL is often presented as the future interface for AI-driven analytics: connect an LLM to your warehouse, ask questions, get answers. The demo works. But production systems reveal a deeper issue: SQL can query structure, but it cannot provide the context required to understand what data actually means.

After years of building data infrastructure, I’ve learned that context is the real bottleneck - for both people and agents. This becomes unavoidable in S3-first, multimodal environments: video, audio, medical scans, sensor streams, and model outputs. In these projects, the source of truth is object storage, and meaning is defined by Python pipelines.

To reason correctly, you need data context across multiple layers:

- **Storage context -** what exists, where it lives, and how it changes
- **Metadata context** - what’s inside files, extracted signals, and hierarchical structure
- **Dataset context** - how files are grouped, reused across datasets, and versioned
- **Code context** - the Python transformations that define semantics and intent

In this talk, I’ll present a practical framework for collecting and using these layers systematically. Using DataChain as a concrete example, I’ll show how typed schemas (e.g., Pydantic), vectorized metadata operations, and scalable Python execution make multimodal workflows understandable, reusable, and agent-ready - especially in Physical AI and biotech.

Attendees will leave with a clear mental model for building data platforms where meaning lives in code, and agents can operate with real context rather than isolated queries.

Source: <https://pretalx.com/pydata-london-2026/talk/BAFKCL/>

## 60. [The Clean Energy Graveyard: Using Python & Gemini to Map the UK's Cancelled Renewable's](https://pretalx.com/pydata-london-2026/talk/R7UEBE/)

**Speakers**: [Damian Bemben](https://pretalx.com/pydata-london-2026/speaker/H89NEW/)

**When and where**: Sunday, 2026-06-07, 11:00–11:45, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Britain has an invisible clean energy graveyard. Over 3,800 clean energy projects have been cancelled in the UK since 2010, representing enough capacity to power millions of homes. This talk presents the Clean Energy Graveyard - an open-source python pipeline & interactive web visualisation that transforms the government's Renewable Energy Planning Database (REPD) into a story about what's blockoing out energy transition.

**Description** (verbatim):

Within this talk, I'll go through some data on Britain's hidden energy crisis, including evaluating current quality of the Renewable Energy Planning Database (REPD), a government project that's been tracking every renewable energy project from beginnning to success/cancellation openly.

While the data is public, it's often difficult to navigate and tells an incomplete story.

When a wind farm is cancelled after 4 years of planning, this represents hundreds of pages of planning documents, countless hours of work with ocmmunity objections, and interventions hidden in planning documents.

The Clean Energy Graveyard is a open-source and free web visualisation tool that seeks to transform the REPD dataset into an interactive clean energy graveyard, using a mixture between GeoPandas for spatial analysis, Pandas for dataset cleaning, and the gemini API to begin intelligently surfacing critical news stories and council data.

The key take-aways from this talk will be:

- How to design and build AI models for the public good, to help transform byzantine systems into open data flows.
- Practical patterns for using API's to enrich datasets at scale.
- Techniques for handling messy government data with inconsistent schemas
- How to create data visualisations that seek to tell human stories, not just difficult to understand statistics.
- How to collaborate and work on open-source public good projects

Prior Knowledge Expected:

Basic familiarity with Python & coding techniques. No prior knowledge of energy policy, LLM api's, geospatial analysis or detailed webs of council websites required. The talk is aimed at intermediate python users & data scientists who want to explore how to use their skills for public good.

Target Audience:

- Data scientists interested in working with government/public sector data
- Developers exploring practical applications of LLMs past typical analysis and summarisation
- Anyone interested in climate/civic tech.

Resources:
Live Demo: nimby.bemben.co.uk
Previous Blog Post about Specific Example: https://ends.substack.com/p/faw-side-community-wind-farm
Previous Presentation Slides: github.com/dambem/nimbydex_slides

Why this talk:

This

Source: <https://pretalx.com/pydata-london-2026/talk/R7UEBE/>

## 61. [What We Expect from XAI - A scientist’s experience between models and users](https://pretalx.com/pydata-london-2026/talk/9HLYEW/)

**Speakers**: [Alessandra Costantino](https://pretalx.com/pydata-london-2026/speaker/8VJYBH/)

**When and where**: Sunday, 2026-06-07, 11:45–12:30, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Explainable AI is frequently invoked to make machine learning systems understandable and trustworthy. In real applications, however, explanations are often expected to justify decisions and support action. Drawing on experience with remote sensing–based risk monitoring, this talk examines the gap between the guarantees of explainability methods and the expectations placed on them by different users. It discusses how explanations can inform practice, how they can be misinterpreted, and when focusing on explainability may obscure deeper problems in models or data.

**Description** (verbatim):

Explainable AI (XAI) emerged as a major research topic with the rise of deep learning and is now being adopted in domains where predictive models support high-impact decisions such as healthcare, finance, environmental monitoring, and public policy. As machine learning systems move into operational use, explanations are increasingly relied upon not only to understand models but also to justify and guide real decisions.
Conceptually, an explanation provides information that allows a human observer to understand a system’s behaviour. In machine learning, the term refers to a broad family of approaches, ranging from interpretable models to post-hoc analysis methods. These techniques are often presented as a way to make complex models understandable and usable by human stakeholders.
A concrete example comes from a project in which I applied machine learning to earth observation data for urban resilience, where explanations were expected to help local authorities plan maintenance and intervention actions to mitigate the impacts of natural hazards in cities. My role as the data scientist placed me between the domain specialists curating the data and the end users relying on the model’s outputs. In practice, this meant translating between different questions: domain specialists wanted to know whether the model’s behaviour made sense given their knowledge of the phenomenon, while end users wanted to know how the outputs could guide concrete actions and planning decisions.
This experience motivates a closer look at what contemporary explainability methods are intended to provide to different users. Many widely used approaches—particularly post-hoc feature attribution techniques—are often interpreted as revealing the reasoning of a model. In practice, however, they typically provide local approximations or sensitivity analyses rather than faithful descriptions of the decision process. For example, feature attribution methods such as SHAP may be read as identifying causal factors, and saliency maps may appear meaningful even when weakly connected to the model’s actual reasoning.
I unpack explainability in contemporary machine learning practice by asking what explanation methods actually guarantee—and what they do not. Drawing on my experience working between domain experts and end users, I reflect on how XAI functions in operational settings and on the expectations attached to explanations when they are used to support decisions.

Intended audience
The talk is aimed at machine learning practitioners, researchers, data scientists, and applied scientists who work with predictive models, as well as anyone who is interested in interpretation of model outputs in practice (including domain experts and decision-makers). No prior expertise in XAI is required.
Type and tone of the talk The presentation is conceptual and experience-driven rather than mathematical. It will use concrete examples and intuitive explanations rather than formal derivations. The tone is reflective and discussion-oriented, focusing on practical interpretation rather than algorithmic detail.

Source: <https://pretalx.com/pydata-london-2026/talk/9HLYEW/>

## 62. [The Human-in-the-Loop is Tired](https://pretalx.com/pydata-london-2026/talk/3YH3WF/)

**Speakers**: [Laura Summers](https://pretalx.com/pydata-london-2026/speaker/3QJLK8/)

**When and where**: Sunday, 2026-06-07, 14:45–15:30, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

A few nights ago I was up to 2am obsessively crafting an LLM plan. (_"Just one more prompt!"_ - famous last words). Yet it still did something inexplicably stupid. 🫠 So yeah: LLMs are both genuinely useful and genuinely destabilising. Focusing on the first and ignoring the second is how people burn out.

This talk is an honest account of what it feels like to be a developer right now, from someone inside it, and some thoughts on what might actually help. My thesis: we've been optimising for _model output_ when we need to be optimising for _human experience_.

I'll share observations from my work, peers and colleagues. The peculiar fatigue of machine supervision: holding the intent in your head while the machine generates volumes of mostly-correct output that still needs your eyes, your judgement, and your taste. The way the satisfying part of the work shrank while the exhausting part grew. The isolation of pair-programming with a machine, and the loss of real human learning, interconnection and collaboration. And underneath all of it: uncertainty. About market conditions, about employability, about whether the skills we've spent years building will still matter.

The second half is about what's been working for me, and what hasn't. On the human side: encouraging pairing and teamwork even when the tools push you toward isolation, sharing the pain openly, naming the uncomfortable thing. On the technical side: structuring your environment to collaborate with LLMs more deliberately — writing plans, configuring project-specific rules. Learning when to stop prompting and just write code. And critically: rebalancing the push and pull of information so that you're directing your attention, not feeling at the mercy of the model's output. More Star Trek, less Black Mirror.

Leave with concrete strategies for recalibrating your workflow, challenges to discuss and the reassurance that if you're finding this hard, you're not broken. The feedback loop is. And we can start fixing that.

**Description** (verbatim):

Outline:

- The feeling: honest anecdotes from inside an AI tooling company navigating its own disruption (~8 min)
- Three named patterns: reward function disruption, intensity trap, isolation drift (~7 min)
- What's working: pre-mortems, judgment distillation, mode-switching discipline, team counter-practices (~10 min)
- The reframe: responsive design as precedent, what still matters, scarce resources are valuable (~5 min)

Source: <https://pretalx.com/pydata-london-2026/talk/3YH3WF/>

## 63. [What Can LLMs Do with Messy Residential Electrification Data?](https://pretalx.com/pydata-london-2026/talk/TL88MJ/)

**Speakers**: [Cedric Clyburn](https://pretalx.com/pydata-london-2026/speaker/VQQDJD/), [Andrew Igdal](https://pretalx.com/pydata-london-2026/speaker/CCHWAP/)

**When and where**: Sunday, 2026-06-07, 15:30–16:15, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Residential energy models like NREL’s ResStock generate the kind of data most humans run from: thousands of buildings, dozens of columns, and at least 8,760 rows per column. Great for research, but difficult for anyone who just wants to ask, “What happens to electricity demand in Texas if homes used solar water heating?” or “How do HVAC upgrades change my annual cooling costs in North Carolina?”

Join us for this session as a University of Texas energy researcher and a Red Hat engineer team up to see what large language models can realistically do with this kind of messy, domain-heavy data using Python. We’ll show how we sample, reshape, and describe large datasets so LLMs can help generate and refine pandas/DuckDB queries, explain upgrade scenarios in plain English, and guide non-experts through “what if” electrification questions. This and more, all while being honest about where the models break down and why humans still need to do the science.

**Description** (verbatim):

ResStock is an incredible tool for residential energy research, but quite tricky for anyone who isn’t deep in the weeds. It produces huge, domain-heavy datasets: thousands of simulated homes, dozens of variables, and hourly time series for a full year. Great if you’re writing a paper, overwhelming if you want to understand how electrification upgrades change bills or demand.

This talk asks a practical question: What can large language models actually do with ResStock-style data, using a Python workflow? Can LLMs help normal people make sense of the benefits of electrification upgrades without pretending the model is “doing the science” for us?

We ground everything in two real ResStock runs: (1) solar thermal water heater upgrades in Texas, and (2) HVAC upgrades across the Southeastern U.S. Both are large and messy, so we can’t just upload the parquet files. Instead, we:

- Use Python (pandas/DuckDB) to sample and aggregate the data into representative slices that fit within context limits.
- Build a clear schema description (“data card”) so the LLM understands variables, units, and constraints.
- Ask the LLM to help where it shines: generating and refining pandas/DuckDB queries from natural-language questions, and explaining upgrade impacts in plain English.

Andrew (UT Austin) brings the ResStock data, research questions, and domain constraints; Cedric (Red Hat) brings the open source + LLM integration side. Attendees will leave with a realistic pattern for using LLMs as helpers, not replacements, when working with large, messy scientific or policy datasets in Python.

Source: <https://pretalx.com/pydata-london-2026/talk/TL88MJ/>

## 64. [No Ropes on a Boat: Coherent Forecasting](https://pretalx.com/pydata-london-2026/talk/RTWLPY/)

**Speakers**: [Thomas Ogden](https://pretalx.com/pydata-london-2026/speaker/ZMGX3E/)

**When and where**: Sunday, 2026-06-07, 16:15–17:00, room Hardwick Hub

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Forecasts live in a high-dimensional space. They vary by origin date, prediction horizon, scenario assumptions, uncertainty, granularity and decision context. Treating them as a single artefact creates ambiguity, semantic drift and misaligned expectations.

In this talk, I’ll show how we reframed forecasting at Spotify as a structured prediction problem not just a modelling task. I’ll cover practical design patterns for representing forecast objects across origins and scenarios, handling probabilistic outputs, implementing hierarchical reconciliation and tracking lineage and versioning in Python-based systems.

Aimed at data scientists and ML engineers working with production systems, this talk offers a framework for thinking about forecast dimensionality and concrete implementation patterns you can apply in your own forecasting platforms.

Source: <https://pretalx.com/pydata-london-2026/talk/RTWLPY/>

## 65. [Python Leadership and Engineering Excellence BoF](https://pretalx.com/pydata-london-2026/talk/AV3A3W/)

**Speakers**: [Sam Joseph](https://pretalx.com/pydata-london-2026/speaker/MZ3Y7X/)

**When and where**: Sunday, 2026-06-07, 10:15–11:15, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Birds of a feather to share what’s working well for us to do the best Python engineering and datascience that we can, while leading the way for our teams.

Source: <https://pretalx.com/pydata-london-2026/talk/AV3A3W/>

## 66. [How to write a PyData proposal](https://pretalx.com/pydata-london-2026/talk/LLVVRQ/)

**Speakers**: [James Fielder](https://pretalx.com/pydata-london-2026/speaker/CPWUST/)

**When and where**: Sunday, 2026-06-07, 11:45–12:30, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

In this unconference session, hear what reviewers actually look for in proposals for PyData and how to frame your idea so it stands out.

Source: <https://pretalx.com/pydata-london-2026/talk/LLVVRQ/>

## 67. [PyData Meetup Organizer Luncheon](https://pretalx.com/pydata-london-2026/talk/BKW3KD/)

**Speakers**: Not listed in the source data

**When and where**: Sunday, 2026-06-07, 12:30–13:30, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Are you a PyData Meetup Organizer? Come join us in the boardroom at lunch to mingle with other leaders.

Source: <https://pretalx.com/pydata-london-2026/talk/BKW3KD/>

## 68. [Surviving (and Thriving) as a Data Professional in the Age of AI Agents](https://pretalx.com/pydata-london-2026/talk/HNKFP8/)

**Speakers**: [Maksym Bilychenko](https://pretalx.com/pydata-london-2026/speaker/DXX9X3/)

**When and where**: Sunday, 2026-06-07, 14:45–15:30, room Board Room- Unconference Track

**Type**: Talk — **Language**: en

**Abstract** (verbatim from the [schedule JSON export](https://pretalx.com/pydata-london-2026/schedule/export/schedule.json)):

Data scientists, analysts and engineers are all feeling the pressure — but what's actually changing, and what's hype? This session brings us together to share real experiences of integrating LLMs and agents into data workflows, honestly assess which skills still matter, and tackle the uncomfortable question: are we building the tools that replace us?

Source: <https://pretalx.com/pydata-london-2026/talk/HNKFP8/>
