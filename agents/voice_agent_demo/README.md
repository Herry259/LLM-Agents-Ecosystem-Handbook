# Voice Assistant Demo

This example illustrates how to build a minimal **voice assistant** using purely open‑source libraries.  The agent listens for your voice, sends the transcript through a simple response function, and speaks the answer back to you.

The demo attempts to use the following packages:

- **[`speech_recognition`](https://github.com/Uberi/speech_recognition)** to capture and transcribe your voice from the microphone.  
- **[`pyttsx3`](https://github.com/nateshmbhat/pyttsx3)** to convert text responses back to speech.  
- **[`transformers`](https://github.com/huggingface/transformers)** (optional) to generate slightly more natural responses using a local language model.

If any of these packages are missing or if no microphone is available, the agent will gracefully fall back to text‑based input/output in the terminal.

## Setup

Install the required dependencies (all optional):

```bash
pip install speechrecognition
pip install pyttsx3
pip install transformers
```

On Linux you may need additional audio libraries such as `portaudio` (`sudo apt-get install portaudio19-dev`) before installing `speechrecognition`.

## Usage

Run the demo with:

```bash
python main.py
```

You will see prompts indicating whether the program is listening.  Speak a question such as “What is the weather today?”  The agent will transcribe your speech, generate a simple response and speak it back.  If voice input is not available, you can type your question instead.

## Extending the Demo

- Integrate with an LLM API (OpenAI, Anthropic, etc.) to produce richer responses.  
- Use the [MCP voice agent examples](../../README.md#voice-ai-agents) as inspiration to add sentiment analysis, context memory or RAG capabilities.  
- Deploy the assistant on devices like Raspberry Pi or smart speakers.