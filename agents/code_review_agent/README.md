# Code Review Agent

This skeleton introduces a **Code Review Agent**.  Its goal is to read source code files, identify potential issues (e.g. stylistic problems, security vulnerabilities) and suggest improvements.  In a complete implementation you might leverage LLMs for natural‑language explanations and tools like `pylint` or `bandit` for static analysis.  The current skeleton only prints a placeholder message.

## Setup

To extend this agent you may need packages such as:

```bash
pip install pylint bandit
```

You can also integrate with the GitHub API to fetch pull requests or commit diffs.

## Usage

```bash
python main.py
```

## Extending

- Implement a function that reads Python files from a directory and runs `pylint` or `bandit` to collect issues.
- Use an LLM (e.g. via the OpenAI API or a local model) to generate human‑readable suggestions based on the static analysis output.
- Optionally, create a CLI that accepts a repository path or integrates with GitHub to review open pull requests automatically.