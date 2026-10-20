class Student:
    def __init__(self, name, marks):
        self.name = name.strip()
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["marks"])