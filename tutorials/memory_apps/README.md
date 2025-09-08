# Memory Apps Tutorials

Large Language Models (LLMs) can maintain *state* across interactions to deliver
more personalised and context‑aware experiences.  Memory can be as simple as
echoing back previous messages in a chat or as sophisticated as persisting
conversation history and knowledge across sessions.  This tutorial directory
introduces techniques and tools for building LLM applications with memory.

## What is memory in LLM apps?

In the context of agents, **memory** refers to mechanisms that retain
information about prior interactions and use it to influence future responses.
Without memory, an agent forgets everything between prompts.  With memory it
can:

- Recall past messages and maintain continuity in a conversation.
- Build a long‑term profile of a user or subject to provide personalised
  recommendations.
- Share state between multiple agents working on the same task.

Frameworks like **LangChain** offer built‑in memory classes such as
`ConversationBufferMemory`, `ConversationSummaryMemory` and
`VectorStoreRetrieverMemory`.  These components store previous messages,
summarise long histories or look up relevant facts from a vector store.

## How to add memory to your agent

To give your agent memory:

1. **Choose a memory type:**  For simple chatbots use a buffer memory that
   appends messages to a list.  For long conversations use a summary memory
   that keeps a running summary to avoid context window limits.
2. **Instantiate the memory:**  When constructing your agent pipeline,
   create the appropriate `Memory` object and pass it into your agent or
   chain.  For example:

   ```python
   from langchain.memory import ConversationSummaryMemory
   from langchain.chat_models import ChatOpenAI

   llm = ChatOpenAI(model="gpt-3.5-turbo")
   memory = ConversationSummaryMemory(llm=llm)
   # Now pass memory to your agent or chain
   ```
3. **Persist memory across runs:**  For multi‑session experiences, save
   memory data to a database or file.  LangChain’s `VectorStoreRetrieverMemory`
   can store messages in a vector database (e.g. FAISS) for retrieval later.
4. **Combine memory and retrieval:**  Retrieval‑augmented generation (RAG)
   and memory complement each other; memory stores personal conversation
   context, while RAG fetches external facts.  See the
   [RAG tutorials](../rag_tutorials/README.md) for more on retrieval.

## Example skeletons

Several skeleton agents in this repository demonstrate memory techniques:

- **AI Meeting Agent** – summarises meeting transcripts and keeps track
  of action items across sessions.
- **Competitor Intelligence Team** – uses a shared memory to store
  observations from multiple agents as they research competitors.
- **Research Synthesizer Agent** – combines retrieval and memory to
  produce reports without repeating the same information.

Each of these skeletons includes a `main.py` that illustrates how to
instantiate memory objects and pass them into the agent workflow.  Use them
as a starting point and experiment with different memory types.

## Tools & resources

- **LangChain Memory Docs:**  The LangChain documentation explains all the
  available memory classes and how to use them effectively.
- **LlamaIndex Persistent Memory:**  LlamaIndex can store data in
  vector databases and retrieve it later, enabling more scalable memory.
- **Mem0 Library:**  Mem0 provides a unified memory layer for LLMs and can
  personalise interactions across applications.

By incorporating memory, your agents can become more conversational,
context‑aware and user‑friendly.  Experiment with different memory
techniques and share your findings with the community!
