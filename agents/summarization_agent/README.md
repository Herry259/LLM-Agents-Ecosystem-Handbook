# Summarization Agent Example

This example demonstrates how to build a simple text summarization agent.  The agent accepts a block of text (for example, an article or long paragraph) and produces a concise summary.

Two implementation paths are provided:

1. **Local summarization with Hugging Face Transformers** – This option runs a pre‑trained summarization model locally.  It requires installing the `transformers` library and downloading a model (e.g. `facebook/bart-large-cnn`).  This path is suitable if you have GPU/CPU resources and prefer to avoid external APIs.
2. **API‑based summarization with OpenAI** – This option uses OpenAI’s GPT models via the `openai` Python package.  You must set an `OPENAI_API_KEY` environment variable with your API key.  It’s a quick way to get high‑quality summaries without managing models locally.

## Running the example

1. Create a virtual environment (optional) and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install openai
# optional for local summarization
pip install transformers torch
```

2. Export your OpenAI API key (if using the API version):

```bash
export OPENAI_API_KEY=sk-your-api-key
```

3. Run the script with the text you want to summarise.  You can type text interactively or pass it as a command‑line argument:

```bash
python main.py "Your long article text goes here..."
```

The script will attempt to use a local summarizer if `transformers` is installed; otherwise, it will fall back to the OpenAI API.

## Notes

- Local summarization models (e.g. BART) may be large (>400 MB).  Downloading them requires a stable internet connection.
- The OpenAI option may incur costs depending on your usage.
- This example is original and intended as a template.  Feel free to adapt it or integrate it with other frameworks like LangChain or LlamaIndex.