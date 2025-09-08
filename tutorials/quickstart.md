# Quick Start: Running Your First Agent

This tutorial guides you through running a basic agent from this repository in just a few steps.  We’ll use the **Summarization Agent** as an example.

## 1. Clone the repository

```bash
git clone https://github.com/your‑username/curated_llm_apps.git
cd curated_llm_apps
```

## 2. Navigate to the agent folder

Our starter agents live under the top‑level `agents` folder.  For the summarisation example:

```bash
cd agents/summarization_agent
```

## 3. Set up a virtual environment (optional but recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install dependencies

Each example lists its optional dependencies in its `README.md`.  For summarization, you may install `transformers` to run a local model:

```bash
pip install transformers
```

If you plan to use OpenAI’s API instead, install the OpenAI package and set your `OPENAI_API_KEY` environment variable.

## 5. Run the agent

```bash
python main.py
```

The placeholder script will print a message indicating where to add your own code.  Follow the suggestions in the example’s `README.md` to implement the desired functionality.

## Next steps

Use the helper script `scripts/create_agent.py` to generate additional agent skeletons.  Refer to other examples in the `advanced`, `teams`, and `rag` folders for inspiration.