# Chat with X Tutorials

One of the most compelling use cases for large language models is allowing
users to *chat with their own data*.  Whether it’s a GitHub repository,
an email inbox, a PDF document or a YouTube video, chat‑with‑X applications
combine retrieval, summarisation and conversational interfaces to make
information easily accessible.  This directory outlines how to build such
applications and points to relevant skeletons in this repository.

## Why chat with your data?

Traditional search is often limited to keyword matching and lacks the
interactive nature of a conversation.  By enabling chat with various
sources, you can:

- **Navigate complex datasets** by asking follow‑up questions rather than
  repeatedly refining queries.
- **Extract insights** without reading the entire document or codebase.
- **Personalise responses** based on previous interactions and user
  preferences.

These benefits are especially powerful when combined with retrieval‑augmented
generation (RAG) and memory.  See our [RAG tutorials](../rag_tutorials/README.md)
and [Memory tutorials](../memory_apps/README.md) for complementary techniques.

## Building blocks

To create a chat‑with‑X app, you typically need the following components:

1. **Data ingestion:**  Load the target content (e.g. GitHub repo, PDF,
   email threads, research papers) and preprocess it.  For code or text
   documents, split them into manageable chunks.  For videos, transcribe
   audio using a service like Whisper.
2. **Indexing:**  Convert the chunks into vector embeddings using a model
   such as `text-embedding-ada-002` or `mpnet`.  Store them in a vector
   database like FAISS, Chroma or Pinecone.
3. **Retrieval:**  At query time, embed the user’s question, retrieve the
   most relevant chunks, and feed them into your LLM along with the
   conversation history.
4. **Conversation loop:**  Use a chat model (e.g. GPT‑3.5, Llama 3) to
   generate answers.  Attach follow‑up questions or memory as needed.

## Example scenarios

Although we don’t host full chat‑with‑X applications here, you can adapt
our skeletons to various data sources.  Below are guidelines for common
scenarios:

### Chat with GitHub

Use the **Code Review Agent** as a starting point.  Load the repository files
into a vector store and build a chat interface that answers questions about
code structure, documentation or potential bugs.  For example, you can
embed each file and retrieve relevant snippets when the user asks,
"What does the `main.py` in the reports generator do?"

### Chat with Email (Gmail)

Extend the **Scheduling Assistant Agent** or **Customer Support Agent** to
connect to a Gmail account via the Gmail API.  Fetch recent emails,
vectorise their contents and allow users to ask about meeting times,
travel itineraries or customer issues.  Remember to handle authentication
securely and respect privacy.

### Chat with PDFs or Research Papers

Combine the **Document Processing Agent** with our RAG pipeline to ingest
PDFs.  Use `pdfplumber` or `PyMuPDF` to extract text, chunk and embed it,
then let the user ask questions like, "Summarise the methodology section"
or "What are the key findings of this paper?"

### Chat with Substack or Blogs

Adapt the **AI Blog to Podcast Agent** to scrape Substack posts or blog
entries.  After indexing the content, the agent can summarise articles,
compare viewpoints or track author themes over time.

### Chat with YouTube Videos

Leverage the **AI Social Media & Podcast Agent** to download video
transcripts.  Use a speech‑to‑text model to transcribe the audio, then
index the transcripts for retrieval.  The chat model can answer questions
about the video content or generate highlights.

## Resources

- **LangChain Documentation:**  Guides on retrieval, vector stores and
  conversational agents.
- **LlamaIndex:**  A library for building LLM applications with indexing
  and retrieval capabilities.
- **Whisper & Speech‑to‑text Tools:**  For extracting transcripts from
  audio and video files.

By following these patterns, you can create powerful conversational
interfaces over almost any data source.  Feel free to contribute new
tutorials or skeletons to this directory!
