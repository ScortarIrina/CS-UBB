import unittest
from src.domain.entities import Student
from src.services.students_service import StudentService


class StudentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_service = StudentService()

    def tearDown(self) -> None:
        pass

    def test_add_new_student(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        self.assertEqual(len(self._student_service.get_list_of_students()), 1)

    def test_generate_students(self):
        self._student_service.generate_students()
        self.assertEqual(len(self._student_service.get_list_of_students()), 10)

    def test_get_list_of_students(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Irina', '916')
        self._student_service.add_new_student(student2.id, student2.name, student2.group)
        self.assertEqual(len(self._student_service.get_list_of_students()), 2)

    def test_get_student_by_id(self):
        self.assertEqual(self._student_service.get_student_by_id(1), None)

    def test_id_not_unique(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        self.assertTrue(self._student_service.id_not_unique(student2.id))

    def test_remove_student_by_id(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        self._student_service.remove_student_by_id('1')
        self.assertEqual(len(self._student_service.get_list_of_students()), 0)

    def test_update_name(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        self._student_service.update_name('1', 'Ana')
        student = self._student_service.get_student_by_id('1')
        self.assertEqual(student.name, 'Ana')

    def test_update_group(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        self._student_service.update_group('1', '912')
        student = self._student_service.get_student_by_id('1')
        self.assertEqual(student.group, '912')
