# Translation & Summarisation Agent

This skeleton introduces a **Translation & Summarisation Agent**.  It would accept a document in one language, summarise its content and optionally translate the summary into another language.  The current version prints a placeholder message.

## Setup

Use machine translation models and summarisation models (e.g. `t5` or `bart`) from the Hugging Face library.  Install required packages with `pip install transformers sentencepiece`.

## Usage

```bash
python main.py
```

## Extending

- Implement a pipeline that summarises the input text using an LLM.
- Translate the resulting summary into a target language.
- Provide a CLI or API for users to specify input and output languages.