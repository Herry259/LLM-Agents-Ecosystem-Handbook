# Starter Agents

This folder acts as an **index** for the simple, single‑purpose agents in this repository.  The actual code for each agent resides at the top level of `agents/`.  Refer to the following entries for the available starter agents and what they do.

| Agent | Description |
|---|---|
| [`summarization_agent`](../summarization_agent) | Condenses long passages of text into concise summaries. |
| [`data_analysis_agent`](../data_analysis_agent) | Loads CSV data, prints descriptive statistics and answers natural‑language questions using `pandasai`. |
| [`travel_itinerary_agent`](../travel_itinerary_agent) | Collects trip details and assembles a synthetic itinerary. |
| [`voice_agent_demo`](../voice_agent_demo) | Listens to your voice, generates a reply and speaks back using `speech_recognition` and `pyttsx3`. |
| [`meme_generator_agent`](../meme_generator_agent) | Overlays a caption onto an image template using Pillow. |
| [`health_fitness_agent`](../health_fitness_agent) | Calculates BMI and offers lifestyle advice. |
| [`breakup_recovery_agent`](../breakup_recovery_agent) | Provides supportive messages for common breakup emotions. |
| [`ai_blog_to_podcast_agent`](../ai_blog_to_podcast_agent) | Converts blog posts into engaging podcast episodes. |
| [`ai_medical_imaging_agent`](../ai_medical_imaging_agent) | Skeleton for processing and analysing medical images. |
| [`ai_music_generator_agent`](../ai_music_generator_agent) | Skeleton for composing music via generative models. |
| [`local_news_agent`](../local_news_agent) | Gathers and summarises local news articles. |
| [`gemini_multimodal_agent_demo`](../gemini_multimodal_agent_demo) | Demonstrates Gemini’s multimodal capabilities with text and image inputs. |

To run any of these agents, change into its directory and execute `python main.py`.  For more information about extending an agent, read the `README.md` inside each agent’s folder.