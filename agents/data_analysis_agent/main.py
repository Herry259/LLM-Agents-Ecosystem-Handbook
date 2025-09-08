"""
Data Analysis Agent
===================

This script provides a basic framework for analysing a CSV dataset.
It supports two modes of operation:

1. Print descriptive statistics using only `pandas`.  This works offline and
   requires no external API keys.
2. Answer natural‑language questions about the dataset if `pandasai` and an
   LLM API key are available.  This mode leverages `pandasai.SmartDataframe`
   under the hood to interpret questions and execute the appropriate Pandas
   operations via an LLM.

The design intentionally avoids proprietary code and can be extended with
additional capabilities such as generating charts, connecting to databases or
using alternative LLM providers.
"""

import argparse
import os
import sys
from typing import Optional

try:
    import pandas as pd
except ImportError as e:
    sys.stderr.write("Error: pandas is required for this script. Please install it via `pip install pandas`.\n")
    raise


def descriptive_statistics(df: pd.DataFrame) -> None:
    """Print simple descriptive statistics for a DataFrame."""
    print("\nDataFrame summary:\n")
    print(df.info())
    print("\nFirst five rows:\n")
    print(df.head())
    print("\nDescriptive statistics (numeric columns):\n")
    print(df.describe())
    missing = df.isnull().sum()
    if missing.any():
        print("\nMissing values per column:\n")
        print(missing)


def answer_with_pandasai(df: pd.DataFrame, question: str) -> Optional[str]:
    """
    Attempt to answer a natural‑language question about a DataFrame using pandasai.

    This function will try to import pandasai and determine whether an API key is
    configured.  It returns a string answer or None if the query could not be
    processed.
    """
    try:
        from pandasai import PandasAI
        from pandasai.llm.openai import OpenAI
        from pandasai.smart_dataframe import SmartDataframe
    except ImportError:
        sys.stderr.write(
            "pandasai is not installed. Falling back to heuristic analysis.\n"
        )
        return None

    # Determine whether an API key is available.  You can also configure other
    # providers supported by pandasai, such as HuggingFaceHub.
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("PANDASAI_API_KEY")
    if not api_key:
        sys.stderr.write(
            "No API key found in environment variables (e.g. OPENAI_API_KEY). "
            "Unable to use pandasai for question answering.\n"
        )
        return None

    llm = OpenAI(api_token=api_key)
    # Wrap the DataFrame in a SmartDataframe
    smart_df = SmartDataframe(df, config={"llm": llm})
    try:
        answer = smart_df.chat(question)
    except Exception as exc:
        sys.stderr.write(f"pandasai failed to answer the question: {exc}\n")
        return None
    return answer


def heuristic_answer(df: pd.DataFrame, question: str) -> str:
    """
    Very basic fallback logic to answer simple questions about a DataFrame.

    This function parses trivial patterns (mean, max, min of a column) and
    computes the result using pandas.  It is not meant to handle complex
    queries but provides a graceful fallback when LLMs are unavailable.
    """
    import re

    question_lower = question.lower()
    # Identify the target column by finding the last word that matches a column name
    target_col = None
    for col in df.columns:
        if col.lower() in question_lower:
            target_col = col
    if target_col is None:
        return "Sorry, I couldn't identify which column you're asking about."

    if "mean" in question_lower or "average" in question_lower:
        value = df[target_col].mean()
        return f"The mean of {target_col} is {value:.3f}."
    if "max" in question_lower or "maximum" in question_lower:
        value = df[target_col].max()
        return f"The maximum of {target_col} is {value}."
    if "min" in question_lower or "minimum" in question_lower:
        value = df[target_col].min()
        return f"The minimum of {target_col} is {value}."
    if "sum" in question_lower or "total" in question_lower:
        value = df[target_col].sum()
        return f"The sum of {target_col} is {value}."
    # As a catch‑all, return column description
    return (
        f"Column {target_col} has dtype {df[target_col].dtype} and "
        f"{df[target_col].isnull().sum()} missing values."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Data Analysis Agent")
    parser.add_argument(
        "--csv_path", required=True, help="Path to the CSV file to analyse"
    )
    parser.add_argument(
        "--question",
        type=str,
        default=None,
        help="Optional natural‑language question about the data",
    )
    args = parser.parse_args()

    # Load the CSV file
    try:
        df = pd.read_csv(args.csv_path)
    except Exception as exc:
        sys.stderr.write(f"Failed to load CSV file: {exc}\n")
        return

    if args.question:
        # Attempt to answer using pandasai first
        answer = answer_with_pandasai(df, args.question)
        if answer is None:
            # Fall back to simple heuristics
            answer = heuristic_answer(df, args.question)
        print(answer)
    else:
        descriptive_statistics(df)


if __name__ == "__main__":
    main()