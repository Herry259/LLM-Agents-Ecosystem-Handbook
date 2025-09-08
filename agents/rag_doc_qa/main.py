"""
RAG Document QA Example
-----------------------

This script implements a simple retrieval‑augmented generation pipeline:

1. Load plain‑text documents from a directory.
2. Split each document into overlapping chunks.
3. Embed the chunks using a SentenceTransformer model.
4. Build a FAISS index for similarity search.
5. Retrieve the most relevant chunks given a user query.
6. Summarise the retrieved text using a local summariser (BART) or fallback summariser.

The goal is to demonstrate the core components of a RAG system without
depending on proprietary services.  You can extend this example by
integrating API‑based models or additional retrieval strategies.
"""

import argparse
import glob
import os
import sys
from typing import List, Tuple

import numpy as np

# Attempt to import required packages.  Helpful error messages are provided
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    sys.stderr.write(
        "Error: sentence-transformers is not installed. Please install it via `pip install sentence-transformers`.\n"
    )
    raise

try:
    import faiss
except ImportError:
    sys.stderr.write(
        "Error: faiss is required for indexing. Install `faiss-cpu` or `faiss-gpu`.\n"
    )
    raise

try:
    from transformers import pipeline
except ImportError:
    sys.stderr.write(
        "Warning: transformers is not installed. Summaries will be truncated.\n"
    )
    pipeline = None  # type: ignore


def load_documents(directory: str) -> List[str]:
    """Load text files from a directory and return a list of their contents."""
    docs = []
    for filepath in glob.glob(os.path.join(directory, "*.txt")):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                docs.append(f.read())
        except Exception as exc:
            sys.stderr.write(f"Failed to read {filepath}: {exc}\n")
    return docs


def chunk_text(text: str, size: int = 512, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks of approximate token length `size`.

    This simplistic splitter assumes roughly one token per word and uses words
    for splitting.  Feel free to replace with a tokenizer for more accurate
    splitting.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += size - overlap
    return chunks


def build_index(chunks: List[str], model_name: str = "all-MiniLM-L6-v2") -> Tuple[faiss.IndexFlatL2, np.ndarray, SentenceTransformer]:
    """Embed chunks and build a FAISS index.  Returns the index, matrix of vectors and model."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, convert_to_numpy=True)
    # Normalize embeddings to improve cosine similarity results
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, embeddings, model


def retrieve(index: faiss.IndexFlatL2, embeddings: np.ndarray, model: SentenceTransformer, question: str, chunks: List[str], top_k: int = 3) -> List[str]:
    """Retrieve the most relevant chunks given a question."""
    q_vec = model.encode([question], convert_to_numpy=True)
    q_vec = q_vec / np.linalg.norm(q_vec, axis=1, keepdims=True)
    distances, indices = index.search(q_vec, top_k)
    retrieved = [chunks[i] for i in indices[0]]
    return retrieved


def summarise(text: str, max_length: int = 256) -> str:
    """Summarise the given text using a local model if available."""
    if pipeline is None:
        # Fallback: return truncated text
        return text[:max_length] + ("..." if len(text) > max_length else "")
    # Use a summarisation pipeline.  Using a small model keeps resource usage low.
    summariser = pipeline("summarization", model="facebook/bart-large-cnn")
    try:
        summary = summariser(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as exc:
        sys.stderr.write(f"Summarisation failed: {exc}\n")
        return text[:max_length] + ("..." if len(text) > max_length else "")


def answer_question(docs_dir: str, question: str, chunk_size: int = 512, overlap: int = 50, top_k: int = 3) -> str:
    """Load documents, build an index and answer a question."""
    documents = load_documents(docs_dir)
    if not documents:
        return "No documents found. Please place plain‑text files in the specified directory."
    all_chunks = []
    for doc in documents:
        all_chunks.extend(chunk_text(doc, size=chunk_size, overlap=overlap))
    # Build index
    index, embeddings, model = build_index(all_chunks)
    retrieved_chunks = retrieve(index, embeddings, model, question, all_chunks, top_k=top_k)
    combined_text = "\n\n".join(retrieved_chunks)
    return summarise(combined_text)


def main() -> None:
    parser = argparse.ArgumentParser(description="RAG Document QA Example")
    parser.add_argument("--docs_dir", required=True, help="Directory containing .txt documents")
    parser.add_argument("--question", required=True, help="Question to ask the documents")
    parser.add_argument("--chunk_size", type=int, default=512, help="Approximate chunk size in words")
    parser.add_argument("--overlap", type=int, default=50, help="Overlap between chunks in words")
    parser.add_argument("--top_k", type=int, default=3, help="Number of chunks to retrieve")
    args = parser.parse_args()

    answer = answer_question(args.docs_dir, args.question, args.chunk_size, args.overlap, args.top_k)
    print("Answer:\n")
    print(answer)


if __name__ == "__main__":
    main()