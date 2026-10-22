
"""Correlation and weighted-score analysis."""

import numpy as np


def calculate_correlations(
    subjects: np.ndarray,
    marks: np.ndarray,
) -> dict:
    """Calculate subject correlations and the strongest pair."""
    if marks.ndim != 2 or marks.shape[1] != len(subjects):
        raise ValueError("Marks columns must match subjects.")

    if marks.shape[0] < 2 or not np.all(np.isfinite(marks)):
        raise ValueError("At least two finite observations are required.")

    stds = np.std(marks, axis=0)
    constant_columns = np.flatnonzero(stds == 0)

    # Correlation is undefined for a constant column.
    correlations = np.corrcoef(marks, rowvar=False)
    correlations = np.atleast_2d(correlations)

    # Replace undefined correlations with NaN explicitly.
    if len(constant_columns):
        correlations[constant_columns, :] = np.nan
        correlations[:, constant_columns] = np.nan

    pairs = []
    for first in range(len(subjects)):
        for second in range(first + 1, len(subjects)):
            value = correlations[first, second]
            if np.isfinite(value):
                pairs.append(
                    {
                        "subject_1": str(subjects[first]),
                        "subject_2": str(subjects[second]),
                        "correlation": round(float(value), 4),
                    }
                )

    strongest_pair = (
        max(pairs, key=lambda pair: abs(pair["correlation"]))
        if pairs
        else None
    )

    subject_correlations = {}
    for index, subject in enumerate(subjects):
        value = correlations[0, index] if index == 0 else correlations[0, index]
        subject_correlations[str(subject)] = (
            round(float(value), 4) if np.isfinite(value) else None
        )

    return {
        "correlation_matrix": correlations,
        "math_correlations": subject_correlations,
        "strongest_pair": strongest_pair,
    }


def weighted_scores(
    students: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
    weights: np.ndarray | None = None,
) -> dict:
    """Calculate weighted scores and compare with simple-average ranking."""
    if marks.ndim != 2 or marks.shape != (len(students), len(subjects)):
        raise ValueError("Dataset dimensions do not match.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be finite.")

    if weights is None:
        weights = np.array([0.30, 0.25, 0.15, 0.10, 0.20])

    weights = np.asarray(weights, dtype=float)

    if weights.shape != (len(subjects),):
        raise ValueError("There must be one weight per subject.")

    if not np.all(np.isfinite(weights)) or np.any(weights < 0):
        raise ValueError("Weights must be finite and non-negative.")

    if not np.isclose(np.sum(weights), 1.0):
        raise ValueError("Weights must add up to 1.0.")

    weighted = marks @ weights
    simple = np.mean(marks, axis=1)

    weighted_order = np.argsort(weighted)[::-1]
    simple_order = np.argsort(simple)[::-1]

    return {
        "weighted_scores": {
            str(students[i]): round(float(weighted[i]), 2)
            for i in range(len(students))
        },
        "weighted_ranking": [str(students[i]) for i in weighted_order],
        "simple_average_ranking": [str(students[i]) for i in simple_order],
        "ranking_changed": not np.array_equal(weighted_order, simple_order),
    }
