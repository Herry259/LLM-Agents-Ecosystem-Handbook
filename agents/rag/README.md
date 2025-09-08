# Retrieval‑Augmented Generation (RAG)

The `rag` folder is reserved for examples that combine large language models with retrieval from external knowledge sources.  RAG techniques allow an agent to **search, retrieve and reason** over relevant documents, enhancing accuracy and grounding responses in factual data.

| Example | Description |
|---|---|
| [`rag_doc_qa`](../rag_doc_qa) | Indexes local documents and answers questions using a summariser.  This skeleton illustrates a basic RAG pipeline that fetches passages, ranks them and generates a consolidated answer. |

When building your own RAG agents, consider how to store and retrieve information efficiently (e.g., vector databases, hybrid search) and how to manage memory across conversations.  For more RAG patterns and best practices, consult the resources listed in the [Evaluation Frameworks guide](../../evaluation_frameworks/README.md).