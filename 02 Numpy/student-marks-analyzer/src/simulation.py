
"""Synthetic data generation and train/test splitting."""

import numpy as np


def generate_random_dataset(
    number_of_students: int = 100,
    number_of_subjects: int = 5,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate reproducible marks and student names."""
    if number_of_students < 2 or number_of_subjects < 1:
        raise ValueError("Use at least 2 students and 1 subject.")

    rng = np.random.default_rng(seed)

    marks = rng.integers(
        low=0,
        high=101,
        size=(number_of_students, number_of_subjects),
    ).astype(float)

    students = np.array(
        [f"Student_{index:03d}" for index in range(1, number_of_students + 1)]
    )

    return students, marks


def summarize_random_dataset(marks: np.ndarray) -> dict:
    """Summarize simulated marks and count students with average >= 50."""
    if marks.ndim != 2 or marks.size == 0:
        raise ValueError("Marks must be a non-empty 2D array.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be finite.")

    averages = np.mean(marks, axis=1)

    return {
        "subject_averages": np.mean(marks, axis=0),
        "subject_standard_deviations": np.std(marks, axis=0),
        "passing_students": int(np.count_nonzero(averages >= 50)),
        "failing_students": int(np.count_nonzero(averages < 50)),
        "student_count": int(marks.shape[0]),
    }


def train_test_split(
    students: np.ndarray,
    marks: np.ndarray,
    test_ratio: float = 0.20,
    seed: int = 42,
) -> dict:
    """Shuffle rows and return aligned training/testing datasets."""
    if marks.ndim != 2 or len(students) != marks.shape[0]:
        raise ValueError("Students and marks must have matching row counts.")

    if len(students) < 2:
        raise ValueError("At least two students are required.")

    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio must be between 0 and 1.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be finite.")

    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(students))

    test_size = max(1, int(round(len(students) * test_ratio)))
    test_size = min(test_size, len(students) - 1)

    test_indices = indices[:test_size]
    train_indices = indices[test_size:]

    return {
        "train_students": students[train_indices],
        "train_marks": marks[train_indices],
        "test_students": students[test_indices],
        "test_marks": marks[test_indices],
    }
