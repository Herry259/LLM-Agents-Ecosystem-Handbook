# Gradio FAQ Bot

This example illustrates how to create a simple question‑answering chatbot using [Gradio](https://gradio.app/).  The bot answers
frequently asked questions about this repository and its contents, making it easier for non‑technical users to navigate the project.

## Features

* Interactive web interface powered by Gradio.
* Predefined knowledge base covering common questions such as:
  - What are agent frameworks?
  - How do I run the examples?
  - How can I contribute?
* Fallback to a generic response if the question is not recognised.

## Usage

1. Install dependencies:

   ```bash
   pip install gradio
   ```

2. Run the app:

   ```bash
   python web_apps/gradio_faq_bot/app.py
   ```

3. Open the displayed link in your browser and start asking questions.

## Customisation

To tailor the bot to your project’s evolving needs, edit the dictionary in `app.py` that maps questions to answers.  You can also
enhance the bot by integrating a retrieval‑augmented generation (RAG) pipeline using the examples in the `rag` folder.

## Inspiration

Providing a gentle introduction and a curated set of answers helps on‑board new users, which is a best practice for open‑source
projects【806548062083687†L539-L551】.  This example demonstrates how to make the project more approachable for everyone.