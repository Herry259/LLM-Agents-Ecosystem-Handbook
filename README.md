# LLM Agents & Ecosystem Handbook


<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook/stargazers"><img src="https://img.shields.io/github/stars/oxbshw/LLM-Agents-Ecosystem-Handbook?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook/issues"><img src="https://img.shields.io/github/issues/oxbshw/LLM-Agents-Ecosystem-Handbook" alt="Issues"></a>
  <a href="https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook/pulls"><img src="https://img.shields.io/github/issues-pr/oxbshw/LLM-Agents-Ecosystem-Handbook" alt="Open PRs"></a>
  <a href="https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook/graphs/contributors"><img src="https://img.shields.io/github/contributors/oxbshw/LLM-Agents-Ecosystem-Handbook" alt="Contributors"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
  <a href="https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook/commits/main"><img src="https://img.shields.io/github/last-commit/oxbshw/LLM-Agents-Ecosystem-Handbook" alt="Last commit"></a>
</p>

<p align="center"><strong>A unified handbook for building, deploying and understanding LLM agents and the wider ecosystem</strong></p>

A polished, curated collection of **Large Language Model (LLM) agents**, tutorials and ecosystem insights. This handbook highlights projects that push the boundaries of generative AI, multi-agent collaboration, retrieval-augmented generation (RAG), voice and game agents, and more. It goes beyond simple link aggregation, aiming to be a one-stop reference for building, deploying, and understanding LLM applications across the entire stack.

> **Tip:** If you enjoy this list, please consider starring the repository to help others discover it!

---

## Table of Contents

