import unittest
from src.domain.entities import Student, Assignment, Grade


class StudentTest(unittest.TestCase):
    def test_student__getters_and_setters(self):
        student = Student(1, 'Irina', 916)
        student.id = 2
        student.name = 'Ana'
        student.group = 915
        self.assertEqual(student.id, 2)
        self.assertEqual(student.name, 'Ana')
        self.assertEqual(student.group, 915)

    def test_student_str_method(self):
        student = Student(1, 'Irina', 916)
        self.assertEqual(len(str(student)), 36)


class AssignmentTest(unittest.TestCase):
    def test_assignment__getters_and_setters(self):
        assignment = Assignment(1, 'menu-driven', '2021-12-10')
        assignment.id = 2
        assignment.description = 'command-driven'
        assignment.deadline = 2021-12-12
        self.assertEqual(assignment.id, 2)
        self.assertEqual(assignment.description, 'command-driven')
        self.assertEqual(assignment.deadline, 2021-12-12)

    def test_assignment_str_method(self):
        assignment = Assignment(1, 'menu-driven', 2021-12-10)
        self.assertEqual(len(str(assignment)), 53)


class GradeTest(unittest.TestCase):
    def test_grade__getters_and_setters(self):
        grade = Grade(1, 1, 10)
        grade.assignment_id = 2
        grade.student_id = 2
        grade.grade_value = 9
        self.assertEqual(grade.assignment_id, 2)
        self.assertEqual(grade.student_id, 2)
        self.assertEqual(grade.grade_value, 9)

    def test_grade_str_method(self):
        grade = Grade(1, 1, 10)
        self.assertEqual(len(str(grade)), 54)
