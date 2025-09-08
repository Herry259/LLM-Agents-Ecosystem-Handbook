# Retrieval‑Augmented Generation (RAG) Tutorials

Retrieval‑augmented generation combines language models with external
knowledge sources to improve accuracy and reduce hallucinations.  These
tutorials outline how to build RAG pipelines using the skeletons in this
repository and common open‑source tools.

## What you will learn

- The basics of retrieval‑augmented generation and why it matters.
- How to index your own documents and query them during inference.
- Integrating retrieval steps into agent workflows for more grounded
  answers.

## Example skeletons

You can start experimenting with RAG using the following example agents:

- **[`rag_doc_qa`](../../agents/rag_doc_qa)** – indexes local documents and answers
  questions using a summariser.  Demonstrates a simple RAG pipeline where
  passages are fetched, ranked and merged into a consolidated answer.
- **[`research_synthesizer_agent`](../../agents/research_synthesizer_agent)** –
  retrieves information from multiple sources and synthesises a coherent report.
  Modify this skeleton to plug in your own vector store or search API.
- **[`knowledge_graph_builder_agent`](../../agents/knowledge_graph_builder_agent)** –
  extracts entities and relations from text and could be combined with RAG to
  enrich answers with structured knowledge.

## Tools & resources

To implement RAG pipelines you might explore frameworks such as
LangChain, LlamaIndex or custom vector stores.  See the
[`docs/best_practices.md`](../../docs/best_practices.md) for guidance on
choosing the right components.