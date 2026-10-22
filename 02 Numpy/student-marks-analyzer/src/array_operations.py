
"""Vectorized transformations using NumPy."""

import numpy as np


def apply_grace_marks(
    marks: np.ndarray,
    grace: float = 5.0,
) -> np.ndarray:
    """Add grace marks without exceeding 100."""
    if marks.ndim != 2 or not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be a finite 2D array.")

    if not np.isfinite(grace) or grace < 0:
        raise ValueError("Grace must be finite and non-negative.")

    return np.clip(marks + grace, 0, 100)


def calculate_percentages(
    marks: np.ndarray,
    maximum_marks: float = 100.0,
) -> np.ndarray:
    """Convert marks to percentages."""
    if marks.ndim != 2 or not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be a finite 2D array.")

    if not np.isfinite(maximum_marks) or maximum_marks <= 0:
        raise ValueError("Maximum marks must be positive and finite.")

    if np.any(marks < 0) or np.any(marks > maximum_marks):
        raise ValueError("Marks fall outside the allowed range.")

    return np.round((marks / maximum_marks) * 100, 2)


def standardize_subjects(marks: np.ndarray) -> np.ndarray:
    """Z-score each subject column independently."""
    if marks.ndim != 2 or marks.size == 0:
        raise ValueError("Marks must be a non-empty 2D array.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be finite.")

    column_means = np.mean(marks, axis=0)
    column_stds = np.std(marks, axis=0)

    safe_stds = np.where(column_stds == 0, 1, column_stds)
    standardized = (marks - column_means) / safe_stds

    # Constant columns become zero after standardization.
    standardized[:, column_stds == 0] = 0
    return np.round(standardized, 3)


def add_average_column(
    marks: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return marks with an appended average column and the averages."""
    if marks.ndim != 2 or marks.shape[1] == 0:
        raise ValueError("Marks must have at least one subject column.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be finite.")

    averages = np.mean(marks, axis=1, keepdims=True)
    combined = np.column_stack((marks, averages))

    return combined, averages.ravel()


def run_transformations(marks: np.ndarray) -> dict:
    """Run all supported transformations."""
    return {
        "grace_marks": apply_grace_marks(marks),
        "percentages": calculate_percentages(marks),
        "standardized": standardize_subjects(marks),
        "marks_with_average": add_average_column(marks)[0],
    }
