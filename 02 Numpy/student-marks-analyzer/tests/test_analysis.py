
"""Unit tests for the Student Marks Analyzer."""

import sys
import unittest
from pathlib import Path

import numpy as np

# Make the src modules importable when tests run from the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from dataset import get_dataset, validate_dataset
from statistics_analysis import calculate_statistics, assign_grade
from filtering import analyze_filters
from array_operations import (
    apply_grace_marks,
    standardize_subjects,
    add_average_column,
)
from correlation import calculate_correlations, weighted_scores
from simulation import generate_random_dataset, train_test_split


class TestDataset(unittest.TestCase):
    def setUp(self):
        self.students, self.subjects, self.marks = get_dataset()

    def test_dataset_dimensions(self):
        self.assertEqual(self.marks.shape, (8, 5))
        self.assertEqual(len(self.students), 8)
        self.assertEqual(len(self.subjects), 5)

    def test_marks_are_in_valid_range(self):
        self.assertTrue(np.all((self.marks >= 0) & (self.marks <= 100)))

    def test_invalid_dataset_shape_raises_error(self):
        with self.assertRaises(ValueError):
            validate_dataset(
                np.array(["Ali", "Sara"]),
                np.array(["Math"]),
                np.array([[80, 90]]),
            )


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.students, self.subjects, self.marks = get_dataset()

    def test_overall_average(self):
        result = calculate_statistics(
            self.students, self.subjects, self.marks
        )
        self.assertAlmostEqual(
            result["overall_average"],
            float(np.mean(self.marks)),
        )

    def test_student_average_axis(self):
        result = calculate_statistics(
            self.students, self.subjects, self.marks
        )
        self.assertAlmostEqual(
            result["student_averages"]["Sara"],
            92.0,
        )

    def test_grade_thresholds(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(75), "B")
        self.assertEqual(assign_grade(60), "C")

    def test_invalid_grade_average(self):
        with self.assertRaises(ValueError):
            assign_grade(101)


class TestFilteringAndOperations(unittest.TestCase):
    def setUp(self):
        self.students, self.subjects, self.marks = get_dataset()

    def test_topper(self):
        result = analyze_filters(
            self.students, self.subjects, self.marks
        )
        self.assertEqual(result["topper"]["name"], "Sara")

    def test_grace_marks_are_capped(self):
        sample = np.array([[98.0, 100.0]])
        result = apply_grace_marks(sample, grace=5)
        np.testing.assert_array_equal(result, [[100.0, 100.0]])

    def test_standardized_columns_have_zero_mean(self):
        result = standardize_subjects(self.marks)
        np.testing.assert_allclose(
            np.mean(result, axis=0),
            np.zeros(self.marks.shape[1]),
            atol=0.002,
        )

    def test_average_column(self):
        combined, averages = add_average_column(self.marks)
        self.assertEqual(combined.shape, (8, 6))
        np.testing.assert_allclose(averages, np.mean(self.marks, axis=1))
        np.testing.assert_allclose(combined[:, -1], averages)


class TestCorrelationAndSimulation(unittest.TestCase):
    def setUp(self):
        self.students, self.subjects, self.marks = get_dataset()

    def test_correlation_matrix_shape(self):
        result = calculate_correlations(self.subjects, self.marks)
        self.assertEqual(
            result["correlation_matrix"].shape,
            (len(self.subjects), len(self.subjects)),
        )

    def test_weights_must_sum_to_one(self):
        with self.assertRaises(ValueError):
            weighted_scores(
                self.students,
                self.subjects,
                self.marks,
                weights=np.array([0.2, 0.2, 0.2, 0.2, 0.1]),
            )

    def test_random_dataset_is_reproducible(self):
        _, first = generate_random_dataset(seed=123)
        _, second = generate_random_dataset(seed=123)
        np.testing.assert_array_equal(first, second)

    def test_train_test_split(self):
        students, marks = generate_random_dataset(100, 5, seed=7)
        split = train_test_split(students, marks, test_ratio=0.2, seed=7)

        self.assertEqual(len(split["train_students"]), 80)
        self.assertEqual(len(split["test_students"]), 20)

        combined = set(split["train_students"]) | set(split["test_students"])
        self.assertEqual(combined, set(students))

        self.assertTrue(
            set(split["train_students"]).isdisjoint(
                set(split["test_students"])
            )
        )


if __name__ == "__main__":
    unittest.main()
