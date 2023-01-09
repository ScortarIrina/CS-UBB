import unittest
from src.domain.entities import Student, Assignment, Grade
from src.services.students_service import StudentService
from src.services.assignments_service import AssignmentService
from src.services.grades_service import GradeService, UserExceptionGrade


class GradeServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_service = StudentService()
        self._assignment_service = AssignmentService()
        self._grade_service = GradeService(self._student_service, self._assignment_service)

    def tearDown(self) -> None:
        pass

    def test_give_assignment_to_student__valid_input__successful_link(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        grade = Grade('1', '1', '10')
        self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 1)

    def test_give_assignment_to_student__invalid_student_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        grade = Grade('1', '-1', '10')

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)

    def test_give_assignment_to_student__invalid_assignment_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        grade = Grade('-1', '1', '10')

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)

    def test_give_assignment_to_student__student_id_does_not_exist__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        grade = Grade('1', '1', '10')

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)

    def test_give_assignment_to_student__assignment_id_does_not_exist__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        grade = Grade('1', '1', '10')

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)

    def test_give_assignment_to_student__student_has_assignment__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        grade = Grade('1', '1', '10')
        self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_student(grade.assignment_id, grade.student_id)

    def test_give_assignment_to_group__valid_input__successful_link(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Sonia', '916')
        self._student_service.add_new_student(student2.id, student2.name, student2.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)

        self._grade_service.give_assignment_to_group('1', '916')
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 2)

    def test_give_assignment_to_group__invalid_assignment_id__raises_exception(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        student2 = Student('2', 'Sonia', '916')
        self._student_service.add_new_student(student2.id, student2.name, student2.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_group('a', '916')

    def test_give_assignment_to_group__assignment_does_not_exist__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_group('1', '916')

    def test_give_assignment_to_group__invalid_group__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.give_assignment_to_group('1', 'a')

    def test_get_list_ungraded_assignments(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        self.assertEqual(len(self._grade_service.get_list_ungraded_assignments()), 1)

    def test_get_list_ungraded_assignments_of_student(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        self.assertEqual(len(self._grade_service.get_list_ungraded_assignments_of_student(student.id)), 1)

    def test_grade_assignment__valid_input__successful_operation(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        self._grade_service.grade_assignment('1', '1', '10')
        self.assertEqual(len(self._grade_service.get_list_graded_assignments_of_student(student.id)), 1)

    def test_grade_assignment__invalid_grade__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.grade_assignment('1', '1', '100')

    def test_grade_assignment__invalid_assignment_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.grade_assignment('a', '1', '10')

    def test_grade_assignment__invalid_student_id__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.grade_assignment('1', 'a', '10')

    def test_grade_assignment__student_id_does_not_exist__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.grade_assignment('1', '2', '10')

    def test_grade_assignment__student_does_not_have_assignment__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.grade_assignment('1', '1', '10')

    def test_remove_assignment_from_grades_by_id__valid_input__successful_removal(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.remove_assignment_from_grades_by_id(assignment.id)
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 0)

    def test_remove_student_from_grades_by_id__valid_input__successful_removal(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.remove_student_from_grades_by_id(student.id)
        self.assertEqual(len(self._grade_service.get_list_of_grades()), 0)

    def test_get_grade(self):
        grade = Grade('1', '1', '10')
        self.assertEqual(self._grade_service.get_grade(grade), 10)

    def test_get_average_of_student_grades(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        self._grade_service.grade_assignment('1', '1', '10')
        self.assertEqual(self._grade_service.get_average_of_student_grades(student.id), 10)

    def test_get_list_average_grade_all_students(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        self._grade_service.give_assignment_to_student(assignment1.id, student1.id)
        self._grade_service.grade_assignment('1', '1', '10')
        student2 = Student('2', 'Irina', '916')
        self._student_service.add_new_student(student2.id, student2.name, student2.group)
        self._grade_service.give_assignment_to_student(assignment1.id, student2.id)
        self._grade_service.grade_assignment('1', '2', '10')
        self.assertEqual(len(self._grade_service.get_list_average_grade_all_students()), 2)

    def test_late_assignment__late_assignment__true(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-11-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        self.assertTrue(self._grade_service.late_assignment(assignment.id))

    def test_late_assignment__not_late_assignment__false(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student.id)
        self.assertFalse(self._grade_service.late_assignment(assignment.id))

    def test_get_student_passed_deadline_assignments__valid_input__returns_valid_list(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)

        assignment1 = Assignment('1', 'menu-driven', '2021-11-10')
        self._assignment_service.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        self._grade_service.give_assignment_to_student(assignment1.id, student.id)

        assignment2 = Assignment('2', 'menu-driven', '2021-11-10')
        self._assignment_service.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)
        self._grade_service.give_assignment_to_student(assignment2.id, student.id)

        self.assertEqual(len(self._grade_service.get_student_passed_deadline_assignments()), 2)

    def test_get_student_passed_deadline_assignments__all_assignments_up_to_date__raises_exception(self):
        student = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student.id, student.name, student.group)

        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        self._grade_service.give_assignment_to_student(assignment1.id, student.id)

        assignment2 = Assignment('2', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)
        self._grade_service.give_assignment_to_student(assignment2.id, student.id)

        with self.assertRaises(UserExceptionGrade):
            self._grade_service.get_student_passed_deadline_assignments()

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__valid_input__successful_operation(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student1.id)
        self._grade_service.grade_assignment('1', '1', '10')
        student2 = Student('2', 'Irina', '916')
        self._student_service.add_new_student(student2.id, student2.name, student2.group)
        self._grade_service.give_assignment_to_student(assignment.id, student2.id)
        self._grade_service.grade_assignment('1', '2', '9')
        self.assertEqual(len(self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade(assignment.id)), 2)

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__invalid_assignment_id__raises_exception(self):
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade('a')

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__no_student_has_this_assignment__raises_exception(self):
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade('1')

    def test_get_list_of_students_with_given_assignment_ordered_by_grade__assignment_not_graded__raises_exception(self):
        student1 = Student('1', 'Irina', '916')
        self._student_service.add_new_student(student1.id, student1.name, student1.group)
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._grade_service.give_assignment_to_student(assignment.id, student1.id)
        with self.assertRaises(UserExceptionGrade):
            self._grade_service.get_list_of_students_with_given_assignment_ordered_by_grade('1')

"""
    def get_list_of_students_with_given_assignment_ordered_by_grade(self, assignment_id):
            
        list_of_graded_assignments = self.__grade_repository.get_list_graded_assignments()
        
        for grade in list_of_graded_assignments:
            if int(grade.assignment_id) != int(assignment_id):
                del grade
                
        return sorted(list_of_graded_assignments, key=self.get_grade, reverse=True)
"""
