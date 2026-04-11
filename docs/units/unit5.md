# Unit 5 — Multi-Agent Systems

## Overview

Design and orchestration of multi-agent systems for scientific research, from LangChain to Google ADK 1.0 with A2A protocol.

## Topics

### Frameworks Covered

| Framework | Focus |
|-----------|-------|
| LangChain | Chains, tools, LCEL |
| LangGraph | Stateful graphs, cycles |
| CrewAI | Role-based collaboration |
| Google ADK 1.0 | Production-ready agents |
| SmolaAgents | Lightweight agents (HF) |

### Advanced Topics

- **A2A Protocol** (Agent-to-Agent) — Cross-framework communication standard
- **RAG & GraphRAG** — Retrieval-Augmented Generation with graphs
- **Mem0 + ChromaDB** — Persistent agent memory
- **Production**: FastAPI, OpenTelemetry, model routing

## Key Notebooks

| Notebook | Topic |
|----------|-------|
| U5_01 | LangChain fundamentals |
| U5_02 | LangGraph stateful agents |
| U5_03 | CrewAI multi-role teams |
| **U5_04** | **Google ADK 1.0 + A2A + Gemma4** |
| U5_05 | RAG and GraphRAG |
| U5_06 | Persistent memory (Mem0) |
| U5_07 | Production: FastAPI + observability |
| U5_08 | Multi-provider model routing |
| U5_09 | SmolaAgents (HuggingFace) |

## U5_04 Highlights — Google ADK + A2A

The most advanced notebook in the unit covers:

- `LlmAgent`, `SequentialAgent`, `ParallelAgent`, `LoopAgent`
- `BuiltInCodeExecutor` — Code execution in secure sandbox
- `BaseTool` with strict Pydantic typing
- Session checkpoints and recovery
- **AgentCard** and A2A discovery protocol
- Cross-framework client with Bearer authentication
- Local fallbacks for exhausted API quotas

[Open Unit 5 in GitHub](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core/tree/main/educational_content/unit_05_multi_agent_sys){ .md-button }
