
"""Filtering, grading, and ranking operations."""

import numpy as np
from statistics_analysis import assign_grade


def analyze_filters(
    students: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
) -> dict:
    """Return useful filters and student rankings."""
    if marks.ndim != 2 or marks.shape != (len(students), len(subjects)):
        raise ValueError("Invalid dataset dimensions.")

    if marks.size == 0 or not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be non-empty and finite.")

    averages = np.mean(marks, axis=1)
    top_index = int(np.argmax(averages))
    ranking_indices = np.argsort(averages)[::-1]

    above_75 = students[averages > 75].tolist()
    has_subject_below_50 = students[np.any(marks < 50, axis=1)].tolist()
    all_subjects_above_80 = students[np.all(marks > 80, axis=1)].tolist()

    grades = {
        str(student): assign_grade(float(avg))
        for student, avg in zip(students, averages)
    }

    ranking = [
        {
            "rank": rank,
            "student": str(students[index]),
            "average": round(float(averages[index]), 2),
            "grade": grades[str(students[index])],
        }
        for rank, index in enumerate(ranking_indices, start=1)
    ]

    return {
        "average_above_75": above_75,
        "has_subject_below_50": has_subject_below_50,
        "all_subjects_above_80": all_subjects_above_80,
        "topper": {
            "name": str(students[top_index]),
            "average": round(float(averages[top_index]), 2),
        },
        "grades": grades,
        "ranking": ranking,
    }
