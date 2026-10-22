
"""NumPy array properties, indexing, and slicing."""

import numpy as np
from dataset import get_dataset


def inspect_array(marks: np.ndarray) -> dict:
    """Return essential information about a marks array."""
    return {
        "shape": marks.shape,
        "dimensions": marks.ndim,
        "size": marks.size,
        "data_type": str(marks.dtype),
    }


def demonstrate_indexing(
    students: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
) -> dict:
    """Demonstrate row, column, slice, and individual-cell access."""
    if marks.shape != (len(students), len(subjects)):
        raise ValueError("Dataset dimensions do not match.")

    hira_index = np.flatnonzero(students == "Hira")
    cs_index = np.flatnonzero(subjects == "CS")

    if len(hira_index) == 0 or len(cs_index) == 0:
        raise ValueError("Hira or CS is missing from the dataset.")

    return {
        "sara_row": marks[students == "Sara"][0].copy(),
        "math_column": marks[:, subjects == "Math"].ravel().copy(),
        "first_three_last_two": marks[:3, -2:].copy(),
        "hira_cs_mark": float(marks[hira_index[0], cs_index[0]]),
    }


def run_array_basics() -> dict:
    """Run all basic array demonstrations."""
    students, subjects, marks = get_dataset()

    return {
        "properties": inspect_array(marks),
        "indexing": demonstrate_indexing(students, subjects, marks),
    }
