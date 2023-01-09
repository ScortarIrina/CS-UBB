import unittest

from domain.data_structure import Iterable
from services.undo_redo_service import UndoRedoService, UndoRedoExceptions, CascadedOperation
from src.domain.assignment import Assignment
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.assignment_repo import AssignmentRepository, AssignmentRepositoryException, \
    AssignmentTextFileRepository, AssignmentBinaryFileRepository
from src.repository.grade_repo import GradeRepository, GradeRepositoryException, GradeTextFileRepository, \
    GradeBinaryFileRepository
from src.repository.student_repo import StudentRepository, StudentRepositoryException, StudentTextFileRepository, \
    StudentBinaryFileRepository
from src.services.students_service import StudentService
from src.services.assignments_service import AssignmentService
from src.services.grades_service import GradeService


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


class StudentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentRepository()

    def tearDown(self) -> None:
        pass

    def test_repo_add_new_student__valid_input__successful_addition(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_get_student_by_id__valid_input__successful_operation(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertIsInstance(self._student_repository.get_student_by_id('1'), Student)

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

    def test_remove_student_by_id__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id__valid_id__successful_removal(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

    def test_update_name__valid_input__successful_update(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        student = self._student_repository.update_name(student.id, 'Ana')
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

    def test_update_group__valid_input__successful_update(self):
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

    def test_generate_student(self):
        self._student_repository.generate_student()
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_get_student_by_id__student_not_in_list__returns_none(self):
        self.assertEqual(self._student_repository.get_student_by_id(1), None)


class StudentTextFileRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentTextFileRepository()

    def tearDown(self) -> None:
        pass

    def test_repo_add_new_student__valid_input__successful_addition(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_repository.get_list_of_students()), 1)

    def test_id_not_unique__id_is_unique__false(self):
        student1 = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Irina', '916')
        self.assertFalse(self._student_repository.id_not_unique(student2.id))

    def test_remove_student_by_id__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id__valid_input__successful_removal(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

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

    def test_repo_add_new_student__valid_input__successful__addition(self):
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

    def test_remove_student_by_id__invalid_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(StudentRepositoryException):
            self._student_repository.remove_student_by_id('-1')

    def test_remove_student_by_id__valid_input__successful_removal(self):
        student = Student('1', 'Irina', '916')
        self._student_repository.add_new_student(student.id, student.name, student.group)
        self._student_repository.remove_student_by_id('1')
        self.assertEqual(len(self._student_repository.get_list_of_students()), 0)

    # def test_update_name__valid_input__successful_update(self):
    #     student = Student('1', 'Irina', '916')
    #     self._student_repository.add_new_student(student.id, student.name, student.group)
    #     self._student_repository.update_name('1', 'Ana')
    #     student = self._student_repository.get_student_by_id('1')
    #     self.assertEqual(student.name, 'Ana')

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

    def test_update_group__valid_input__successful_update(self):
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

    def test_remove_student_by_id__invalid_group__raises_exception(self):
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

    def test_id_not_unique__given_id_not_unique__True(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('1', 'menu-driven', '2021-12-10')
        self.assertTrue(self._assignment_repository.id_not_unique(assignment2.id))

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

    def test_remove_assignment_by_id__invalid_id__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(AssignmentRepositoryException):
            self._assignment_repository.remove_assignment_by_id('a')

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

    def test_remove_assignment_by_id__assignment_in_list__successful_removal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.remove_assignment_by_id('1')
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 0)

    def test_update_description(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_description('1', 'cucu')
        self.assertEqual(assignment.description, 'menu-driven')

    def test_update_deadline(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_deadline('1', '2021-12-10')
        self.assertEqual(assignment.deadline, assignment.deadline)

    def test_update_description__empty_description__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(AssignmentRepositoryException):
            self._assignment_repository.update_description('1', '')

    def test_generate_assignments(self):
        self._assignment_repository.generate_assignments()
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)


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


class GradeRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_repository = GradeRepository()

    def tearDown(self) -> None:
        pass

    def test_give_assignment_to_student__valid_input__successful_operation(self):
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

    def test_remove_assignment_from_grades_by_id__valid_input__successful_removal(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__valid_input__successful_removal(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_student_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__invalid_id__raises_exception(self):
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

    def test_give_assignment_to_student__valid_input__successful_operation(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 1)

    def test_get_grade_by_student_id__invalid_input__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_grade_by_student_id('1'), None)

    def test_student_does_not_have_given_assignment__student_not_with_that_assignment__true(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        self.assertTrue(self._grade_repository.student_does_not_have_given_assignment('2', '1'))

    def test_remove_assignment_from_grades_by_id__valid_input__successful_removal(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__valid_input__successful_removal(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_student_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__invalid_id__raises_exception(self):
        grade = Grade('1', '1', '10')
        self._grade_repository.give_assignment_to_student(grade.assignment_id, grade.student_id, grade.grade_value)
        with self.assertRaises(GradeRepositoryException):
            self._grade_repository.remove_student_from_grades_by_id('a')

    def test_get_assignment_by_id__assignment_not_in_list__asserts_equal_with_none(self):
        self.assertEqual(self._grade_repository.get_assignment_by_id(1), None)

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

    def test_give_assignment_to_student__valid_input__successful_operation(self):
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

    def test_remove_assignment_from_grades_by_id__valid_input__successful_removal(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('1', '2', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__valid_input__successful_removal(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_student_from_grades_by_id('1')
        self.assertEqual(len(self._grade_repository.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__invalid_id__raises_exception(self):
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


class UndoRedoServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._undo_redo_service = UndoRedoService()
        self._student_repo = StudentRepository()
        self._student_service = StudentService(self._student_repo, self._undo_redo_service)
        self._assignment_repo = AssignmentRepository()

    def tearDown(self) -> None:
        pass

    def test_undo__possible__successful_operation(self):
        self._student_service.add_new_student('1', 'Irina', '916')
        self._undo_redo_service.undo()
        self.assertEqual(len(self._student_service.get_list_of_students()), 0)

    def test_undo__impossible__raises_exception(self):
        with self.assertRaises(UndoRedoExceptions):
            self._undo_redo_service.undo()

    def test_redo__possible__successful_operation(self):
        self._student_service.add_new_student('1', 'Irina', '916')
        self._undo_redo_service.undo()
        self._undo_redo_service.redo()
        self.assertEqual(len(self._student_service.get_list_of_students()), 1)

    def test_redo__impossible__raises_exception(self):
        with self.assertRaises(UndoRedoExceptions):
            self._undo_redo_service.redo()


class CascadedOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        self._cascaded_operation = CascadedOperation()
        self._assignment_repo = AssignmentRepository()

    def tearDown(self) -> None:
        pass

    def test_add(self):
        assignment = Assignment('1', 'cucu', '2022-01-14')
        operation = self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._cascaded_operation.add(operation)
        self.assertEqual(self._cascaded_operation._operations[0], operation)

    def test_undo(self):
        self._cascaded_operation.undo()

    def test_redo(self):
        self._cascaded_operation.redo()


class IterableTest(unittest.TestCase):
    def setUp(self) -> None:
        self._iterable = Iterable()

    def tearDown(self) -> None:
        pass

    def test_iter(self):
        self.assertEqual(self._iterable.__iter__(), self._iterable)

    def test_next(self):
        self._iterable.append("aaaa")
        self._iterable.append("bbbb")
        self._iterable.__next__()
        self._iterable.__next__()
        with self.assertRaises(StopIteration):
            self._iterable.__next__()

    def test_set_item(self):
        self._iterable.append("aaaa")
        self._iterable.append("bbbb")
        self._iterable.__setitem__(0, "haha")

    def test_delitem(self):
        self._iterable.append("aaaa")
        self._iterable.append("bbbb")
        self._iterable.__delitem__(0)
        self.assertEqual(len(self._iterable), 1)

    def test_gnome_sort_id(self):
        self._iterable.append(Student(15, "ana", 2))
        self._iterable.append(Student(7, "ana", 2))
        self._iterable.append(Student(10, "ana", 2))
        self._iterable.append(Student(8, "ana", 2))
        self._iterable.gnome_sort(self._iterable.compare_id)
        self.assertEqual(str(self._iterable[0]), str(Student(7, "ana", 2)))
        self.assertEqual(str(self._iterable[1]), str(Student(8, "ana", 2)))
        self.assertEqual(str(self._iterable[2]), str(Student(10, "ana", 2)))
        self.assertEqual(str(self._iterable[3]), str(Student(15, "ana", 2)))

    def test_gnome_sort_grades(self):
        self._iterable.append(Grade(101, 555, 5))
        self._iterable.append(Grade(100, 145, 9))
        self._iterable.append(Grade(108, 694, 2))
        self._iterable.append(Grade(111, 421, 7))
        self._iterable.gnome_sort(self._iterable.compare_grades)
        self.assertEqual(str(self._iterable[3]),str(Grade(108, 694, 2)))
        self.assertEqual(str(self._iterable[2]),str(Grade(101, 555, 5)))
        self.assertEqual(str(self._iterable[1]),str(Grade(111, 421, 7)))
        self.assertEqual(str(self._iterable[0]),str(Grade(100, 145, 9)))

    def test_filter_past_deadline__true(self):
        assignment = Assignment('1', 'cucu', '2021-01-14')
        self._iterable.append(assignment)
        self.assertTrue(self._iterable.filter_past_deadline(assignment))

    def test_filter_past_deadline__false(self):
        assignment = Assignment('1', 'cucu', '2023-01-14')
        self._iterable.append(assignment)
        self.assertFalse(self._iterable.filter_past_deadline(assignment))

    def test_filter_id(self):
        self._iterable.append(Grade(101, 555, 5))
        self._iterable.append(Grade(100, 145, 9))
        self._iterable.append(Grade(101, 694, 2))
        self._iterable.append(Grade(111, 421, 7))
        filtered = self._iterable.filter(self._iterable.filter_by_assignment_id, 101)
        self.assertEqual(str(filtered[0]), str(Grade(101, 555, 5)))
        self.assertEqual(str(filtered[1]), str(Grade(101, 694, 2)))


class StudentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repo = StudentRepository()
        self._undo_redo_service = UndoRedoService()
        self._student_service = StudentService(self._student_repo, self._undo_redo_service)

    def tearDown(self) -> None:
        pass

    def test_generate_assignments(self):
        self._student_service.generate_students()
        self.assertEqual(len(self._student_service.get_list_of_students()), 10)

    def test_add_new_assignment__valid_input__successful_addition(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        self.assertEqual(len(self._student_service.get_list_of_students()), 1)

    def test_add_new_student__duplicate_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(ValueError):
            self._student_service.add_new_student('1', 'Irina', '916')

    def test_get_student_by_id__valid_input__successful_operation(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        self.assertIsInstance(self._student_service.get_student_by_id('1'), Student)

    def test_id_not_unique__id_not_unique__true(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('1', 'Irina', '916')
        self.assertTrue(self._student_service.id_not_unique(student2.id))

    def test_id_not_unique__id_is_unique__false(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Irina', '916')
        self.assertFalse(self._student_service.id_not_unique(student2.id))

    def test_remove_student_by_id__valid_id__successful_removal(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        self._student_service.remove_student_by_id('1')
        self.assertEqual(len(self._student_service.get_list_of_students()), 0)

    def test_update_name__valid_input__successful_update(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        student = self._student_service.update_name('1', 'Ana')
        self.assertEqual(student.name, 'Ana')

    def test_update_group__valid_input__successful_update(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        student = self._student_service.update_group('1', '915')
        self.assertEqual(student.group, '915')


class AssignmentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._assignment_repo = AssignmentRepository()
        self._undo_redo_service = UndoRedoService()
        self._assignment_service = AssignmentService(self._assignment_repo, self._undo_redo_service)

    def tearDown(self) -> None:
        pass

    def test_generate_assignments(self):
        self._assignment_service.generate_assignments()
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 10)

    def test_add_new_assignment__valid_input__successful_addition(self):
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 1)

    def test_add_new_assignment__invalid_id__raises_error(self):
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(ValueError):
            self._assignment_service.add_new_assignment('1', 'cucu', '2022-01-14')

    def test_get_assignment_by_id__assignment_in_list__asserts_equal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(str(self._assignment_service.get_assignment_by_id(1)), str(assignment))

    def test_id_not_unique__given_id_not_unique__True(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('1', 'menu-driven', '2021-12-10')
        self.assertTrue(self._assignment_service.id_not_unique(assignment2.id))

    def test_remove_assignment_by_id__assignment_in_list__successful_removal(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_service.remove_assignment_by_id('1')
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 0)

    def test_update_description__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_service.update_description(1, 'command-driven')
        assignment = self._assignment_service.get_assignment_by_id(1)
        self.assertEqual(assignment.description, 'command-driven')

    def test_update_deadline__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_service.update_deadline('1', '2021-12-15')
        assignment = self._assignment_service.get_assignment_by_id(1)
        self.assertEqual(assignment.deadline, '2021-12-15')


class GradesServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_repo = GradeRepository()
        self._student_repo = StudentRepository()
        self._assignment_repo = AssignmentRepository()
        self._undo_redo_service = UndoRedoService()
        self._grade_service = GradeService(self._grade_repo, self._student_repo, self._assignment_repo, self._undo_redo_service)

    def tearDown(self) -> None:
        pass

    def test_get_list_of_grades(self):
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 0)

    def test_student_does_not_have_given_assignment__true(self):
        student = Student('1', 'Irina', '916')
        assignment1 = Assignment('1', 'cucu', '2022-01-14')
        assignment2 = Assignment('2', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        self._assignment_repo.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self.assertTrue(self._grade_service.student_does_not_have_given_assignment(2, 1))

    def test_student_does_not_have_given_assignment__false(self):
        student = Student('1', 'Irina', '916')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self.assertFalse(self._grade_service.student_does_not_have_given_assignment(1, 1))

    def test_give_assignment_to_student__valid_input__successful_link(self):
        student = Student('1', 'Irina', '911')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 1)

    def test_give_assignment_to_student__invalid_student_id__raises_exception(self):
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.give_assignment_to_student('-1', '1')

    def test_give_assignment_to_student__invalid_assignment_id__raises_exception(self):
        self._student_repo.add_new_student('1', 'Irina', '911')
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.give_assignment_to_student('1', '-2')

    def test_give_assignment_to_student__link_already_made_raises_exception(self):
        student = Student('1', 'Irina', '912')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.give_assignment_to_student(1, 1)

    def test_give_assignment_to_group__valid_input__successful_link(self):
        student = Student('1', 'Irina', '922')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_group('1', '922')
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 1)

    def test_give_assignment_to_group__invalid_assignment_id__raises_exception(self):
        student = Student('1', 'Irina', '922')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.give_assignment_to_group('a', '922')

    def test_give_assignment_to_group__invalid_group__raises_exception(self):
        student = Student('1', 'Irina', '922')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.give_assignment_to_group('1', 'a')

    def test_get_list_ungraded_assignments(self):
        student = Student('1', 'Irina', '921')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self.assertEqual(len(self._grade_service.get_list_ungraded_assignments()), 1)

    def test_get_list_ungraded_assignments_of_student(self):
        student = Student('1', 'Irina', '924')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._grade_service.get_list_ungraded_assignments_of_student(1)), 0)

    def test_grade_assignment__valid_input__successful_grading(self):
        student = Student('1', 'Irina', '931')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self._grade_service.grade_assignment('1', '1', '10')
        self.assertEqual(len(self._grade_service.get_list_graded_assignments_of_student('1')), 1)

    def test_grade_assignment__invalid_grade__raises_exception(self):
        student = Student('1', 'Irina', '932')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.grade_assignment('1', '1', 'a')

    def test_grade_assignment__invalid_assignment_id__raises_exception(self):
        student = Student('1', 'Irina', '934')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.grade_assignment('a', '1', '10')

    def test_grade_assignment__invalid_student_id__raises_exception(self):
        student = Student('1', 'Irina', '935')
        assignment = Assignment('1', 'cucu', '2022-02-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.grade_assignment('1', 'a', '10')

    def test_grade_assignment__student_id_does_not_exist__raises_exception(self):
        student = Student('1', 'Irina', '936')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.grade_assignment('1', '2', '10')

    def test_get_grade(self):
        grade = Grade('1', '1', '10')
        self.assertEqual(self._grade_service.get_grade(grade), 10)

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__valid_input__successful_operation(self):
        student = Student('1', 'Irina', '936')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        assignment1 = Assignment('1', 'cucu', '2022-01-14')
        self._assignment_repo.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('2', 'cucu', '2022-01-14')
        self._assignment_repo.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)
        self._grade_service.give_assignment_to_student('1', '1')
        self._grade_service.give_assignment_to_student('2', '1')
        self._grade_service.grade_assignment('1', '1', '10')
        self.assertEqual(len(self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade('1')), 1)

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__invalid_input1__raises_exception(self):
        student = Student('1', 'Irina', '936')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade('1')

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__invalid_input2__raises_exception(self):
        student = Student('1', 'Irina', '936')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student('1', '1')
        with self.assertRaises(GradeRepositoryException):
            self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade('1')

    def test_late_assignment__assignment_is_late__true(self):
        assignment = Assignment('1', 'cucu', '2021-01-14')
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertTrue(self._grade_service.late_assignment(assignment.id))

    def test_late_assignment__assignment_is_not_late__false(self):
        assignment = Assignment('1', 'cucu', '2023-01-14')
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertFalse(self._grade_service.late_assignment(assignment.id))

    def test_get_students_with_pass_deadline_assignments__list_not_empty__successful_operation(self):
        student = Student('1', 'Irina', '926')
        assignment = Assignment('1', 'cucu', '2021-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student('1', '1')
        self.assertEqual(len(self._grade_service.get_students_with_pass_deadline_assignments()), 1)

    def test_get_students_with_pass_deadline_assignments__list_empty__raises_exception(self):
        student = Student('1', 'Irina', '926')
        assignment = Assignment('1', 'cucu', '2022-01-14')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student('1', '1')
        with self.assertRaises(GradeRepositoryException):
            self.assertEqual(len(self._grade_service.get_students_with_pass_deadline_assignments()), 1)

    def test_get_average_of_student_grades(self):
        student = Student('1', 'Irina', '938')
        assignment = Assignment('1', 'cucu', '2022-01-12')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self._grade_service.grade_assignment('1', '1', '10')
        self.assertEqual(self._grade_service.get_average_of_student_grades('1'), 10)

    def test_get_list_average_grade_all_students(self):
        student = Student('1', 'Irina', '921')
        assignment = Assignment('1', 'cucu', '2022-01-13')
        self._student_repo.add_new_student(student.id, student.name, student.group)
        self._assignment_repo.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(1, 1)
        self._grade_service.grade_assignment('1', '1', '10')
        self.assertEqual(len(self._grade_service.get_list_average_grade_all_students()), 1)
