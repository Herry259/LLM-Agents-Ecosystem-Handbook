# OpenAI Research Agent

This skeleton serves as a starting point for an **OpenAI Research Agent**.  A
fully functional version might search for academic papers, extract
relevant information and summarise it.  The current files provide a
placeholder message only.

## Setup

To parse scholarly articles you can use libraries like
[`arxiv`](https://pypi.org/project/arxiv/) or web scraping tools.  If
you integrate with OpenAI APIs, ensure you have an API key set in
your environment.

## Usage

```bash
python main.py
```

## Extending

- Use the `arxiv` API or crossref to search for papers on a topic.
- Download PDFs and extract text using `pdfminer.six` or `PyPDF2`.
- Summarise the text using a local model or OpenAI’s summarisation endpoints.