import unittest
from src.domain.entities import Student
from src.repository.student_repository import UserExceptionStudent, StudentRepository


class StudentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentRepository()

    def tearDown(self) -> None:
        pass

    def test_repo_add_new_student(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_repo_exception__id_not_unique(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.add_new_student(student2.id, student2.name, student2.name)

    def test_repo_exception__id_not_valid(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('-3', 'Irina', '916')
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.add_new_student(student2.id, student2.name, student2.name)

    def test_repo_exception__name_is_empty(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', '', '916')
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.add_new_student(student2.id, student2.name, student2.name)

    def test_repo_exception__invalid_name(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', '123', '916')
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.add_new_student(student2.id, student2.name, student2.name)

    def test_repo_exception__invalid_group(self):
        student = Student('1', 'Irina', '1')
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.add_new_student(student.id, student.name, student.name)

    def test_id_not_unique(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        self.assertTrue(self._student_repository.id_not_unique(student2.id))

    def test_remove_student_by_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

    def test_update_name(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.update_name('1', 'Ana')
        student = self._student_repository.get_student_by_id('1')
        self.assertEqual(student.name, 'Ana')

    def test_update_name__empty_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.update_name('1', '')

    def test_update_name__invalid_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.update_name('1', '123')

    def test_update_group(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.update_group('1', '912')
        student = self._student_repository.get_student_by_id('1')
        self.assertEqual(student.group, '912')

    def test_update_group__invalid_group__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(UserExceptionStudent):
            self._student_repository.update_group('1', '1')

    def test_generate_students(self):
        self._student_repository.generate_students()
        self.assertEqual(len(self._student_repository.get_list_of_students()), 10)

    def test_get_student_by_id(self):
        self.assertEqual(self._student_repository.get_student_by_id(1), None)

    def test_repository(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        student = Student('2', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 2)
