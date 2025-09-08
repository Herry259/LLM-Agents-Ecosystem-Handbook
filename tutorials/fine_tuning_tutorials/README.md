# LLM Fine‑Tuning Tutorials

Fine‑tuning allows you to adapt a base language model to a specific domain
or task by training it on a curated dataset.  While large foundation
models excel at general‑purpose reasoning and generation, they may lack
nuanced knowledge of specialised fields or company‑specific terminology.
Fine‑tuning bridges this gap and enables more accurate, contextual and
efficient responses.

> **Disclaimer:** Fine‑tuning large models can be computationally expensive
> and may require access to GPUs or cloud resources.  Always verify the
> licensing terms for the model you plan to fine‑tune.

## When to fine‑tune

Consider fine‑tuning when:

- Your application needs to handle highly specialised language (legal,
  medical, technical) that base models may not understand well.
- You have proprietary data (e.g. support tickets, knowledge base) that
  cannot be shared with a public API but should inform the model.
- You need to increase reliability, reduce hallucinations or enforce
  consistent output formats.

For many use cases, retrieval‑augmented generation (RAG) suffices
without fine‑tuning.  RAG attaches relevant context to the prompt,
letting a frozen base model generate grounded answers.  See our
[RAG tutorials](../rag_tutorials/README.md) for details.

## Steps to fine‑tune a model

1. **Select a base model:**  Choose a model that aligns with your needs
   (e.g. Llama 3, Gemma 3, Mistral) and is permissively licensed.  Smaller
   models are easier to fine‑tune on consumer hardware.
2. **Prepare the dataset:**  Collect high‑quality training examples in
   the form of *instruction–response* pairs.  Clean and anonymise the
   data to protect sensitive information.
3. **Choose a method:**  You can fine‑tune full weights (requires more
   resources) or use parameter‑efficient techniques like LoRA, PEFT
   adapters or QLoRA.  Libraries such as **Transformers**, **PEFT** and
   **Axolotl** provide easy‑to‑use APIs.
4. **Train the model:**  Use a script or notebook to run the training
   loop.  Monitor metrics like loss and make sure the model isn’t
   overfitting.  For LoRA, you’ll merge the adapter into the base model
   after training.
5. **Evaluate the model:**  Test your fine‑tuned model on held‑out
   examples or real user queries.  Compare its performance against the
   original model and iterate as needed.

## Resources and examples

- **Axolotl** – A flexible fine‑tuning framework that supports LoRA,
  QLoRA and multi‑GPU training.  See the official examples for tuning
  Llama 3 and Mistral.
- **Transformers & PEFT** – Hugging Face’s libraries make it easy to
  load models, apply PEFT adapters and train them on custom datasets.
- **OpenAI/Gemini Fine‑tuning APIs** – Several providers offer
  platform‑specific APIs for customising base models, though costs and
  capabilities vary.
- **QLoRA & LoRA Papers** – Read the original research papers to understand
  the principles behind parameter‑efficient fine‑tuning.

Our repository does not include full fine‑tuning scripts, but you can
adapt the [`code_review_agent`](../../agents/code_review_agent) and
[`technical_translation_agent`](../../agents/technical_translation_agent)
skeletons as post‑fine‑tuning evaluation harnesses.  Train a model on
your domain data, then plug it into these agents to see how its
performance improves.

Fine‑tuning is a powerful technique, but it’s not always necessary.
Explore retrieval, memory and prompt engineering first—then consider
fine‑tuning for maximum performance.
