# PyData Amsterdam 2026 talks

Collected from the official PyData Amsterdam 2026 programme. The conference site embeds a schedule planner served from <https://pydata-guide-web.onrender.com/planner.html>, backed by a plain JSON data file at <https://pydata-guide-web.onrender.com/schedule/data.json> (generated 2026-09-10, fetched 2026-09-20). The schedule page is at <https://amsterdam.pydata.org/program>.

The JSON file uses its own schema, not Pretalx frab: 61 session records (`talks`) plus 40 programme activities (`activities`). The 40 activities are registrations, coffee breaks, and lunch breaks; they carry no speakers or descriptions and are excluded from the talk records but noted here for completeness. All 61 schedule records are kept, including opening/closing notes and the keynote, talk, long-talk, and tutorial sessions.

Speaker names in this export are plain strings (comma separated, split on ", " for multi-speaker sessions); the export carries no speaker profile URLs, so none are recorded. Abstracts come from the `description` field, falling back to `summary` where description is empty. Every talk record carries its canonical session URL (a pretalx.com talk page under the hood) and the data-file URL as source.

Machine-readable version of this data: [`talks.json`](https://github.com/thibaudcolas/python-at-fosdem/blob/main/docs/knowledge-base/2026-python-events/pydata-amsterdam-2026/talks.json) in this directory.

## Talks

## 1. [Opening notes](https://pretalx.com/pydata-amsterdam2026/talk/TRY3BC/)

**Speakers**: Not listed in the source data

**When and where**: Thursday 2026-09-10, 09:00–09:30, room The Grid

**Type**: Opening notes

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

tbd

Source: <https://pretalx.com/pydata-amsterdam2026/talk/TRY3BC/>

## 2. [From LLMs to Agents and from words to actions](https://pretalx.com/pydata-amsterdam2026/talk/RXAHBU/)

**Speakers**: Jay Alammar, Maarten Grootendorst

**When and where**: Thursday 2026-09-10, 09:30–10:20, room The Grid

**Type**: Keynote

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/RXAHBU/>

## 3. [Beyond the Holdout: Mitigating Censoring Bias with Asymmetric IPW](https://pretalx.com/pydata-amsterdam2026/talk/WBBVBF/)

**Speakers**: Leonardo Amorim

**When and where**: Thursday 2026-09-10, 10:35–11:05, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

## Topic and Relevance

Censoring caused by a model policy occurs when its action prevents the predicted outcome from being observed. In fraud systems, blocked transactions never produce counterfactual fraud labels. Metrics from surviving transactions can then give the wrong answer, and retraining on those labels can reproduce the previous model's blind spots.

This controlled synthetic experiment preserves the true outcome before applying the policy. It provides an oracle for evaluation while recreating the labels available after deployment. Six scenarios vary global drift, hidden regional signal, regional drift, trigger rate, holdout size, and base rate. Every method uses the same LightGBM configuration and is evaluated with normalized partial AUC through 20% FPR.

## Target Audience

The talk is intended for data scientists and machine learning engineers working in fraud, risk, credit, moderation, recommendations, or any setting where model actions affect which labels remain observable.

## Audience Takeaways

- Understand how a policy can bias production metrics and future training data by censoring labels.
- Recognize why a randomized holdout is needed for unbiased evaluation after deployment.
- Understand the tradeoff between giving every uncensored label equal weight and using inverse propensity weighting on flagged holdout observations.
- Learn how Asymmetric IPW uses pooled holdout validation to choose between those methods without requiring the data regime to be diagnosed manually.

## Talk Type and Approach

This is a conceptual and experimental talk. Visual examples introduce the censoring mechanism. The simulation then compares no retraining, incremental learning, no holdout, holdout only, dropping, and pure IPW. Asymmetric IPW selects between the two strongest methods.

Dropping and pure IPW use the same training rows. Dropping gives every row equal weight. Pure IPW upweights flagged holdout observations by the inverse holdout probability. This isolates the tradeoff between the lower variance of dropping and the lower bias of IPW.

The results are presented with paired comparisons and 95% confidence intervals. At the late endpoint, dropping clearly wins in three scenarios, IPW clearly wins in two, and one comparison is a statistical tie with a numerical IPW lead. Asymmetric IPW makes one choice from pooled holdout validation, without access to test performance. In retrospective evaluation, that choice matches the endpoint with the higher mean test score in all six late scenarios and statistically ties the fixed better endpoint in all twelve scenario and period comparisons. The same winner-matching pattern was observed in a real fraud dataset.

## Required Background Knowledge

Basic familiarity with supervised classification and model evaluation is useful. LightGBM, inverse propensity weighting, and normalized partial AUC are mentioned in the talk.

## Scope and Structure

- Censoring caused by model policies: 5 minutes
- Simulation design and assumptions: 4 minutes
- Why unbiased measurement requires a holdout: 5 minutes
- Retraining methods and the dropping versus IPW tradeoff: 6 minutes
- Asymmetric IPW, results, and limitations: 5 minutes
- Q&A: 5 minutes

The source files, generated results, and executed notebooks will be published on GitHub and shared during the presentation.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/WBBVBF/>

## 4. [Enhance: Feeding the World with Data through Multi-Objective Optimization](https://pretalx.com/pydata-amsterdam2026/talk/BE9HP3/)

**Speakers**: Marijn Markus

**When and where**: Thursday 2026-09-10, 10:35–11:05, room Entropy

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk presents Enhance, a large-scale data platform developed by Capgemini, UN World Food Programme and Tilburg University's Zero Hunger Lab. Enhance combines operations research, data science, and policy modeling to improve global food systems.

Enhance solves a multi-objective optimization problem: identifying diets that minimize cost while meeting nutritional requirements and reducing environmental impact. The platform integrates diverse datasets—food composition, prices, environmental indicators, and demographic needs—and translates them into actionable policy insights.

The underlying models have been developed in collaboration with academic partners, including research groups from Tilburg University, with contributions from PhD researchers specializing in optimization and food systems.

We will cover:

Optimization approach: Linear and multi-objective programming to balance cost, nutrition, and sustainability
Data integration: Handling heterogeneous, country-specific datasets
Architecture: Python-based analytics stack deployed on cloud infrastructure
Policy simulation: Evaluating interventions such as subsidies, imports, and fortified foods
Real-world application: Case studies including Cambodia, where Enhance-informed insights supported agricultural policy decisions to improve dietary outcomes - like introducing new kinds of fortified rice as a result of analysis.

An optional live demo can showcase how optimization scenarios can be run interactively to explore policy trade-offs in real time.

**Scope boundaries:**
We focus on optimization modeling, system design, and applied impact. We do not cover deep learning architectures or low-level infrastructure tuning.

**Target audience:**
Data scientists, ML engineers, and researchers interested in applied optimization and real-world impact. Plus anyone who likes to use data to help feed the world better.

Required background knowledge:
-Basic Python

- Basic statistics
- Basic understanding of machine learning optimization concepts

Structure (30 minutes):

- Introduction: Global food challenge & role of Enhance — 5 min
- Modeling diets as multi-objective optimization problems — 10 min
- Platform architecture & data pipeline — 5 min
- Case study: Cambodia & policy impact — 5 min
- Optional live demo + Q&A — 5 min

Source: <https://pretalx.com/pydata-amsterdam2026/talk/BE9HP3/>

## 5. [From Query to Discovery: Building an AI Agent That Helps Travelers Explore](https://pretalx.com/pydata-amsterdam2026/talk/Y7CCXA/)

**Speakers**: Giampaolo Casolla, Steven Mi

**When and where**: Thursday 2026-09-10, 10:35–11:05, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk presents battle-tested patterns from building and shipping an LLM-powered discovery system to production. The focus is on three practical problems every team faces when moving LLM features from prototype to production: managing latency and cost at scale, building evaluation infrastructure you can trust, and designing for graceful failure.

**Target audience**: ML/AI Engineers and Data Scientists shipping LLM-powered features to production. Intermediate level, familiarity with LLMs and Python assumed.

**Prior knowledge**: Basic understanding of LLM APIs, Python, and pytest.

**Key takeaways**:

- How to implement a dual-LLM tier strategy to balance cost, latency, and quality
- A deterministic evaluation approach (pass@k with pytest) that avoids LLM-as-judge flakiness
- Production hardening patterns: scope gating, graceful degradation, every stage optional

**Outline (30 min)**:

1. The problem: why natural language breaks traditional search (3 min)
   - Live example: "sunset tours in Barcelona for a couple under 50 euros"
   - Why keyword/semantic search can't handle filters, preferences, exclusions, and serendipity
   - What's missing: reasoning, orchestration, conversational context

2. Architecture overview (5 min)
   - Multi-stage LangGraph pipeline: ContextResolver, Interpreter, Parallel Retrieval, NanoFilter, Grading, Synthesizer
   - Intent interpretation: concrete example of parsing natural language into structured intent
   - Routing logic: SIMPLE/DEEP/FILTERED paths based on query complexity

3. Dual-LLM tier strategy (5 min)
   - The problem: one model doesn't fit all stages
   - Tier mapping: which model for which stage and why
   - Results: 60% latency reduction, 4x cost savings, nano-tier recall 0.9 / precision 0.7

4. Production hardening (3 min)
   - Scope gating: reject non-travel queries early
   - Graceful degradation: partial results are better than no results
   - Every stage is optional: the pipeline adapts when components fail

5. Evaluation infrastructure (10 min)
   - Why not LLM-as-judge: non-deterministic evals in CI produce flaky tests, flaky tests kill trust
   - pass@k approach: run each test case k=3 times via pytest-rerunfailures, pass if any succeeds
   - 816 tests, 21 custom metrics, 4 datasets, 32 parallel workers, 0 LLM-as-judge calls in CI
   - Real regression story: date inference change broke text extraction, caught before shipping

6. Key lessons and Q&A (4 min)
   - Right model per stage, deterministic evals over LLM-as-judge, graceful degradation by design, invest in eval infrastructure early

Source: <https://pretalx.com/pydata-amsterdam2026/talk/Y7CCXA/>

## 6. [A short tour of forgotten Machine Learning algorithms](https://pretalx.com/pydata-amsterdam2026/talk/GDUDY8/)

**Speakers**: Christiaan Erdbrink

**When and where**: Thursday 2026-09-10, 11:15–11:45, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**In an age dominated by generative AI, it’s easy to lose touch with the foundational building blocks of modelling and algorithmic problem solving.**
This informal talk is not an introduction to classical Machine Learning (ML), nor a mathematical deep-dive into the details of learning algorithms. Instead, it’s a fun-yet-serious **history of science tour honouring the life cycles of lesser known classical ML methods**.

This should be interesting to new generations of **data scientists**, who may not have had the chance to learn about these algorithms yet, and older generations as well. Both are invited to reflect on whether today’s models are in every way better than the oldies.

We’ll walk through the high-level working of a few selected algorithms. Each will be illustrated with a **real-life use case**. In addition, valuable, universal modelling insights are highlighted. This then leads to surprising connections and verdicts about these methods.

**Python code** snippets and simulation results are shown throughout the presentation, and a link to a public Github repo with notebooks and literature references will be shared. The talk itself is not a full demo or tutorial, however.

The **takeaways** of this talk flow naturally from the benefits of studying classical ML. It’s not just about understanding how algorithms learn from data, but also about expanding your toolkit and ability to see cross-links. And finally, we might even recognise cases where the original is the better choice.

> **Structure:**
> Introduction — 5 min
> Algorithm 1: Kernel Machines — 5 min
> Algorithm 2: Genetic Programming — 5 min
> Algorithm 3: Orthogonal Matching Pursuit — 5 min
> Algorithm 4: Hierarchical Mixture of Experts — 5 min
> Final insight and Q&A — 5 min

Source: <https://pretalx.com/pydata-amsterdam2026/talk/GDUDY8/>

## 7. [Beyond Benchmarks: Optimizing LLMs and Puzzle Agents for Cryptic Crosswords](https://pretalx.com/pydata-amsterdam2026/talk/VYG7HY/)

**Speakers**: Pauline van Nies

**When and where**: Thursday 2026-09-10, 11:15–11:45, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Outline

- 0-5 min: Introduction Language models and Cryptic Crosswords, benchmarking different LLMs
- 5 - 10 min: Is it possible to improve the LLM performance by expert guided few-shot learning using prompt optimization?
- 10 -15 min: Is it possible to improve the LLM performance by knowledge distillation using finetuning?
- 15 - 20 min: LLMs + tools: Agent framework choice and setup
- 20 -25 min: Showcase Cryptic Crosswords solving by agents & Comparison LLMs
- 25 - 30 min: Lessons learned and explanation how transferable is the framework to business related tasks and even more complex puzzles (AIVD Christmas puzzle?)

We are interested in evaluating and optimizing language models on a complex task that requires linguistic insight and creativity. Cryptic crosswords contain clues with misleading surface reading, whose solutions require disambiguation of wordplay. Hence, a language model needs to conduct multi-step (iterative) reasoning by extracting and/or identifying the relevant components of a cryptic clue that lead to the final answer. Our aim is to get a better understanding of the capabilities and bottlenecks of language models, as well as an interesting insight in how language models solve a task that in humans is described as a feeling of ‘the solution just falls in place’.

Thus, we set up an evaluation pipeline for language models to test their ability to solve cryptic clues (Dutch and English datasets). In this presentation, we will share the results of comparing different LLMs and optimization approaches on performing this specific task. We apply standard optimization search methods like adjusting the temperature and using Chain-of-thought, adding domain expertise and the few-shot approach. Additionally, we apply automated prompt engineering using the DSPy framework. We will showcase this approach of systematically experimenting, tracking results (mlflow) and optimizing a language model and prompt.

Next, we will show if an LLM can learn to solve a cryptic clue, by either knowledge distillation from expert reasoning traces as a guided few-shot approach for in-context learning or by transferring the behaviour of an LLM teacher to an (initially worse performing) LLM student with finetuning.

Finally, we simulate how LLM agents can solve a cryptic crossword together, using different strategies that humans would do naturally. In the agent framework, tools such as look up of anagrams and synonyms are provided to the react agent to help solving the clues. The implementation of the puzzle agent framework and the choice for its technical framework (LangGraph over Google ADK) is elaborated on and the challenges to overcome. We will show with a demo how the puzzle agent framework (depending on the LLM it is powered by) in real-time solves a cryptic crossword.

We summarize the conclusions and comment shortly on how these insights relate to business projects. We also give an outlook on the question: how transferable is this puzzle agent framework to even more complex puzzles? In the Netherlands the holy grail of puzzle solving are the AIVD Christmas puzzles which contains a.o. language puzzles. We will comment on the possibility to solve those with the puzzle agent framework and future approaches.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/VYG7HY/>

## 8. [Cold Start at Scale: Three Years of Experiments in a Travel Marketplace](https://pretalx.com/pydata-amsterdam2026/talk/EXBMZD/)

**Speakers**: Theodore Meynard

**When and where**: Thursday 2026-09-10, 11:15–11:45, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Cold start is a structural trap in two-sided marketplaces. New items lack behavioral signals, so ranking models under-expose them, which delays the very signals needed to rank them well. Left unaddressed, this feedback loop suppresses new inventory, weakens supplier trust, and degrades long-term marketplace health.

This talk presents our journey to break that loop in a large-scale travel marketplace with 200k+ activities. Over three years, we evolved from a brittle fixed-slot exposure system to a fully integrated ranking framework. The path was not linear: several of our most intuitive ideas failed.

We'll walk through three years of experiments: what we tried, what failed, and what worked. Along the way, we share how we framed trade-offs between short-term revenue and long-term marketplace health, and how reframing the core question unlocked the right metric, the right business case, and the roadmap.

You'll leave with three transferable lessons:

1. **Explore fast:** on new problems, small experiments beat big designs
2. **Constraints are hypotheses:** giving the model more freedom consistently outperformed restricting it
3. **Change the question, change the outcome:** the metric you optimise for determines what solutions become visible

Source: <https://pretalx.com/pydata-amsterdam2026/talk/EXBMZD/>

## 9. [The Context Trap: Addressing Item Neglect and Calibration in Deep Point-Wise Rankers](https://pretalx.com/pydata-amsterdam2026/talk/MDCKAF/)

**Speakers**: Akhila Vangara, Belle Bruinsma, Laura Israel

**When and where**: Thursday 2026-09-10, 11:15–11:45, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

In this session, we address a common problem in deep ranking systems: When models prioritize contextual signals over item-specific attributes, they lose the ability to differentiate between items in the same context, leading to poor calibration and unreliable downstream decision-making.

Besides introducing different architectural interventions to address item-neglect in deep neural networks, we will share real-world results from productionized models. We will demonstrate that forcing the model to prioritize item features and specific interactions can improve ranking performance. To ensure these concepts are actionable, we will showcase practical implementations and code snippets that can be integrated into modern deep-learning pipelines.

Talk Outline:

Introduction & Problem Statement (3 min)
The Impact of Item Neglect (5 min)
Architectural Interventions (14 min)
Real-World Example and Results (3 min)
Q&A (5 min)

Source: <https://pretalx.com/pydata-amsterdam2026/talk/MDCKAF/>

## 10. [DuckLake: The Lakehouse That Finally Embraces the Database](https://pretalx.com/pydata-amsterdam2026/talk/ADK8J8/)

**Speakers**: Graziano Montanaro

**When and where**: Thursday 2026-09-10, 11:55–12:25, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Modern lakehouse formats brought ACID transactions and schema evolution to object storage, but they also introduced substantial metadata machinery. Apache Iceberg uses JSON metadata and Avro manifests, while Delta Lake maintains a transaction log and periodic checkpoints. These designs are proven and widely supported, but operating them can involve metadata maintenance, log processing, orphan-file cleanup, and additional catalog infrastructure.

DuckLake takes a different approach: it stores lakehouse metadata in ordinary SQL tables while keeping table data as Parquet on local or object storage. Wether it's PostgreSQL, SQLite, or DuckDB, each of them can act as the transactional catalog and single source of truth. With release v1.0 DuckLake is now production-ready, with a stable specification and backward-compatibility guarantees.

What will be covered

Why SQL-backed metadata? A concise comparison with Iceberg manifests and Delta transaction logs, including the operational trade-offs of each approach.

DuckLake architecture: How relational catalog tables represent schemas, snapshots, statistics, partitions, and data files—and how this enables snapshot isolation and multi-table ACID transactions.

Live demo with Python and DuckDB:

Connect to a PostgreSQL-backed DuckLake catalog and inspect its metadata

Ingest and query a managed table

Execute an atomic multi-statement transaction

Query historical snapshots and inspect changes through the change data feed

Demonstrate schema evolution, upserts, and maintenance operations

Limitations: The catalog database becomes critical infrastructure; access control currently relies on the catalog and storage systems; heavily conflicting writes can exhaust retries; and the broader multi-engine ecosystem is still less mature than Iceberg or Delta Lake.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/ADK8J8/>

## 11. [Maybe 3 Minutes, Maybe Chaos – when Conformal Prediction meets my commuting life](https://pretalx.com/pydata-amsterdam2026/talk/XDZ3HW/)

**Speakers**: Konstantinos Tsoumas

**When and where**: Thursday 2026-09-10, 11:55–12:25, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Forecasts are very brave little things: they happily tell you “3 minutes late” without telling you whether that estimate is solid or about to collapse into chaos. Standard forecasting models usually give point predictions, not prediction intervals with guarantees. That is where conformal prediction helps. This talk is about turning train delay forecasts into uncertainty aware predictions with coverage guarantees, using conformal prediction under realistic time-series drift.

However, time series are rude. Once drift, disruptions, and changing conditions appear, plain conformal prediction starts to struggle because yesterday’s calibration may no longer match today’s reality. The question easily now turns from “what is conformal prediction?” to which conformal method still works when the world shifts?"

Inspired by my daily nightmares, using **open source** Dutch train delay data, the core of the talk is a practical comparison of three conformal strategies for time series forecasting, presented as a deployment progression (Fixed split conformal prediction, Adaptive conformal inference (ACI), EnbPI). Those methods are approaching common problems in forecasting like drift, in different ways and that's why they were chosen. All of these approaches are implemented in well known libraries like MAPIE and are available to the user to support **open source**.

The outline:

- Commuter tragedy ( personal train commuting struggles)
- Why point forecasts are not enough
- How conformal prediction helps (add calibrated uncertainty on top of any forecaster)
- Wait a second, plot twist: time series ruin everything: plain conformal breaks in time series (drift, dependence)
- The method ladder: - Fixed Split CP: simple baseline (the naïve but lovable baseline) - ACI: adapt online to recent errors (the anxious adapter constantly updating) - EnbPI: handle sequential dependence with ensembles (the ensemble chaos manager)
- What to use when

Note that the above is an outline of the talk and not a per-slide equivalent. The main dissection, in terms of time, is that the first part will introduce the general problem (and my personal story) of point forecasts and the vanilla solution in 7 minutes. In the next section, the different approaches will be introduced in about 8 minutes. With the 10 minutes left, the direction will be on the practical answer of comparing strengths, weaknesses, and when to use which of the methods shown. The rest will be left for Q&A. The idea is to make this talk engaging with the audience.

This talk is unique among all prior PyData conformal prediction sessios. Conformal Prediction PyData talks have tended to emphasize on a broad overview of conformal prediction for time-series forecasting.

Unlike the time series focus at PyData Seattle 2023, the large‑scale forecasting angle at PyData London 2024, the energy‑grid case study at PyData Eindhoven 2023, the MAPIE library deep‑dive at PyData Global 2024, the gentle intro in Amsterdam 2024, the sktime/skpro probabilistic workshop in Amsterdam 2023, the regression only focus in London 2019 PyData and last year's PyData Amsterdam 2025 conformal prediction talk focused on either classification or general approach in time series, this talk shows the difference methods in Conformal Prediction and helps with "when to use which strategy in production". This is very crucial cause vanilla conformal prediction does break in production as mentioned above.

This talk is **built are around only open source** materials like libraries (Nixtla, Pandas), datasets (Rijdendetreinen). The code will be shared with the audience as well.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/XDZ3HW/>

## 12. [Reliable, rigorous, wrong: A psychometric view of LLM evals](https://pretalx.com/pydata-amsterdam2026/talk/DK7SZW/)

**Speakers**: Jodie Burchell

**When and where**: Thursday 2026-09-10, 11:55–12:25, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Modern LLM evaluation increasingly focuses on making scores more trustworthy: using held-out datasets, calibrating LLM judges, running evals in CI, controlling experimental variation, and applying rigorous statistics. These are all valuable techniques, but they leave a more fundamental question unanswered: what does the resulting score actually measure, and what conclusions does it justify?

This talk introduces that question through psychometrics, the field concerned with measuring constructs that cannot be observed directly. We’ll focus on the concept of validity: the evidence that supports the interpretation we want to make from a score. Applied to LLM evals, validity gives us a practical way to work backwards from the claim we care about. If we say an agent is “helpful”, for example, we can ask whether our eval cases actually sample helpful behaviour, whether irrelevant factors such as task structure change the score, whether independent measures of helpfulness agree, and whether better eval scores correspond to better outcomes in the real application.

We’ll make these ideas concrete using failures of LLM reasoning assessments. We’ll look at cases validity checks fail, and show that the supposed reasoning ability of LLMs are reflective of something rather different. A live Python demo will let us explore one of these effects ourselves. These examples provide controlled demonstrations of the same validity problems that can occur in application-specific evals.

We’ll then return to real LLM applications and show how validity can improve the way we design and interpret our evals. Rather than asking only “what metric should I track?”, we’ll start with “what claim do I want this eval to support?” and use that to guide the choice of cases, scoring criteria, robustness checks, corroborating evidence, and the boundaries within which the result should generalise.

The talk will cover:

- Why knowing that an eval score changed is different from knowing that a system improved.
- How psychometrics deals with latent constructs, and how validity turns an eval score into an evidence-based claim about a system.
- How to look for validity evidence in practice: whether an eval captures the intended behaviour, survives irrelevant changes, agrees with other measures, and predicts outcomes we care about.
- Examples from LLM reasoning assessments, including a live demonstration of how assessment conditions can change apparent model performance.
- Four questions to apply when designing your own evals: What claim am I trying to support? What else could move the score? What other evidence should agree with it? Where does the interpretation stop?

This is an intermediate talk but designed to be accessible to anyone who has worked with machine-learning metrics or LLM applications. No prior knowledge of psychometrics is required, and the core ideas will be introduced from first principles.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/DK7SZW/>

## 13. [Your dashboard is too late: Building real-time KPI alerting systems with Python](https://pretalx.com/pydata-amsterdam2026/talk/GUDRCR/)

**Speakers**: Thijs Bressers

**When and where**: Thursday 2026-09-10, 11:55–12:25, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Topic & Relevance**
Most organizations rely on dashboards for monitoring KPIs, resulting in delayed reactions and missed signals. Meanwhile, data teams struggle with alert fatigue and brittle threshold systems.

This talk introduces a Python-based, event-driven KPI framework that transforms metrics into actionable signals.

**Technical Depth**
KPI definitions using Pydantic / typed schemas
Execution using DuckDB
Rule-based and statistical alerting
Dependency graphs between KPIs
Alert delivery via Slack/webhooks
Anomaly detection (lightweight stats)

**Target Audience**
Data engineers
Analytics engineers
Data scientists working with metrics and monitoring

**Level**:
Intermediate

**Audience Takeaways**
How to define KPIs as code (not dashboards)
How to build alerting systems that reduce noise
How to structure dependency-aware KPI evaluation
How to enable self-service monitoring for teams

**Required Background**
Python
Basic data analysis (Pandas/SQL)
Familiarity with KPIs or business metrics

**Talk Type & Approach**
Practical, system design oriented
Code examples + architecture
Real-world patterns (not theoretical)

**Outline (30 min)**
Introduction why dashboards fail (5 min): Passive vs active data systems
KPI Modelling (8 min): Metrics as code, semantic definitions
Execution Layer (5 min): Computing KPIs with DuckDB (or Pandas/Polars)
Alerting System (8 min): Rules, anomaly detection, dependencies
System Demo / Example Flow (3 min): From KPI change → alert → action
Takeaways (1 min): Principles for operational data systems

Source: <https://pretalx.com/pydata-amsterdam2026/talk/GUDRCR/>

## 14. [Embed First, Predict Later: Energy forecasting from weather embeddings](https://pretalx.com/pydata-amsterdam2026/talk/9GR8L8/)

**Speakers**: Kai Jeggle

**When and where**: Thursday 2026-09-10, 13:30–14:15, room Fractal

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

### Beyond Text and Images

In computer vision, nobody hand-crafts features anymore. The field went from manual feature engineering to end-to-end CNNs to self-supervised foundation models like DINO that produce reusable representations from unlabeled data. Same story in NLP. The lesson both fields converged on: learning what things _are_ and learning what to _predict_ from them are better done as two separate steps.

Often people working with high-dimensional real world data beyond text and vision haven't made that jump yet. The default is still: pick some variables that you think represent your input space and relate to your target, flatten them into a dataframe, and feed it to a tree-based model or neural network. It gets you surprisingly far. But when your input space is high-dimensional and complex while targets are low-dimensional - often single numbers - this approach leaves signal on the table and tends not to generalize to related tasks.

This talk is about closing that gap and giving the audience the tools to do it themselves.

### The Representation Bottleneck

The obvious alternative is to train a larger (transformer) neural network end-to-end on the raw data. But in specialized domains, labeled data is hard to come by. e.g. a model trying to predict energy generation from weather has to figure out what storms and cloud systems look like at the same time as learning how they relate to the target variable, all only guided by a scarcely available loss signal. In practice the results are often disappointing and “deep learning doesn’t work for our use case” becomes the sentiment.

### Building Blocks of the Pipeline

We walk through three components that together form a reusable recipe:

**1. The backbone.** This can be taking the encoder of a publicly available pre-trained foundation model, in our example we are using the encoder of the Aurora AI weather model by Microsoft Research. Alternatively, a backbone can also be trained e.g. using masked autoencoders. The task of the backbone is to compress raw inputs into dense embeddings that capture abstract patterns, in our example weather regimes, seasonal cycles etc.. The backbone is trained without any task-specific supervision. We discuss how to pick a backbone that fits your domain and what to look for.

**2. The embeddings.** Dense numerical vector representations created by passing raw high-dimensional input (e.g. weather data) through the backbone.

**3. Downstream models.** Small models that map embeddings to a specific target. These models are cheap to train, e.g. using personal hardware or a single GPU. The same set of embeddings can serve many different downstream tasks. Put differently, the downstream model picks relevant representations from all representations extracted by the backbone. In our example this can be wind production forecasting, solar prediction, energy demand estimation, or insurance damage assessment. No need to rerun the backbone for each new task.

## Outline

The talk introduces a general paradigm, but we spend most of the time on our concrete showcase, always circling back to how each step generalizes and how the audience can apply it to their own use case.

- Introduction and Problem Setting: 5 min
- Building blocks: 5 min
- Energy/Weather data showcase: 15 min
- Examples from other domains, practical tips: 15 min
- Q&A: 5 min

Source: <https://pretalx.com/pydata-amsterdam2026/talk/9GR8L8/>

## 15. [Grounding AI Agents in Your Data Model](https://pretalx.com/pydata-amsterdam2026/talk/CHWKKQ/)

**Speakers**: Ricardo Angel Granados Lopez

**When and where**: Thursday 2026-09-10, 13:30–14:15, room Entropy

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Every governance tool we already trust (ERDs, semantic layers, data catalogs, etc.) assumes someone already got the data model right before writing it down. That assumption is quietly breaking as AI starts drafting that first pass. This talk shows a citation-grounded pipeline, live: an agent drafts an ontology from a real dbt project, and a validator mechanically checks every claim it can, flagging rather than silently trusting the ones it can't.

Target audience: data engineers, analytics engineers, and ML/AI practitioners working with structured data pipelines. Basic SQL and data-modeling familiarity is assumed; no dbt or formal ontology/semantic-web background is needed. Especially relevant if you're already using AI coding agents in your own data work and have felt the "it forgot everything from last session" problem, or if you're evaluating how to bring AI agents into a data platform responsibly.

Audience takeaways:

A concrete, working pattern for citation-grounded AI-assisted documentation, adaptable to your own project
A precise mental model for what can be mechanically verified versus what always requires human judgment
A live demonstration of the pattern actually catching mistakes
An honest map of what this approach solves today, and what it deliberately doesn't
Scope: the approach, in four stages

Extract: pull structural facts from the project (e.g. a dbt manifest), zero AI involvement, deterministic and correct by construction
Draft: an AI agent proposes documentation/ontology claims, citing exactly where each one comes from
Validate: every citable claim is mechanically checked against the extracted facts; claims that can't be mechanically checked are flagged, never silently trusted
Signoff: a human explicitly confirms every flagged item before it counts as settled, tied to the exact claim text so a later edit invalidates a stale approval
Scope: what this does not solve

It doesn't automate grain or cardinality reasoning; those stay human judgment calls, permanently, by design, not a current limitation waiting to close
It doesn't check live data values at runtime (NULL drift, row-count anomalies, and similar); this operates at the documentation/metadata layer, not as a data-quality or observability tool
It's not a claim that AI can replace the architectural judgment good ontology design requires, only that AI can help draft and citation-check the structural layer faster, with a human still owning the design decisions
Outline (40 min content + 5 min Q&A):

0–5 min: The claims tools like ERDs and semantic layers make, and why AI complicates them
5–12 min: What it actually took to get an AI agent to draft a data model worth trusting
12–20 min: The mechanism: extract, draft, validate, signoff, live
20–28 min: Running the validator live, against a real project
28–35 min: Grounding a genuinely ambiguous table, live
35–40 min: Where this goes next, and what we're not claiming
40–45 min: Q&A

Source: <https://pretalx.com/pydata-amsterdam2026/talk/CHWKKQ/>

## 16. [Inside the Mind of an LLM](https://pretalx.com/pydata-amsterdam2026/talk/NPZNKA/)

**Speakers**: Luca Baggi

**When and where**: Thursday 2026-09-10, 13:30–14:15, room Anomaly

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Mechanistic interpretability treats neural networks not as statistical black boxes, but as complex, _reverse-engineerable source code_. The ultimate goal of the field is to map the internal weights and activations of a transformer directly to discrete, human-understandable algorithms.

This session traces the mathematical and empirical evolution of the field, exploring how researchers spent recent years validating core working hypotheses, such as the Linear Representation Hypothesis (LRH) and feature superposition, within controlled toy settings before successfully scaling them to modern state-of-the-art architectures. We will deconstruct how to isolate **monosemantic concepts** from dense layers using techniques like **sparse dictionary learning**, examine Anthropic's milestones in mapping computational subnets, and evaluate how **activation steering** translates into a live, low-latency mechanism for model control that does not require fine-tuning.

To anchor these concepts, we will showcase how Ramp Labs deployed activation steering in practice, and examine Anthropic’s 2026 discovery of **functional emotion circuits**. We will then address current limitations exposed by these applications, such as the subjectivity of post-hoc automated feature labelling, before concluding with how the field is evolving beyond traditional dictionary learning toward newly proposed architectures like "Natural Language Autoencoders" designed specifically to bypass these fundamental limits.

### Outline

- 0-5': Intro and LLM steering demo (Ramp Labs).
- 5-15': From polysemantic neurons to monosemantic features.
- 15-25': From dictionary learning to circuit tracing.
- 25-30': Shortcomings of dictionary learning.
- 30-35': LLM steering
- 35-40': Newest research trends (Anthropic, Nous Research) and conclusions.

### Target audience

Aimed at data scientists and AI engineers. Attendees should have a basic understanding of core transformer primitives such as attention, residuals and activations. No prior interpretability background is required; necessary vector-space intuition will be built from scratch.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/NPZNKA/>

## 17. [Lightning talks](https://pretalx.com/pydata-amsterdam2026/talk/GJ7ETY/)

**Speakers**: You are all invited!

**When and where**: Thursday 2026-09-10, 13:30–14:15, room The Grid

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

-

Source: <https://pretalx.com/pydata-amsterdam2026/talk/GJ7ETY/>

## 18. [A/B Testing Plenary Debates in the Dutch Parliament with Multi-Agent AI using LangGraph](https://pretalx.com/pydata-amsterdam2026/talk/Z87GCU/)

**Speakers**: Jeroen Nelen

**When and where**: Thursday 2026-09-10, 14:25–14:55, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Simulating real-world human institutions with LLMs introduces unique technical challenges.
For example, how do you enforce strict procedural rules without destroying dynamic debate
flow? How do you keep agents grounded in distinct political identities without leaning into
caricature? And how do you measure the systemic impact of structural changes? These
topics will be addressed in this presentation.

### Outline:

1. Introduction & Problem Statement (4 min): Context on parliament simulation,
   project scope, and the motivation behind modeling democratic reforms.
2. Architecture & Deterministic State (6 min): Using LangGraph to manage state
   transitions, turn-taking, and procedural parliamentary rules throughout the debate.
3. Traceability & Debugging (3 min): Using LangSmith to monitor prompt inputs, tool
   calls, and token costs for debugging
4. Grounding Agents & Mitigating Bias (6 min): Combining structured context,
   party-filtered RAG, and voting histories to ground agent speeches and reduce base
   model bias.
5. A/B Testing Systemic Reforms & Findings (7 min): Evaluates structural
   democratic reforms by simulating 238 debate runs to measure their impact on debate
   quality and policy outcomes.
6. Limitations & Conclusions (4 min): Addressing the inherent limitations of using
   LLMs for simulations and validating transcripts with domain experts.
7. Q&A

### Takeaways:

- How do you transfer a real-world system such as debates into a full multi-agent
  simulation
- How to control next-turn decisions in this multi-agent using custom bidding phases
- Grounding the agent personas using RAG to make sure the agent doesn’t rely on
  internal knowledge
- How to create an A/B experiment to test systemic changes.

### Impact

The impact of this project created additional evidence that reforms in the parliament are
necessary. The findings have been used in a report by this think tank with advice on how to
strengthen democracy and is read by politicians, journalists and policy experts.
Generalized applications
This multi-agent simulation could be interesting in any team environment where you would
like to have multiple agents with distinct opinions, expertise and philosophies. You could
instruct them to come to a consensus and see how that plays out. For instance, engineering
teams, executive boards, focus groups or cross-functional teams could be simulated.

### Generalized applications

This multi-agent simulation could be interesting in any team environment where you would
like to have multiple agents with distinct opinions, expertise and philosophies. You could
instruct them to come to a consensus and see how that plays out. For instance, engineering
teams, executive boards, focus groups or cross-functional teams could be simulated.

### Target audience

This talk is interesting for Machine Learning Engineers, Data Scientists, and Developers who
want to start or have experience with building AI agents, RAG and layered prompting

Source: <https://pretalx.com/pydata-amsterdam2026/talk/Z87GCU/>

## 19. [Scaling Two-Way Fixed Effects Models in Python with pyfixest: Lessons from Airline Pricing](https://pretalx.com/pydata-amsterdam2026/talk/FAAVMX/)

**Speakers**: Rutger Lit

**When and where**: Thursday 2026-09-10, 14:25–14:55, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Two-way fixed effects (TWFE) models** are widely used to analyze panel data in pricing, demand modeling, and experimentation. In small examples they appear straightforward. In real-world **Python workflows** they are often not.

This talk focuses on how to estimate TWFE models in practice using `pyfixest`, with an emphasis on **scalability, correct specification, and interpretation**.

We start with a brief recap of TWFE models and their role in panel data analysis. We then introduce `pyfixest` as a Python tool for estimating models with **high-dimensional fixed effects**, and show how it differs from more naive approaches. In particular, we discuss why explicitly constructing dummy variables is infeasible in large datasets, and how within-transformations allow estimation without exploding memory.

The core of the talk is a set of real-world **airline pricing applications**. These include both experimental settings and observational analyses used to estimate price elasticities from historical data. The data is structured along multiple dimensions (such as route, time, and booking horizon), which makes TWFE a natural modeling choice, but also exposes several practical challenges:

- high-dimensional fixed effects that make naive implementations computationally infeasible
- specification choices where fixed effects absorb the variation needed for identification
- clustered standard errors that depend critically on the correct level of aggregation
- temporal dependence that can lead to overconfident inference if not handled carefully
- data issues such as boundary effects or leakage across time periods

Using `pyfixest`, we show how to specify models for these settings, how to run them efficiently, and how to diagnose when results should not be trusted. The focus is on what practitioners actually encounter: models that run but give misleading answers due to subtle specification errors.

The talk concludes with a set of **practical guidelines** for applying TWFE models in Python: how to structure data, how to choose fixed effects and clustering levels, and what checks to perform before interpreting results.

The goal is not to present TWFE as a general solution, but to show how it can be applied in a **controlled and reliable way** in large-scale Python workflows.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/FAAVMX/>

## 20. [The modern tool builder: CLIs, agents, and PEP 723](https://pretalx.com/pydata-amsterdam2026/talk/B8BRSA/)

**Speakers**: Jeroen Janssens

**When and where**: Thursday 2026-09-10, 14:25–14:55, room Entropy

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**script** (_noun_, _Computing_) A sequence of instructions, often single-purpose and context-dependent, that is interpreted by another program.

**tool** (_noun_, _Computing_) A reusable and flexible piece of software designed to solve problems across different contexts or aid in accomplishing diverse tasks.

Being able to write Python scripts is an incredibly useful skill, allowing you to automate nearly any task imaginable. However, with a bit of extra effort, those brittle scripts can be transformed into robust, reusable tools. In particular, tools that you can run from the command line or that can be run by coding agents. Future-you will thank you for making the extra effort.

In this talk, we will explore why you should graduate from writing scripts to building tools, particularly command-line interfaces (CLIs).

CLIs have been around for over 50 years. Thanks to the rise of coding agents, being able to understand and use the command line is now more important than ever. I'd say there are three reasons for this. First, coding agents rely on CLI tools such as find, grep, and git (and maybe yours!). Second, some coding agents, such as Claude Code, are themselves CLI tools that you can incorporate into your scripts. Third, agents are actually really good at helping you to build your own tools, so if you use them there's really no excuse anymore.

The talk first explains why you should consider turning your scripts into flexible, reusable tools. Then, it covers the steps needed in order to do so. Outline:

- Introduction: The CLI Renaissance (5 mins)
- The Unix Philosophy is the AI Tool Philosophy (5 mins)
- Designing for Humans and Agents (10 mins)
- Zero-Setup Execution with PEP 723 (5 mins)
- Polishing the Interface (5 mins)

Source: <https://pretalx.com/pydata-amsterdam2026/talk/B8BRSA/>

## 21. [When Context Breaks: Recursive Language Models with DSPy](https://pretalx.com/pydata-amsterdam2026/talk/SPZLFK/)

**Speakers**: Niels van Galen Last

**When and where**: Thursday 2026-09-10, 14:25–14:55, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Current LLM workflows work surprisingly well until context becomes the bottleneck. Tasks like multi-file code changes, long-log debugging, or stateful tool use that many teams attempt to solve with prompt engineering or agents often succeed at small scale and then become brittle as the amount of context grows.

This talk introduces Recursive Language Models (RLMs), a different approach in which context is treated as data that can be programmatically explored, decomposed, and revisited - rather than input that must be consumed in a single prompt. This shifts long-context LLM systems from brittle prompt orchestration to programs that explicitly explore, track, and update context over time.

Using DSPy as a concrete Python implementation, I will demonstrate how this approach turns a failing long-context task into a tractable one, and what this shift means for designing LLM systems in practice.

Attendees will leave with a clear mental model for when standard prompting breaks, what RLMs change technically, and how to prototype this pattern in practice.

Many LLM systems work well on the first version of a task and then degrade as the problem grows. A prompt that succeeds on one file struggles on ten; a workflow that works for a short sequence becomes brittle when it must track more state, revisit earlier decisions, or reason over larger context. In practice, the limitation is often not model capability, but the assumption that all relevant context must fit into a single prompt or prompt loop.

This talk introduces Recursive Language Models (RLMs) through that failure mode first. RLMs treat context not as input to be consumed, but as data that can be programmatically explored, decomposed, and revisited. Instead of relying on a single prompt, the model interacts with context through code, recursively breaking problems into smaller parts and selectively accessing only what is needed.

Using DSPy's `dspy.RLM` as a concrete Python implementation, I will demonstrate this shift with a compact example. We start with a task that works under a standard approach and then fails as the context grows. I then show how an RLM-style solution changes the structure of the problem: from brittle prompt orchestration to a program that explores context step by step, maintains explicit state, and revisits intermediate results when needed.

While the underlying idea is general, DSPy provides a clean way to prototype this pattern in Python, using a sandboxed REPL and recursive calls to interact with context. For many practitioners still writing prompts by hand, DSPy offers a structured path from prompt engineering to programmatic LLM systems.

Attendees will leave with:

- a concrete understanding of why prompt-based and agent-style approaches become brittle as context grows
- a practical mental model for treating context as something to operate on, not just consume
- a clear starting point for implementing this pattern in Python using DSPy

This is a technical talk for Python practitioners building LLM systems who want a more robust abstraction for long-context reasoning than "add more context" or "add another agent step.

Proposed structure (30 minutes)

- Introduction: where current LLM workflows break as context grows (5 min)
- A concrete example: a task that works at small scale and fails with larger context (5 min)
- Why this happens: limits of prompt-based and agent-style approaches (5 min)
- The shift: treating context as something to explore rather than consume (5 min)
- Recursive Language Models (RLMs): core idea and intuition (5 min)
- DSPy example: implementing the pattern in Python (5 min)

Optional extension (45 minutes)

- Additional time for a deeper implementation walkthrough and discussion of trade-offs, limitations, and real-world applications

Source: <https://pretalx.com/pydata-amsterdam2026/talk/SPZLFK/>

## 22. [Distilling LLMs into Classical ML for 5,000+ Classes](https://pretalx.com/pydata-amsterdam2026/talk/YPZA7R/)

**Speakers**: Oz Mendelsohn

**When and where**: Thursday 2026-09-10, 15:05–15:35, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Topic and Relevance**
We built a production system that uses an LLM as an offline labeling engine for a 5,000+ class text classification problem, then distills that into a classical ML model (gradient-boosted trees) that meets real-time latency requirements. This is knowledge distillation - but with a classical model as the student instead of a smaller LLM.
This matters now because LLM quality and cost have reached a point where they can serve as reliable domain-expert labelers for complex, large-scale taxonomies - not just simple annotation tasks. This talk shares the architecture, tradeoffs, and lessons from running this system in production.
**Outline (25 min + 5 min Q&A)**
_The Problem (5 min)_: 5,000+ class taxonomy where each class has formal definitions and correct labeling requires deep domain expertise. Manual labeling is economically infeasible. Unlabeled production data is abundant.
_The LLM as Labeling Engine (7 min)_: Multi-step agentic workflows with external reference documents produce high-quality labels. We cover our quality assessment approach (qualitative review, subset testing, error analysis) and address the imperfect-labels objection: even fitting to the LLM's mistakes, matching its performance in a fast classical model is already a strong result.
_Distilling into Production (6 min)_: Gradient-boosted trees trained on LLM labels achieve sub-real-time latency - this is what makes the product possible. We discuss the distillation framing and the path toward small fine-tuned transformers as the labeled data keep increasing.
_Active Learning Loop (5 min)_: Automated pipeline: production traffic → frequency-prioritized novel input detection → LLM labeling → retraining. Models versioned with DVC/git, deployment through PRs with daily human review. Many of cycles, steady accuracy improvement.
_When Does This Apply? (2 min)_: Open discussion on what makes a problem a fit for this pattern.
**Audience Takeaways**
The LLM-as-labeling-oracle pattern: when it applies, key design decisions, and what to watch out for - from a real production system.
How to think about imperfect LLM labels and manage labeling cost through frequency-based prioritization.
A practical approach to git-based active learning using (mostly) open-source tools (DVC, git, MLflow, LLM APIs).
**Target Audience**
Data scientists and ML engineers building products with large label spaces or labeling bottlenecks. Assumes basic supervised ML knowledge and general LLM familiarity.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/YPZA7R/>

## 23. [Real-time vs Batch Features for ML: Lessons from Fraud Detection at Scale](https://pretalx.com/pydata-amsterdam2026/talk/ABUNQA/)

**Speakers**: Csanád Bakos

**When and where**: Thursday 2026-09-10, 15:05–15:35, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk draws from production experience building and operating a real-time feature platform at a large online second-hand marketplace. The platform runs dozens of independent Apache Flink streaming jobs computing user behavior signals for ML-based fraud detection, processing millions of events per second.

**Outline with timing (25 min talk + 5 min Q&A):**

- **Why real-time features for fraud detection** (5 min)
  - The fraud timeline: what happens between a bad actor's first action and detection
  - Batch features introduce a blind spot of tens of minutes to hours. Streaming closes it to seconds
  - When the added complexity of real-time is justified — and when batch is good enough

- **Architecture: from event streams to inference and training** (10 min)
  - Event-driven pipeline: CDC and event streams from Kafka → Flink processing → Feature Store → ML inference
  - Reactive triggers: ML re-scoring fired automatically based on feature updates or specific user actions
  - Reusing streaming output for model training: sinking features to a data warehouse. Why a raw dump isn't suitable for training and the strategies we applied to make it work alongside batch-produced datasets (backfills, deduplication, data cleaning)

- **Streaming vs batch feature engineering** (7 min)
  - Fundamental differences: bounded vs unbounded data, incremental vs full recomputation
  - Key Flink building blocks that make real-time work: stateful operators, fault tolerance, exactly-once guarantees, horizontal scaling
  - Operational realities: checkpointing, state management, deployment complexity
  - Flink can also do batch — but when real-time isn't needed, dbt with your favourite data warehouse is likely a better fit — will explore why

- **Wrap-up and Q&A** (3 min + 5 min)
  - Key lessons and challenges that remain
  - Open discussion

**Approach:** Practical and experience-driven. Architecture diagrams, concrete production examples, and honest discussion of trade-offs. No live coding or demos.

**Required background knowledge:** Basic understanding of what ML features are. Familiarity with Kafka or event-driven systems is helpful but not required — key concepts will be briefly introduced.

**Scope:** We focus on the architecture and trade-offs of real-time feature engineering for ML, not on Flink APIs or framework internals. The talk is grounded in a fraud detection use case but the patterns are applicable to any domain where feature freshness matters. We will not compare Flink to other stream processing frameworks directly, but the principles shared will help attendees evaluate what capabilities matter for their own use cases.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/ABUNQA/>

## 24. [The unreasonable effectiveness of DAS: ML on fiber-optic vibration data for rail monitoring](https://pretalx.com/pydata-amsterdam2026/talk/HDXACL/)

**Speakers**: Joost van 't Schip, Schelto Crone

**When and where**: Thursday 2026-09-10, 15:05–15:35, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Technical depth**
We start by showing what DAS data actually looks like: a continuous waterfall of vibration amplitudes across distance and time, sampled at thousands of hertz along up to 100 km of fiber at 1m spatial resolution. This is a unique type of data that most of the audience will not have encountered before, which makes it a good foundation for the rest of the talk. From there, we walk through two real-time ML/signal processing pipelines that both operate on the same raw data source.

_Trespasser detection:_ We convert windows of raw DAS data into 2D STFT spectrograms and treat the problem as an image detection task using YOLOv8. We'll cover why this spectrogram-as-image approach works well, how we trained the model, and the steps we took to optimize it for edge hardware: exporting to ONNX, applying model optimization and running inference using the Intel MKL-optimized onnxruntime — all to achieve real-time performance on a CPU-only server with no GPU.

_Train detection and tracking:_ Here we take a more classical signal processing route. We use STA/LTA (short-term average / long-term average) triggering to detect train presence in the DAS signal in real time, then feed detections into a Kalman filter to continuously track each train's position along the fiber. This pipeline shows that simple well-understood techniques get you real-time results with minimal computational overhead.

We'll briefly touch on two additional use cases under active exploration: rail defect detection and subsurface monitoring. These illustrate the breadth of what a single DAS installation can support.

**Scope feasibility**
The talk fits comfortably in a 25-minute slot. We cover one shared data source (DAS) and two main applications. The defect detection and subsurface topics are kept brief. We include multiple demo footages of the systems running on real DAS data.

**Educational value**
The audience will see a full journey from an unusual raw signal to real-time detections using two very different approaches (deep learning and classical signal processing). Practical takeaways include: how to reframe a sensor signal as an image detection problem, how to optimize a YOLO model for CPU-only edge deployment using ONNX and hardware-specific runtimes, and how to apply classic signal processing techniques. These techniques are transferable well beyond rail monitoring.

**Relevance to the conference**
The entire stack is Python-based (h5py, onnxruntime, numpy/scipy). The talk highlights a real-world use case where current state-of-the-art ML and signal processing techniques come together to solve a practical infrastructure problem in real time on constrained hardware. In doing so, the project contributes to keeping rail infrastructure safe and reliable, improving the quality of the public transport system.

**Outline:**
Intro in DAS for rail monitoring: 10 min
Real-time train detection and tracking: 7.5 min
Trespasser detection: 7.5 min
Other work: 5 min
Q&A: 5 min

Source: <https://pretalx.com/pydata-amsterdam2026/talk/HDXACL/>

## 25. [Your A/B Test Is Leaking: Practical Lessons in Measuring Network Effects](https://pretalx.com/pydata-amsterdam2026/talk/B9QGMW/)

**Speakers**: Dror A. Guldin

**When and where**: Thursday 2026-09-10, 15:05–15:35, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk surveys approaches for measuring network effects in A/B tests, grounded in practical experience running experiments in highly-networked products. Each method is presented with its intuition, applicability, and real-world trade-offs. Not as a linear progression, but as a toolkit where the right choice depends on the product context, technical feasibility, and privacy constraints.

## Outline:

**Why this matters** (2 min). Experiments exist to quantify trade-offs. When network effects are present but unmeasured, we're making launch decisions on incomplete, or misleading, data. Concrete example: a UI change that boosts one behavior while suppressing another through indirect exposure, where a naive A/B test shows a positive result but the true net effect is negative.

**The core problem** (3 min). SUTVA and why it breaks in networked products. Visual intuition for how treatment "leaks" through user interactions. Why the measured effect in a standard A/B test can be an underestimate, an overestimate, or even directionally wrong.

**The toolkit** (16 min). Six approaches, each with trade-offs:

1. _Ignoring network effects (YOLO)_: when it's a reasonable approximation and when it'll burn you. (2 min)
2. _Bi-directional metrics_: logging interactions from both sender and receiver, then summing effects. Intuitive and practical for 1:1 interactions. (2 min)
3. _Translation coefficients_: estimating multipliers that convert direct impact to ecosystem-level impact. Necessary for 1:many features and engagement metrics. (2 min)
4. _Double-sided gating_: ensuring control users aren't exposed to the feature via interactions with treated users. When it works, when it's technically or otherwise infeasible (3 min)
5. _Cluster-based randomization_: randomizing at the group/region/cluster level to contain spillovers. Trade-offs around power, cluster definition, and residual leakage. (3 min)
6. _Bipartite analysis_: modeling the experiment as a bipartite graph with treatment units on one side and outcome units on the other, using exposure-reweighted linear estimation (Harshaw et al., 2021) to recover the total effect. Will also cover some practical innovations in implementing this approach in practice (4 min)

**Decision framework & takeaways** (4 min). A practical guide for choosing the right approach based on interaction type (1:1 vs 1:many), technical feasibility, privacy requirements, and statistical power considerations.

Q&A (5 min)

Source: <https://pretalx.com/pydata-amsterdam2026/talk/B9QGMW/>

## 26. [Amidst the Visualization and Art of Data](https://pretalx.com/pydata-amsterdam2026/talk/VFY7MA/)

**Speakers**: Nadieh Bremer

**When and where**: Thursday 2026-09-10, 16:05–16:55, room The Grid

**Type**: Keynote

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/VFY7MA/>

## 27. [Techie vs Comic Episode 3: Natural Intelligence](https://pretalx.com/pydata-amsterdam2026/talk/NFLWNA/)

**Speakers**: Arda Kaygan

**When and where**: Thursday 2026-09-10, 17:20–17:50, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Prompt engineering is dead. But comedy is still alive. So is Arda, (thank god… ) PyData’s critically acclaimed standup comedian / data scientist. Rolling through life, career and delegated thinking amid falling em dashes from the sky, he is returning for another tale of absurdity. In this intentionally non-informative talk he will take the audience through his journey of acceptance in the age of AI as a developer and a person with a very natural intelligence. Given his newfound confidence on building agents, he will also share his new ventures that make a lot of sense. Expect guest appearances (likely to be human) and an escape from token counts that matter.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/NFLWNA/>

## 28. [Analytics future](https://pretalx.com/pydata-amsterdam2026/talk/UAKVAE/)

**Speakers**: Christophe Blefari

**When and where**: Friday 2026-09-11, 09:00–09:50, room The Grid

**Type**: Keynote

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

tbd

Source: <https://pretalx.com/pydata-amsterdam2026/talk/UAKVAE/>

## 29. [Data First, Model Second: Three Strategies for Production Computer Vision](https://pretalx.com/pydata-amsterdam2026/talk/UPGM73/)

**Speakers**: Alexander Kern, Guus van der Ham

**When and where**: Friday 2026-09-11, 10:05–10:50, room The Grid

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

## Overview

This talk argues that production computer vision performance is fundamentally a data problem, not a model problem, and presents three data-side strategies to back that claim. Rather than showcasing results or benchmarks, we share the principles and workflows we believe are essential for any practitioner deploying computer vision in the real world.

The entire talk is grounded in a single, concrete case: counting crates moving through a logistics environment. We chose this case precisely because it sounds trivial. It is not. The gap between "this should work" and "this actually works in production" turned out to be almost entirely a data gap, not a model gap. To increase performance in production, we focused on improving our dataset instead of augmentations, backbones, or hyperparameters.

The three strategies are presented as complementary principles, not isolated techniques. Each one is explained through the lens of this case, with honest discussion of what worked, what didn't, and what we'd approach differently. The talk is designed so that attendees walk away with transferable thinking they can apply to their own pipelines, regardless of domain or framework.

### **Outline with Estimated Timing (45 min)**

**Opening & framing (5 min)**

We open with the case itself: crates on transport dollies moving through a logistics facility. The task sounds simple, count what you see. We use this apparent simplicity as the hook: what happens when you deploy this in production, where crates are stacked unpredictably, mixed with foreign objects, and seen under conditions your training data never captured? This sets up the central thesis: the model was never the bottleneck. The data was. We frame the three strategies as essential workflows for production-grade computer vision.

**Strategy 1: Annotation quality at scale (12 min)**

Production datasets are systematically mislabelled, and teams rarely acknowledge it. We show how to use the model's own predictions to surface annotation errors using confidence disagreements and embedding-based clustering to find the most ambiguous, error-prone samples. We walk through the iterative review workflow: when to inspect, what to correct, and when to stop. The key principle: annotation quality is not a one-time task but a continuous loop that should be integrated into your production pipeline.

**Strategy 2: Synthetic data generation (10 min)**

Some edge cases simply don't exist in your real dataset: new crate types, unusual stacking configurations, lighting conditions you haven't encountered yet. We explain how synthetic data can fill these gaps, the decisions involved in scene design and rendering, and the challenge of bridging the domain gap between synthetic and real images. We're candid about the limitations: synthetic data doesn't transfer automatically. We also address one honest exception to our "data first, model second" thesis: to close the domain gap between synthetic and real images, we use a domain adversarial training approach that is, strictly speaking, a model-side intervention.

**Strategy 3: Intelligent dataset reduction (10 min)**

More data is not always better data. In production, you are continuously collecting vast amounts of unlabelled data. Annotating all of it is both impractical and counterproductive: most samples are highly similar and add little to the model's performance. We present the principle of curating maximally informative subsets from large uncurated pools, selecting what to train on rather than training on everything. We show results from our own pipeline where a fraction of the dataset matched or outperformed the full set, and discuss the trade-offs of aggressive curation and how to manage them.

**Lessons learned & closing (8 min)**

We reflect on what was harder than expected, how the three strategies interact (and sometimes conflict), and what we'd do differently. The closing message: these strategies form a continuous data pipeline, not a one-time fix. Production is never "done," but these workflows make your life significantly easier when you're running a computer vision solution in the real world. Open floor for questions.

### **Additional Details**

**Prior knowledge expected:** Familiarity with supervised learning and basic object detection concepts (bounding boxes, confidence scores). No specific framework or tooling knowledge required.

**Talk type:** Principles-based, case-study grounded. No live demos or benchmark comparisons. The goal is conceptual clarity and transferable judgment, not replicating a specific stack.

**Scope boundaries:** This talk focuses exclusively on data-side interventions. We do not cover model architecture choices, deployment infrastructure, or real-time inference optimisation.

**Materials:** Slides will be shared publicly after the conference.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/UPGM73/>

## 30. [Scheduling at Scale: Building a Railway Timetable Optimizer in Python](https://pretalx.com/pydata-amsterdam2026/talk/XJJUQH/)

**Speakers**: Merel Groen, Willem Feijen

**When and where**: Friday 2026-09-11, 10:05–10:50, room Anomaly

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk presents a real-world case study of building a railway timetable optimization system in Python, designed to support planners during infrastructure maintenance when network capacity is reduced.

**Problem Context**
Railway timetables must satisfy strict safety constraints and balance multiple stakeholders (national, freight, and international trains). During planned maintenance, the original timetable often becomes infeasible, requiring generation of alternative schedules that minimize disruption.

**Approach**
We model the problem using:

- Periodic Event Scheduling Problem (PESP) for network timing constraints
  - Including optimization decisions such as cancellations, re-routing, and time adjustments
- Station Capacity Models (SCM) for track assignment

The implementation is built entirely in Python, combining:

- Object-oriented design for maintainability
- Optimization modeling via Pyomo (solver-agnostic) and gurobipy (solver-specific)

**Key Technical Insights**
We discuss several practical engineering decisions:

- Trade-offs between solver-agnostic and solver-specific approaches
- Transition from solvers (SCIP to Gurobi) due to scaling limitations
- Performance bottlenecks in model translation and how persistent interfaces influences runtime
- Structuring large Python optimization projects

**Relevance**
This talk provides a practical, end-to-end perspective on applying optimization in production systems—bridging theory, implementation, and engineering trade-offs.

**Outline**
Note: We prefer the Deep Dive Talk (45 min) format to fully cover the technical trade-offs, but have included a Standard Talk (30 min) alternative.

Deep Dive Talk

- Introduction & Problem Context — 5 min
- Modeling the Railway Optimization Problem (PESP + SCM) — 10 min
- Python Implementation & Code Architecture — 5 min
- Solver Integration: Pyomo vs Gurobi — 15 min
- Q&A — 10 min

Standard Talk

- Introduction & Problem Context — 3 min
- Modeling the Railway Optimization Problem (PESP + SCM) — 7 min
- Python Implementation & Code Architecture — 4 min
- Solver Integration: Pyomo vs Gurobi — 11 min
- Q&A — 5 min

**Target Audience**

- Data scientists working with optimization problems
- Operations researchers
- Software engineers building production systems
- Intermediate level (basic Python required; optimization knowledge helpful but not mandatory)

**Prior Knowledge Expected**

- Basic Python
- Familiarity with optimization concepts (helpful but not required)

**Keywords**
optimization, operations research, pyomo, gurobi, gurobipy, scheduling, transportation, python, public transport, timetable

Source: <https://pretalx.com/pydata-amsterdam2026/talk/XJJUQH/>

## 31. [Serving Personalized ML at Scale with Evolving Runtimes](https://pretalx.com/pydata-amsterdam2026/talk/DAUQVR/)

**Speakers**: Rayan Daod

**When and where**: Friday 2026-09-11, 10:05–10:50, room Fractal

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Most ML systems serve a handful of general models to all users. On the other hand, a growing class of products instead trains a model per user on their own data, which is what the Atinary SDLabs platform does: these per-user models power our Bayesian Optimization algorithms that recommend the next experiments to run. With training code updated roughly every two weeks and an inference latency budget of a few seconds, how can we persist and serve these models in scalable ways while satisfying product requirements?

To build such a system, one could think of deploying a dedicated inference service per user. However this would quickly become operationally infeasible (at least for us). What about a shared inference environment then? Well, at the same time, the training code might be regularly improved, meaning that models trained just weeks apart may depend on incompatible runtimes. This makes shared inference environments risky or even impossible...

In this talk, I'll walk you through a real production system built under these constraints. We will first go through different architectural options and how we evaluated strategies such as enforcing strict backward compatibility, retraining only on breaking changes, or building large monolithic inference images that support every historical model version. For each option, I'll discuss not only technical feasibility, but also operational cost and impact on developer experience.

Finally, I'll explain the solution we ultimately chose for our scalability and latency requirements: a single inference service that dynamically loads models at request time, paired with an overnight post-release retraining job that proactively refreshes models for our most active users. I will then go through the open source tech stack: MLflow for model persistence, MLServer as the serving engine, the Open Inference Protocol as standardized interface, and KServe for Kubernetes-native scaling. The same setup supports both local development and production deployments, enabling fast iteration without compromising reliability.

This talk is aimed at ML engineers, platform engineers, and applied data scientists who are building or operating Python-based ML systems in production and want practical insights on handling evolving runtimes, multi-model serving, and real-world constraints.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/DAUQVR/>

## 32. [When should an AI Agent say "I Don't Know"? Confidence, routing, and multi-turn evaluation in a LLM system](https://pretalx.com/pydata-amsterdam2026/talk/ZXZCFJ/)

**Speakers**: Tara Farzami

**When and where**: Friday 2026-09-11, 10:05–10:50, room Entropy

**Type**: Long talk (45 minutes)

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Target Audience:  
It's aimed at people who now have to ship agents rather than prototype them, and it covers the part they struggle with most— evaluation and reliability. The same TomTom APIs are public through TomTom's MCP server and Agent Toolkit, so anyone can try this afterwards.

Required Background
Familiarity with LLMs, basic agent workflows, and production ML or software systems will be helpful.

Audience Takeaways
People leave with patterns they can reuse: return options instead of guessing when a request is ambiguous, get facts from tools rather than the model, pick a different model per task to control latency and cost, and build layered evaluations that show whether a change actually helped. All of it works in plain Python.

Outline:

- Intro — why plausible answers are not enough — 4min
- TAIA architecture — tool-using Python/FastAPI backend, TomTom APIs, session state, and client handoff — 8min
- Grounding and ambiguity — when the agent should act, ask, or say it does not know — 7min
- Model routing and latency — separate models, instant acknowledgements, cost, and UX delay-masking — 5min
- Evaluation — pytest-bdd/Gherkin scenarios, deterministic checks, LLM judges, and telemetry — 7min
- Takeaways and Q&A — what generalizes beyond cars, TomTom MCP/Agent Toolkit, and audience questions — 7min

Source: <https://pretalx.com/pydata-amsterdam2026/talk/ZXZCFJ/>

## 33. [DuckDB + ADBC: Faster, Easier Data Analytics](https://pretalx.com/pydata-amsterdam2026/talk/TRBXRH/)

**Speakers**: Matt Topol

**When and where**: Friday 2026-09-11, 11:05–11:35, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

DuckDB and ADBC have rapidly become popular tools for data analytics in Python. DuckDB, an embeddable columnar database (think: SQLite, but for analytics), is easy to install, highly capable, and yet often faster than heavyweight cloud systems and analytics platforms like Apache Spark. ADBC (”Arrow Database Connectivity”), meanwhile, provides a universal data access API and per-vendor driver implementations. While the idea is similar to JDBC and ODBC, those standards suffer from several problems: performance is lacking due to being row-based, JDBC requires a JVM, and driver installation and configuration is difficult.

When combined, these projects complement each other and make data analytics in Python even faster and easier. DuckDB can be natively used as an ADBC driver, while the new `adbc` extension we have developed lets it also act as an ADBC client and fetch/ingest data through any of a dozen drivers.

We aim to show how all of these tools work together and make it easy to connect Python and DuckDB to vendors ranging from BigQuery to SQL Server. We’ll introduce Apache Arrow and ADBC and explain how we maximize performance because Arrow’s columnar format is natively supported by DuckDB. We’ll then demonstrate DuckDB’s ADBC interface, the `adbc` extension, how to use `dbc`(an easy way to install ADBC drivers, modeled after tools like `uv`), and new ADBC features like connection profiles (for configuring connection parameters more easily).

Outline:

- Intro & Demo (5 minutes)
- Easy Driver Setup with `dbc` and ADBC Connection Profiles (10 minutes)
- How Apache Arrow, ADBC, and DuckDB Work Together (5 minutes)
- Future Work (5 minutes)
- Q&A (5 minutes)

Source: <https://pretalx.com/pydata-amsterdam2026/talk/TRBXRH/>

## 34. [Modernizing Spark: Performance Boost without Rewrite](https://pretalx.com/pydata-amsterdam2026/talk/YMKPBU/)

**Speakers**: Santosh Pingale, Shehab Amin

**When and where**: Friday 2026-09-11, 11:05–11:35, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

A typical data platform often assumes a reliance on scalable computing solutions, ensuring that the same data processing jobs can remain efficient and cost-effective while the amount of data grows. However, in reality, this assumption does not always hold true when meeting the evolving demands of the business.

Data engineering practitioners face a critical dilemma: hardware costs grow proportionally as the business scales, while switching to a more performant solution implies prohibitive engineering costs due to the need to rewrite entire workloads.

This pattern was observed a decade ago when teams moved from MapReduce systems to then-innovative solutions such as Apache Spark. The same theme occurs today, as Spark is challenged by successor compute systems designed specifically for modern cloud environments.
This talk discusses the modernization of Apache Spark workloads. The goal is to achieve orders-of-magnitude improvements in compute time and hardware cost without requiring code changes. The solutions largely fall into two categories:

1. Spark accelerators. These solutions replace physical operators with highly optimized ones written in other programming languages. The optimized operators are injected using the Spark plugin mechanism.
2. Alternative server implementations of the Spark Connect protocol. These solutions allow Spark clients to connect to them via gRPC for the same DataFrame operations. Such solutions present an opportunity to eliminate the deficiencies of JVM-based data systems entirely.

The talk will discuss the pros and cons of both categories of solutions and present an empirical study of their performance. It will also explain the common technologies that make these performance improvements possible: the Apache Arrow in-memory format and the Rust programming language.

As a concluding case study, this talk will discuss how custom Python logic (UDFs and data sources) is supported in Spark, and how modernization efforts can be driven by Rust and PyO3. Python code is historically known to be slow in Spark due to the friction between the Python runtime and the JVM. However, this modernization effort can make Python workloads highly performant in Spark. This opens up a wide range of possibilities in agentic workflows, where standard data processing is often blended with custom business logic and integrations.

This talk is intended for data scientists, data engineers, and ML engineers interested in scalable ETL pipelines and OLAP workloads. The audience will not only be equipped with a handbook for the production-ready modernization of Spark workloads, but will also gain an in-depth understanding of the current trends in modern data system innovations.

For the audience, prior experience with Apache Spark is nice to have but not required. Knowledge with data system internals is not needed as this talk serves for educational purposes on such topics.

Here is an outline of the talk:

- Problem description (2 minutes)
- Overview of Spark workload modernization solutions (5 minutes)
- Techniques behind the scenes (8 minutes)
  - Arrow in-memory format
  - Query planning and execution in Rust
- Performance comparison and discussions (5 minutes)
- Case study: Performant Python in Spark (5 minutes)
- Q & A (5 minutes)

Source: <https://pretalx.com/pydata-amsterdam2026/talk/YMKPBU/>

## 35. [The A/B Testing Blind Spot: Solving the Opt-In Paradox with Randomized Encouragement and DoubleML](https://pretalx.com/pydata-amsterdam2026/talk/Q7CB9J/)

**Speakers**: Kexin Fei, Lin Jia

**When and where**: Friday 2026-09-11, 11:05–11:35, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Target Audience**

- **Roles:** Data Scientists, Machine Learning Scientists, Applied Scientists, Economists.
- **Experience Level:** Intermediate.

**Required Background Knowledge**
Familiarity with standard A/B testing, introductory linear regression, and basic causal inference concepts (e.g., confounders, selection bias). Basic knowledge of Python’s scientific stack (e.g., `scikit-learn`).

**Talk Type and Approach**
Simulation-driven and Practical. The session will blend a live-coded Python simulation with mathematical intuition (DAGs) and a real-world product case study.

**Audience Takeaways**

- **Conceptual:** Visually understand why standard observational methods (like Propensity Score Matching or naive Doubly Robust ML) structurally fail for opt-in features due to collider bias.
- **Strategic:** Learn how to disentangle a product's intrinsic value from its marketing reach, preventing the business from abandoning highly effective features simply due to poor adoption UX.
- **Practical:** Gain a Python blueprint for implementing Randomized Encouragement Design (RED) and the Interactive Instrumental Variable Model (`DoubleMLIIVM`) to handle heavy-tailed, highly skewed platform data.

**Topic and Relevance**
Across online marketplaces, measuring the impact of voluntary features—whether it is a customer opting into a loyalty program, an e-commerce seller adopting a pricing tool, or a vacation host enabling "instant booking"—is notoriously difficult. These opt-in mechanics introduce a severe **"Trilemma"** for Data Science: **Voluntary Adoption** (the opt-in barrier), **Extreme User Heterogeneity**, and **Finite Sample Sizes** within eligible cohorts. This Trilemma creates a paradox: standard A/B tests severely dilute the Intention-to-Treat (ITT) effect across non-adopters, while observational methods introduce fatal selection bias. This talk provides a rigorous framework to solve this trilemma, allowing organizations to disentangle true product quality from adoption bottlenecks.

**Technical Depth & Educational Value**
This talk moves beyond theory by using code-driven simulations to visualize causal failures, providing a robust structural solution for each part of the Trilemma:

- **Solving Voluntary Adoption (Simulation & RED):** We will use a simulation to demonstrate why conditioning on adoption—via Propensity Score Matching or naive ML—fails. By forcing a comparison between treated adopters and control matches, we inadvertently compare a mixed-motivation group against a "super-motivation" group, resulting in **Collider Bias**. To escape this, we introduce **Randomized Encouragement Design (RED)** as a valid Instrumental Variable (IV) to bypass the collider and target the Local Average Treatment Effect (LATE).
- **Solving Heterogeneity (The DoubleML Engine):** While RED provides the causal framework, standard Two-Stage Least Squares (`2SLS`) assumes linear, additive effects. We will explain why this "Linearity Trap" fails for highly skewed platform data (where the impact on a highly engaged "whale" user is exponentially different than on a casual user). We introduce **Double Machine Learning** (`DoubleML`) to handle this extreme non-linear heterogeneity.
- **Solving Finite Samples:** Because we often cannot simply "run the test longer" for time-bound campaigns or limited user cohorts, we must maximize statistical power. We will showcase how to parameterize the `DoubleMLIIVM` model using `Tweedie` Regressors. This specifically models the zero-inflated and right-skewed nature of platform metrics (like spend or total bookings), drastically reducing residual variance to achieve precise causal estimates.

**Anticipated Reviewer Questions**
_Why not just use rank-based tests (e.g., Mann-Whitney U) to handle the extreme variance and outliers of this data?_ We will explicitly address this in the talk as the **"Metric Alignment Problem."** While robust to outliers, rank tests evaluate whether the median shifts. In a business context, total volume (the sum of revenue or bookings) is the primary success metric. A rank-based test could show a statistically significant shift by helping thousands of low-activity users, while actual total volume remains flat due to the variance of "whale" users. Furthermore, RED + `DoubleML` allows us to estimate the causal lift in actual business units, which is strictly required for ROI analysis.

**Scope and Structure (30 Minutes Total)**

- **Minutes 0-5: The Business Context & The Trilemma.** Introduce the opt-in paradox across platform ecosystems. Define the "Trilemma" preventing us from measuring true ROI: Voluntary Adoption, Extreme Heterogeneity, and Finite Sample Sizes.
- **Minutes 5-15: The Measurement Trap & RED Framework.** Using a Python simulation, we visualize the failure of standard A/B tests (dilution) and observational models (Collider Bias). We solve this conceptual hurdle by introducing Randomized Encouragement Design (RED) to create a valid instrument.
- **Minutes 15-20: The Variance Problem & DoubleML.** We explain why standard IV estimation (`2SLS`) isn't enough for highly skewed user data. We walk through the `DoubleML` Python implementation (`DoubleMLIIVM`), highlighting the use of `Tweedie` Regressors to handle zero-inflated data and recover the precise LATE.
- **Minutes 20-25: Empirical Case Study.** We apply the full RED + `DoubleML` framework to a real-world product decision, demonstrating step-by-step how it recovered the signal from the noise and saved a high-potential feature from being abandoned due to poor UX discovery.
- **Minutes 25-30: Summary, Learnings & Q&A.** A quick recap of the architectural blueprint (the "how-to" for attendees). Open the floor for Q&A.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/Q7CB9J/>

## 36. [The New Polars Engine That Tackles Megabyte to Terabyte Workloads](https://pretalx.com/pydata-amsterdam2026/talk/MKAK8X/)

**Speakers**: Thijs Nieuwdorp

**When and where**: Friday 2026-09-11, 11:05–11:35, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Audience and prerequisites: Attendees should be comfortable with a DataFrame API. Prior Polars experience is helpful but not required. No distributed-systems background assumed. Concepts like "shuffles" and "partitioning" are introduced as they come up.

Structure: A presentation with slides that follow one query through different dataset sizes:

- 10 GB on a single-node: morsel-driven, streaming execution; how we optimize performance on the single node.
- 100 GB, single-node: how a single node can process more data than expected.
- 1 TB, vertical scaling vs horizontal scaling: how out-of-core computation stretches a single node to its maximum and when the jump to distributed execution is worth the overhead.
- 10TB distributed: three technical challenges a distributed DataFrame engine has to solve: Plan partitioning at stage boundaries, data shuffling between nodes (and how to minimize it), and worker coordination.
  The talk pairs engine internals with visualisations that support decision making based on scenarios.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/MKAK8X/>

## 37. [Agent-Friendly Data Platforms: Semantic Layers, Tool APIs, and Guardrails for Agentic](https://pretalx.com/pydata-amsterdam2026/talk/ZASNRB/)

**Speakers**: Borja Enrique Vilar Martos

**When and where**: Friday 2026-09-11, 11:50–12:20, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

While the AI ecosystem has hyper-focused on model capabilities, the data infrastructure required to support autonomous agents in production is often an afterthought. This talk provides a practical, vendor-neutral blueprint for data engineers supporting internal AI agents.

The technical depth focuses on the shift from SQL-centric, batch-oriented warehouses to API-driven, semantically rich data layers designed for tool-using agents. We’ll address core engineering challenges in agentic use cases:

Semantic translation: agents struggle with raw, normalized schemas. We’ll cover how semantic layers (metrics/dimensions/contracts) give agents deterministic business definitions instead of “best guess” SQL.
Tooling & APIs: moving from direct SQL access to scoped tools (REST/GraphQL, stored procedures, or function-calling endpoints) that agents can use reliably without hallucinating table names or join paths.
State & memory: combining OLAP (analytics) with vector search (context retrieval) and lightweight OLTP/state stores (work tracking, approvals) so agents have both short-term context and durable memory.
Governance (the blast radius): enforcing RBAC for agent service accounts, query/endpoint allowlists, rate limits and budgets, and audit logs that let you answer “what happened, who/what asked, and why?”

This talk avoids AI hype by focusing strictly on the backend engineering and infrastructure required to make agents reliable, safe, and performant.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/ZASNRB/>

## 38. [Computer Use Beyond the Demo: Bringing Legacy Systems into the Agentic Era](https://pretalx.com/pydata-amsterdam2026/talk/EANR9W/)

**Speakers**: Sako Arts

**When and where**: Friday 2026-09-11, 11:50–12:20, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

### Scope and Structure (estimated 30 minutes total):

Wonderful as an Open Agentic Platform (3 minutes)

- Headless and multicloud architecture.
- Support for multiple model providers and modalities.
- Connecting agents to enterprise tools, data, and operating environments. The Legacy-System Problem (3 minutes)
- High-value workflows that exist only behind a user interface.
- Why traditional integrations are often unavailable or too expensive.
  -Computer Use as the last-mile integration layer.

The Production Architecture (6 minutes)

- Connecting agents to real desktop environments.
- Supporting Windows, remote desktops, VPNs, and customer-managed infrastructure. ● Separating agent execution from the desktop being controlled.
- Designing for restricted enterprise networks.
  Capturing the Human Process (4 minutes)
- Recording experienced human workers.
- Using Gemini to divide recordings into phases and draft an initial SOP. ● Human annotation of actions, preconditions, reasons, and expected outcomes. ● Iteratively expanding the SOP when new branches or failures are discovered.

The Siebel Case Study (5 minutes)

- A complex, approximately one-hour back-office workflow.
- Operating a legacy Windows system without a modern API.
- Initial problems with latency, brittleness, and undocumented exceptions. ● Moving from a proof of access toward a reliable production workflow.

Reliability, Auditability, and Human Control (3 minutes)

- Live viewing and session recording.
- Approvals before irreversible actions.
- Human escalation and operational handoff.
- Recovery from unexpected screens and backend failures.
- Using execution data to improve the process over time.

Conclusion (1 minute)

- Legacy systems do not need to be rebuilt before they can participate in agentic workflows.
- Computer Use can make them accessible, but production success depends on architecture, process knowledge, observability, and control.
- The real opportunity is turning undocumented human operations into reliable and auditable software.

Topic and Relevance
Relevant for teams automating high-frequency processes in legacy systems where APIs are unavailable and operational control, auditability, and recovery are critical.

Audience Takeaways
How to make legacy systems available to AI agents—and how process documentation, hybrid interaction patterns, observability, and human escalation separate a Computer Use demonstration from production automation.

Talk Type and Approach
A technical architecture and production-engineering talk grounded in a real deployment, including its limitations, failures, and lessons learned.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/EANR9W/>

## 39. [Trillion-Token Pretraining: Building a Foundational Model for payment data](https://pretalx.com/pydata-amsterdam2026/talk/EUY789/)

**Speakers**: Martin Iglesias Goyanes, Raúl Soutelo Quintela

**When and where**: Friday 2026-09-11, 11:50–12:20, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Building a foundation model for payments data requires rethinking assumptions borrowed from NLP and vision. This talk walks through why traditional ML hits a ceiling on tabular financial data, the architectural decisions, choosing between a hierarchical payment encoder and a language-model framing, and the engineering required to pretrain at the scale of trillions of tokens.

**We cover:**

- Why payments need a foundation model
- Architecture trade-offs: hierarchical encoder vs. treating features as tokens, payments as sentences, sequences as documents; concrete pros and cons of each (information bottleneck, context window blowup)
- Tokenization: representing mixed numeric, categorical, and high-cardinality ID features as a single vocabulary; handling missing fields and temporal structure
- How to handle sequences ranging from 1k to 100M payments per entity and extract meaningful signal
- Pretraining objectives: masked feature modeling, next-event prediction, and contrastive tasks
- Comparing standard attention, Flash Attention, windowed attention, and Mamba SSMs across memory, compute, and wall-clock time
- Inference constraints (P50 30ms SLA, 3000 tx/s peaks, 99.9999% uptime)
- Results and impact on various ML models (fraud detection, entity resolution, and more)

Attendees will leave knowing how to apply state-of-the-art techniques for adapting self-supervised pretraining to non-text sequential data: how to tokenize heterogeneous tabular features, which pretraining objectives work, architectural trade-offs, and how to serve a large model under strict latency constraints.

**Timing (25 min + 5 min Q&A):**

- Problem framing and motivation - 5 min
- Data: sequences and tokenization - 5 min
- Architecture and pretraining objectives - 5 min
- Engineering challenges - 5 min
- Results and lessons learned - 5 min
- Q&A - 5 min

**Target audience:** Intermediate-level; familiarity with Transformers and self-supervised learning is assumed.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/EUY789/>

## 40. [Open Weights, Cloud Scale: Architecture Patterns for Faster and Cheaper Production Agents](https://pretalx.com/pydata-amsterdam2026/talk/V8XH8S/)

**Speakers**: Nicolai van der Smagt

**When and where**: Friday 2026-09-11, 13:25–13:55, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk is for Python developers moving agents from prototype to production. It explains four architecture patterns for reducing inference cost and task completion time for agents using managed, open-weight models, drawing on real long-context, tool-using workloads.

1. Model qualification: Build a representative evaluation set, define task-specific quality and latency requirements, and select the serving configuration with the lowest measured cost per successfully completed task. Model size, throughput, generation length, retries, and failure rate are treated as parts of the same decision.
2. Context design: Separate stable and volatile context, serialize prompts and tool definitions, and structure conversation history to maximize safe prefix-cache reuse. Observed cached tokens are measured, not inferred.
3. Runtime routing: Route only across models that have passed the quality gate. Use task type, complexity, risk, conversation phase, and generation budget to select the fastest and most economical qualified model, with explicit fallback and escalation policies.
4. Targeted adaptation: Fine-tune or distill a smaller model when the workload is repeated, measurable, and stable. Compare the fixed cost of data preparation, training, evaluation, and deployment with the recurring savings from lower latency, lower inference cost, shorter prompts, or fewer retries.

The four patterns are connected through a Python reference architecture using OpenAI-compatible endpoints, deterministic prompt construction, task evaluation, routing policies, fallbacks, and request-level telemetry. A common scorecard tracks task success, structured-output validity, latency, cached tokens, retries, and inference cost.

Attendees will learn how to choose between closed APIs, local models, and managed open inference; how to apply the four patterns in a practical order; and how to measure whether an optimization improves the cost and response time of successful task completion without reducing quality. The session is scoped to 25 minutes and uses architecture diagrams, short code examples, and a single running case rather than a live demo.

Outline (25 minutes + 5 minutes Q&A)

1. Why open weights and managed cloud inference (4 minutes): Compare closed APIs, local models, self-managed serving, and managed open inference.
2. Pattern 1, model qualification (4 minutes): Define quality gates and identify the optimal balance of quality, cost and latency.
3. Pattern 2, context design and prefix reuse (4 minutes): Implement stable prefixes, deterministic serialization, prefix caching, and request-level cache measurement.
4. Pattern 3, runtime routing (4 minutes): Select the fastest and most economical qualified model for each task, with fallback and escalation policies.
5. Pattern 4, targeted adaptation (4 minutes): Evaluate when adaptation changes the inference economics enough to justify its fixed costs.
6. Python reference architecture (3 minutes): Connect prompt construction, evaluation, routing, endpoints, fallbacks, and telemetry.
7. Decision framework and takeaways (1 minute): Apply the patterns in order and select the appropriate deployment model.
8. Token Factory and invitation (1 minute): Explore Nebius Token Factory as a managed implementation of the architecture and explain how attendees can try it.
9. Q&A (5 minutes).

Source: <https://pretalx.com/pydata-amsterdam2026/talk/V8XH8S/>

## 41. [Systems for Scale: Architecting a Nationwide Energy Forecasting Platform](https://pretalx.com/pydata-amsterdam2026/talk/CBE9UC/)

**Speakers**: Corné Vriends, Daria Mustafina, Mohit Kumar

**When and where**: Friday 2026-09-11, 13:25–13:55, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This is a systems architecture talk, not a forecasting tutorial or a general MLOps overview. We will not cover modeling techniques, domain-specific feature engineering, or monitoring dashboards in depth — the focus is on the architectural decisions that make portfolio-scale forecasting operationally viable.
Introduction & Problem Framing (4 minutes)

- The scale: ~100 thousand models, 20 million forecasts per week, 30 TB of time-series data, weekly retraining SLA.
- Why this is a systems problem, not a modeling problem: the bottleneck is orchestration, registry, and evaluation — not algorithm choice.
- Where standard stacks break: MLflow metadata limits, per-model CI/CD, individual-model evaluation.
- Talk roadmap: three patterns, one architecture diagram, no live demo.

Architectural Overview (3 minutes)

- A single diagram of the end-to-end platform.
- Brief mention of supporting infrastructure (data lake, feature store, inference, monitoring) — flagged as out of scope for depth, available in Q&A.

Pattern 1: Heterogeneous Parallel Training (7 minutes)

- The global-vs-local question at portfolio scale: when does one Spark ML model beat thousands of local models, and vice versa?
- Our decision framework — four axes that determine the global-vs-local split:
  - Data volume per entity — sparse history → global; deep per-series history → local.
  - Signal heterogeneity — homogeneous behavior across entities → global; strongly divergent patterns (EV charging, heat pumps, prosumers) → local.
  - Cold-start behavior — new or weakly observed entities must forecast from day one → global; warm historical context available → local.
  - Operational cost — training/registry/serving budget is tight → global; added complexity justified by better local decisions → local.
- Unified workflow architecture: Spark ML for global models and applyInPandas for local models, orchestrated in a single PySpark job.
- What generalizes: the routing logic, the partitioning strategy, the failure-isolation pattern.

Pattern 2: A Registry That Scales Beyond MLflow (6 minutes)

- Where managed MLflow broke for us at scale:
  - Retrieval latency — API calls to fetch models degrade to tens of seconds to several minutes once the registry holds 50k+ model versions, making batch inference pipelines unacceptably slow.
  - Artifact storage creep — even at ~1 KB per serialized model, 100k models registered weekly compounds to ~5 TB/year of artifacts with no built-in lifecycle control; storage costs scale superlinearly due to metadata overhead.
  - Platform limits — Databricks workspace resource limits become a hard constraint at this scale.
- What we kept from the MLflow mental model (experiment tracking, versioning concepts) and what we replaced (artifact storage, metadata queries, model retrieval).
- Our registry schema: versioning, parameter tracking, artifact storage, and lineage at portfolio scale.
- What generalizes: the schema design, the read/write access patterns, the integration points with training and inference.

Pattern 3: Portfolio-Level Promotion Gates (7 minutes)

- Why per-model metrics can be misleading: a challenger model may outperform at the portfolio level while still underperforming on individual local level.
- Distributed backtesting with strict temporal integrity: parallel folds across thousands of entities, no leakage.
- Champion/challenger design: experimental pipelines running in parallel with production on identical folds.
- Promotion criteria: portfolio-aggregated metrics + operational robustness + an explainable driver for the improvement — not just better numbers.
- What generalizes: the aggregation logic, the promotion checklist, the parallel-pipeline architecture.

Takeaways & Q&A (3 minutes)

- The three patterns, restated as a checklist.
- The shift from a model-centric to a system-centric view of ML.
- Pointers to topics deferred to Q&A: monitoring, resilience, retraining strategy, feature store.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/CBE9UC/>

## 42. [When RAG is not enough: Architecting for 10M+ context windows](https://pretalx.com/pydata-amsterdam2026/talk/DQXPVN/)

**Speakers**: Azamat Omuraliev

**When and where**: Friday 2026-09-11, 13:25–13:55, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Topic and Relevance:**
While the industry relies on RAG for targeted retrieval, RAG falls apart on tasks requiring dense, cross-document reasoning (e.g., repository-wide codebase migrations, comprehensive financial audits). Furthermore, while 1M-token windows exist, a 10M-token workload is fundamentally out of reach for a single inference call. This talk addresses a critical engineering bottleneck: how do we build agents capable of acting on 10M+ tokens of necessary context using today’s constrained models?

**Target Audience & Required Background:**

- Roles: AI Engineers, System Architects, Backend Developers.
- Experience Level: Intermediate to Advanced.
- Required Background: Familiarity with LLM limitations, standard RAG pipelines, and general system design.

**Takeaways:**

- Concrete strategies for handling 10M+ tokens, including hierarchical summarization, MapReduce-style LLM workflows, and multi-agent routing.
- A framework for deciding when to use standard RAG, when to max out a long-context window, and when to deploy complex chunking and aggregation strategies.

**Structure:**

- Introduction (5 min): The 10M token wall. Why standard RAG fails at holistic reasoning, and why we can't just rely on larger context windows.
- Evaluating the Limits (10 min): Benchmarking degradation. Analyzing recall drop-off, "lost in the middle" phenomena, and latency spikes as context scales up to 1M+ tokens.
- Strategies for 10M+ Tokens (10 min): Architectural tactics to process impossible volumes. Covering hierarchical processing, iterative graph-based retrieval, and agentic data synthesis.
- Lessons Learned and Q&A (5 min): Best practices, cost considerations, and audience questions.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/DQXPVN/>

## 43. [When Should AI Speak? Letting Agents Decide When It's Their Turn](https://pretalx.com/pydata-amsterdam2026/talk/KHXZLR/)

**Speakers**: Anna Pillar, Emir Can

**When and where**: Friday 2026-09-11, 13:25–13:55, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This idea started with a practical question: if coding agents still struggle to directly translate business requirements into working software, why not build an agentic Scrum team? The first fundamental question arose: but who speaks next? To answer this, we decided to implement and evaluate different turn-taking strategies to see which results in the most productive conversations and best overall results.

Our agentic Scrum team was tasked to refine a shared-expenses application, with various role-based agents representing classic roles from a Scrum team (Product Owner, Tech Lead, QA, Architect, etc.). They must collaboratively turn a business request into a backlog of implementable user stories under explicit rules about how turns are allocated.

After a light introduction to conversation analysis theory and game-style bidding, we present four turn-taking strategies:

1. Fixed-order speaking,
2. Importance-based self-selection where agents run a think step and emit urgency scores,
3. An obligation-first strategy that detects direct questions and prioritizes the addressed agent with an auction-style fallback if no questions were asked by the previous agent,
4. A role-based facilitator that manages an agenda and enforces constraints on speaking dominance.

We will walk through the implementation of each strategy, explaining the architecture and design decisions behind them.

Finally, we present our evaluation strategy and compare backlog quality, and conversation-level metrics. Think about participation balance, fraction of questions answered within a few turns, redundancy, topic drift, and urgency realism, all scored using LLM-as-a-judge. The implementation is lightweight, using a Python runner and notebooks, and a public repository will be shared via GitHub.

**Outline (30 minutes)**

- 0-5 min: Motivation and problem outline; limitations of naive turn-taking
- 5-10 min: Scenario and background; agent roles, Scrum refinement, and conversation analysis theory
- 10-20 min: Architecture and implemented turn-taking strategies
- 20-27 min: Evaluation strategy, metrics, and results
- 27-30 min: Learnings from building multi-agent systems, limitations
- 30-35 min: Open questions

Source: <https://pretalx.com/pydata-amsterdam2026/talk/KHXZLR/>

## 44. [Deterministic Orchestration for ML Experiments with Coding Agents](https://pretalx.com/pydata-amsterdam2026/talk/KRSRVM/)

**Speakers**: Iryna Kondrashchenko, Oleh Kostromin

**When and where**: Friday 2026-09-11, 14:10–14:40, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Coding agents have improved over the past year to the point where they can iterate on a codebase with minimal supervision. ML projects look like a natural fit: the iteration loop is well defined and the code surface is small compared to a full application. ML is not a single-trajectory task, though. Picking the right configuration involves exploration: random sampling over hyperparameters, architectural variants, data subsets. Domain knowledge alone rarely settles the question, and the exploration is repetitive, which is why people want to automate it. A recent example of this direction is Karpathy's [`autoresearch`](https://github.com/karpathy/autoresearch), which showed that a coding agent given an `.md` prompt can spin up its own worktrees and track experiments in a CSV. However, the trajectory it explored was single and shallow, and most of the modifications it tried could have been handled by a grid search. Real autonomous experimentation needs more structure than that.

The natural next step is to add a second LLM agent on top to coordinate the others, but in practice this does not hold up. The orchestrating agent drifts in the same way the workers do, just on a longer horizon: after a few dozen experiments it forgets which directions were already tried, mixes unrelated changes into a single step, or commits to a branch that the metrics do not justify. The coordination problem cannot be solved by adding more prompting.

The approach we'll present takes the opposite direction. Coordination is handled by deterministic, non-LLM code, and the LLM is used only where open-ended generation is actually needed. The orchestrator runs experimentation as a tree search in which each node represents a hypothesis-constrained modification to a reproducible baseline, and modifications are restricted to a single aspect per step so that the resulting metric change can be attributed.

From there, we walk through what this looks like in practice. We start with how the LLM work inside the tree is split by role: a proposing node generates candidate modifications, an implementing node turns a chosen proposal into code, and a debugging node is invoked when an experiment fails to run. Each role operates with a fresh context and a narrow scope rather than a single agent carrying the full history. We then cover the supporting infrastructure that makes the tree practical in real projects: git worktrees for branch isolation and parallel execution, and an anti-repetition memory that prevents the same hypothesis from coming back under different wording.

Additionally, we cover two components that are extremely useful for these kind of systems. The first is the path for prior results to flow back into fresh agent contexts. For this we use a real experiment tracking backend exposed through a token-efficient query interface, which doubles as the surface where a human can step in to inspect the results. The second is the choice not to reimplement the coding CLI itself: `Claude Code`, `Codex`, and similar tools are dispatched as replaceable backends, and can be easily swapped or even combined with almost no code changes.

We close with lessons from running this on real experimentation work, including where the deterministic structure helped, where it got in the way, and where a well-specified hyperparameter sweep is still the better tool.

**Outline:**

- Why ML experimentation breaks coding agents (5 min)
  - Differences between Software Development and ML
  - `autoresearch` and its limits
- What goes wrong when an LLM orchestrates other LLMs (4 min)
- The deterministic orchestrator (8 min)
  - Tree search over hypothesis-constrained modifications
  - Role-separated nodes: proposing, implementing, debugging
  - Importance of fresh context and narrow scope per node
- Supporting infrastructure (5 min)
  - Git worktrees for branch isolation and parallel execution
  - Anti-repetition memory
  - Tocken-efficient agent interface for experiment tracking tools
- Adoption and trade-offs (3 min)
  - Human-in-the-loop
  - Harness-agnostic integration with `Claude Code`, `Codex`, and similar
  - Lessons from real work, and when a regular Optuna search is still better
- Q&A (5 min)

**Target audience:**

The talk is aimed at ML engineers, applied researchers, and data scientists who have tried using coding agents to drive experimentation, or are considering it, and at platform engineers who are asked to support such workflows. Familiarity with a standard training and evaluation loop is assumed. No prior experience with multi-agent systems is required.

**Learning outcomes:**

By the end of the talk, attendees will have a clear picture of how to build a system for autonomous ML experimentation on top of widely used coding harnesses like `Claude Code`, `Codex` (or any other), as well as an understanding of the limitations of such a system.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/KRSRVM/>

## 45. [No GIL, Real Gains: Porting a C++ Python Extension to Free-Threaded Python 3.14](https://pretalx.com/pydata-amsterdam2026/talk/EKZMWT/)

**Speakers**: Auxten Wang

**When and where**: Friday 2026-09-11, 14:10–14:40, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Python 3.14’s free-threaded build makes it possible for threads to run Python code in parallel — but C and C++ extension modules do not benefit automatically. To see real speedups, extension authors need to opt in explicitly, remove hidden GIL assumptions, and audit shared state carefully.

In this talk, I’ll walk through a real migration of a Python extension that embeds a multi-threaded C++ analytical engine. The engine already had parallel execution internally, but several interactions with Python still serialized execution: calling Python UDFs, accessing DataFrame-backed columns, and handling large numbers of strings.

I’ll show three concrete changes that made free-threading pay off in practice: moving Python UDF execution in-process, declaring the extension module GIL-independent and making its global state thread-safe, and selectively replacing high-level Unicode APIs with lower-level CPython string access on hot paths. Along the way, I’ll discuss what broke, what did not scale as expected, and where the stable ABI stopped being compatible with our performance goals.

You’ll leave with a practical checklist for porting extension modules to free-threaded Python 3.14, a clearer picture of when no-GIL actually helps, and benchmark results from real analytical workloads on a 16-core machine. No ClickHouse knowledge is required — the talk is aimed at Python developers who maintain native extensions, build data tooling, or care about making Python scale across cores.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/EKZMWT/>

## 46. [Rebuilding Picnic’s Recipe Recommender](https://pretalx.com/pydata-amsterdam2026/talk/VUJB7A/)

**Speakers**: Majid Hajiheidari, Thijs Sluijter

**When and where**: Friday 2026-09-11, 14:10–14:40, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Picnic is a fast-growing online supermarket operating at large scale across Europe, where machine learning is deeply embedded in the customer experience and operational systems. Recipe recommendations are a particularly relevant problem for us: they help customers discover what to cook, connect inspiration directly to their weekly grocery shop, and create a natural setting for personalisation at scale.

A seemingly simple update of the product UI fundamentally changed the underlying recommendation problem. Instead of retrieving a small set of relevant recipes from a large catalogue, we now needed to rank a constrained set of candidates. That forced us to rethink not only the model, but the experimentation stack around it.

In this talk, we will discuss three main topics:

- How a change in our application UI reframed our recommendation problem from a retrieval problem to a ranking problem, and how that informed our modelling choices.
- How we applied Sutton’s Bitter Lesson and Representation Learning to create a scalable feature and modelling pipeline with large expressive power across all customer cohorts, including those new to buying recipes.
- How we used Polars and Autoresearch to speed up our offline experimentation iterations and automate hyperparameter tuning.

This talk is aimed at ML engineers, Data Scientists, RecSys and IR practitioners, and Product Owners and Managers working within any of these domains. It combines technical details with real-world modelling choices, leading to tangible business impact.

Attendees will learn how to recognise when a product change has altered the underlying ML problem, how model expressiveness and data-pipeline design interact, and how to automate experimentation without giving up scientific rigour.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/VUJB7A/>

## 47. [When one score is not enough: matching real-world groundwater time series at scale](https://pretalx.com/pydata-amsterdam2026/talk/YVEPAV/)

**Speakers**: Luisa Orozco

**When and where**: Friday 2026-09-11, 14:10–14:40, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

We present a practical framework for harmonising partially overlapping groundwater level time-series from two different sources. The case study comes from Dutch groundwater databases, where records that describe the same physical process may differ in metadata, temporal coverage, quality-control history, and observation artifacts. The stakeholder constraint is central: these harmonised records are used as input to hydrogeological models, so false matches are more harmful than missing matches. This makes the task a certainty-first matching problem rather than one of simply retrieving the closest candidate.

The talk compares three complementary matching scores:

- metadata fingerprinting: used to encode structured record similarity and constrain candidate selection;
- Dynamic Time Warping (DTW): used for shape-based comparison of time-series under imperfect alignment;
- Point-wise value comparison: used as a simpler and more controllable baseline in cases where direct time-series comparison remains meaningful.

We show that no method dominates across the full range of real-world artifacts present in the data. In particular, we will inspect records showing recurring archetypes such as vertical shifts, gap creation/filling during quality control, and censored values to explain why each method succeeds in some cases and fails in others. This is not a “best metric” talk. The main contribution is a method-aware, certainty-first workflow: instead of trusting a single score, we use failure modes observed across archetypes to reason about which scores are informative and when a match should remain unresolved.

To ground the discussion technically, we present evaluation results on curated datasets derived from verified migration records, where the true matches are known. The performance is assessed using precision retrieval metrics (including precision at 1 and precision at 3), and use selected examples to show why nearest spatial candidates, compressed representations, or shape-based similarity can each break down under realistic data pathologies. We discuss which parts of the workflow are domain-specific and which generalize to other time-series matching and data harmonisation problems.

The talk is aimed at data scientists, ML practitioners, data engineers, and researchers working with time-series matching, record linkage, or large-scale harmonisation of real-world observational data. The value for attendees is practical: how to think about matching when precision matters more than recall, how to identify archetypes that systematically break common comparison methods, and how to combine interpretable scores into a scalable workflow that can abstain when uncertainty is high.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/YVEPAV/>

## 48. [AI You Can Bet Your Business On: How Mars' Context-Lake Builds the Trust Bridge Between People and AI](https://pretalx.com/pydata-amsterdam2026/talk/CFNEQT/)

**Speakers**: van Balkom, Patrick

**When and where**: Friday 2026-09-11, 14:55–15:25, room Anomaly

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

My goal is to take you on a journey from a common, high-stakes problem of not trusting the guessing black box of AI in my day to day work to a practical PoC that proofs a solution that we are ready to scale at MARS.

Part 1: The High-Stakes Reality

The Hook: I'll start with a direct question: "We all agree AI is the future, but are you willing to bet your business on it?" This immediately frames the real-world stakes.

My Credibility: You'll learn I lead digital transformation for 500 planners at Mars and before that globally at Unilever supply chain. This isn't a lab experiment; it's about applying AI to a complex global business where mistakes have consequences.

The "Aha!" Moment: I'll introduce the "2% Problem"—showing how 98% accuracy per step is a recipe for failure in a complex ecosystem. This reveals the hidden fragility of most AI strategies and a key reason in my experience why AI is not trusted at the workspace in many companies.

Part 2: The Core Conflict
Today's AI: We'll explore the "brilliant guesser" model of AI and how current practices (RAG, bigger models, contextengineering, ... ) are just improving the guesswork, not eliminating it.

The Bottleneck: I'll distinguish between simple tasks where guesswork is fine and core processes where it's dangerous, letting you see your own company's challenges.

The Human Problem: We'll confront the conflict: AI competing with your experts, not collaborating. This creates a slow, painful adoption path where employees have no incentive to help an AI that might replace them. In this scenario AI has to work very hard to outsmart the employee by just guessing how things are done based on the data in the datalake and some unstructured documents on a sharepoint.

Part 3: A Proven Solution

The New Concept: I'll introduce the "Context-Lake"—a structured knowledge reservoir that both humans and AI can read, understand, and collaborate on. I will share the high level architecture here as well how we are combiing: agents, datalake, a graphical database and intelligent process tools like Celonis, Sygnavio and different workflow tools.

The "How-To": You'll learn the simple principle behind it: capturing the Why, Who, How, and What of any process in a mindmap (for humans) that becomes a knowledge graph (for AI).

The "Why Now": I'll explain how AI makes this practical today, turning the knowledge from meetings and interviews into a "digital twin" of your operational brain incl a high level design of our solution combining Gemini technology with a seperate graph database.

The Trust Bridge in Action: You'll see a real Mars example (carton thickness) where we captured the logic of two different experts. I'll show how making the how of our processes explicit in this "glass box" builds trust and delivers business value like speed, quality, efficient human connects,...

Part 4: Your Actionable Takeaways

Clear Lessons Learned: You'll get three concrete principles from our journey:
-Trust & Consistency is at the foundation of doing business - guesswork is not the ideal in that context
-Contextlake is the essential visual Bridge between the current reality of company employees and the AI support of the future. (the mindmap-to-graph pipeline)
-Experts are no subjects - Empower Experts as Teachers through fast low cost and intuitive feedback loops.

Conclusion & Q&A:

Source: <https://pretalx.com/pydata-amsterdam2026/talk/CFNEQT/>

## 49. [Answers you can question: building a verifiable AI analytics agent](https://pretalx.com/pydata-amsterdam2026/talk/BANDQK/)

**Speakers**: Alex Litvinov

**When and where**: Friday 2026-09-11, 14:55–15:25, room The Grid

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

**Description**
An architecture talk about an AI analytics agent that non-technical people at Manychat use daily, and the design decisions that make its answers checkable instead of merely plausible.

It covers why raw warehouse access is the wrong default for an LLM agent and what must sit between the question and the data: curated context that stays fresh and is loaded selectively for each question, an explicit way to determine how much an answer can be trusted, and a way to catch regressions when any of it changes. It’s an experience report as much as an architecture talk: what we learned while building it, what we still want to improve, and why we’ve kept it in-house so far.

**Solution limitations**

- Confidently wrong answers are cheaper to catch, not eliminated. The design lowers the cost of verification but does not guarantee correctness.
- Context freshness is enforced only where we built tooling for it, the semantic layer and the BI mirror. Everywhere else it is still manual.
- Answer validation is still human. Anything that matters gets checked by an analyst.

**Audience takeaways**

- The confidence that AI analytics is something a small team can build in-house today and start experimenting with
- What an answer has to carry to make it verifyable: the numbers, the views it used, the grain, etc, and the SQL to re-run.
- How to keep context fresh without relying on anyone remembering to update it: metadata files generated by tooling rather than written by hand, a CI check that blocks a pull request when the SQL changed and the documentation did not.
- Why less context produces better answers, and the mechanism we use: per-domain metadata that is pulled in only when the question matches it, instead of one large context loaded for every question.
- Ways to evaluate a system whose output is never identical twice and detect when changes introduce regressions.

The talk is for data engineers, analytics engineers, and analysts who are asked to put an agent in front of a warehouse. Prior knowledge: a rough understanding of how analytics work is organized.

**Outline**

- Introduction (2 min)
- Why raw warehouse access fails (3 min)
- The architecture + demo (4 min)
- Context layers: views metadata, always-on rules, per-question routing, and trust levels (7 min)
- Evaluation and observability: the golden set, analyst notifications, and traces (3 min)
- Build vs. buy (3 min)
- Learnings, limitations, and open problems (3 min)

Source: <https://pretalx.com/pydata-amsterdam2026/talk/BANDQK/>

## 50. [Evaluating Agents at Scale: From 50 Examples to a Production Flywheel](https://pretalx.com/pydata-amsterdam2026/talk/XUC7LQ/)

**Speakers**: Bauke Brenninkmeijer

**When and where**: Friday 2026-09-11, 14:55–15:25, room Fractal

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Why this talk
Building agents is easy; knowing whether they work is not. Most teams shipping LLM agents evaluate with vibes-based spot-checking or reach for academic benchmarks that don't reflect their workload. This talk gives you a different starting point: a methodology that has emerged from working on production agents over the last two years.

Agents break classical ML evaluation in several ways at once. Outputs are non-deterministic across multiple tool calls, trajectories branch, state mutates in external systems that must be checked rather than inferred, and "correctness" is judged along multiple axes simultaneously.

What does work is an iterative, human-in-the-loop process that looks a lot like how outsourced annotators used to be validated on Mechanical Turk, applied to LLM judges.

Running example
Throughout the talk we evaluate a data-analysis agent answering questions like "what's month-over-month revenue growth for EMEA in Q3?" Failure modes we grade against include wrong queries, right queries with wrong aggregations, hallucinated numbers reported without actually running anything, correct answers reached via invalid paths, and multi-turn context loss.

Outline (30 minutes, including 5 min Q&A)

1. The evaluation gap (3 min) — why agents break classical evaluation.

2. Start with humans, not infrastructure (5 min) — bootstrapping from ~50 hand-reviewed examples, binary pass/fail with written critiques, why this beats scored rubrics.

3. Align an LLM-as-a-judge (7 min) — treat the judge like a model you validate. Dev/test split applied to evaluation itself. Panel-of-judges to mitigate bias. A short live walkthrough.

4. Agent-specific evaluation (5 min) — three levels (single-step, full-turn, multi-turn) and three dimensions to grade (final response, trajectory, state changes). Handling non-determinism at scale.

5. Scaling: offline, online, continuous (4 min) — CI integration, error analysis as the dominant time spend, and a brief look at automated prompt optimization via natural-language feedback.

6. Takeaways and Q&A (6 min)

What you'll take away
A concrete process to bootstrap agent evaluation this week with ~50 examples and no ML infrastructure.
The alignment recipe for an LLM judge you can actually trust at scale.
How to evaluate trajectory and state, not just the final output.
A CI/production pattern for continuous evaluation.
Who this is for
Intermediate Python practitioners building or operating LLM agents in production. Not a "what is an agent" introductory talk.

What this talk is not
A product demo. A survey of benchmarks. An academic tour of the LLM-evaluation literature. The patterns work with any LLM SDK and any test runner.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/XUC7LQ/>

## 51. [Instro: An open-source Python library for interfacing with hardware test equipment](https://pretalx.com/pydata-amsterdam2026/talk/T7WDCJ/)

**Speakers**: Lizzy Chanpaibool

**When and where**: Friday 2026-09-11, 14:55–15:25, room Entropy

**Type**: Talk

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Instro is an open-source Python library that puts one typed API in front of power supplies, DAQs, multimeters, oscilloscopes, and more.

Write your test once, swap the driver, and your code stays put. We drive a power supply live using the built-in simulator, no hardware required, and show how to add your own.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/T7WDCJ/>

## 52. [Mothering the Machine](https://pretalx.com/pydata-amsterdam2026/talk/7PX99N/)

**Speakers**: Andy Kitchen, Laura Summers

**When and where**: Friday 2026-09-11, 16:00–16:50, room The Grid

**Type**: Keynote

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

-

Source: <https://pretalx.com/pydata-amsterdam2026/talk/7PX99N/>

## 53. [Closing notes](https://pretalx.com/pydata-amsterdam2026/talk/7LV38T/)

**Speakers**: Not listed in the source data

**When and where**: Friday 2026-09-11, 16:50–17:10, room The Grid

**Type**: Closing Notes Friday

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

tbd

Source: <https://pretalx.com/pydata-amsterdam2026/talk/7LV38T/>

## 54. [Beyond LLM-as-Judge: Using GLIDE for Reliable, Scalable Evaluation of GenAI Systems](https://pretalx.com/pydata-amsterdam2026/talk/ZSYGEC/)

**Speakers**: Grégoire Martinon

**When and where**: Saturday 2026-09-12, 10:00–11:00, room Room A

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This session dives into rigorous evaluation methods, following prediction-powered statistical methods for AI system evaluation, as packaged in the [GLIDE library](https://github.com/EmertonData/glide).

The package allows engineers to leverage the seminal work of [Prediction-Powered-Inference (PPI++)](https://www.science.org/doi/10.1126/science.adi6000) and [Active Statistical Inference](https://dl.acm.org/doi/10.5555/3692070.3694680) to correct for LLM-as-Judge bias. GLIDE provides statistical guarantees that are often missing in modern LLM evaluation pipelines.

The presentation will outline the methodology of evaluation-driven-development and showcase live demos using GLIDE on a concrete use case.

Outline
• Introduction (5 min): The Agentic Boom and the Reliability Crisis
• The Methodology (10 min): High-level intuition of prediction-powered inference
• GLIDE in Action (10 min): Live Demo, using GLIDE to evaluate a RAG agent
• Future & Community (5 min): The GLIDE roadmap and how to contribute

Source: <https://pretalx.com/pydata-amsterdam2026/talk/ZSYGEC/>

## 55. [Polars Open Source Sprint: Fix Your First Issue or Build Your Own Expression Plugin](https://pretalx.com/pydata-amsterdam2026/talk/GHQQ9S/)

**Speakers**: Ritchie Vink, Thijs Nieuwdorp

**When and where**: Saturday 2026-09-12, 10:00–11:00, room Room B

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Polars is developed in the open, but the step from user to contributor can be big: a Rust codebase, build times, and unfamiliar conventions. This sprint removes that friction by putting you in a room with the people who build Polars.

You choose one of two tracks at the start.

Track 1: Good first issues. We walk through the repository layout, the build and test workflow, and how a change moves from issue to merged PR. Then you pick an issue labelled "good first issue" (Python API, documentation, or Rust, depending on your comfort) and work on it with review and guidance during the session.

Track 2: Expression plugins. Polars lets you register your own expressions written in Rust and call them from Python like any built-in. We start from a template, build a small plugin end to end, and then you extend it with functionality relevant to your own work: a domain-specific string parser, a custom aggregation, a distance metric, whatever Polars is missing for you.

What you will learn:

- How the Polars codebase and contribution workflow are organised
- How to build Polars from source and run the test suite
- How the expression plugin system works and when it beats map_elements or a UDF
- How to scaffold, compile, and call a plugin from Python

Outline:

1. Intro: how Polars is developed, how plugins fit into the expression engine (15 min)
2. Track kickoff: pick an issue, or scaffold a plugin (15 min)
3. Sprint: hands-on work with support from the Polars team (75 min)
4. Wrap-up: voluntary show and tell, open PRs, next steps (15 min)

Prerequisites (please do these before the session; the first Polars build takes 20+ minutes and Wi-Fi is shared):

- Laptop with a GitHub account, git, and a recent Python installed
- Rust toolchain via rustup (https://rustup.rs)
- Track 1: fork and clone https://github.com/pola-rs/polars, follow the build steps in the contributing guide (https://docs.pola.rs/development/contributing), and confirm that importing your local build works
- Track 2: install maturin, and generate a project from the Polars plugin cookiecutter template (https://github.com/MarcoGorelli/cookiecutter-polars-plugins); the accompanying plugin tutorial is a useful read beforehand
- Optional: browse the "good first issue" label on the Polars repo and shortlist one or two you find interesting

A setup checklist and links will be shared in a GitHub repo ahead of the session.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/GHQQ9S/>

## 56. [Polars Open Source Sprint: Fix Your First Issue or Build Your Own Expression Plugin](https://pretalx.com/pydata-amsterdam2026/talk/NCZA73/)

**Speakers**: Ritchie Vink, Thijs Nieuwdorp

**When and where**: Saturday 2026-09-12, 11:10–12:10, room Room B

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Polars is developed in the open, but the step from user to contributor can be big: a Rust codebase, build times, and unfamiliar conventions. This sprint removes that friction by putting you in a room with the people who build Polars.

You choose one of two tracks at the start.

Track 1: Good first issues. We walk through the repository layout, the build and test workflow, and how a change moves from issue to merged PR. Then you pick an issue labelled "good first issue" (Python API, documentation, or Rust, depending on your comfort) and work on it with review and guidance during the session.

Track 2: Expression plugins. Polars lets you register your own expressions written in Rust and call them from Python like any built-in. We start from a template, build a small plugin end to end, and then you extend it with functionality relevant to your own work: a domain-specific string parser, a custom aggregation, a distance metric, whatever Polars is missing for you.

What you will learn:

- How the Polars codebase and contribution workflow are organised
- How to build Polars from source and run the test suite
- How the expression plugin system works and when it beats map_elements or a UDF
- How to scaffold, compile, and call a plugin from Python

Outline:

1. Intro: how Polars is developed, how plugins fit into the expression engine (15 min)
2. Track kickoff: pick an issue, or scaffold a plugin (15 min)
3. Sprint: hands-on work with support from the Polars team (75 min)
4. Wrap-up: voluntary show and tell, open PRs, next steps (15 min)

Prerequisites (please do these before the session; the first Polars build takes 20+ minutes and Wi-Fi is shared):

- Laptop with a GitHub account, git, and a recent Python installed
- Rust toolchain via rustup (https://rustup.rs)
- Track 1: fork and clone https://github.com/pola-rs/polars, follow the build steps in the contributing guide (https://docs.pola.rs/development/contributing), and confirm that importing your local build works
- Track 2: install maturin, and generate a project from the Polars plugin cookiecutter template (https://github.com/MarcoGorelli/cookiecutter-polars-plugins); the accompanying plugin tutorial is a useful read beforehand
- Optional: browse the "good first issue" label on the Polars repo and shortlist one or two you find interesting

A setup checklist and links will be shared in a GitHub repo ahead of the session.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/NCZA73/>

## 57. [Stop Early, Decide Smarter: Bayesian Sequential Testing for LLM Benchmarking](https://pretalx.com/pydata-amsterdam2026/talk/BBXLSD/)

**Speakers**: Ryan Marinelli

**When and where**: Saturday 2026-09-12, 11:10–12:10, room Room A

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Fixed-sample benchmarking is the default in NLP and LLM evaluation, but it has two failure modes: it over-runs when models are clearly different early on, and under-runs when tight comparisons require more evidence than the budget allows. Sequential hypothesis testing, long standard in clinical trials and A/B testing, offers a cleaner framework: keep sampling until a decision threshold is crossed, or until a maximum budget is exhausted.

This talk applies that framework specifically to LLM and agent benchmarking and covers:

1. The statistical case: Why pass@k evaluation is often wasteful, and what sequential Bayes factors and posterior stopping criteria offer instead

2. Design choices: Prior elicitation, stopping thresholds, and how to handle multi-model comparisons without inflating error rates

3. Practical implementation: A walkthrough of a pip-installable Python package built on this framework

4. Limitations and scope: When sequential testing helps, when it doesn't, and how to sanity-check results

The talk is self-contained; attendees need only basic familiarity with probability and Python.

Outline (30 min):
Motivation: the cost of fixed-N benchmarking — 5 min
Sequential testing foundations (Bayes factors, stopping rules) — 8 min
Demo: the Python package on real benchmark data — 10 min
Design guidance, edge cases, and Q&A — 7 min

You can find the repo materials in: https://github.com/rymarinelli/bayesbench-notebook

Source: <https://pretalx.com/pydata-amsterdam2026/talk/BBXLSD/>

## 58. [Do you know how well your model is doing? Evaluate your LLMs](https://pretalx.com/pydata-amsterdam2026/talk/R3KMAB/)

**Speakers**: Cheuk Ting Ho

**When and where**: Saturday 2026-09-12, 13:00–14:00, room Room B

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

We will begin with an essential revision of the Hugging Face Transformers library, covering
basic LLM inference and fine-tuning. The core of the workshop will introduce and provide deep practice with Lighteval, an efficient and powerful LLM evaluation framework. Participants will learn how to leverage Lighteval to compare various LLMs available on the Hugging Face Hub using a range of pre-built tasks and metrics.
Finally, we will delve into advanced evaluation techniques, focusing on creating custom tasks and metrics tailored to unique, real-world application requirements. Participants will learn how to prepare custom datasets on the Hugging Face Hub and integrate them into Lighteval for precise, domain-specific evaluation. By the end of this workshop, you will possess the practical skills to rigorously evaluate, benchmark, and fine-tune your LLMs with confidence.

**Outline:**

**Part 1**

- Presentation: The importance of evaluation of LLMs
  - Compare performance of LLM for specific tasks
  - Benchmark the fine-tuning performance
  - Rail guard the LLM responses
- Coding exercise: Introduction and revision of Hugging Face Transformers
  - Revision of using Transformers for LLM influence
  - Fine tuning a LLM with transformers

**Part 2**

- Presentation: Introduction of Lighteval
  - What is Lighteval and what can it do
  - Different tasks and metrics available in Lighteval
- Coding exercise: Using Lighteval to compare LLMs
  - Familiar the use of Lighteval
  - Compare two LLMs on Hugging Face Hub
  - Experiment with different tasks and metrics

**Part 3**

- Presentation: Advance use of Lighteval
  - Introduction of custom tasks and metrics
  - What is needed for creating custom tasks and metrics
  - How to put custom tasks and metrics together
- Coding exercise: Practice with custom tasks and metrics
  - Uploading datasets to Hugging Face Hub
  - Creating custom tasks and metrics
  - Using custom tasks and metrics to compare LLMs

This workshop involves comparing different models, benchmarks the impact of fine-tuning, and ensures your LLM adheres to safety guidelines.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/R3KMAB/>

## 59. [Taking Flight: Zero-Copy Data Transfer at Scale with Apache Arrow Flight and Friends](https://pretalx.com/pydata-amsterdam2026/talk/NTQMFY/)

**Speakers**: Anders Bogsnes

**When and where**: Saturday 2026-09-12, 13:00–14:00, room Room A

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

In this talk, you will see why Arrow Flight makes building infrastructure to serve large amounts of data feasible. I will go through a brief breakdown of what Arrow is, and what benefits it brings before moving on to looking at the Arrow Flight specification.

By going through each of the components that makes up the Arrow Flight specification, you'll be able to start building your own Arrow flight server. I will take you through benchmarking Arrow Flight vs the classic REST Api and show the massive speed increases. I will go through how to build your own Arrow Flight server and demonstrate how easy it is to build a Client.

At the end, you'll have an understanding of what purpose Arrow Flight serves in your stack, and if you should take advantage of it.

Attendees are requested to clone [this GitHub repository](https://github.com/andersbogsnes/pydata-amsterdam-2026-taking-flight-with-arrow-flight) in advance and complete the environment setup described in the README (requires `uv`, Docker, and Docker Compose), along with the data-fetch and bootstrap steps, to ensure a smooth, hands-on experience.

Source: <https://pretalx.com/pydata-amsterdam2026/talk/NTQMFY/>

## 60. [LLM Evaluation in Production: A/B Testing and Observability](https://pretalx.com/pydata-amsterdam2026/talk/QCHL8T/)

**Speakers**: Kader Miyanyedi, Özge Çinko

**When and where**: Saturday 2026-09-12, 14:00–15:00, room Room B

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

Modern LLM development is not just about running a single model. Even small changes can affect output quality, safety, and user experience. In this session, attendees will learn how to use Langfuse to log LLM outputs, run A/B tests, and track important metrics.

We will also explore why A/B testing is important in LLM development and how to compare different models or prompt versions using real user data.

By the end of the session, attendees will understand how to:

- Design data-driven A/B tests in LLM development workflows

- Combine code, tests, and experiments to create reliable, repeatable testing processes

- Log experiments and track model performance and user-facing outputs with Langfuse

- Define and use simple metrics to evaluate LLM quality and behavior

- Make better decisions by comparing different prompts or model versions

This session gives Python developers a framework to integrate experiments, tests, and data into LLM development, enabling reliable, repeatable, and data-driven workflows.

Attendees are requested to clone [this GitHub repository](https://github.com/Kadermiyanyedi/llm-evaluation-pydata-amsterdam-tutorial) in advance and complete the setup described in the README, to ensure a smooth, hands-on experience!

Source: <https://pretalx.com/pydata-amsterdam2026/talk/QCHL8T/>

## 61. [Reuniting the two distant cousins: Orchestrating your end-to-end Data Engineering Workflow Leveraging Python in Apache Beam and Apache Airflow](https://pretalx.com/pydata-amsterdam2026/talk/ASSD9U/)

**Speakers**: Sadeeq Akintola

**When and where**: Saturday 2026-09-12, 14:00–15:00, room Room A

**Type**: Tutorial

**Abstract** (verbatim from the [schedule data JSON](https://pydata-guide-web.onrender.com/schedule/data.json)):

This talk explores the synergy between Apache Beam and Apache Airflow, demonstrating how to create a robust, end-to-end data engineering workflow using Python. We will dive into the challenges of orchestrating complex data processing tasks and show how combining Airflow's scheduling capabilities with Beam's data processing framework can create more efficient and manageable data pipelines. Both Airflow and Beam processes will be written in beginner-level python - so if you are a beginner or intermediate data engineer or architect, this session is for you! Lastly, we will cover integrations with Cloud Platform services, including Cloud Functions, BigQuery, SendGrid email, and the latest Gemini AI models.

Attendees can access the GitHub repository [here](https://github.com/SadeeqAkintola/pydata-amsterdam).

Source: <https://pretalx.com/pydata-amsterdam2026/talk/ASSD9U/>
