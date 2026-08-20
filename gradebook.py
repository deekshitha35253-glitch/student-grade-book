import json
from pathlib import Path


class Gradebook:
    def __init__(self, data_file=None):
        self.data_file = Path(data_file) if data_file else Path(__file__).with_name("data.json")
        self.data = {
            "students": {},
            "subjects": {},
            "marks": {},
        }
        self.load()

    def load(self):
        if self.data_file.exists():
            with self.data_file.open("r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.save()

    def save(self):
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

    @staticmethod
    def validate_marks(marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

    @staticmethod
    def calculate_grade(marks):
        Gradebook.validate_marks(marks)
        if marks >= 80:
            return "A"
        if marks >= 70:
            return "B"
        if marks >= 60:
            return "C"
        if marks >= 50:
            return "D"
        return "F"

    @staticmethod
    def calculate_performance(average):
        return {
            "A": "Excellent",
            "B": "Very Good",
            "C": "Good",
            "D": "Average",
            "F": "Needs Improvement",
        }[Gradebook.calculate_grade(average)]

    @staticmethod
    def mark_key(student_id, subject_id):
        return f"{student_id}:{subject_id}"

    def add_student(self, student_id, name):
        self.data["students"][student_id] = name
        self.save()
        return "Student added successfully."

    def add_subject(self, subject_id, subject_name):
        self.data["subjects"][subject_id] = subject_name
        self.save()
        return "Subject added successfully."

    def add_mark(self, student_id, subject_id, marks):
        if student_id not in self.data["students"]:
            return "Error: Student not found."
        if subject_id not in self.data["subjects"]:
            return "Error: Subject not found."
        try:
            self.validate_marks(marks)
        except ValueError:
            return "Error: Marks must be between 0 and 100."

        mark_key = self.mark_key(student_id, subject_id)
        if mark_key in self.data["marks"]:
            return "Error: Marks already recorded for this student and subject."

        self.data["marks"][mark_key] = marks
        self.save()
        grade = self.calculate_grade(marks)
        return f"Mark added successfully.\nGrade: {grade}"

    def student_marks(self, student_id):
        result = []
        for mark_key, marks in self.data["marks"].items():
            saved_student_id, subject_id = mark_key.split(":", 1)
            if saved_student_id == student_id:
                result.append((subject_id, marks))
        return result

    def report(self, student_id):
        if student_id not in self.data["students"]:
            return "Error: Student not found."

        student_name = self.data["students"][student_id]
        lines = [f"Student: {student_name}"]
        entries = self.student_marks(student_id)
        if not entries:
            lines.append("No marks recorded.")
            return "\n".join(lines)

        total = 0
        for subject_id, marks in entries:
            subject_name = self.data["subjects"].get(subject_id, subject_id)
            grade = self.calculate_grade(marks)
            lines.extend(
                [
                    f"Subject: {subject_name}",
                    f"Marks: {marks}",
                    f"Grade: {grade}",
                ]
            )
            total += marks

        count = len(entries)
        average = total / count
        lines.extend(
            [
                f"Average Marks: {average:.2f}",
                f"Performance: {self.calculate_performance(average)}",
                f"Subjects Count: {count}",
            ]
        )
        return "\n".join(lines)

    def list_students(self):
        if not self.data["students"]:
            return "No students found."
        return "\n".join(
            f"{student_id}: {name}" for student_id, name in sorted(self.data["students"].items())
        )

    def list_subjects(self):
        if not self.data["subjects"]:
            return "No subjects found."
        return "\n".join(
            f"{subject_id}: {subject_name}"
            for subject_id, subject_name in sorted(self.data["subjects"].items())
        )
