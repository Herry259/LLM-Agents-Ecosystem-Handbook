# Legal Contract Summariser Agent

This skeleton provides the basis for a **Legal Contract Summariser Agent**.  Such an agent would parse lengthy legal contracts, identify key clauses (e.g. obligations, liabilities, termination) and produce concise summaries.  The current implementation simply prints a placeholder message.

## Setup

When extending this agent you may use libraries like `pdfplumber` to extract text and `spacy` or `nltk` for legal entity recognition.  Install via pip:

```bash
pip install pdfplumber spacy
```

## Usage

```bash
python main.py
```

## Extending

- Implement a parser that extracts clauses and definitions from contracts.
- Use a legal domain LLM or fine‑tuned model to summarise obligations and highlight risks.
- Provide structured output (e.g. a checklist) for faster review by legal professionals.