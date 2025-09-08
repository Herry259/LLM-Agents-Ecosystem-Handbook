"""
Multi‑Agent Team Demo
---------------------

This script demonstrates a simple multi‑agent workflow with two agents:

* **Researcher** – retrieves notes about a given topic.  It first tries to
  import the `wikipedia` package; if unavailable or if the query fails, it
  falls back to a built‑in knowledge base defined in this file.  The result
  is stored in a shared memory dictionary.

* **Writer** – reads the research notes from memory and writes a short report.
  It uses a summarisation pipeline from the `transformers` library when
  available; otherwise it truncates the notes.

Agents communicate through a central Coordinator which manages the shared
memory and logs messages.  This architecture can be extended to include
additional agents and more complex coordination logic.
"""

import argparse
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

try:
    import wikipedia  # type: ignore
except ImportError:
    wikipedia = None  # type: ignore

try:
    from transformers import pipeline  # type: ignore
except ImportError:
    pipeline = None  # type: ignore


# A simple fallback knowledge base for demonstration purposes
FALLBACK_KB = {
    "Large language models": (
        "Large language models (LLMs) are neural networks with billions of parameters that"
        " can generate and understand human language.  They are trained on vast amounts"
        " of text and can be fine‑tuned for tasks like translation, summarisation, and"
        " question answering. LLMs are the foundation for many modern AI agents and"
        " conversational systems."
    ),
    "Agent collaboration": (
        "Agent collaboration involves multiple AI agents communicating and coordinating"
        " to solve tasks.  Agents may specialise in different roles, such as planning,"
        " information retrieval, and decision making.  A coordinator manages the flow"
        " of information between agents and resolves conflicts."
    ),
}


@dataclass
class Coordinator:
    memory: Dict[str, Any] = field(default_factory=dict)

    def log(self, message: str) -> None:
        print(message)

    def set_memory(self, key: str, value: Any) -> None:
        self.memory[key] = value

    def get_memory(self, key: str) -> Optional[Any]:
        return self.memory.get(key)


class Agent:
    def __init__(self, name: str, coordinator: Coordinator) -> None:
        self.name = name
        self.coordinator = coordinator

    def send(self, message: str) -> None:
        self.coordinator.log(f"[{self.name}] {message}")

    def perform_task(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ResearcherAgent(Agent):
    """Agent responsible for retrieving information about a topic."""

    def perform_task(self, topic: str) -> None:
        self.send(f"Researching topic: '{topic}'...")
        notes: Optional[str] = None
        # Try to fetch summary from Wikipedia if available
        if wikipedia is not None:
            try:
                notes = wikipedia.summary(topic, sentences=5)  # type: ignore
                self.send("Found summary on Wikipedia.")
            except Exception as exc:
                self.send(f"Wikipedia lookup failed: {exc}")
        # Fall back to built‑in knowledge base
        if not notes:
            notes = FALLBACK_KB.get(topic, "No information available.")
            self.send("Using fallback knowledge base.")
        self.coordinator.set_memory("research_notes", notes)
        self.send("Stored research notes in memory.")


class WriterAgent(Agent):
    """Agent responsible for writing a report from research notes."""

    def perform_task(self) -> None:
        notes = self.coordinator.get_memory("research_notes")
        if not notes:
            self.send("No research notes found. Cannot write a report.")
            return
        self.send("Writing report...")
        report = self.summarise(notes)
        self.coordinator.set_memory("report", report)
        self.send("Report generated and stored in memory.")
        self.send(f"\n--- Report ---\n{report}\n--- End of Report ---")

    def summarise(self, text: str, max_length: int = 200) -> str:
        """
        Summarise text using a local transformer model if available; otherwise
        return the text truncated to the given length.
        """
        if pipeline is not None:
            summariser = pipeline("summarization", model="facebook/bart-large-cnn")  # type: ignore
            try:
                summary = summariser(text, max_length=max_length, min_length=60, do_sample=False)
                return summary[0]["summary_text"]
            except Exception as exc:
                self.send(f"Summariser failed: {exc}. Returning truncated text.")
        # Fallback: truncate
        return text[:max_length] + ("..." if len(text) > max_length else "")


def main() -> None:
    parser = argparse.ArgumentParser(description="Multi‑Agent Team Demo")
    parser.add_argument("--topic", type=str, default="Large language models", help="Topic to research")
    args = parser.parse_args()

    coordinator = Coordinator()
    researcher = ResearcherAgent(name="Researcher", coordinator=coordinator)
    writer = WriterAgent(name="Writer", coordinator=coordinator)

    researcher.perform_task(topic=args.topic)
    writer.perform_task()


if __name__ == "__main__":
    main()