# AI Blog to Podcast Agent

This is a skeleton for an **AI Blog to Podcast Agent**.  Its goal is to take written articles
or blog posts and convert them into spoken audio episodes.  The current version
simply prints a message indicating where your logic should go.  Use this as a
starting point for building a pipeline that fetches blog content, converts
the text to speech using a library like `gtts` or `pyttsx3`, and produces a
podcast file (e.g., MP3).

## Setup

You can use `gtts` or another TTS library when you extend this agent:

```bash
pip install gtts
```

## Usage

```bash
python main.py
```

## Extending

- Fetch articles using RSS feeds or web scraping (see the Web Scrapping Agent for ideas).
- Use a text summarisation model to condense long posts before narration.
- Combine with background music and intros/outros to create a polished podcast.