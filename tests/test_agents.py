import subprocess
import sys
from pathlib import Path


def test_ai_deep_research_agent_runs() -> None:
    """Ensure that the AI Deep Research agent runs with a query without errors."""
    script_path = (
        Path(__file__).resolve().parents[1]
        / "agents"
        / "ai_deep_research_agent"
        / "main.py"
    )
    result = subprocess.run(
        [sys.executable, str(script_path), "--query", "test topic"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "preparing a deep research report" in result.stdout.lower()


def test_task_planner_summarise_runs() -> None:
    """Ensure that the task planner CLI summarises without errors."""
    script_path = (
        Path(__file__).resolve().parents[1]
        / "complete_apps"
        / "task_planner"
        / "main.py"
    )
    # call summarise on tasks; first add a test task to ensure output is not empty
    subprocess.run(
        [sys.executable, str(script_path), "add", "--task", "test task", "--due", "2100-01-01"],
        capture_output=True,
        text=True,
    )
    result = subprocess.run(
        [sys.executable, str(script_path), "summarise"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "task" in result.stdout.lower()