#!/usr/bin/env python3
"""Agent Skeleton Generator
---------------------------

This script automates the creation of new agent skeletons within the
`agents` directory of the repository.  Provide an agent name and a short
description, and the script will generate a folder containing a
`README.md` and a `main.py` with boilerplate content.

Example usage:

```bash
python scripts/create_agent.py --name "AI Gardening Agent" --description "Helps plan and track your gardening tasks."
```
"""

import argparse
from pathlib import Path
import textwrap


README_TEMPLATE = """# {name}

This directory contains the skeleton for a **{name}**.

{description}

Currently it only includes a placeholder `main.py`. Use it as a starting point to implement your agent logic.

## Usage

```bash
python main.py
```

## Extending

Describe how you would expand this agent to fulfil its purpose.
"""

MAIN_TEMPLATE = '''"""{name} (Skeleton)

Placeholder script for {name}. Replace this with your agent logic.
"""

def main():
    print("This is a placeholder for {name}. Add your code here.")

if __name__ == "__main__":
    main()
'''


def create_skeleton(name: str, description: str, examples_dir: Path, *, force: bool = False) -> None:
    """Create a new agent skeleton directory with a README and main.py.

    By default this function refuses to overwrite an existing skeleton if the
    target directory already exists and contains files.  Pass
    ``force=True`` to allow overwriting existing files.
    """
    dir_name = name.lower().replace(" ", "_")
    target = examples_dir / dir_name
    # If the directory exists and has any files and not forcing, warn and exit
    if target.exists() and any(target.iterdir()) and not force:
        print(f"Agent skeleton at {target} already exists. Use --force to overwrite.")
        return
    target.mkdir(parents=True, exist_ok=True)
    readme_content = README_TEMPLATE.format(name=name, description=description)
    (target / "README.md").write_text(textwrap.dedent(readme_content))
    main_py = MAIN_TEMPLATE.format(name=name)
    (target / "main.py").write_text(main_py)
    print(f"Agent skeleton created at {target}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a new agent skeleton.")
    parser.add_argument("--name", required=True, help="Display name of the agent.")
    parser.add_argument("--description", required=True, help="Short description of the agent.")
    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Overwrite an existing skeleton if it already exists. Without this flag, the "
            "script will refuse to overwrite non-empty directories."
        ),
    )
    args = parser.parse_args()
    examples_dir = Path(__file__).resolve().parents[1] / "agents"
    create_skeleton(args.name, args.description, examples_dir, force=args.force)


if __name__ == "__main__":
    main()