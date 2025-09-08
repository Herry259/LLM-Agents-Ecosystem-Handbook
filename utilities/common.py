"""Common helper functions for examples.

This module defines small utility functions that can be imported by example
agents.  Keeping helpers in a single place avoids duplication and makes it
easier to maintain shared logic.
"""

from typing import Iterable, List


def chunk_text(text: str, max_tokens: int = 500) -> List[str]:
    """Split a long string into chunks of at most `max_tokens` words.

    Args:
        text: The input text to split.
        max_tokens: Approximate number of words per chunk.

    Returns:
        A list of substrings, each containing up to `max_tokens` words.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunk = " ".join(words[i : i + max_tokens])
        chunks.append(chunk)
    return chunks


def flatten(iterables: Iterable[Iterable]) -> List:
    """Flatten one level of nesting from a list of iterables."""
    return [item for sub in iterables for item in sub]