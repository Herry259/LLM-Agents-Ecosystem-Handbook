# RAG Document QA

This example showcases a simple **retrieval‑augmented generation (RAG)** pipeline that you can run locally.  
RAG combines **information retrieval** with **language modelling** so that you can ask questions about your own documents and receive coherent answers.

The provided script will:

1. **Load and chunk documents** from a directory of plain‑text files.  
2. **Embed** each chunk using the [Sentence Transformers](https://www.sbert.net) library.  
3. **Build a FAISS index** for efficient similarity search.  
4. **Retrieve** the most relevant chunks for a given question.  
5. **Summarise** the retrieved text using a local summarisation model (BART) or your own LLM.

This approach is a simplified take on the RAG examples featured in other repositories, but all components here are open source and self‑contained.

## Setup

Install the required dependencies:

```bash
pip install sentence-transformers
pip install faiss-cpu  # or faiss-gpu if you have CUDA
pip install transformers
```

For larger models or better performance you may also install `torch` with GPU support.

## Usage

Place your `.txt` documents in a folder, e.g. `documents/`.  Each file should contain plain text.  Then run:

```bash
python main.py --docs_dir documents --question "What are the main topics discussed?"
```

The script will print the answer generated from the most relevant document chunks.  You can adjust the number of chunks retrieved and other parameters via command‑line options—run `python main.py -h` for details.

## Extending the Pipeline

This example is intentionally minimal.  Ideas for extensions include:

- Adding PDF parsing via `pdfplumber` or `PyPDF2` and converting the text into chunks.  
- Replacing the summariser with an API call to OpenAI, Anthropic or Gemini to improve answer quality.  
- Persisting the FAISS index to disk so that you can reuse it across sessions.  
- Integrating with frameworks like **[LangChain](https://github.com/langchain-ai/langchain)** or **[LlamaIndex](https://github.com/run-llama/llama_index)** for more sophisticated RAG pipelines.