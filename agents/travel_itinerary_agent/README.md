# Travel Itinerary Agent

This example demonstrates a simple **travel planning agent**.  It asks a few
questions about your destination and dates, then constructs a basic
itinerary using locally defined sample data.  The goal is to illustrate
how an agent might gather requirements, reason about options and produce
a user‑friendly schedule without relying on external APIs.

Unlike the fully featured travel agents in other repositories, this script
does not book flights or hotels.  Instead, it shows how to structure the
logic so you can later plug in real APIs such as Skyscanner, Expedia or
OpenWeather.  Because we respect licensing, no third‑party code is copied
from the original projects.

## Setup

No special dependencies are required beyond the Python standard library.

## Usage

Run the agent and follow the prompts:

```bash
python main.py
```

You will be asked for:

1. Your destination city (e.g., “Paris”).
2. Departure and return dates (YYYY‑MM‑DD format).
3. Preferred activities (sightseeing, museums, food, etc.).

The agent will then assemble a simple itinerary consisting of flight times,
hotel suggestions and daily activities.  All data is synthetic—feel free to
edit `main.py` to add more destinations or integrate live data sources.

## Extending the Agent

- Integrate with an airline/hotel API to fetch real availability and pricing.
- Use [OpenStreetMap](https://www.openstreetmap.org) or Google Places to suggest attractions.
- Incorporate weather forecasts using a public API such as [OpenWeatherMap](https://openweathermap.org).  
- Wrap this logic in a conversational interface using a framework like LangChain or AutoGen.