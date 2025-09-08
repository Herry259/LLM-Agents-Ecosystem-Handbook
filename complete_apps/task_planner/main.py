"""
Task Planner CLI
================

This script implements a simple command‑line task planner.  Users can add tasks with optional due dates, list them sorted by
deadline and summarise all tasks.  Tasks are stored persistently in a JSON file.  This example demonstrates how to build a
complete application from an agent skeleton, appealing to both developers and non‑developers.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from dateutil import parser as date_parser
from typing import List, Dict

TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks() -> List[Dict[str, str]]:
    """Load tasks from the JSON file."""
    if TASKS_FILE.exists():
        with TASKS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks: List[Dict[str, str]]) -> None:
    """Save tasks to the JSON file."""
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(description: str, due: str) -> None:
    tasks = load_tasks()
    task = {"description": description}
    if due:
        try:
            date_obj = date_parser.parse(due)
            task["due"] = date_obj.isoformat()
        except Exception:
            print(f"Warning: could not parse due date '{due}'. Saving without due date.")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {description}")


def list_tasks() -> None:
    tasks = load_tasks()
    # Sort tasks by due date; tasks without due date go last
    def sort_key(t):
        return date_parser.parse(t["due"]) if "due" in t else datetime.max
    tasks_sorted = sorted(tasks, key=sort_key)
    if not tasks_sorted:
        print("No tasks found.")
        return
    print("\nTask list:\n")
    for i, task in enumerate(tasks_sorted, 1):
        desc = task["description"]
        due = task.get("due")
        if due:
            due_date = date_parser.parse(due)
            overdue = due_date < datetime.now()
            status = "(OVERDUE)" if overdue else ""
            print(f"{i}. {desc} – due {due_date.date()} {status}")
        else:
            print(f"{i}. {desc} – no due date")


def summarise_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks to summarise.")
        return
    descriptions = [t["description"] for t in tasks]
    all_text = " ".join(descriptions)
    try:
        from utilities.common import chunk_text  # type: ignore
        # Use chunk_text to split the combined descriptions into shorter parts
        chunks = chunk_text(all_text, max_chars=200)
        summary = f"You have {len(tasks)} tasks. Topics include: " + ", ".join(
            chunk[:50].strip() for chunk in chunks
        )
        print(summary)
    except Exception:
        # Fallback: naive summarisation if utilities cannot be imported
        previews = []
        for desc in descriptions:
            preview = desc[:50].strip()
            if len(desc) > 50:
                preview += "..."
            previews.append(preview)
        summary = f"You have {len(tasks)} tasks: " + ", ".join(previews)
        print(summary)


def main():
    parser = argparse.ArgumentParser(description="Task Planner CLI")
    subparsers = parser.add_subparsers(dest="command")
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("--task", required=True, help="Task description")
    parser_add.add_argument("--due", help="Due date (e.g. 2025-09-10)")
    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_sum = subparsers.add_parser("summarise", help="Summarise all tasks")
    args = parser.parse_args()
    if args.command == "add":
        add_task(args.task, args.due)
    elif args.command == "list":
        list_tasks()
    elif args.command == "summarise":
        summarise_tasks()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()