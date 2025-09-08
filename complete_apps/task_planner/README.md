# Task Planner

The **Task Planner** is a fully working command‑line application built atop the ideas in this repository.  It demonstrates how to
evolve an agent skeleton into a complete tool.  The planner stores tasks with due dates, displays them in order of urgency and
provides a summary of pending work.

## Features

* **Add tasks** with a description and optional due date.
* **List tasks** sorted by due date, with overdue items highlighted.
* **Summarise tasks** using the summarisation function from the `utilities` module.  This condenses all task descriptions into a short overview.

## Running the planner

1. Install dependencies:

   ```bash
   pip install python-dateutil
   ```

2. Run the program:

   ```bash
   python main.py add --task "Write project proposal" --due 2025-09-10
   python main.py list
   python main.py summarise
   ```

3. Tasks are stored in `tasks.json` in the same folder.  Feel free to edit this file manually or script additions.

## Implementation notes

This application uses standard Python libraries and a small helper function `chunk_text` from `utilities/common.py` to summarise
task descriptions.  It does not require any external API keys.  The program structure illustrates how to move from a skeleton
example to a real application, making the repository valuable for both developers and curious beginners.