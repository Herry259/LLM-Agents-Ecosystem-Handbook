"""
Summarization Agent

This script demonstrates how to summarise text using either a local
transformers model or the OpenAI API.  It checks for an available
transformers pipeline and falls back to OpenAI if necessary.

Usage:
    python main.py "Your text to summarise"

Environment variables:
    OPENAI_API_KEY  (required for API-based summarization)
"""

import os
import sys

def summarize_with_transformers(text: str) -> str:
    """Attempt to summarise text using a local Hugging Face model.

    Requires the `transformers` library and a summarization model.
    Returns the summary or raises an ImportError if transformers
    is not available.
    """
    from transformers import pipeline  # type: ignore

    # You can change the model to any summarisation model available on the Hub.
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device=0 if os.environ.get("CUDA_VISIBLE_DEVICES") else -1,
    )
    summary = summarizer(
        text,
        max_length=130,
        min_length=30,
        do_sample=False,
    )
    return summary[0]["summary_text"]


def summarize_with_openai(text: str) -> str:
    """Summarise text using the OpenAI API.

    Requires the `openai` library and an API key in the `OPENAI_API_KEY`
    environment variable.
    """
    import openai  # type: ignore

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY environment variable is not set. Please set it to use the OpenAI API."
        )
    openai.api_key = api_key

    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


def main() -> None:
    if len(sys.argv) < 2:
        print("Please provide the text to summarise as a command-line argument.")
        sys.exit(1)
    text = sys.argv[1]

    summary = None
    # Try to use transformers first
    try:
        summary = summarize_with_transformers(text)
        print("Summary (local transformers):\n")
        print(summary)
    except ImportError:
        print("Transformers library not available; falling back to OpenAI API...")
    except Exception as exc:
        print(f"Local summarization failed: {exc}\nFalling back to OpenAI API...")

    if summary is None:
        try:
            summary = summarize_with_openai(text)
            print("Summary (OpenAI API):\n")
            print(summary)
        except Exception as exc:
            print(f"OpenAI summarization failed: {exc}")
            sys.exit(1)


if __name__ == "__main__":
    main()