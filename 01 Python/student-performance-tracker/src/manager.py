from student import Student
from performance import PerformanceAnalyzer


class StudentManager:
    def __init__(self, storage):
        self.storage = storage
        self.students = self.storage.load()

    def add_student(self, name, marks):
        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        if any(
            student.name.casefold() == name.casefold()
            for student in self.students
        ):
            raise ValueError("Student already exists.")

        if not marks:
            raise ValueError("Enter at least one mark.")

        if any(
            isinstance(mark, bool)
            or not isinstance(mark, (int, float))
            or not 0 <= mark <= 100
            for mark in marks
        ):
            raise ValueError(
                "Every mark must be between 0 and 100."
            )

        student = Student(name, marks)
        self.students.append(student)
        self.storage.save(self.students)

        return student

    def get_report(self):
        return [
            PerformanceAnalyzer.analyze(student)
            for student in self.students
        ]

    def get_topper(self):
        if not self.students:
            return None

        return max(
            self.students,
            key=lambda student:
                PerformanceAnalyzer.calculate_average(
                    student.marks
                )
        )

    def get_ranking(self):
        return PerformanceAnalyzer.rank_students(
            self.students
        )