"""
Voice Assistant Demo
--------------------

This script implements a simple voice assistant.  It listens for audio
input from your microphone, transcribes it into text, generates a reply
using a basic response function (or an optional local language model),
and then speaks the answer back to you.  If voice or text‑to‑speech
libraries are unavailable, it falls back to terminal input and output.
"""

import sys

try:
    import speech_recognition as sr  # type: ignore
except ImportError:
    sr = None  # type: ignore

try:
    import pyttsx3  # type: ignore
except ImportError:
    pyttsx3 = None  # type: ignore

try:
    from transformers import pipeline  # type: ignore
except ImportError:
    pipeline = None  # type: ignore


def listen() -> str:
    """Listen for audio and return a transcribed string.  Falls back to input()."""
    if sr is None:
        return input("You: ")
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recogniser.listen(source, phrase_time_limit=5)
    try:
        return recogniser.recognize_google(audio)
    except Exception as exc:
        print(f"Speech recognition failed ({exc}). Switching to text input.")
        return input("You: ")


def speak(text: str) -> None:
    """Speak the given text if TTS is available, otherwise print it."""
    if pyttsx3 is not None:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Assistant: {text}")


def generate_reply(query: str) -> str:
    """Generate a simple reply to a user query.

    If the transformers library is available, use a small causal model to
    produce a generic continuation.  Otherwise, respond with a canned reply.
    """
    # Basic heuristic responses for common questions
    q_lower = query.lower()
    if "weather" in q_lower:
        return "I'm not connected to the internet, but I hope the weather is nice where you are!"
    if "your name" in q_lower or "who are you" in q_lower:
        return "I'm a simple voice assistant demo created with Python."
    if "time" in q_lower:
        from datetime import datetime

        return f"The current time is {datetime.now().strftime('%H:%M')}"
    # Use a language model if available to generate more interesting replies
    if pipeline is not None:
        try:
            generator = pipeline(
                "text-generation",
                model="distilgpt2",
                max_new_tokens=30,
                do_sample=True,
                temperature=0.7,
            )
            response = generator(query + "\nAssistant:", num_return_sequences=1)[0]["generated_text"]
            # Return only the generated part after the query
            return response.split("Assistant:")[-1].strip()
        except Exception:
            pass
    return "I'm sorry, I don't have an answer for that, but I'm learning!"


def main() -> None:
    print("Welcome to the Voice Assistant Demo. Ask me anything or say 'quit' to exit.")
    while True:
        user_input = listen()
        if not user_input:
            continue
        if user_input.strip().lower() in {"quit", "exit", "stop"}:
            speak("Goodbye!")
            break
        reply = generate_reply(user_input)
        speak(reply)


if __name__ == "__main__":
    main()