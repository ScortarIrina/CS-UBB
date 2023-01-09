import unittest
from src.domain.entities import Grade
from src.repository.grade_repository import UserExceptionGrade, GradeRepository


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
        with self.assertRaises(UserExceptionGrade):
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
        with self.assertRaises(UserExceptionGrade):
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
        with self.assertRaises(UserExceptionGrade):
            self._grade_repository.get_list_graded_assignments_of_student('a')

    def test_repo_exception(self):
        grade1 = Grade('1', '1', '10')
        grade2 = Grade('2', '1', '10')
        self._grade_repository.give_assignment_to_student(grade1.assignment_id, grade1.student_id, grade1.grade_value)
        self._grade_repository.give_assignment_to_student(grade2.assignment_id, grade2.student_id, grade2.grade_value)
        self._grade_repository.remove_assignment_from_grades_by_id('1')
        with self.assertRaises(UserExceptionGrade):
            self._grade_repository.remove_assignment_from_grades_by_id('-1')
