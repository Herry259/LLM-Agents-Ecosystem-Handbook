## Interactive notebooks

To supplement the agent templates and tutorials, this repository includes
Jupyter notebooks that demonstrate practical workflows end‑to‑end.  Notebooks
are ideal for experimenting with APIs, testing new ideas and iterating
quickly without modifying the underlying scaffolding.

### Getting started

Open `notebooks/getting_started.ipynb` in your favourite Jupyter interface
(
e.g. `jupyter lab` or VS Code).  It walks you through setting up an
environment, loading a foundation model via your preferred framework and
executing simple prompts.  You can use this as a template for future
experiments.

### Creating new notebooks

If you wish to create your own notebooks:

1. Use an existing notebook as a starting point and copy it under the
   `notebooks/` folder with a descriptive name.
2. Document each step with markdown cells so others can follow along.
3. Ensure any custom code is modular and, where possible, references
   functions or agents defined in the repository.  This keeps your
   notebooks aligned with the main codebase.
4. Feel free to open a pull request to share your experiments with the
   community!

### Linking notebooks and tutorials

The tutorials under `tutorials/` complement the notebooks.  For example,
the RAG tutorials explain how to build a retrieval‑augmented agent, while
a notebook can show the same concepts interactively.  We encourage you to
cross‑reference notebooks from tutorials or vice versa, fostering a richer
learning experience.