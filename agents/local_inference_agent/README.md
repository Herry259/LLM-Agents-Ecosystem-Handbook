# Local Inference Agent

This skeleton demonstrates how to run a large language model entirely on your
own hardware without relying on cloud APIs.  By using lightweight
implementations such as `llama‑cpp‑python` or quantised GGML models, you can
perform text generation and question answering offline.

## Purpose

Large language models are often accessed via hosted APIs, which can raise
privacy, latency and cost concerns.  A **local inference agent** allows you
to embed a model directly in your application, making it ideal for
sensitive use cases or environments with limited internet connectivity.

## Setup

1. Install the `llama‑cpp‑python` library:

   ```bash
   pip install llama‑cpp‑python
   ```

2. Download a quantised model file (e.g. `ggml‑vicuna‑7B.q4_0.bin`) and
   point the agent to the file in `main.py`.

## Usage

Run the placeholder agent to see how local inference can be wired up:

```bash
cd agents/local_inference_agent
python main.py
```

## Extending

Replace the stub in `main.py` with code that loads your chosen model via
`llama‑cpp‑python` and implements a simple prompt loop.  You can then use
this skeleton as the foundation for offline summarisation, question
answering or chat agents.