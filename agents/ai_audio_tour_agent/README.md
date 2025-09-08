# AI Audio Tour Agent

This skeleton provides a foundation for building an audio tour guide.  The
agent takes a list of points of interest (POIs) such as museum exhibits,
historical landmarks or artwork, generates engaging descriptions using an
LLM and converts them into spoken audio.  Visitors can listen to the
narration through a mobile app or device.

## Workflow

1. **Input selection:**  Provide a list of POIs with titles and optional
   text descriptions.
2. **Description generation:**  Use an LLM to craft concise, engaging
   descriptions tailored to the audience.
3. **Speech synthesis:**  Convert the generated text to speech using a
   TTS library (e.g., `pyttsx3`, Azure TTS, ElevenLabs).
4. **Playback:**  Serve the audio files to users via a web or mobile app.

## Setup

```bash
pip install transformers pyttsx3
```

## Usage

Run the agent:

```bash
python main.py
```

The script will ask for a list of POIs and output placeholder audio prompts.
Replace the LLM and TTS integration in `main.py` with your preferred
libraries or APIs.

## Extensions

- Integrate geolocation to automatically trigger audio when a user
  approaches a POI.
- Add multilingual support for tours in different languages.
