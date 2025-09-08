# AI Deep Research Agent

This skeleton is for an **AI Deep Research Agent**.  Such an agent would
delve into multiple sources to produce a comprehensive report on a
topic.  The current implementation includes a basic CLI that accepts a
`--query` argument and prints a placeholder message describing the intended
behaviour.  It serves as a starting point for your own implementation.

## Setup

Install the project dependencies from the repository root:

```bash
pip install -r ../../requirements.txt
```

If you extend this agent to fetch external data or run language models you may need
additional packages such as `requests` or `openai`.

## Usage

Run the script with a topic to research:

```bash
python main.py --query "impact of generative AI on education"
```

The placeholder will acknowledge your query.  In a real implementation you would
replace the placeholder logic with calls to retrieval and summarisation functions.

## Extending

- Define a workflow for collecting information from credible sources.
- Use summarisation models to condense long documents.
- Organise findings into a structured report with citations.
- Handle exceptions and network failures gracefully.

For guidance on building full agents and evaluating them, see the [docs](../../docs) and
[evaluation_frameworks](../../evaluation_frameworks) directories.