
"""Dataset creation and validation for the Student Marks Analyzer."""

import numpy as np
from numpy.typing import NDArray

StringArray = NDArray[np.str_]
FloatArray = NDArray[np.float64]

STUDENTS: StringArray = np.array(
    ["Ali", "Sara", "Bilal", "Hira", "Usman", "Zainab", "Omar", "Ayesha"],
    dtype=str,
)

SUBJECTS: StringArray = np.array(
    ["Math", "Physics", "Chemistry", "English", "CS"],
    dtype=str,
)

MARKS: FloatArray = np.array(
    [
        [80, 72, 65, 70, 88],
        [95, 90, 92, 85, 98],
        [60, 55, 70, 65, 58],
        [85, 78, 80, 90, 82],
        [45, 50, 40, 55, 48],
        [90, 94, 88, 92, 96],
        [70, 65, 72, 60, 75],
        [78, 82, 76, 88, 80],
    ],
    dtype=np.float64,
)


def validate_dataset(
    students: StringArray,
    subjects: StringArray,
    marks: FloatArray,
) -> None:
    """Raise ValueError if the dataset violates expected rules."""
    if students.ndim != 1 or subjects.ndim != 1:
        raise ValueError("Students and subjects must be 1D arrays.")

    if marks.ndim != 2:
        raise ValueError("Marks must be a 2D array.")

    if marks.shape != (len(students), len(subjects)):
        raise ValueError(
            "Marks shape must match the number of students and subjects."
        )

    if len(students) == 0 or len(subjects) == 0:
        raise ValueError("Students and subjects cannot be empty.")

    if len(np.unique(students)) != len(students):
        raise ValueError("Student names must be unique.")

    if len(np.unique(subjects)) != len(subjects):
        raise ValueError("Subject names must be unique.")

    if not np.all(np.isfinite(marks)):
        raise ValueError("Marks must contain only finite numbers.")

    if np.any((marks < 0) | (marks > 100)):
        raise ValueError("Marks must be between 0 and 100.")


def get_dataset() -> tuple[StringArray, StringArray, FloatArray]:
    """Return independent copies of the default dataset."""
    validate_dataset(STUDENTS, SUBJECTS, MARKS)
    return STUDENTS.copy(), SUBJECTS.copy(), MARKS.copy()
