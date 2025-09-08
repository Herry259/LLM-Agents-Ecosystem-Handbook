# Multi‑Agent Team Demo

This example illustrates how multiple agents can collaborate to complete a task.  
While the [Curated LLM Apps](../../README.md) repository catalogues dozens of advanced multi‑agent applications, this demo keeps things simple so you can understand the core concepts.

We implement two agents:

1. **Researcher Agent** – gathers information about a topic by reading from a local knowledge base or, if available, using the `wikipedia` API.  
2. **Writer Agent** – takes the research notes and drafts a short report using a summariser.

A **Coordinator** orchestrates the workflow by assigning tasks and passing messages between agents.  The agents communicate via shared memory (a Python dictionary).  You can extend this pattern to more agents or more complex behaviours.

This demo is intentionally lightweight and does not rely on proprietary frameworks.  It serves as a template for building your own agent teams.

## Setup

Install dependencies (all optional):

```bash
pip install wikipedia               # optional, enables live Wikipedia queries
pip install transformers
```

The script will fall back to a local text snippet and simple summarisation if these packages are missing.

## Usage

Run the demo with a topic:

```bash
python main.py --topic "Large language models"
```

The Researcher will gather notes on the topic and store them in memory.  The Writer will then summarise the notes into a short report.  You will see the agents' messages printed to the console.

## Extending the Demo

To make this more powerful:

- Introduce additional agents such as an **Editor** or **Fact‑Checker**.
- Swap the knowledge source for your own documents or an API of your choice.
- Incorporate asynchronous execution so agents can operate in parallel.
- Persist the shared memory to a file or database.

We hope this example helps you design your own multi‑agent workflows!