# Data Analysis Agent

This example demonstrates how to perform **lightweight data analysis** on a CSV dataset using Python.  
It is inspired by the *AI Data Analysis Agent* category but uses only open‑source tools so that you can run it locally without proprietary dependencies.  
The script supports two modes:

1. **Descriptive statistics:** Quickly load a CSV file and print summary statistics (column types, means, counts, missing values) using only `pandas`.  
2. **Natural‑language queries:** If you have the [`pandasai`](https://github.com/pandas-ai/pandas-ai) package and an LLM API key available, you can ask questions about your data in plain English.  The agent will leverage an LLM to interpret the query and run the appropriate `pandas` operations.

> **Note:** This example is original work and does not reuse code from other repositories.  It is provided as a starting point—you are encouraged to extend it for your own datasets and models.

## Setup

Clone this repository and navigate to the `agents/data_analysis_agent` directory.  Then install the required dependencies:

```bash
pip install pandas
pip install pandasai==1.*  # optional, only needed for natural‑language queries
pip install openai         # optional, used by pandasai if you supply an OpenAI API key
```

If you plan to use the natural‑language query mode with an LLM provider, set the appropriate environment variables.  For example, for OpenAI you must set `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY=sk-...
```

Alternatively, `pandasai` also supports locally hosted models via Hugging Face; see its documentation for details.

## Usage

To analyse a CSV file and print descriptive statistics:

```bash
python main.py --csv_path path/to/your/data.csv
```

To ask a natural‑language question about the data:

```bash
python main.py --csv_path path/to/your/data.csv --question "Which country has the highest GDP?"
```

The script will detect whether `pandasai` and an API key are available and fall back to simple heuristics if not.  See the in‑line comments in `main.py` for more details.

## Example Dataset

For quick experimentation, you can download a sample dataset such as the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) or any CSV file of your choice.  Save it locally and pass the path via `--csv_path`.

## Extending the Agent

- Integrate with **[LangChain](https://github.com/langchain-ai/langchain)** to compose queries and tool calls.  
- Use **[pandas-profiling](https://github.com/pandas-profiling/pandas-profiling)** to generate HTML reports.  
- Connect to a database (PostgreSQL, SQLite, etc.) instead of a CSV file for larger datasets.

We look forward to seeing how you build upon this example!  Feel free to open a pull request with improvements.