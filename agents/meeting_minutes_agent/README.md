# Meeting Minutes Agent

This skeleton defines a **Meeting Minutes Agent**.  It would transcribe meeting audio, summarise key points and action items, and distribute minutes to participants.  The current version prints a placeholder message.

## Setup

To implement this agent, use speech‑to‑text libraries (e.g. `whisper` or `speech_recognition`) and summarisation models.  Ensure you have appropriate recordings and permission for transcription.

## Usage

```bash
python main.py
```

## Extending

- Convert meeting recordings to text using an STT model.
- Identify decisions, action items and deadlines from the transcript.
- Format and email minutes to attendees automatically.