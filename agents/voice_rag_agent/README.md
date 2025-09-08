# Voice RAG Agent (Retrieval‑Augmented Generation)

This skeleton combines voice input with retrieval‑augmented generation.  The
agent listens to a spoken question, transcribes it, retrieves relevant
documents from a knowledge base and uses an LLM to generate a grounded
answer.  Finally, it speaks the answer back to the user.

## Workflow

1. **Speech input:**  Record a voice query using a microphone.
2. **Transcription:**  Convert the audio to text via a speech‑to‑text model.
3. **Retrieval:**  Embed the text query, search a vector store and fetch
   top‑k relevant documents.
4. **Generation:**  Send the retrieved context and query to an LLM to
   produce an answer.
5. **Speech output:**  Synthesize the answer and play it to the user.

## Setup

```bash
pip install speechrecognition pyttsx3
```

You will also need a vector store (e.g., FAISS, Chroma) and an embedding
model from `sentence-transformers` or similar.  Adjust the dependencies
according to your preferred stack.

## Usage

Run the agent with:

```bash
python main.py
```

The current implementation is a stub.  Populate the TODO sections in
`main.py` with actual speech processing, retrieval and generation logic.

## Further exploration

- Use the tutorials in [`tutorials/rag_tutorials`](../../tutorials/rag_tutorials) to
  learn how to build the retrieval pipeline.
- Explore multi‑turn dialogues by storing the conversation history in
  memory (see [`tutorials/memory_apps`](../../tutorials/memory_apps)).
