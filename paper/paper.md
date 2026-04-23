---
title: 'Antigravity Nano Research Multiagentic Core: An Open Educational Framework for Multi-Agent AI in Computational Nanotechnology'
tags:
  - Python
  - multi-agent systems
  - nanotechnology
  - computational materials science
  - large language models
  - graph retrieval-augmented generation
  - model context protocol
  - education
authors:
  - name: Luis José Yudico-Anaya
    orcid: 0000-0002-7490-3304
    affiliation: 1
affiliations:
  - name: Universidad de La Ciénega del Estado de Michoacán de Ocampo, México
    index: 1
date: 23 April 2026
bibliography: paper.bib
---

# Summary

**Antigravity Nano Research Multiagentic Core** is an open-source framework
that integrates multi-agent large language model (LLM) systems with
computational nanotechnology research and education. The system provides a
structured six-unit curriculum (30+ Jupyter notebooks) that progressively
covers nanoscale simulation, machine learning for materials, and multi-agent
orchestration. A central design goal is accessibility: a fully reproducible
demonstration system based on Au$_{13}$ nanoclusters
(`educational_content/unit_06_integration_project/`) runs end-to-end without
any API keys or paid subscriptions, using only the open-source Atomic Simulation
Environment [@Larsen2017], scikit-learn [@Pedregosa2011], and mock retrieval components.

The framework targets graduate students, researchers, and educators in
computational materials science who wish to adopt AI-assisted workflows without
starting from scratch. It is simultaneously a *teaching platform* (complete
curriculum, rubric, executable demos) and a *research prototype* (Graph RAG,
Model Context Protocol integration, production deployment with FastAPI).

# Statement of Need

The adoption of LLM-based agents in computational science is growing rapidly,
yet the existing ecosystem presents a fragmented landscape: general-purpose
frameworks (LangGraph [@LangGraph2024], CrewAI [@CrewAI2024], Google ADK
[@GoogleADK2025], smolagents [@Smolagents2024], AutoGen [@AutoGen2023],
MetaGPT [@MetaGPT2023]) do not address domain-specific scientific tools such
as atomistic simulators, materials databases, or spectroscopic data pipelines.
Conversely, specialized computational chemistry platforms (AiiDA, AutomatMiner,
ChemCrow) do not offer multi-agent orchestration, educational pathways, or
systematic comparison of LLM frameworks.

This gap has practical consequences: a researcher or instructor who wishes to
teach or prototype an AI-assisted nanotechnology workflow must integrate
multiple libraries manually, often reinventing common infrastructure (LLM
routing, tool registration, observability, deployment). No existing open
resource provides (1) a complete, executable curriculum in this domain,
(2) a principled comparison of seven major agent frameworks from the perspective
of scientific computing, and (3) a demonstration that runs without paid API
access.

**Antigravity Nano Research Multiagentic Core** addresses all three gaps.
By combining a structured educational progression with production-quality
components—automated tests, CI/CD, FastAPI deployment, Graph RAG, and MCP
integration—it lowers the barrier for scientific groups to adopt agentic AI
while producing pedagogically sound teaching materials.

# Software Description

## Architecture

The system is organized into six progressive educational units:

| Unit | Topic | Key Technologies |
|:-----|:------|:----------------|
| 1 | Nanoscale Modeling | ASE [@Larsen2017], RDKit, OpenMM |
| 2 | Molecular Simulation (MD, DFT) | ASE/EMT, OpenMM |
| 3 | Machine Learning for Nanomaterials | scikit-learn [@Pedregosa2011], PyTorch |
| 4 | Applied AI in Nanotechnology | Materials Project API, Computer Vision |
| 5 | Multi-Agent Systems | LangGraph, CrewAI, ADK, smolagents, AutoGen |
| 6 | Integration Project | Full pipeline, FastAPI, deployment |

Each unit contains 2–9 Jupyter notebooks with a common structure: executable
demonstration first, conceptual explanation second, and scaffolded exercises
connecting to the student's own research.

## Unified LLM Routing

