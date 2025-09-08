# Technical Translation Agent

This skeleton provides a starting point for a **Technical Translation Agent**.  Such an agent would translate specialised documents (e.g. technical manuals, API documentation) from one language to another while preserving domain‑specific terminology.  The current version is a stub that prints a placeholder message.

## Setup

For machine translation, you can leverage pre‑trained models such as those provided by the [Helsinki NLP `OpusMT` models](https://huggingface.co/Helsinki-NLP) via the Hugging Face `transformers` library.  Install the necessary packages with:

```bash
pip install transformers sentencepiece
```

## Usage

```bash
python main.py
```

## Extending

- Choose an appropriate translation model for your source and target languages (e.g. `Helsinki-NLP/opus-mt-en-fr` for English to French).
- Implement a function that loads the model and tokeniser, translates input text and returns the output.
- Add domain terminology dictionaries or post‑processing rules to ensure technical terms are translated correctly.