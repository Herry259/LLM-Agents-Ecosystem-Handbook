# Travel Planner MCP Agent Team

This example showcases a **multi‑agent team** that uses the Model Context
Protocol to coordinate travel planning.  Each sub‑agent has a distinct
responsibility (e.g., itinerary creation, booking flights/hotels, sending
emails) and they share state via memory.  MCP actions allow the agents to
interact with external services securely (e.g., booking websites, email
providers).

## Team roles

| Agent | Responsibility |
|---|---|
| Planner Agent | Gathers user preferences and outlines the trip. |
| Booking Agent | Uses MCP to book flights, hotels and activities. |
| Communication Agent | Sends confirmation emails and reminders via MCP. |

## Setup

```bash
pip install aiohttp
```

You will need MCP endpoints for interacting with booking APIs and email
services.  Configure these in `main.py`.

## Running the team

```bash
python main.py
```

The script sets up the agents and simulates a simple conversation.  Extend
the code to handle real user inputs, integrate retrieval and add memory.
