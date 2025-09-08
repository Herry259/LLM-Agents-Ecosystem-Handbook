# Agent Framework Comparison

This document expands upon the summary table in the root `README.md`.  It provides more detail on the philosophy, strengths and trade‑offs of each open‑source agent framework.  Star counts are approximate as of July 2025.

## LangGraph

**Philosophy:** Treat multi‑step agent workflows as a directed acyclic graph (DAG) where each node represents a tool invocation or decision.  This explicit representation makes it easy to debug and branch complex flows.  LangGraph is built as an extension to LangChain and benefits from its ecosystem of connectors【913044646548243†L44-L63】.

**Strengths:**
- Clear visualisation of workflows, including branching and loops.
- Integrates seamlessly with LangChain tools and memory modules.
- Suitable for projects that need deterministic orchestration and reproducibility.

**Trade‑offs:**
- Requires learning graph concepts; may be overkill for simple linear tasks.

## OpenAI Agents SDK

**Philosophy:** Provide a structured runtime for building agents that can reason, plan and call tools via the OpenAI API.  Emphasises role‑based communication and integrates deeply with OpenAI models【913044646548243†L64-L80】.

**Strengths:**
- Native support for OpenAI function calling and model endpoints.
- Role abstraction simplifies multi‑agent conversations.
- Built‑in tracing and guardrails to improve reliability.

**Trade‑offs:**
- Less flexible with non‑OpenAI providers.
- Relies on hosted APIs for production workloads.

## AutoGen (AG2)

**Philosophy:** Enable event‑driven conversations between specialised agents.  Agents communicate asynchronously, invoking tools and humans as needed【913044646548243†L127-L147】.

**Strengths:**
- Scales to complex tasks by decomposing them into conversations among planner, researcher and executor agents.
- Supports human‑in‑the‑loop interactions.
- Active community and high star count.

**Trade‑offs:**
- Setup can be complex for small projects.
- Limited first‑class support for non‑conversation workflows.

## CrewAI

**Philosophy:** Model teams of agents (“crew”) with defined roles and memory.  Agents coordinate tasks collaboratively, passing messages and results【913044646548243†L105-L125】.

**Strengths:**
- Simple API to define agent roles and assign tasks.
- Built‑in error handling and fallback strategies.
- Good for projects where collaboration among agents mimics human teams.

**Trade‑offs:**
- May require custom tooling to integrate with external APIs.
- Limited support for asynchronous messaging compared to AutoGen.

## Semantic Kernel

**Philosophy:** Compose “skills” (functions) into complete plans.  Strong focus on enterprise security, compliance and .NET integration【913044646548243†L150-L169】.

**Strengths:**
- Supports C#, Python and Java, making it attractive for enterprise developers.
- Fine‑grained control over plan execution and memory storage.
- Tight integration with Azure and other Microsoft services.

**Trade‑offs:**
- The .NET focus may be less appealing to pure Python environments.
- Smaller community compared to LangChain and AutoGen.

## LlamaIndex Agents

**Philosophy:** Combine retrieval‑augmented generation with agent behaviours.  Agents use LlamaIndex to access data sources and tools, then reason to produce answers【913044646548243†L171-L191】.

**Strengths:**
- Excellent for data‑centric applications where information retrieval is crucial.
- Large ecosystem of connectors for databases, vector stores and APIs.
- Can operate offline for privacy‑sensitive use cases.

**Trade‑offs:**
- Requires understanding of retrieval mechanics.
- May not be necessary for tasks that don’t involve external data.

## Smolagents

**Philosophy:** Provide a minimal, code‑centric agent loop where the LLM writes and executes Python code directly【913044646548243†L82-L103】.

**Strengths:**
- Lightweight and easy to embed in existing codebases.
- Ideal for rapid automation of small tasks.

**Trade‑offs:**
- Lacks orchestration primitives for complex workflows.
- Less mature ecosystem.

## Strands Agents

**Philosophy:** Offer a model‑agnostic SDK that runs anywhere and integrates with major providers like Amazon Bedrock, Anthropic, OpenAI and Ollama【913044646548243†L194-L214】.

**Strengths:**
- Flexible provider support and built‑in observability via OpenTelemetry.
- Suitable for organisations that need to switch models or vendors.

**Trade‑offs:**
- Smaller community and fewer examples compared to incumbents.

## Pydantic AI

**Philosophy:** Define agent inputs, outputs and tool signatures using Pydantic models to ensure type safety【913044646548243†L216-L232】.

**Strengths:**
- Strong type validation and error feedback.
- Familiar developer experience for FastAPI users.

**Trade‑offs:**
- Overhead of defining schemas may slow rapid prototyping.


For a tabular comparison of these frameworks, refer to the table in the root `README.md`.