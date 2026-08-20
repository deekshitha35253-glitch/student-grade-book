import tempfile
import unittest
from pathlib import Path

from gradebook import Gradebook


class GradebookTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "test_data.json"
        self.gradebook = Gradebook(self.data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_grade_a(self):
        self.assertEqual(Gradebook.calculate_grade(82), "A")

    def test_grade_b(self):
        self.assertEqual(Gradebook.calculate_grade(75), "B")

    def test_grade_c(self):
        self.assertEqual(Gradebook.calculate_grade(65), "C")

    def test_grade_d(self):
        self.assertEqual(Gradebook.calculate_grade(55), "D")

    def test_grade_f(self):
        self.assertEqual(Gradebook.calculate_grade(40), "F")

    def test_invalid_high_marks(self):
        with self.assertRaises(ValueError):
            Gradebook.calculate_grade(105)

    def test_invalid_low_marks(self):
        with self.assertRaises(ValueError):
            Gradebook.calculate_grade(-5)

    def test_student_creation(self):
        message = self.gradebook.add_student("S01", "Ravi")
        self.assertEqual(message, "Student added successfully.")
        self.assertEqual(self.gradebook.data["students"]["S01"], "Ravi")

    def test_subject_creation(self):
        message = self.gradebook.add_subject("PYTHON", "Python")
        self.assertEqual(message, "Subject added successfully.")
        self.assertEqual(self.gradebook.data["subjects"]["PYTHON"], "Python")

    def test_mark_creation(self):
        self.gradebook.add_student("S01", "Ravi")
        self.gradebook.add_subject("PYTHON", "Python")
        message = self.gradebook.add_mark("S01", "PYTHON", 82)
        self.assertEqual(message, "Mark added successfully.\nGrade: A")

    def test_performance_label(self):
        self.assertEqual(Gradebook.calculate_performance(82), "Excellent")

    def test_duplicate_marks(self):
        self.gradebook.add_student("S01", "Ravi")
        self.gradebook.add_subject("PYTHON", "Python")
        self.gradebook.add_mark("S01", "PYTHON", 82)
        message = self.gradebook.add_mark("S01", "PYTHON", 90)
        self.assertEqual(message, "Error: Marks already recorded for this student and subject.")

    def test_student_report(self):
        self.gradebook.add_student("S01", "Ravi")
        self.gradebook.add_subject("PYTHON", "Python")
        self.gradebook.add_mark("S01", "PYTHON", 82)
        report = self.gradebook.report("S01")
        self.assertIn("Student: Ravi", report)
        self.assertIn("Subject: Python", report)
        self.assertIn("Marks: 82", report)
        self.assertIn("Grade: A", report)
        self.assertIn("Average Marks: 82.00", report)
        self.assertIn("Performance: Excellent", report)


if __name__ == "__main__":
    unittest.main()
