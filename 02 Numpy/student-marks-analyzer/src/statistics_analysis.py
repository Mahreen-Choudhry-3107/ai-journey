
"""Statistical analysis of student marks."""

import numpy as np


def validate_marks(marks: np.ndarray) -> None:
    """Validate that marks form a non-empty numeric matrix."""
    if marks.ndim != 2 or marks.size == 0:
        raise ValueError("Marks must be a non-empty 2D array.")

    if not np.issubdtype(marks.dtype, np.number):
        raise ValueError("Marks must be numeric.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must be finite.")


def calculate_statistics(
    students: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
) -> dict:
    """Calculate overall, student-wise, and subject-wise statistics."""
    validate_marks(marks)

    if marks.shape != (len(students), len(subjects)):
        raise ValueError("Dataset dimensions do not match.")

    student_avg = np.mean(marks, axis=1)
    subject_avg = np.mean(marks, axis=0)
    subject_std = np.std(marks, axis=0)
    hardest_index = int(np.argmin(subject_avg))
    easiest_index = int(np.argmax(subject_avg))

    return {
        "student_averages": dict(zip(students.tolist(), student_avg.tolist())),
        "subject_averages": dict(zip(subjects.tolist(), subject_avg.tolist())),
        "subject_std": dict(zip(subjects.tolist(), subject_std.tolist())),
        "overall_average": float(np.mean(marks)),
        "overall_median": float(np.median(marks)),
        "overall_minimum": float(np.min(marks)),
        "overall_maximum": float(np.max(marks)),
        "hardest_subject": str(subjects[hardest_index]),
        "easiest_subject": str(subjects[easiest_index]),
    }


def student_report(
    students: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
) -> list[dict]:
    """Build a detailed report for every student."""
    validate_marks(marks)

    if marks.shape != (len(students), len(subjects)):
        raise ValueError("Dataset dimensions do not match.")

    averages = np.mean(marks, axis=1)
    reports = []

    for index, student in enumerate(students):
        reports.append(
            {
                "name": str(student),
                "subject_marks": {
                    str(subject): float(mark)
                    for subject, mark in zip(subjects, marks[index])
                },
                "average": round(float(averages[index]), 2),
                "grade": assign_grade(float(averages[index])),
            }
        )

    return reports


def assign_grade(average: float) -> str:
    """Assign a grade using the project's defined thresholds."""
    if not np.isfinite(average) or not 0 <= average <= 100:
        raise ValueError("Average must be finite and between 0 and 100.")

    if average >= 85:
        return "A"
    if average >= 70:
        return "B"
    return "C"