- [Top Agent Frameworks](#top-agent-frameworks)
- [Agent Toolkits & Platforms](#agent-toolkits--platforms)
- [Starter AI Agents](#starter-ai-agents)
- [Advanced AI & Domain-Specific Agents](#advanced-ai--domain-specific-agents)
- [Multi-Agent Teams](#multi-agent-teams)
- [Voice & Game Agents](#voice--game-agents)
- [RAG & Memory Examples](#rag--memory-examples)
- [MCP Agent Integrations](#mcp-agent-integrations)
- [LLM Evaluation Frameworks](#llm-evaluation-frameworks)
- [Example Projects](#example-projects)
- [Tutorials & Learning Resources](#tutorials--learning-resources)
  - [RAG Tutorials](#rag-tutorials)
  - [Memory Apps Tutorials](#memory-apps-tutorials)
  - [Chat with X Tutorials](#chat-with-x-tutorials)
  - [LLM Fine-Tuning Tutorials](#llm-fine-tuning-tutorials)
- [Other Educational Spaces](#other-educational-spaces)
- [Unique Features](#unique-features)
- [Languages & Multilingual Support](#languages--multilingual-support)
- [Interactive Demos & Resources](#interactive-demos--resources)
  - [Web Apps](#web-apps)
  - [Jupyter Notebooks](#jupyter-notebooks)
- [Datasets & Design Assets](#datasets--design-assets)
- [Documentation & Roadmap](#documentation--roadmap)
- [Complete Applications](#complete-applications)
- [Beginner’s Guide](#beginners-guide)
- [Contributing](#contributing)
- [License](#license)
- [Maintainer](#maintainer)

---

## Why this repository stands out

This curated collection aims to be a **comprehensive resource** for developers and researchers building their own LLM applications. In addition to code examples, it provides:

- **Comparative analysis of leading agent frameworks:** A quick matrix contrasting frameworks (LangGraph, AutoGen, CrewAI, Smolagents, etc.) with key features to help you choose.
- **Guidance on framework selection:** Practical advice based on task complexity, collaboration needs and ecosystem integrations.
- **LLM evaluation toolbox:** Summaries of tools like Promptfoo, DeepEval, MLflow LLM Evaluate, RAGAs and Langfuse to measure performance and safety.
- **60+ skeleton projects:** The `agents` folder contains scaffolded agents across many domains (blogging, medical imaging, music generation, multimodal input, news, finance, research, scraping, consultancy, system design, compliance, marketing, scheduling, supply-chain, healthcare, education). Each skeleton includes a `README.md` and `main.py`.
- **Agent skeleton generator:** [`scripts/create_agent.py`](scripts/create_agent.py) to spin up new agent skeletons in seconds.

---

## Top Agent Frameworks

| Framework | Description & Key Features |
|---|---|
| **LangGraph** | Graph/DAG-based orchestration for complex multi-step workflows. |
| **OpenAI Agents SDK** | Structured runtime with tool-calling and role-based agents. |
| **AutoGen (AG2)** | Event-driven multi-agent conversations and human-in-the-loop. |
| **CrewAI** | Role-based “crew” collaboration with memory and error handling. |
| **Google AgentKit (ADK)** | Modular Gemini/Vertex AI agent kit with hierarchical tools. |
| **Dify** | Low-code builder with RAG and function calling. |
| **LangChain & Tools** | Mature chains, memory and 3rd-party integrations. |
| **Smolagents** | Minimal, code-centric loop (agents write & execute code). |
| **Semantic Kernel** | .NET-first skills/plans; enterprise-friendly. |
| **LlamaIndex Agents** | Retrieval-focused agents for data-heavy apps. |
| **Strands Agents** | Provider-agnostic SDK with OpenTelemetry. |
| **Pydantic AI** | Type-safe IO/tool signatures with great DX. |

---

## Agent Toolkits & Platforms

| Project | Description |
|---|---|
| **AutoGPT** | Toolkit for autonomous agents (creation, benchmarking, UI/CLI). |
| **Ollama** | Run LLMs locally across macOS/Windows/Linux/Docker. |
| **Lobe Chat** | Open-source chat UI with plugins and multimodal support. |
| **OpenDevin** | Open initiative towards an AI software engineer. |
| **Open Interpreter** | Natural-language coding & local computer control. |
| **MetaGPT** | Multi-agent “virtual company” for complex tasks. |
| **PrivateGPT** | Secure offline Q&A over your documents. |
| **GPT-Engineer** | From natural-language spec to code. |
| **LlamaIndex Tools** | Connectors/tools for data agents. |
| **Flowise** | Drag-and-drop builder for LLM workflows. |
| **FastChat** | Train/serve/evaluate chatbots. |
| **Mem0** | Memory layer for personalised LLMs. |
| **Cal.ai** | Scheduling assistant with email handling. |
| **Aider** | CLI pair-programming agent with Git integration. |
| **Jan** | Offline ChatGPT-style desktop app. |

---

## Starter AI Agents

| Agent | Description |
|---|---|
| **AI Blog to Podcast Agent** | Convert blog posts into podcasts. |
| **AI Data Analysis Agent** | Insights from CSV/structured data. |
| **AI Travel Agent** | Trip itineraries (local/cloud). |
| **AI Music Generator** | Compose via generative models. |
| **AI Meme Generator (Browser)** | Creates memes by overlaying captions on images. |
| **AI Breakup Recovery Agent** | Supportive advice for emotional situations. |
| **AI Health & Fitness Agent** | Health metrics & coaching. |
| **Gemini Multimodal Agent** | Text+image multimodal demo. |

---

## Advanced AI & Domain-Specific Agents

| Agent | Description |
|---|---|
| **AI Deep Research Agent** | Multi-source research & synthesis. |
| **AI Consultant Agent** | Domain-expert strategy & advice. |
| **AI System Architect Agent** | From requirements to architecture. |
| **AI Lead Generation Agent** | Identify & qualify prospects. |
| **AI Meeting Agent** | Summaries & action items. |
| **OpenAI Research Agent** | Research workflows with tools. |
| **Explainable AI Finance Agent** | Finance with interpretability. |
| **Web Scraping Agent** | Crawl & extract structured data. |
| **Document Processing Agent** | OCR + analysis/summarisation. |
| **Sentiment Analysis Agent** | Classify sentiment at scale. |
| **Technical Translation Agent** | Preserve domain terminology. |
| **Research Synthesizer Agent** | RAG + coherent reporting. |

---

## Multi-Agent Teams

| Team | Description |
|---|---|
| **Competitor Intelligence Team** | Market/competitor research & reporting. |
| **Finance Agent Team** | Budgeting, forecasting and reporting. |
| **Teaching Agent Team** | Lesson planning, delivery and assessment. |
| **Multi-Agent Team Demo** | Cross-role collaboration patterns. |
| **Mixture of Agents Demo** | Specialised agent ensembles. |

---

## Voice & Game Agents

| Agent | Description |
|---|---|
| **Voice Summary Agent** | Transcribe and summarise audio. |
| **AI Audio Tour Agent** | Generate audio tours for museums/cities. |
| **Customer Support Voice Agent** | Handle spoken queries and log issues. |
| **Voice RAG Agent** | Voice input + retrieval + TTS. |
| **Tic-Tac-Toe Agent** | Autonomous gameplay template. |

---

## RAG & Memory Examples

| Example | Description |
|---|---|
| **Agentic RAG with Reasoning** | Retrieval → reasoning → generation. |
| **Hybrid Search RAG** | Vector + keyword retrieval. |
| **Vision RAG** | Apply RAG to visual data. |
| **CRAG (Corrective RAG)** | Human-feedback corrective loop. |
| **Local RAG Agent** | Fully offline retrieval pipeline. |

---

## MCP Agent Integrations

| Agent | Description |
|---|---|
| **Browser MCP Agent** | Drive a browser (search/click/forms). |
| **GitHub MCP Agent** | Read/write/manage repositories. |
| **Notion MCP Agent** | Create/update/query Notion pages & DBs. |
| **Travel Planner MCP Agent Team** | Multi-agent trip planning via MCP. |

---

## LLM Evaluation Frameworks

See [`evaluation_frameworks/README.md`](evaluation_frameworks/README.md) for details about Promptfoo, DeepEval, MLflow LLM Evaluate, RAGAs, Deepchecks, LangSmith, TruLens, Arize Phoenix and Langfuse.

---

## Example Projects

The `agents` directory contains many **agent skeletons** organised by category. Category folders (`starter`, `advanced`, `teams`, `rag`) act as **indexes**, while each agent lives in its own top-level folder under `agents/`.

### Quick picks

- **Summarization Agent** – [agents/summarization_agent](agents/summarization_agent)  
- **Data Analysis Agent** – [agents/data_analysis_agent](agents/data_analysis_agent)  
- **Travel Itinerary Agent** – [agents/travel_itinerary_agent](agents/travel_itinerary_agent)  
- **Voice Assistant Demo** – [agents/voice_agent_demo](agents/voice_agent_demo)  
- **Meme Generator Agent** – [agents/meme_generator_agent](agents/meme_generator_agent)  
- **Health & Fitness Agent** – [agents/health_fitness_agent](agents/health_fitness_agent)  
- **Breakup Recovery Agent** – [agents/breakup_recovery_agent](agents/breakup_recovery_agent)  
- **AI Blog to Podcast Agent** – [agents/ai_blog_to_podcast_agent](agents/ai_blog_to_podcast_agent)  
- **AI Medical Imaging Agent** – [agents/ai_medical_imaging_agent](agents/ai_medical_imaging_agent)  
- **AI Music Generator Agent** – [agents/ai_music_generator_agent](agents/ai_music_generator_agent)  
- **Local News Agent** – [agents/local_news_agent](agents/local_news_agent)  
- **Gemini Multimodal Demo** – [agents/gemini_multimodal_agent_demo](agents/gemini_multimodal_agent_demo)

---

## Tutorials & Learning Resources

Hands-on tutorials live in [`tutorials/`](tutorials) directory.

- **RAG Tutorials** → [`tutorials/rag_tutorials`](tutorials/rag_tutorials)  
- **Memory Apps Tutorials** → [`tutorials/memory_apps`](tutorials/memory_apps)  
- **Chat with X Tutorials** → [`tutorials/chat_with_x_tutorials`](tutorials/chat_with_x_tutorials)  
- **Fine-Tuning Tutorials** → [`tutorials/fine_tuning_tutorials`](tutorials/fine_tuning_tutorials)

---

## Other Educational Spaces

- **Interactive demos & notebooks:** [`web_apps`](web_apps), [`notebooks`](notebooks)  
- **Datasets & design assets:** [`datasets`](datasets), [`design`](design)  
- **LLM ecosystem overview:** [`ecosystem/overview.md`](ecosystem/overview.md)  
- **Complete applications:** [`complete_apps`](complete_apps)

---

## Unique Features

- **Educational focus:** Detailed tutorials (RAG, memory, chat with X, fine-tuning) + 60+ scaffolded agents.  
- **Framework comparison & guidance:** Practical, vendor-neutral advice.  
- **Agent skeleton generator:** `scripts/create_agent.py`.  
- **Evaluation toolbox:** Promptfoo, DeepEval, RAGAs, etc.  
- **Ecosystem breadth:** Training, tools, production, local inference, operations, interpretability.  
- **Community roadmap:** See [`docs/roadmap.md`](docs/roadmap.md).  

---

## Languages & Multilingual Support

We welcome translations. See [`TRANSLATION.md`](TRANSLATION.md). A **Technical Translation Agent** exists under `agents/technical_translation_agent`.

---

## Interactive Demos & Resources

### Web Apps

- **Streamlit Summariser** – [`web_apps/streamlit_summarizer`](web_apps/streamlit_summarizer)  
- **Gradio FAQ Bot** – [`web_apps/gradio_faq_bot`](web_apps/gradio_faq_bot)

### Jupyter Notebooks

- **Getting Started** – [`notebooks/getting_started.ipynb`](notebooks/getting_started.ipynb)

---

## Datasets & Design Assets

- **Sample dataset** – [`datasets/sample_products.csv`](datasets/sample_products.csv) (+ [`datasets/README.md`](datasets/README.md))  
- **Architecture diagram** – [`design/architecture_diagram.png`](design/architecture_diagram.png) (+ [`design/README.md`](design/README.md))

---

## Documentation & Roadmap

- **Best practices** – [`docs/best_practices.md`](docs/best_practices.md)  
- **Framework comparison** – [`docs/framework_comparison.md`](docs/framework_comparison.md)  
- **Evaluation frameworks guide** – [`evaluation_frameworks/README.md`](evaluation_frameworks/README.md)  
- **Quickstart** – [`tutorials/quickstart.md`](tutorials/quickstart.md)  
- **Roadmap** – [`docs/roadmap.md`](docs/roadmap.md)  
- **Changelog** – [`CHANGELOG.md`](CHANGELOG.md)

---

## Complete Applications

- **Task Planner** – [`complete_apps/task_planner`](complete_apps/task_planner)  
- **Health Coach** – [`complete_apps/health_coach`](complete_apps/health_coach)

---

## Beginner’s Guide

If you’re new to LLMs, start here → [`docs/beginners_guide.md`](docs/beginners_guide.md)

---

## Contributing

Contributions are welcome! Please open an issue or PR. Ensure new entries are permissively licensed (MIT/Apache-2.0) and well-documented.

---

## License

MIT — see [LICENSE](LICENSE).

---

## Maintainer

Curated & maintained by **Sayed Allam** ([oxbshw](https://github.com/oxbshw)). If you find this helpful, please ⭐ star the repo and share feedback via issues/PRs.
