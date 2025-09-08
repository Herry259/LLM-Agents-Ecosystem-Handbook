# Browser MCP Agent

This skeleton provides a starting point for integrating the **Model Context
Protocol (MCP)** with a web browser.  MCP allows an agent to perform
actions on external systems (such as browsers) in a controlled and
observable manner.  Use this agent to automate web searches, form filling
or navigation while maintaining safety and auditability.

## Features

- Sets up an MCP client that can send commands to a browser agent.
- Defines placeholder functions for actions like `open_url`, `click`
  and `type_text`.
- Demonstrates how to stream back observations (page content) to the
  LLM for reasoning.

## Setup

1. Install dependencies:

   ```bash
   pip install websockets aiohttp
   ```

2. Set up an MCP server or use an existing browser MCP endpoint.  This
   skeleton assumes there is a service listening for MCP messages and
   controlling a browser instance.

## Usage

Run the agent with:

```bash
python main.py
```

The script will connect to your MCP server and run a simple sequence of
actions (e.g., navigate to a URL).  Replace the placeholder actions with
your own logic, or integrate it into a larger agent pipeline.

## Extending the agent

- Implement a robust command protocol to support clicking, typing and
  scrolling.
- Integrate with the conversation loop of your agent so the LLM can
  decide which browser actions to take based on intermediate results.
- Use this skeleton as a foundation for building voice assistants or
  multi‑agent workflows that interact with websites.
