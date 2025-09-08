# Email Classification Agent

This skeleton provides a foundation for building agents that automatically categorise
incoming emails.  It is useful for triaging support tickets, prioritising
notifications or separating spam from legitimate messages.

## Objective

Offer a minimal structure for loading email text, extracting features and
classifying each message into predefined categories such as spam, promotion
or personal.  You can integrate classical machine learning models or
language models to improve accuracy.

## Setup

1. Install Python 3.8+ and common NLP libraries:

   ```bash
   pip install scikit-learn nltk
   ```

2. Prepare a dataset of labelled emails to train your classifier.

## Usage

Run the placeholder script to ensure the environment is configured.

```bash
python main.py
```

## Extending

Replace the placeholder code in `main.py` with logic to load emails,
vectorise them (e.g. using TF‑IDF) and feed them into a classifier or LLM.
You can also integrate email APIs such as IMAP or Gmail to fetch real
messages.
