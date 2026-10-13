import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import main


class StudentManagementTests(unittest.TestCase):

    def test_save_and_load_students(self):
        with tempfile.TemporaryDirectory() as temp:
            data_dir = Path(temp)
            data_file = data_dir / "students.json"

            student_data = {
                "S101": {
                    "name": "Ravi Kumar",
                    "age": "20",
                    "course": "Python",
                    "email": "ravi@example.com"
                }
            }

            with patch.object(main, "DATA_DIR", data_dir), \
                 patch.object(main, "DATA_FILE", data_file):
                main.save_students(student_data)
                loaded = main.load_students()

            self.assertEqual(loaded, student_data)

    def test_add_student(self):
        students = {}
        inputs = ["S102", "Anu", "19", "Java", "anu@example.com"]

        with patch("builtins.input", side_effect=inputs):
            with patch.object(main, "save_students") as save:
                main.add_student(students)

        self.assertIn("S102", students)
        self.assertEqual(students["S102"]["name"], "Anu")
        save.assert_called_once()

    def test_duplicate_student_id(self):
        students = {"S101": {"name": "Ravi"}}

        with patch("builtins.input", side_effect=["S101"]):
            with patch.object(main, "save_students") as save:
                main.add_student(students)

        self.assertEqual(len(students), 1)
        save.assert_not_called()

    def test_delete_student(self):
        students = {"S101": {"name": "Ravi"}}

        with patch("builtins.input", side_effect=["S101", "y"]):
            with patch.object(main, "save_students"):
                main.delete_student(students)

        self.assertNotIn("S101", students)

    def test_search_student(self):
        students = {
            "S101": {
                "name": "Ravi Kumar",
                "age": "20",
                "course": "Python",
                "email": "ravi@example.com"
            }
        }

        with patch("builtins.input", return_value="ravi"):
            with patch("builtins.print") as output:
                main.search_student(students)

        displayed = " ".join(
            str(call) for call in output.call_args_list
        )
        self.assertIn("S101", displayed)
        self.assertIn("Ravi Kumar", displayed)


if __name__ == "__main__":
    unittest.main()
