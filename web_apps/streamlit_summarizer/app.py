"""
Streamlit Summariser App
========================

This Streamlit application provides a simple web interface for summarising long passages of text.  It attempts to use a local
transformer model (BART) for summarisation and falls back to the OpenAI API if configured.  The logic is similar to the
`agents/summarization_agent` but presented in an interactive GUI suitable for non‑developers.

Running this app requires installing `streamlit` and `transformers`.  Optionally install `openai` and set the environment variable
`OPENAI_API_KEY` for cloud summarisation.
"""

import os
import streamlit as st
from typing import Optional

def summarise_text(text: str) -> str:
    """Attempt to summarise text using a local transformer, falling back to OpenAI API.

    Args:
        text: The input text to summarise.

    Returns:
        A summarised version of the text.  If summarisation fails, returns a message explaining the failure.
    """
    if not text or len(text.split()) < 5:
        return "Please enter more substantial text to summarise."

    # Try local summariser
    try:
        from transformers import pipeline
        summariser = pipeline("summarization", model="facebook/bart-large-cnn")
        result = summariser(text, max_length=60, min_length=20, do_sample=False)
        return result[0]["summary_text"]
    except Exception as e:
        # Fall back to OpenAI if configured
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return f"Local summarisation failed ({e}). Please install the model or set OPENAI_API_KEY for fallback."
        try:
            import openai
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a helpful assistant that summarises text."},
                          {"role": "user", "content": f"Summarise the following text: {text}"}],
                temperature=0.5,
                max_tokens=100,
            )
            return response.choices[0].message["content"].strip()
        except Exception as ex:
            return f"OpenAI API summarisation failed: {ex}"


def main() -> None:
    st.set_page_config(page_title="Summariser", page_icon="📝")
    st.title("📄 Text Summariser")
    st.write(
        "Enter a block of text and click **Summarise**. The app will return a short summary. "
        "It first tries to use a local transformer model and falls back to the OpenAI API if configured."
    )
    text = st.text_area("Your Text", height=300)
    if st.button("Summarise"):
        with st.spinner("Generating summary..."):
            summary = summarise_text(text)
        st.subheader("Summary")
        st.write(summary)


if __name__ == "__main__":
    main()