import unittest

from src.domain.Assignment import Assignment
from src.domain.Grade import Grade
from src.domain.Student import Student


#  ~~~~~~~~~~~~~~~ TESTS FOR DOMAIN ~~~~~~~~~~~~~~~
from src.repository.assignment_repo import AssignmentRepository, AssignmentRepositoryException, \
    AssignmentTextFileRepository, AssignmentBinaryFileRepository
from src.repository.grade_repo import GradeRepository, GradeRepositoryException, GradeTextFileRepository, \
    GradeBinaryFileRepository
from src.repository.student_repo import StudentRepository, StudentRepositoryException, StudentTextFileRepository, \
    StudentBinaryFileRepository
from src.services.students_service import StudentService


class StudentTest(unittest.TestCase):
    def test_student__getters_and_setters(self):
        student = Student('1', 'Irina', '916')
        student.name = 'Ana'
        student.group = 915
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, 'Ana')
        self.assertEqual(student.group, 915)

    def test_student_str_method(self):
        student = Student('1', 'Irina', 916)
        self.assertEqual(len(str(student)), 36)


class AssignmentTest(unittest.TestCase):
    def test_assignment__getters_and_setters(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        assignment.description = 'command-driven'
        assignment.deadline = 2021-12-12
        self.assertEqual(assignment.id, 1)
        self.assertEqual(assignment.description, 'command-driven')
        self.assertEqual(assignment.deadline, 2021-12-12)

    def test_assignment_str_method(self):
        assignment = Assignment(1, 'menu-driven', 2021-12-10)
        self.assertEqual(len(str(assignment)), 53)


class GradeTest(unittest.TestCase):
    def test_grade__getters_and_setters(self):
        grade = Grade(1, 1, 10)
        grade.grade_value = 9
        self.assertEqual(grade.assignment_id, 1)
        self.assertEqual(grade.student_id, 1)
        self.assertEqual(grade.grade_value, 9)

    def test_grade_str_method(self):
        grade = Grade(1, 1, 10)
        self.assertEqual(len(str(grade)), 54)


#  ~~~~~~~~~~~~~~~ TESTS FOR REPOSITORY ~~~~~~~~~~~~~~~

class StudentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentRepository()

    def tearDown(self) -> None:
        pass

    def test_repo_add_new_student(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_id_not_unique__id_not_unique__true(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        self.assertTrue(self._student_repository.id_not_unique(student2.id))

    def test_id_not_unique__id_is_unique__false(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Irina', '916')
        self.assertFalse(self._student_repository.id_not_unique(student2.id))

    def test_remove_student_by_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

    def test_update_name__valid_input__successful_update(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.update_name('1', 'Ana')
        student = self._student_repository.get_student_by_id('1')
        self.assertEqual(student.name, 'Ana')

    def test_update_name__empty_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_name('1', '')

    def test_update_name__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_name('a', 'Ana')

    def test_update_name__invalid_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
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
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_group('1', '1')

    def test_generate_students(self):
        self._student_repository.generate_student()
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_get_student_by_id__student_not_in_list__returns_none(self):
        self.assertEqual(self._student_repository.get_student_by_id(1), None)


class StudentTextFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentTextFileRepository()

    def tearDown(self) -> None:
        pass

    def test_repo_add_new_student(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_id_not_unique__id_not_unique__true(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        self.assertTrue(self._student_repository.id_not_unique(student2.id))

    def test_id_not_unique__id_is_unique__false(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Irina', '916')
        self.assertFalse(self._student_repository.id_not_unique(student2.id))

    def test_remove_student_by_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

    def test_update_name__valid_input__successful_update(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.update_name('1', 'Ana')
        student = self._student_repository.get_student_by_id('1')
        self.assertEqual(student.name, 'Ana')

    def test_update_name__empty_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_name('1', '')

    def test_update_name__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_name('a', 'Ana')

    def test_update_name__invalid_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
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
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_group('1', '1')

    def test_generate_students(self):
        self._student_repository.generate_student()
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)


class StudentBinaryFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentBinaryFileRepository()

    def tearDown(self) -> None:
        pass

    def test_repo_add_new_student(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_id_not_unique__id_not_unique__true(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        self.assertTrue(self._student_repository.id_not_unique(student2.id))

    def test_id_not_unique__id_is_unique__false(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Irina', '916')
        self.assertFalse(self._student_repository.id_not_unique(student2.id))

    def test_remove_student_by_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

    def test_update_name__valid_input__successful_update(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.update_name('1', 'Ana')
        student = self._student_repository.get_student_by_id('1')
        self.assertEqual(student.name, 'Ana')

    def test_update_name__empty_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_name('1', '')

    def test_update_name__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_name('a', 'Ana')

    def test_update_name__invalid_name__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
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
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.update_group('1', '1')

    def test_generate_students(self):
        self._student_repository.generate_student()
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_get_student_by_id__student_not_in_list__returns_none(self):
        self.assertEqual(self._student_repository.get_student_by_id(1), None)

    def test_remove_student_by_id__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('a')


class AssignmentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._assignment_repository = AssignmentRepository()

    def tearDown(self) -> None:
        pass

    def test_add_new_assignment__valid_input__successful_addition(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_id_not_unique__given_id_unique__False(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('2', 'menu-driven', '2021-12-10')
        self.assertFalse(self._assignment_repository.id_not_unique(assignment2.id))

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._assignment_repository.get_assignment_by_id(1), None)

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(str(self._assignment_repository.get_assignment_by_id(1)), str(assignment))

    def test_remove_assignment_by_id__assignment_in_list__successful_removal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.remove_assignment_by_id('1')
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 0)

    # def test_remove_assignment_by_id__invalid_id__raises_exception(self):
    #     assignment = Assignment('1', 'menu-driven', '2021-12-10')
    #     self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
    #     with self.assertRaises(UserExceptionAssignment):
    #         self._assignment_repository.remove_assignment_from_assignments_by_id('-1')

    def test_update_description__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_description(1, 'command-driven')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.description, 'command-driven')

    def test_update_description__empty_description__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(AssignmentRepositoryException):
            self._assignment_repository.update_description('1', '')

    def test_update_deadline__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_deadline('1', '2021-12-15')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.deadline, '2021-12-15')

    def test_generate_assignments(self):
        self._assignment_repository.generate_assignments()
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_repository(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        assignment = Assignment('2', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 2)


class AssignmentTextFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._assignment_repository = AssignmentTextFileRepository()

    def tearDown(self) -> None:
        pass

    def test_add_new_assignment__valid_input__successful_addition(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_id_not_unique__given_id_unique__False(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('2', 'menu-driven', '2021-12-10')
        self.assertFalse(self._assignment_repository.id_not_unique(assignment2.id))

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._assignment_repository.get_assignment_by_id(1), None)

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(str(self._assignment_repository.get_assignment_by_id(1)), str(assignment))

    def test_remove_assignment_by_id__assignment_in_list__successful_removal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.remove_assignment_by_id('1')
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 0)

    def test_update_description__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_description(1, 'command-driven')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.description, 'command-driven')

    def test_update_description__empty_description__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(AssignmentRepositoryException):
            self._assignment_repository.update_description('1', '')

    def test_update_deadline__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_deadline('1', '2021-12-15')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.deadline, '2021-12-15')

    def test_generate_assignments(self):
        self._assignment_repository.generate_assignments()
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_repository(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        assignment = Assignment('2', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 2)


class AssignmentBinaryFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._assignment_repository = AssignmentBinaryFileRepository()

    def tearDown(self) -> None:
        pass

    def test_add_new_assignment__valid_input__successful_addition(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_id_not_unique__given_id_unique__False(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('2', 'menu-driven', '2021-12-10')
        self.assertFalse(self._assignment_repository.id_not_unique(assignment2.id))

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._assignment_repository.get_assignment_by_id(1), None)

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(str(self._assignment_repository.get_assignment_by_id(1)), str(assignment))

    def test_remove_assignment_by_id__assignment_in_list__successful_removal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.remove_assignment_by_id('1')
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 0)

    def test_update_description__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_description(1, 'command-driven')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.description, 'command-driven')

    def test_update_description__empty_description__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(AssignmentRepositoryException):
            self._assignment_repository.update_description('1', '')

    def test_update_deadline__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_deadline('1', '2021-12-15')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.deadline, '2021-12-15')

    def test_generate_assignments(self):
        self._assignment_repository.generate_assignments()
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_repository(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        assignment = Assignment('2', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 2)


class GradeRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_repository = GradeRepository()

    def tearDown(self) -> None:
        pass

    def test_give_assignment_to_student(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 1)

    def test_get_grade_by_student_id__valid_input__asserts_equal(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = self._grade_repository.get_grade_by_student_id('1')
        self.assertEqual(grade.grade_value, '10')

    def test_get_grade_by_student_id__invalid_input__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_grade_by_student_id('1'), None)

    def test_student_does_not_have_given_assignment__student_not_with_that_assignment__true(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertTrue(self._grade_repository.student_does_not_have_given_assignment('2', '1'))

    def test_student_does_not_have_given_assignment__student_with_that_assignment__false(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertFalse(self._grade_repository.student_does_not_have_given_assignment('1', '1'))

    def test_remove_assignment_from_grades_by_id(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_student_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__raises_exception(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.remove_student_from_grades_by_id('a')

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_assignment_by_id(1), None)

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(str(self._grade_repository.get_assignment_by_id('1')), str(grade))

    def test_get_list_ungraded_assignments(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_ungraded_assignments()), 2)

    def test_get_list_graded_assignments(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_graded_assignments()), 2)

    def test_get_list_ungraded_assignments_of_student(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_ungraded_assignments_of_student('2')), 2)

    def test_get_list_ungraded_assignments_of_student__raises_exception(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.get_list_ungraded_assignments_of_student('a')

    def test_get_list_graded_assignments_of_student(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_graded_assignments_of_student('2')), 2)

    def test_get_list_graded_assignments_of_student__raises_exception(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.get_list_graded_assignments_of_student('a')


class GradeTextFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_repository = GradeTextFileRepository()

    def tearDown(self) -> None:
        pass

    def test_give_assignment_to_student(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 1)

    def test_get_grade_by_student_id__valid_input__asserts_equal(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = self._grade_repository.get_grade_by_student_id('1')
        self.assertEqual(grade.grade_value, '10')

    def test_get_grade_by_student_id__invalid_input__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_grade_by_student_id('1'), None)

    def test_student_does_not_have_given_assignment__student_not_with_that_assignment__true(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertTrue(self._grade_repository.student_does_not_have_given_assignment('2', '1'))

    def test_student_does_not_have_given_assignment__student_with_that_assignment__false(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertFalse(self._grade_repository.student_does_not_have_given_assignment('1', '1'))

    def test_remove_assignment_from_grades_by_id(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_student_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__raises_exception(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.remove_student_from_grades_by_id('a')

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_assignment_by_id(1), None)

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(str(self._grade_repository.get_assignment_by_id('1')), str(grade))

    def test_get_list_ungraded_assignments(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_ungraded_assignments()), 2)

    def test_get_list_graded_assignments(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_graded_assignments()), 2)

    def test_get_list_ungraded_assignments_of_student(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_ungraded_assignments_of_student('2')), 2)

    def test_get_list_ungraded_assignments_of_student__raises_exception(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.get_list_ungraded_assignments_of_student('a')

    def test_get_list_graded_assignments_of_student(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_graded_assignments_of_student('2')), 2)

    def test_get_list_graded_assignments_of_student__raises_exception(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.get_list_graded_assignments_of_student('a')


class GradeBinaryFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_repository = GradeBinaryFileRepository()

    def tearDown(self) -> None:
        pass

    def test_give_assignment_to_student(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 1)

    def test_get_grade_by_student_id__valid_input__asserts_equal(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = self._grade_repository.get_grade_by_student_id('1')
        self.assertEqual(grade.grade_value, '10')

    def test_get_grade_by_student_id__invalid_input__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_grade_by_student_id('1'), None)

    def test_student_does_not_have_given_assignment__student_not_with_that_assignment__true(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertTrue(self._grade_repository.student_does_not_have_given_assignment('2', '1'))

    def test_student_does_not_have_given_assignment__student_with_that_assignment__false(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertFalse(self._grade_repository.student_does_not_have_given_assignment('1', '1'))

    def test_remove_assignment_from_grades_by_id(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_student_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__raises_exception(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.remove_student_from_grades_by_id('a')

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_assignment_by_id(1), None)

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(str(self._grade_repository.get_assignment_by_id('1')), str(grade))

    def test_get_list_ungraded_assignments(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_ungraded_assignments()), 2)

    def test_get_list_graded_assignments(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_graded_assignments()), 2)

    def test_get_list_ungraded_assignments_of_student(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_ungraded_assignments_of_student('2')), 2)

    def test_get_list_ungraded_assignments_of_student__raises_exception(self):
        grade = Grade('1', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', 0)
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.get_list_ungraded_assignments_of_student('a')

    def test_get_list_graded_assignments_of_student(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_graded_assignments_of_student('2')), 2)

    def test_get_list_graded_assignments_of_student__raises_exception(self):
        grade = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        grade = Grade('2', '2', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.get_list_graded_assignments_of_student('a')
