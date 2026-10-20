from pathlib import Path

from manager import StudentManager
from storage import StudentStorage
from performance import PerformanceAnalyzer


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "students.json"


def display_report(manager):
    reports = manager.get_report()

    if not reports:
        print("\nNo students found.")
        return

    print("\n" + "=" * 65)
    print(f"{'NAME':<15}{'AVERAGE':<12}{'GRADE':<10}{'STD DEV':<12}")
    print("=" * 65)

    for report in reports:
        print(
            f"{report['name']:<15}"
            f"{report['average']:<12.2f}"
            f"{report['grade']:<10}"
            f"{report['std_dev']:<12.2f}"
        )

    print("=" * 65)


def add_student_menu(manager):
    try:
        name = input("Student name: ").strip()

        raw_marks = input(
            "Enter marks separated by commas (e.g. 80,90,75): "
        )

        marks = [
            float(value.strip())
            for value in raw_marks.split(",")
        ]

        manager.add_student(name, marks)
        print("Student added and saved successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def show_topper(manager):
    topper = manager.get_topper()

    if topper is None:
        print("No students available.")
        return

    average = PerformanceAnalyzer.calculate_average(
        topper.marks
    )

    print(
        f"Topper: {topper.name} | "
        f"Average: {average:.2f} | "
        f"Grade: {PerformanceAnalyzer.get_grade(average)}"
    )


def show_ranking(manager):
    ranking = manager.get_ranking()

    if not ranking:
        print("No students available.")
        return

    print("\nStudent Rankings")

    for position, student in enumerate(ranking, start=1):
        average = PerformanceAnalyzer.calculate_average(
            student.marks
        )
        print(f"{position}. {student.name} - {average:.2f}")


def main():
    try:
        storage = StudentStorage(DATA_FILE)
        manager = StudentManager(storage)
    except (ValueError, OSError) as error:
        print(f"Unable to start application: {error}")
        return

    while True:
        print("\n===== STUDENT PERFORMANCE TRACKER =====")
        print("1. Add student")
        print("2. View report")
        print("3. Show topper")
        print("4. Show rankings")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student_menu(manager)

        elif choice == "2":
            display_report(manager)

        elif choice == "3":
            show_topper(manager)

        elif choice == "4":
            show_ranking(manager)

        elif choice == "5":
            print("Thank you for using the tracker!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()