A central utility function `get_llm()` provides transparent routing across
five LLM backends: OpenRouter (cloud, multi-model), Gemini 2.5 Flash/Pro
(Google), Llama 4 Scout (Meta via OpenRouter), Kimi-K2.5 (Moonshot AI), and
Ollama (fully local inference). This design ensures that the same notebook
code runs regardless of the available backend, enabling use in resource-
constrained environments (no GPU, no paid API) and in production deployments
interchangeably.

## Au$_{13}$ Reproducible Demonstration

Unit 6 (`U6_03`) implements a four-tool agentic pipeline for Au$_{13}$
nanocluster research:

1. **Structure optimizer** — ASE/EMT geometry optimization
2. **Property predictor** — Gradient Boosting Regressor (scikit-learn) trained
   on cluster size features
3. **Literature search** — mock Graph RAG backed by NetworkX [@NetworkX2008]
4. **Report generator** — structured JSON report via LLM

The complete pipeline runs in under five minutes on a standard laptop without
internet connectivity, producing a reproducible analysis report. This serves
as the canonical demonstration for the course and as a baseline for benchmarking
in future research publications.

## Graph RAG with Multiple Backends

Unit 5 (`U5_06`) implements a Graph Retrieval-Augmented Generation module
supporting four storage backends:

- **NetworkX** [@NetworkX2008] — in-memory prototype, zero dependencies
- **Kùzu** [@Kuzu2023] — embedded graph database, no server required
- **Neo4j** — production graph database with Cypher query language
- **Graphiti** [@Graphiti2024] — episodic memory for stateful agents

A decision table guides users and agents through backend selection based on
data size, query type (factual, relational, temporal), and deployment constraints.

## Model Context Protocol Integration

Unit 5 (`U5_04`) implements an MCP server [@MCP2024] that exposes ASE
computational tools—structure optimization, energy calculation, band gap
estimation—as standardized JSON-RPC tools consumable by any MCP-compliant
agent. This establishes a reproducible interface between LLM orchestrators
and domain-specific scientific calculators, independent of the LLM backend.

## Observability and Deployment

The framework integrates LangSmith [@LangSmith2024] for distributed tracing
of agent calls, token usage, and tool invocations. Production deployment
is implemented via FastAPI [@FastAPI2018] using the modern `lifespan` context
manager pattern, with a ready-to-adapt `Dockerfile` for containerized deployment.

## Test Suite

The project includes an automated test suite validated on Python 3.11:

- **19 unit tests** (`tests/test_unit05.py`) covering arithmetic safety,
  security constraints (import blocking, attribute access blocking), and
  external skill module integrity — all passing (0.16 s, pytest 9.0.2)
- **`tests/test_unit03_parte2.py`** — neural network logic validation
- **`tests/test_external_skills.py`** — modular skill system tests
- GitHub Actions CI executes the full test suite on every push to `main`

## External Skills

The `external_skills/` directory provides nine reusable Python modules for
scientific validation: `stability_guardian` (MD timestep validation),
`basis_set_architect` (DFT basis set recommendation), `toxicity_predictor`
(molecular toxicity mock), `socratic_debugger` (pedagogical feedback
generator), `librarian_rag` (literature RAG), and orchestration utilities
(`context_loader`, `task_classifier`, `output_scorer`, `episodic_retriever`,
`trace_annotator`, `token_budget_guard`). All skills are designed as
drop-in modules that can be used independently or composed in agent workflows.

# Acknowledgements

The author thanks the teams behind the open-source tools that make this
framework possible: ASE [@Larsen2017] (DTU Physics), LangGraph [@LangGraph2024]
and LangSmith [@LangSmith2024] (LangChain Inc.), smolagents [@Smolagents2024]
(Hugging Face), Google ADK [@GoogleADK2025] (Google LLC), AutoGen [@AutoGen2023]
(Microsoft Research), MetaGPT [@MetaGPT2023], the Model Context Protocol
[@MCP2024] (Anthropic), Kùzu [@Kuzu2023], Graphiti [@Graphiti2024] (Zep AI),
FastAPI [@FastAPI2018], NetworkX [@NetworkX2008], scikit-learn [@Pedregosa2011],
and NumPy [@Harris2020].

This work was carried out at the Universidad de La Ciénega del Estado de
Michoacán de Ocampo (UCEMICH), México.

# References
