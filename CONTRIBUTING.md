# Contributing Guidelines

Thank you for your interest in contributing!  This repository is a curated list of projects and resources for building Large Language Model (LLM) applications and agent frameworks.  We welcome contributions that make the list more comprehensive, accurate and useful.

## What to Contribute

- **New projects or frameworks:** If you know of an open‑source LLM app, agent framework or toolkit that isn’t listed here, feel free to submit it.  Please provide a short description and link to the project.
- **Updates:** Star counts and descriptions change over time.  If you notice outdated information, outdated links or outdated star counts, please open a pull request to update them.  Use the GitHub API or project page to verify approximate stars.
- **Tutorials and examples:** You can add new categories (e.g. "Chat with X" or "Fine‑tuning tutorials") or contribute examples that showcase best practices, retrieval‑augmented generation or memory management.
- **Corrections:** If you spot mistakes (typos, formatting, factual errors), please fix them.

## How to Contribute

1. **Open an issue:** Before making a large addition or change, please open an issue to discuss your proposal.  This helps maintainers understand your ideas and avoid duplication.
2. **Fork the repository:** Create a personal copy of this repo on GitHub.
3. **Create a branch:** Make your changes in a new branch off of `main`.
4. **Include citations:** When adding factual claims (e.g., star counts or feature descriptions), cite a reliable source.  For GitHub star counts, it’s acceptable to reference the project’s GitHub API endpoint.  For feature descriptions, link to documentation or articles.
5. **Submit a pull request:** Describe your changes clearly and reference any related issues.  The maintainers will review and merge it.

## Generating new agent skeletons

To maintain consistency across agents, you can generate a new agent skeleton using the helper script in [`scripts/create_agent.py`](scripts/create_agent.py).  Run the script with `--name` and `--description` arguments to create a new subdirectory under `agents/` with a pre‑populated `README.md` and `main.py`.

## Code of Conduct

Please be respectful and follow the principles of open and inclusive collaboration.  Harassment or abusive behaviour will not be tolerated.  For detailed expectations and enforcement procedures, see our local [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the MIT License, just like the rest of this repository.