# Voice Summary Agent

This skeleton demonstrates how to build an agent that listens to spoken
input, transcribes it to text and produces a concise summary.  It can
serve as the basis for voice memo applications, meeting assistants or
hands‑free note taking.

## What it does

- Listens to the microphone or loads an audio file.
- Transcribes speech into text using a speech‑to‑text model (e.g., Whisper).
- Summarises the transcript with an LLM to produce a brief overview.

## Setup

1. Install the necessary dependencies:

   ```bash
   pip install speechrecognition pydub transformers
   ```

2. (Optional) Download a local speech‑to‑text model like Whisper for offline
   transcription or use a cloud API.

## Usage

Run the agent via:

```bash
python main.py
```

The script will prompt you to either record audio from your microphone or
provide a path to an existing audio file.  It will then print a summary
placeholder; customise the summarisation logic in `main.py`.

## Extending the agent

- Integrate with the microphone for live voice notes.
- Add conversation memory so the agent can summarise multiple clips into a
  running journal.
- Connect to external services (e.g., Notion, email) to store summaries.
