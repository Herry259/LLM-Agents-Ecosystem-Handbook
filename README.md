# LLM Agents & Ecosystem Handbook

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


<p align="center"><strong>A unified handbook for building, deploying and understanding LLM agents and the wider ecosystem</strong></p>

A polished, curated collection of **Large Language Model (LLM) agents**, tutorials and ecosystem insights.  This handbook highlights projects that push the boundaries of generative AI, multi‑agent collaboration, retrieval‑augmented generation (RAG), voice and game agents and more.  It goes beyond simple link aggregation, aiming to be a one‑stop reference for building, deploying and understanding LLM applications across the entire stack.

> **Tip:** If you enjoy this list, please consider starring the repository to help others discover it!

## Sources & Credits

This collection was inspired by and builds upon insights from the following resources:

- [Shubhamsaboo/awesome‑llm‑apps](https://github.com/Shubhamsaboo/awesome-llm-apps) – a comprehensive catalog of LLM apps using AI agents, RAG, multi‑agent teams and voice agents.
- [Slavakurilyak/awesome‑ai‑agents](https://github.com/slavakurilyak/awesome-ai-agents) – a curated list of agentic AI projects with star counts and descriptions.
- [Firecrawl’s Top Frameworks for 2025](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks-2025) – analysis of leading open‑source agent frameworks with star counts and key features【710521934811195†L166-L191】【710521934811195†L226-L247】.
- [APIpie’s Top AI Agent Frameworks](https://apipie.ai/docs/blog/top-10-opensource-ai-agent-frameworks-may-2025) – ranking and comparison of open‑source frameworks【650021038249031†L68-L116】.

We have reorganized and summarized content from these sources to improve clarity and highlight standout projects. All original content remains under their respective licenses.

## Table of Contents

- [Top Agent Frameworks](#top-agent-frameworks)
- [Agent Toolkits & Platforms](#agent-toolkits--platforms)
- [Starter AI Agents](#starter-ai-agents)
- [Advanced AI & Domain‑Specific Agents](#advanced-ai--domain-specific-agents)
- [Multi‑Agent Teams](#multi-agent-teams)
* [Voice & Game Agents](#voice--game-agents)
- [RAG & Memory Examples](#rag--memory-examples)
 - [MCP Agent Integrations](#mcp-agent-integrations)
 - [LLM Evaluation Frameworks](#llm-evaluation-frameworks)
 - [Example Projects](#example-projects)
 - [Contributing](#contributing)

* [Tutorials & Learning Resources](#tutorials--learning-resources)
  * [RAG Tutorials](#rag-tutorials)
  * [Memory Apps Tutorials](#memory-apps-tutorials)
  * [Chat with X Tutorials](#chat-with-x-tutorials)
  * [LLM Fine‑Tuning Tutorials](#llm-fine-tuning-tutorials)

* [Other educational spaces](#other-educational-spaces)
* [Unique features](#unique-features)
* [Languages & multilingual support](#languages--multilingual-support)

* [Why this repository stands out](#why-this-repository-stands-out)
* [Interactive demos & resources](#interactive-demos--resources)
  * [Web apps](#web-apps)
  * [Jupyter notebooks](#jupyter-notebooks)
* [Datasets & design assets](#datasets--design-assets)
* [Documentation & roadmap](#documentation--roadmap)
* [Complete applications](#complete-applications)
* [Beginner’s guide](#beginner’s-guide)

## Why this repository stands out

Unlike other lists that merely collect links to ready‑made projects, this curated
collection aims to be a **comprehensive resource** for developers and
researchers building their own LLM applications.  In addition to code
examples, it provides:

- **Comparative analysis of leading agent frameworks:**  A table that
  contrasts frameworks such as LangGraph, AutoGen, CrewAI and Smolagents with
  star counts and key features.  You can quickly decide which framework fits
  your use case.
- **Guidance on framework selection:**  A section detailing how to choose
  between frameworks based on task complexity, collaboration requirements and
  ecosystem integrations【913044646548243†L276-L296】.
- **LLM evaluation toolbox:**  A dedicated directory of evaluation
  frameworks summarising tools like Promptfoo, DeepEval, MLflow LLM Evaluate,
  RAGAs and Langfuse【716183580503338†L71-L149】.  These resources help you
  measure the performance and safety of your agents.
 - **Over sixty skeleton projects:**  The `agents` folder now contains more than sixty
  scaffolded agents covering domains such as blogging, medical imaging, music
  generation, multimodal input, news aggregation, finance, research, web
  scraping, deep research, consultancy, system design and lead generation,
  along with specialised verticals like compliance checking, marketing,
  scheduling, supply‑chain optimisation, healthcare and education.  Each
  skeleton includes a `README.md` and `main.py` to get you started without
  copying proprietary code.
- **Agent skeleton generator:**  A script at [`scripts/create_agent.py`](scripts/create_agent.py)
  that automates the creation of new agent skeletons.  Simply pass a name
  and description, and it will generate a ready‑to‑fill directory.  This
  makes it easy to scale your library of experiments.

By focusing on education, comparison and extensibility, this repository
helps you build **original, production‑ready LLM applications** rather than
simply copying existing ones.

## Top Agent Frameworks

| Framework | Description & Key Features | Stars* | Sources |
|---|---|---|---|
| **LangGraph** – [github](https://github.com/langchain-ai/langgraph) | A graph‑based extension to LangChain where each agent step is a node in a directed acyclic graph. This explicit workflow makes it easier to model multi‑step tasks, handle branching and debug flows【913044646548243†L44-L63】. | ~11.7 k | Firecrawl |
| **OpenAI Agents SDK** – [github](https://github.com/openai/agents) | Provides a structured runtime for building agents that can reason, plan and call external APIs. It uses a familiar role‑based API and integrates natively with OpenAI model endpoints【913044646548243†L64-L80】. | ~9.3 k | Firecrawl |
| **AutoGen (AG2)** – [github](https://github.com/ag2ai/ag2) | Microsoft’s event‑driven conversation framework where specialized agents chat asynchronously to solve complex tasks. Supports multi‑agent conversations, real‑time tool invocation and human‑in‑the‑loop workflows【913044646548243†L127-L147】. | ~43.6 k | Firecrawl |
| **CrewAI** – [github](https://github.com/crewAIInc/crewAI) | Role‑based orchestration where agents collaborate as a “crew.” Each agent has a distinct skillset, and the framework coordinates workflows, memory and error handling【913044646548243†L105-L125】. | ~30.5 k | Firecrawl |
| **Google ADK** – [github](https://github.com/google/agentkit) | Modular kit from Google for building agents that leverage Gemini/Vertex AI. Supports hierarchical compositions and custom tool development for customer engagement. | ~7.5 k | Firecrawl |
| **Dify** – [github](https://github.com/baichuan-inc/dify) | Low‑code platform with a drag‑and‑drop builder, built‑in retrieval‑augmented generation and function calling. Popular for quickly deploying agents without coding【710521934811195†L296-L316】. | ~93.6 k | Firecrawl |
| **LangChain & LangChain Tools** – [github](https://github.com/langchain-ai/langchain) | Comprehensive framework and tool ecosystem for chaining prompts, managing memory and integrating with numerous providers【889503799721868†L40-L48】. | ~112 k | Awesome AI Agents |
| **Smolagents** – [github](https://github.com/huggingface/smolagents) | Minimal, code‑centric agent loop from Hugging Face. Agents write and execute code directly, making it ideal for quick automation tasks without complex orchestration【913044646548243†L82-L103】. | ~22 k | Langfuse Blog |
| **Semantic Kernel** – [github](https://github.com/microsoft/semantic-kernel) | Microsoft’s .NET‑first framework for composing “skills” into full plans. Supports C#, Python and Java with enterprise‑grade security and compliance【913044646548243†L150-L169】. | ~26 k | Langfuse Blog |
| **LlamaIndex Agents** – [github](https://github.com/run-llama/llama_index) | Retrieval‑augmented agent layer built on LlamaIndex. Excels at fusing data from local or external stores into coherent answers and is ideal for data‑heavy applications【913044646548243†L171-L191】. | ~44 k | Langfuse Blog |
| **Strands Agents** – [github](https://github.com/strands-agents/sdk-python) | Model‑agnostic agent SDK that runs anywhere and supports providers like Amazon Bedrock, Anthropic, OpenAI and Ollama. Emphasizes observability with built‑in OpenTelemetry tracing【913044646548243†L194-L214】. | ~3 k | Langfuse Blog |
| **Pydantic AI** – [github](https://github.com/pydantic/pydantic-ai) | Type‑safe Python framework where you define agent inputs, outputs and tool signatures with Pydantic models. Provides FastAPI‑style developer experience and built‑in telemetry【913044646548243†L216-L232】. | ~12 k | Langfuse Blog |
| **Semantic Kernel vs LangGraph vs AutoGen** – See [Langfuse’s comparison](https://langfuse.com/blog/2025-03-19-ai-agent-comparison) for a detailed feature matrix across these frameworks【913044646548243†L236-L273】. |  |  |

\*Star counts are approximate as of July 2025 and may have changed.

## Agent Toolkits & Platforms

| Project | Description | Stars* | Sources |
|---|---|---|---|
| **AutoGPT** – [github](https://github.com/Significant-Gravitas/AutoGPT) | Comprehensive toolkit for autonomous agents, featuring Forge (agent creation), agbenchmark (performance evaluation), a leaderboard, user‑friendly UI and CLI【889503799721868†L28-L33】. | ~177k | Awesome AI Agents |
| **Ollama** – [github](https://github.com/ollama/ollama) | Tool for running large language models locally on macOS, Windows, Linux and Docker. Provides a library of models and quickstart guides【889503799721868†L35-L39】. | ~148k | Awesome AI Agents |
| **Lobe Chat** – [github](https://github.com/lobehub/lobe-chat) | Open‑source UI framework for building ChatGPT/LLM‑based chat apps. Supports speech synthesis, multi‑modal inputs and extensible plugins【889503799721868†L49-L53】. | ~64k | Awesome AI Agents |
| **OpenDevin** – [github](https://github.com/OpenDevin/OpenDevin) | Open‑source initiative aiming to replicate and enhance the autonomous AI software engineer Devin. Focuses on collaboration and complex task execution【889503799721868†L55-L59】. | ~61k | Awesome AI Agents |
| **Open Interpreter** – [github](https://github.com/OpenInterpreter/open-interpreter) | Coding agent allowing LLMs to execute code locally, with interactive and programmatic chats. Enables natural‑language interaction and control of your computer’s keyboard and mouse【889503799721868†L60-L66】. | ~60k | Awesome AI Agents |
| **MetaGPT** – [github](https://github.com/geekan/MetaGPT) | Multi‑agent framework where GPTs collaborate within a virtual software company to tackle complex tasks【889503799721868†L78-L81】. | ~58k | Awesome AI Agents |
| **PrivateGPT** – [github](https://github.com/zylon-ai/private-gpt) | Secure, offline tool for querying documents with LLMs. Offers high‑level and low‑level APIs for privacy‑conscious, context‑aware applications【889503799721868†L82-L86】. | ~56k | Awesome AI Agents |
| **GPT‑Engineer** – [github](https://github.com/gpt-engineer-org/gpt-engineer) | Converts natural‑language software specifications into executable code and supports iterative improvements【889503799721868†L92-L96】. | ~55k | Awesome AI Agents |
| **LlamaIndex Tools** – [github](https://github.com/run-llama/llama_index) | Collection of tools for building data agents, including connectors to shopping data, OpenAPI, Wikipedia, Gmail and Google Calendar【889503799721868†L107-L112】. | ~43k | Awesome AI Agents |
| **Flowise** – [github](https://github.com/FlowiseAI/Flowise) | Drag‑and‑drop interface for constructing LLM workflows. Supports Docker deployment and offers authentication, streaming and custom tool integration【889503799721868†L115-L119】. | ~42k | Awesome AI Agents |
| **FastChat** – [github](https://github.com/lm-sys/FastChat) | Platform for training, serving and evaluating LLM chatbots with distributed multi‑model support and built‑in API【889503799721868†L122-L125】. | ~39k | Awesome AI Agents |
| **Mem0** – [github](https://github.com/mem0ai/mem0) | Intelligent memory layer that enhances LLM personalization by retaining and utilizing contextual information across applications【889503799721868†L126-L129】. | ~38k | Awesome AI Agents |
| **Cal.ai** – [github](https://github.com/calcom/cal.com/tree/main/apps/ai) | AI scheduling assistant that manages email communications for booking, rearranging and rescheduling meetings using LangChain Agent Executor【889503799721868†L131-L134】. | ~37k | Awesome AI Agents |
| **Aider** – [github](https://github.com/paul-gauthier/aider) | Command‑line pair programming tool that edits local git repositories using GPT‑3.5/GPT‑4 and makes automatic git commits【889503799721868†L136-L139】. | ~36k | Awesome AI Agents |
| **Jan** – [github](https://github.com/janhq/jan) | Development‑stage ChatGPT alternative that runs fully offline across diverse hardware platforms【889503799721868†L141-L144】. | ~35k | Awesome AI Agents |

\*Star counts approximate as of July 2025.

## Starter AI Agents

These are simple, single‑purpose agents ideal for learning and quick experimentation:

| Agent | Description |
|---|---|
| **AI Blog to Podcast Agent** | Converts blog posts into engaging podcast episodes. |
| **AI Data Analysis Agent** | Performs data analysis and generates insights from structured or semi‑structured datasets. |
| **AI Travel Agent** | Plans travel itineraries with options for local or cloud execution. |
| **AI Music Generator** | Composes music pieces in various styles using generative models. |
| **AI Meme Generator (Browser)** | Generates memes by combining text and images via a browser‑controlled agent. |
| **AI Breakup Recovery Agent** | Provides compassionate advice to help users navigate breakups. |
| **AI Health & Fitness Agent** | Offers personalized health and fitness recommendations based on user goals. |
| **Gemini Multimodal Agent** | Demonstrates Gemini’s multimodal capabilities with text and image inputs. |

## Advanced AI & Domain‑Specific Agents

These sophisticated agents tackle complex tasks, often leveraging multi‑agent architectures or domain expertise:

| Agent | Description |
|---|---|
| **AI Deep Research Agent** | Conducts in‑depth research across multiple sources and compiles comprehensive reports. |
| **AI Consultant Agent** | Acts as a domain expert (e.g., marketing, engineering) to provide strategic advice. |
| **AI System Architect Agent** | Designs software or system architectures based on user requirements. |
| **AI Lead Generation Agent** | Identifies and qualifies potential leads for sales and marketing teams. |
| **AI Financial Coach Agent** | Provides personalized financial advice and investment guidance. |
| **AI Movie Production Agent** | Coordinates script development, casting suggestions and production planning. |
| **AI Journalist Agent** | Generates news articles and press releases with citations and tone analysis. |
| **AI Meeting Agent** | Summarizes meeting transcripts and extracts action items. |
| **AI Product Launch Intelligence Agent** | Analyzes market trends and competitive landscapes for new product launches. |
| **AI Social Media & Podcast Agent** | Schedules social media posts and generates podcast content for various platforms. |

## Multi‑Agent Teams

These examples show how agents can collaborate as teams, each playing a specialized role:

| Team | Description |
|---|---|
| **Competitor Intelligence Team** | Researches competitors, analyzes market positioning and synthesizes findings. |
| **Finance Agent Team** | Coordinates budgeting, forecasting and reporting tasks across multiple agents. |
| **Legal Agent Team** | Drafts, reviews and manages legal documents with compliance checks. |
| **Recruitment Agent Team** | Screens CVs, conducts preliminary interviews and ranks candidates. |
| **Real Estate Agent Team** | Assists with property searches, valuation and negotiation. |
| **Teaching Agent Team** | Develops lesson plans, delivers content and assesses learner progress. |
| **Travel Planner Agent Team** | Creates detailed travel itineraries with flights, hotels and activities. |

## Voice & Game Agents

| Agent | Description |
|---|---|
| **Voice Summary Agent** | Listens to audio, transcribes it and summarises the content. |
| **AI Audio Tour Agent** | Generates audio tours for museums, cities or landmarks. |
| **Customer Support Voice Agent** | Handles spoken customer queries, logs issues and escalates when necessary. |
| **Voice RAG Agent** | Combines voice input with retrieval‑augmented generation and speaks the answer back to the user. |
| **Tic‑Tac‑Toe Agent** | Plays tic‑tac‑toe, providing a template for autonomous game playing. |

## RAG & Memory Examples

Retrieval‑augmented generation (RAG) combines LLMs with external knowledge sources, while memory techniques allow agents to remember context across sessions.

| Example | Description |
|---|---|
| **Agentic RAG with Reasoning** | Demonstrates a RAG pipeline where the agent retrieves information, reasons over it and generates answers. |
| **Hybrid Search RAG** | Uses both vector and keyword search to improve retrieval quality. |
| **Vision RAG** | Applies RAG to visual data, retrieving relevant images or diagrams to answer questions. |
| **CRAG (Corrective RAG)** | Incorporates human feedback to correct and refine the retrieval process. |
| **Local RAG Agent** | Runs retrieval pipelines completely offline for privacy‑sensitive scenarios. |

## MCP Agent Integrations

MCP (Model Context Protocol) enables AI agents to interact with external systems securely. Here are a few examples that integrate MCP servers:

| Agent | Description |
|---|---|
| **[Browser MCP Agent](agents/browser_mcp_agent)** | Controls a web browser to perform actions like searching, clicking and form filling. |
| **[GitHub MCP Agent](agents/github_mcp_agent)** | Interacts with GitHub repositories to read, write and manage code. |
| **[Notion MCP Agent](agents/notion_mcp_agent)** | Integrates with Notion to create, update and query pages and databases. |
| **[Travel Planner MCP Agent Team](agents/travel_planner_mcp_agent_team)** | Combines MCP agents with a multi‑agent team to plan complex trips. |

## LLM Evaluation Frameworks

Evaluating LLM systems is crucial for reliable and safe applications.  We’ve summarised a number of open‑source evaluation tools in a separate document.  See the [`evaluation_frameworks/README.md`](evaluation_frameworks/README.md) for detailed descriptions and links to Promptfoo, DeepEval, MLflow LLM Evaluate, RAGAs, Deepchecks, LangSmith, TruLens, Arize Phoenix and Langfuse【716183580503338†L71-L149】.

## Example Projects

The `agents` directory contains a large number of **agent skeletons** organised by category.  To avoid duplicating code, the category folders (`starter`, `advanced`, `teams`, `rag`) now act purely as **indexes**.  Each agent lives in its own top‑level folder inside `agents/`, and the index readmes link back to the actual code.  Use these skeletons as starting points and extend them to fit your use case.

### Starter Agents

These single‑purpose agents are great for learning and quick experimentation:

 - **Summarization Agent** – [agents/summarization_agent](agents/summarization_agent): condenses long text using a local transformer model or the OpenAI API.
 - **Data Analysis Agent** – [agents/data_analysis_agent](agents/data_analysis_agent): loads CSV data, prints descriptive statistics and answers natural‑language queries via `pandasai`.
 - **Travel Itinerary Agent** – [agents/travel_itinerary_agent](agents/travel_itinerary_agent): collects trip details and assembles a synthetic itinerary.
 - **Voice Assistant Demo** – [agents/voice_agent_demo](agents/voice_agent_demo): listens to your voice, generates a reply and speaks back using `speech_recognition` and `pyttsx3`.
 - **Meme Generator Agent** – [agents/meme_generator_agent](agents/meme_generator_agent): overlays a caption onto an image template using Pillow.
 - **Health & Fitness Agent** – [agents/health_fitness_agent](agents/health_fitness_agent): calculates BMI and offers lifestyle advice.
 - **Breakup Recovery Agent** – [agents/breakup_recovery_agent](agents/breakup_recovery_agent): provides supportive messages for common breakup emotions.
 - **AI Blog to Podcast Agent** – [agents/ai_blog_to_podcast_agent](agents/ai_blog_to_podcast_agent): converts blog posts into engaging podcasts.
 - **AI Medical Imaging Agent** – [agents/ai_medical_imaging_agent](agents/ai_medical_imaging_agent): skeleton for processing and analysing medical images.
 - **AI Music Generator Agent** – [agents/ai_music_generator_agent](agents/ai_music_generator_agent): skeleton for composing music via generative models.
 - **Local News Agent** – [agents/local_news_agent](agents/local_news_agent): gathers and summarises local news articles.
 - **Gemini Multimodal Demo** – [agents/gemini_multimodal_agent_demo](agents/gemini_multimodal_agent_demo): demonstrates multimodal input processing.

### Advanced & Domain‑Specific Agents

These skeletons tackle more sophisticated tasks and can serve as foundations for domain‑specific applications:

 - **AI Deep Research Agent** – [agents/ai_deep_research_agent](agents/ai_deep_research_agent)
 - **AI Consultant Agent** – [agents/ai_consultant_agent](agents/ai_consultant_agent)
 - **AI System Architect Agent** – [agents/ai_system_architect_agent](agents/ai_system_architect_agent)
 - **AI Lead Generation Agent** – [agents/ai_lead_generation_agent](agents/ai_lead_generation_agent)
 - **AI Financial Coach Agent** – [agents/ai_financial_coach_agent](agents/ai_financial_coach_agent)
 - **AI Movie Production Agent** – [agents/ai_movie_production_agent](agents/ai_movie_production_agent)
 - **AI Product Launch Intelligence Agent** – [agents/ai_product_launch_intelligence_agent](agents/ai_product_launch_intelligence_agent)
 - **AI Journalist Agent** – [agents/ai_journalist_agent](agents/ai_journalist_agent)
 - **AI Meeting Agent** – [agents/ai_meeting_agent](agents/ai_meeting_agent)
 - **OpenAI Research Agent** – [agents/openai_research_agent](agents/openai_research_agent)
 - **Explainable AI Finance Agent** – [agents/xai_finance_agent](agents/xai_finance_agent)
 - **Web Scraping Agent** – [agents/web_scrapping_ai_agent](agents/web_scrapping_ai_agent)
 - **Document Processing Agent** – [agents/document_processing_agent](agents/document_processing_agent) – uses OCR to extract text from scanned documents or PDFs and provides a starting point for further analysis or summarisation.
 - **Sentiment Analysis Agent** – [agents/sentiment_analysis_agent](agents/sentiment_analysis_agent) – analyses the sentiment (positive, negative or neutral) of input text such as reviews or social media posts.
 - **Technical Translation Agent** – [agents/technical_translation_agent](agents/technical_translation_agent) – translates technical documents between languages while preserving domain‑specific terminology.
 - **Code Review Agent** – [agents/code_review_agent](agents/code_review_agent) – scans source code, runs linters or static analysis tools and uses an LLM to generate human‑readable suggestions for improvements.
 - **Research Synthesizer Agent** – [agents/research_synthesizer_agent](agents/research_synthesizer_agent) – retrieves information from multiple sources and synthesises a coherent report, demonstrating retrieval‑augmented generation patterns.

### Multi‑Agent Teams

These examples demonstrate how multiple agents can collaborate:

 - **Multi‑Agent Team Demo** – [agents/multi_agent_team](agents/multi_agent_team)
 - **Mixture of Agents Demo** – [agents/mixture_of_agents](agents/mixture_of_agents)
 - **Competitor Intelligence Team** – [agents/ai_competitor_intelligence_agent_team](agents/ai_competitor_intelligence_agent_team)
 - **Finance Agent Team** – [agents/ai_finance_agent_team](agents/ai_finance_agent_team)
 - **Teaching Agent Team** – [agents/ai_teaching_agent_team](agents/ai_teaching_agent_team)

### Retrieval‑Augmented Generation

 - **RAG Document QA** – [agents/rag_doc_qa](agents/rag_doc_qa): basic pipeline that indexes local documents and answers questions using a summariser.

These skeletons are intentionally simple and rely solely on open‑source libraries.  Build upon them by integrating additional frameworks, tools or APIs to create full‑fledged applications.  If you need to generate a new skeleton quickly, use the helper script in [`scripts/create_agent.py`](scripts/create_agent.py).

## Interactive Demos & Resources

Beyond code skeletons, this repository provides interactive demonstrations and resources to help you learn and showcase LLM capabilities without writing code.

### Web apps

- **Streamlit Summariser** – [`web_apps/streamlit_summarizer`](web_apps/streamlit_summarizer): a user‑friendly summarisation tool that anyone can run locally.  Enter text, click **Summarise** and see the results instantly.
- **Gradio FAQ Bot** – [`web_apps/gradio_faq_bot`](web_apps/gradio_faq_bot): an interactive chatbot that answers common questions about this repository.  Ideal for onboarding new users.

### Jupyter notebooks

- **Getting Started Notebook** – [`notebooks/getting_started.ipynb`](notebooks/getting_started.ipynb): an introductory notebook that demonstrates loading the sample dataset and performing basic analysis.  You can run it via JupyterLab or VS Code to explore the data interactively.

## Datasets & Design Assets

To support data‑driven examples and make the project visually engaging, we include:

- **Sample datasets** – [`datasets/sample_products.csv`](datasets/sample_products.csv) provides fictitious product data that you can use with the data analysis agent.  See [`datasets/README.md`](datasets/README.md) for details and guidelines for adding new datasets.
- **Design resources** – [`design/architecture_diagram.png`](design/architecture_diagram.png) offers a high‑level diagram of an agent system.  Use it in presentations or documentation.  See [`design/README.md`](design/README.md) for more information.

## Documentation & Roadmap

The project includes comprehensive documentation beyond this README.  Explore the following resources:

- **Best practices** – [`docs/best_practices.md`](docs/best_practices.md) summarises expert advice on promoting and maintaining open source projects【806548062083687†L501-L509】【806548062083687†L539-L551】.
- **Framework comparison** – [`docs/framework_comparison.md`](docs/framework_comparison.md) delves deeper into the strengths and trade‑offs of each agent framework【913044646548243†L64-L80】【913044646548243†L150-L169】.
- **Evaluation frameworks guide** – [`evaluation_frameworks/README.md`](evaluation_frameworks/README.md) reviews tools for assessing LLM agents【716183580503338†L71-L149】.
- **Tutorials** – [`tutorials/quickstart.md`](tutorials/quickstart.md) helps you get up and running with the examples and explains how to use the agent generator.
- **Roadmap** – [`docs/roadmap.md`](docs/roadmap.md) outlines future enhancements and long‑term vision for this repository.
- **Changelog** – [`CHANGELOG.md`](CHANGELOG.md) lists new features and improvements in each release.

## Complete Applications

While skeletons are great starting points, it’s also helpful to see fully functional programs.  The `complete_apps` directory
contains finished applications built on top of the ideas in this repository:

- **Task Planner** – [`complete_apps/task_planner`](complete_apps/task_planner): a command‑line tool for managing tasks with due dates, listing them in order of urgency and summarising your workload.
- **Health Coach** – [`complete_apps/health_coach`](complete_apps/health_coach): an interactive console program that calculates BMI, estimates caloric needs and offers basic fitness advice.

These examples show how you can evolve a simple skeleton into a polished product without external dependencies.

## Beginner’s Guide

If you’re new to large language models or coding, start with the **Beginner’s Guide** located at [`docs/beginners_guide.md`](docs/beginners_guide.md).  It explains what agents are, suggests ways to explore the project without writing code, and
points to the right resources for when you’re ready to dive deeper.


## Tutorials & Learning Resources

Beyond code skeletons, this repository offers **hands‑on tutorials** that walk you
through building real applications.  Each tutorial lives in the
[`tutorials/`](tutorials) directory and includes high‑level explanations,
code examples and links to relevant skeleton agents.

### RAG Tutorials

Learn how to implement retrieval‑augmented generation (RAG) pipelines.  The
[`rag_tutorials`](tutorials/rag_tutorials) folder explains what RAG is,
shows how to index documents, and demonstrates agents that retrieve data
before answering questions.

### Memory Apps Tutorials

The [`memory_apps`](tutorials/memory_apps) tutorials teach you how to add
state and context to your agents.  You’ll explore different memory types
(buffer, summarising, vector‑store memory) and see examples of agents that
retain conversation history across sessions.

### Chat with X Tutorials

Want to chat with a GitHub repo, your email inbox or a PDF?  The
[`chat_with_x_tutorials`](tutorials/chat_with_x_tutorials) directory
illustrates how to build conversational interfaces over diverse data
sources by combining retrieval, summarisation and memory.

### LLM Fine‑Tuning Tutorials

Fine‑tuning adapts a base model to your specific domain.  The
[`fine_tuning_tutorials`](tutorials/fine_tuning_tutorials) directory covers
when and how to fine‑tune models, discusses techniques like LoRA and PEFT
and points to resources for running your own experiments.

## Other educational spaces

In addition to tutorials, we provide a variety of learning resources:

- **Interactive demos & notebooks:**  Web apps and Jupyter notebooks in
  [`web_apps`](web_apps) and [`notebooks`](notebooks) let you test agents
  without writing code.
- **Datasets & design assets:**  Sample datasets and architecture diagrams
  under [`datasets`](datasets) and [`design`](design) support data‑driven
  exploration and visual explanation.
- **Evaluation frameworks:**  Our [evaluation frameworks guide](evaluation_frameworks/README.md)
  summarises tools to measure your agents’ performance and safety.
- **Complete applications:**  Finished projects in [`complete_apps`](complete_apps)
  show how to evolve a skeleton into a full product.
- **LLM ecosystem overview:**  A high‑level guide
  [`ecosystem/overview.md`](ecosystem/overview.md)
  synthesises research & training frameworks, generative AI tools,
  productionisation, local inference, LLM operations and interpretability
  into one coherent narrative【577320243189096†L247-L267】【244354101175071†L253-L307】.

## Unique features

Several aspects distinguish this repository from other collections of LLM
apps:

- **Educational focus:**  Detailed tutorials (RAG, memory, chat with X,
  fine‑tuning) complement over sixty scaffolded agents, so you can learn
  by doing rather than copying opaque code.
- **Framework comparison & guidance:**  A comparative analysis of leading
  agent frameworks with star counts, strengths and trade‑offs helps you
  choose the right tool【913044646548243†L276-L296】.
- **Agent skeleton generator:**  A helper script (`scripts/create_agent.py`) lets
  you spin up new agents quickly, encouraging experimentation and reuse.
- **Evaluation toolbox:**  We summarise state‑of‑the‑art evaluation
  frameworks like Promptfoo, DeepEval and RAGAs, and provide guidelines on
  choosing one【716183580503338†L71-L149】.
- **Community‑driven roadmap:**  The [roadmap](docs/roadmap.md) lays out
  planned features and invites community input.

  - **Ecosystem breadth:**  Unlike many curated lists that focus narrowly on
    agents or tools, this repository now includes a holistic ecosystem
    overview covering training frameworks, AI tools, production pipelines,
    local inference, operations and interpretability (see
    `ecosystem/overview.md`).  Our aim is to be a one‑stop
    resource for builders across the LLM stack.

- **Voice & game agents:**  In addition to text‑centric examples,
  the repository includes skeletons for voice summarisation, audio tours,
  customer support voice bots, voice‑enabled RAG and autonomous game playing.

## Languages & multilingual support

The primary language of this repository is English.  However, we believe that
developers around the world should be able to learn from and contribute to
this project in their native language.  To that end we maintain a
[Translation & Localization Guide](TRANSLATION.md) that explains how to add
translations of README files and documentation into other languages.

If you’d like to help translate the documentation, please open an issue or
pull request following the steps in the translation guide.  We also include a
**Technical Translation Agent** skeleton in the `agents/technical_translation_agent`
directory that can serve as a starting point for localising your own projects.

## Other curated lists & resources

In addition to the examples and tutorials contained here, there are many other
open‑source resources in the LLM ecosystem.  We maintain a summary of
complementary "awesome lists" under [`resources/awesome_lists`](resources/awesome_lists/README.md).
These external repositories focus on specific aspects of the LLM stack and are
worth exploring for broader context:

- **Awesome‑LLM** – a curated list of research papers, tools and courses for
  training and deploying large language models【353244841090028†L254-L258】.
- **awesome‑ai‑tools** – a collection of generative AI tools and services
  spanning text, code, images and video【725796767296810†L255-L266】.
- **awesome‑production‑llm** – focuses on the tooling needed to run LLMs in
  production, from data pipelines and fine‑tuning to evaluation and serving【577320243189096†L247-L267】.
- **awesome‑llm‑agents** – aggregates agent frameworks such as CrewAI,
  LangChain, AutoGen and Llama Index, highlighting their strengths and
  multi‑agent capabilities【759911502420073†L257-L331】.
- **awesome‑local‑llm** – collects platforms and engines for running
  models locally without cloud dependencies【411141313589789†L249-L276】.
- **awesome‑llmops** – compiles tools for LLM operations (LLMOps) including
  model hosting, security, evaluation and monitoring【244354101175071†L253-L307】.
- **awesome‑llm‑interpretability** – lists papers, tools and communities
  dedicated to understanding and interpreting LLMs【209448133516183†L249-L252】.

These lists complement our focus on agent development by covering topics such as
model training, deployment, operations and interpretability.  Referencing them
helps you see where our project fits in the wider landscape and underscores
our commitment to transparent, community‑driven curation.



## Choosing the Right Framework

Selecting an agent framework depends on several factors beyond star counts.  Based on the Langfuse comparison article, consider the following variables when evaluating frameworks【913044646548243†L276-L296】:

- **Task complexity & workflow structure:**  Simple automations may work best with minimal loops like **Smolagents**, whereas complex, multi‑step workflows benefit from explicit graph‑based orchestration (**LangGraph**) or skill‑based plans (**Semantic Kernel**).
- **Collaboration & multi‑agent needs:**  Multi‑agent projects (e.g. planner‑researcher‑writer) require frameworks that support asynchronous conversation and role delegation. **AutoGen** and **CrewAI** shine for these scenarios【913044646548243†L105-L125】【913044646548243†L127-L147】.
- **Integrations & ecosystem:**  If your agents need deep integration with certain providers or enterprise systems, choose a framework aligned with that ecosystem—**OpenAI Agents SDK** for the OpenAI stack, **Google ADK** for Gemini/Vertex AI, **Strands Agents** for multi‑provider flexibility or **Semantic Kernel** for .NET and Azure environments【913044646548243†L64-L80】【913044646548243†L150-L169】【913044646548243†L194-L214】.
- **Type safety & developer experience:**  Projects requiring strict type definitions and reliable validation may benefit from **Pydantic AI**, which offers a FastAPI‑style developer experience and automatic schema generation【913044646548243†L216-L232】.

These guidelines will help you match your project’s requirements with the most suitable agent framework.

## Contributing

We welcome contributions of new projects, frameworks, agents or tutorials! Please open an issue or pull request with a short description and link. When adding a project, please ensure it is licensed permissively (MIT, Apache 2.0, etc.) and that its documentation is clear and helpful.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Maintainer

This repository is curated and maintained by **Sayed Allam** ([oxbshw](https://github.com/oxbshw)).  If you find it useful, please consider starring the repository and opening issues or pull requests with your feedback.  Contributions are welcome from the community!
