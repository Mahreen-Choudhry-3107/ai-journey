import json
from pathlib import Path

from student import Student


class StudentStorage:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(
            parents=True, exist_ok=True
        )

    def save(self, students):
        data = [student.to_dict() for student in students]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load(self):
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open(
                "r", encoding="utf-8"
            ) as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON must contain a list.")

            return [
                Student.from_dict(item) for item in data
            ]

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise ValueError(
                f"Could not load student data: {error}"
            ) from error