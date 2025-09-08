# Breakup Recovery Agent

This example provides a compassionate **breakup recovery assistant**.  The agent
listens to the user’s feelings and offers supportive messages based on
themes it detects in the input.  It aims to demonstrate how an agent can
use simple natural‑language processing heuristics to deliver empathy.

Although it cannot replace friends, family or professional counselling,
this script shows how you might build a more advanced conversational
coach using open‑source tools and an LLM backend.

## Setup

No external dependencies are required beyond the Python standard library.
If you wish to add sentiment analysis or more sophisticated responses,
you can install packages like `nltk` or integrate an API.

## Usage

```bash
python main.py
```

The agent will prompt you to share how you’re feeling.  Enter one or more
sentences describing your emotions.  It will then respond with a
thoughtful message tailored to common breakup experiences.  Type “quit” to
exit.

## Extending the Agent

- Use a sentiment analysis library (e.g., [VADER](https://github.com/cjhutto/vaderSentiment))
  to classify emotions and adjust responses dynamically.
- Integrate with an LLM to generate customised reflections and coping
  strategies.
- Maintain session history to provide continuity across multiple
  conversations.