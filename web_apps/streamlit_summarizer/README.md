# Streamlit Summarizer App

This example demonstrates how to build a simple text summarization web application using [Streamlit](https://streamlit.io/).  It provides a user‑friendly interface that anyone can use to quickly summarise long passages of text without writing any code.

## How it works

The app accepts a block of text from the user and attempts to produce a concise summary.  It first tries to use a local Hugging Face transformer model (e.g. `facebook/bart‑large‑cnn`) to generate the summary.  If the model is not available locally, it falls back to using the OpenAI API as described in the [`summarization_agent`](../../agents/summarization_agent/README.md).  This dual strategy allows users to run the app entirely offline or with cloud support.

## Running the app

1. **Install dependencies**:

   ```bash
   pip install streamlit transformers
   # Optional: to use the OpenAI API fallback
   pip install openai
   ```

2. **Launch the app**:

   From the root of this repository, run:

   ```bash
   streamlit run web_apps/streamlit_summarizer/app.py
   ```

3. **Interact**:

   In your browser, paste or type the text you want to summarise and click **Summarise**.  The summary will appear below the text box.  If the summarisation fails (e.g. no model available), an informative error message will guide you.

## Extending this example

This is just a starting point.  You can extend the app to support multiple languages, allow file uploads, or integrate with other agent frameworks from this repository.  See the [tutorials](../../tutorials/quickstart.md) for tips on installing models and using the agent generator.

## Sources

The design of this app was inspired by the need to make NLP tools accessible to non‑technical users, as emphasised in discussions on promoting open source projects【806548062083687†L501-L509】.  By providing a clean web interface, we make summarisation approachable for everyone.