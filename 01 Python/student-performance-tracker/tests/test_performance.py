import sys
import unittest
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from student import Student
from performance import PerformanceAnalyzer


class TestPerformanceAnalyzer(unittest.TestCase):

    def test_average(self):
        self.assertAlmostEqual(
            PerformanceAnalyzer.calculate_average([80, 90, 70]),
            80.0
        )

    def test_grade_a(self):
        self.assertEqual(
            PerformanceAnalyzer.get_grade(90), "A"
        )

    def test_grade_b(self):
        self.assertEqual(
            PerformanceAnalyzer.get_grade(75), "B"
        )

    def test_grade_c(self):
        self.assertEqual(
            PerformanceAnalyzer.get_grade(60), "C"
        )

    def test_empty_marks(self):
        self.assertEqual(
            PerformanceAnalyzer.calculate_average([]), 0.0
        )

    def test_analyze_student(self):
        student = Student("Ali", [80, 90, 70])
        report = PerformanceAnalyzer.analyze(student)

        self.assertEqual(report["name"], "Ali")
        self.assertEqual(report["average"], 80.0)
        self.assertEqual(report["grade"], "B")


if __name__ == "__main__":
    unittest.main()