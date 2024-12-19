import unittest
from student import Student
from student_list import StudentList
from file_handler import load_students, save_students
import os


class TestStudentProgram(unittest.TestCase):

    def setUp(self):
        self.student1 = Student("Alice", "12345", 20, "F")
        self.student2 = Student("Bob", "67890", 22, "M")
        self.student_list = StudentList()

    def test_add_student(self):
        self.student_list.add_student(self.student1)
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "Alice")

    def test_add_student_sorting(self):
        self.student_list.add_student(self.student2)
        self.student_list.add_student(self.student1)
        self.assertEqual(self.student_list.students[0].name, "Alice")
        self.assertEqual(self.student_list.students[1].name, "Bob")

    def test_delete_student(self):
        self.student_list.add_student(self.student1)
        self.student_list.delete_student("Alice")
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        self.student_list.add_student(self.student1)
        self.student_list.update_student("Alice", phone="54321", age=21, sex="F")
        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.phone, "54321")
        self.assertEqual(updated_student.age, 21)
        self.assertEqual(updated_student.sex, "F")

    def test_load_students(self):
        test_file = "test_students.csv"
        with open(test_file, "w") as file:
            file.write("name,phone,age,sex\n")
            file.write("Alice,12345,20,F\n")
            file.write("Bob,67890,22,M\n")
        students = load_students(test_file)
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].name, "Alice")
        self.assertEqual(students[1].name, "Bob")
        os.remove(test_file)

    def test_save_students(self):
        test_file = "test_students.csv"
        self.student_list.add_student(self.student1)
        self.student_list.add_student(self.student2)
        save_students(test_file, self.student_list.students)
        with open(test_file, "r") as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 3)  # Header + 2 students
        self.assertIn("Alice,12345,20,F\n", lines)
        self.assertIn("Bob,67890,22,M\n", lines)
        os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
