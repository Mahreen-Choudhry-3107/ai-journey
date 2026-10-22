
"""Main entry point for the Student Marks Analyzer."""

import json
from pathlib import Path

import numpy as np

from dataset import get_dataset
from array_basics import run_array_basics
from statistics_analysis import calculate_statistics, student_report
from filtering import analyze_filters
from array_operations import run_transformations
from correlation import calculate_correlations, weighted_scores
from simulation import (
    generate_random_dataset,
    summarize_random_dataset,
    train_test_split,
)


def json_default(value):
    """Convert NumPy objects into JSON-compatible Python values."""
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"Cannot serialize {type(value).__name__}")


def print_section(title: str, data) -> None:
    """Print a readable section of the report."""
    print(f"\n{'=' * 65}")
    print(title.upper())
    print("=" * 65)
    print(json.dumps(data, indent=2, default=json_default, allow_nan=False))


def main() -> None:
    """Run all project analyses."""
    students, subjects, marks = get_dataset()

    print("STUDENT MARKS ANALYZER — NumPy Edition")
    print(f"Students: {len(students)} | Subjects: {len(subjects)}")

    # Milestone 1: Array basics
    basics = run_array_basics()
    print_section("Milestone 1 — Array Basics", basics)

    # Milestone 2: Statistical analysis
    statistics = calculate_statistics(students, subjects, marks)
    reports = student_report(students, subjects, marks)
    print_section("Milestone 2 — Statistics", statistics)
    print_section("Student Reports", reports)

    # Milestone 3: Filtering and ranking
    filters = analyze_filters(students, subjects, marks)
    print_section("Milestone 3 — Filtering and Ranking", filters)

    # Milestone 4: Transformations
    transformations = run_transformations(marks)
    print_section("Milestone 4 — Array Transformations", transformations)

    # Milestone 5: Correlation and weighted scores
    correlations = calculate_correlations(subjects, marks)
    weighted = weighted_scores(students, subjects, marks)
    print_section("Milestone 5 — Correlation", correlations)
    print_section("Weighted Scores", weighted)

    # Milestone 6: Simulation and train/test split
    random_students, random_marks = generate_random_dataset(
        number_of_students=100,
        number_of_subjects=len(subjects),
    )
    simulation = summarize_random_dataset(random_marks)
    split = train_test_split(random_students, random_marks)

    print_section("Milestone 6 — Simulation", simulation)
    print_section(
        "Train/Test Split",
        {
            "train_count": len(split["train_students"]),
            "test_count": len(split["test_students"]),
            "train_shape": split["train_marks"].shape,
            "test_shape": split["test_marks"].shape,
        },
    )

    # Save a compact summary as a JSON report.
    output_dir = Path(__file__).resolve().parent.parent / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "statistics": statistics,
        "topper": filters["topper"],
        "ranking": filters["ranking"],
        "weighted_scores": weighted["weighted_scores"],
        "strongest_correlation_pair": correlations["strongest_pair"],
        "simulation": simulation,
    }

    report_path = output_dir / "analysis_summary.json"
    report_path.write_text(
        json.dumps(
            summary,
            indent=2,
            default=json_default,
            allow_nan=False,
        ),
        encoding="utf-8",
    )

    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
