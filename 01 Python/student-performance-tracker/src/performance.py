from statistics import mean, pstdev


class PerformanceAnalyzer:

    @staticmethod
    def calculate_average(marks):
        if not marks:
            return 0.0
        return mean(marks)

    @staticmethod
    def get_grade(average):
        if average >= 85:
            return "A"
        elif average >= 70:
            return "B"
        return "C"

    @staticmethod
    def calculate_std_dev(marks):
        if not marks:
            return 0.0
        return pstdev(marks)

    @classmethod
    def analyze(cls, student):
        average = cls.calculate_average(student.marks)

        return {
            "name": student.name,
            "average": round(average, 2),
            "grade": cls.get_grade(average),
            "std_dev": round(
                cls.calculate_std_dev(student.marks), 2
            )
        }

    @classmethod
    def rank_students(cls, students):
        return sorted(
            students,
            key=lambda student: cls.calculate_average(
                student.marks
            ),
            reverse=True
        )