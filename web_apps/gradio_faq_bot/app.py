"""
Gradio FAQ Bot
==============

This module implements a simple FAQ chatbot using Gradio.  It presents a textbox where users can ask questions and returns
predefined answers.  If the question is not recognised, a default message is returned.  This example is intentionally simple
to illustrate how to build user‑friendly interfaces with minimal code.
"""

import gradio as gr

# A simple knowledge base mapping lowercased keywords to responses
FAQ_KB = {
    "agent frameworks": "Agent frameworks such as LangGraph, AutoGen and CrewAI provide abstractions for building multi‑step applications with LLMs.  See the table in the repository’s README for a comparison.",
    "run examples": "To run examples, navigate to the appropriate folder under 'examples' and follow the instructions in the README.  Most examples can be started with `python main.py` after installing the listed dependencies.",
    "contribute": "You can contribute by creating a new agent skeleton using the generator script under 'scripts' and submitting a pull request.  Please read CONTRIBUTING.md for guidelines.",
    "evaluation": "The project includes a guide to LLM evaluation frameworks.  Check the 'evaluation_frameworks' directory to learn more.",
}


def answer_question(query: str) -> str:
    """Return a response to the user based on the question content.

    Args:
        query: The user’s question.

    Returns:
        A response string.
    """
    if not query:
        return "Please enter a question."

    q = query.lower()
    for keyword, answer in FAQ_KB.items():
        if keyword in q:
            return answer
    return "I’m sorry, I don’t have an answer for that. Please refer to the README or CONTRIBUTING guidelines."


def main() -> None:
    iface = gr.Interface(
        fn=answer_question,
        inputs=gr.inputs.Textbox(lines=2, placeholder="Ask a question about this repository..."),
        outputs="text",
        title="FAQ Bot",
        description="Ask me questions about the curated LLM apps repository!",
    )
    iface.launch()


if __name__ == "__main__":
    main()