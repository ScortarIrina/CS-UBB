import unittest
from src.domain.entities import Assignment
from src.repository.assignment_repository import UserExceptionAssignment, AssignmentRepository


class AssignmentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._assignment_repository = AssignmentRepository()

    def tearDown(self) -> None:
        pass

    def test_add_new_assignment__valid_input__successful_addition(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 1)

    def test_add_new_assignment__invalid_input__raises_exception(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('-1', 'menu-driven', '2021-12-10')
        with self.assertRaises(UserExceptionAssignment):
            self._assignment_repository.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)

    def test_add_new_assignment__id_not_unique__raises_exception(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('1', 'menu-driven', '2021-12-10')
        with self.assertRaises(UserExceptionAssignment):
            self._assignment_repository.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)

    def test_add_new_assignment__empty_description__raises_exception(self):
        assignment = Assignment('1', '', '2021-12-10')
        with self.assertRaises(UserExceptionAssignment):
            self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)

    def test_id_not_unique__given_id_not_unique__True(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('1', 'menu-driven', '2021-12-10')
        self.assertTrue(str(self._assignment_repository.id_not_unique(assignment2.id)))

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
        self._assignment_repository.remove_assignment_from_assignments_by_id('1')
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 0)

    def test_remove_assignment_by_id__invalid_id__raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(UserExceptionAssignment):
            self._assignment_repository.remove_assignment_from_assignments_by_id('-1')

    def test_update_description__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_description(1, 'command-driven')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.description, 'command-driven')

    def test_update_description_raises_exception(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        with self.assertRaises(UserExceptionAssignment):
            self._assignment_repository.update_description('1', '')

    def test_update_deadline__assignment_in_list__successful_update(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_repository.update_deadline('1', '2021-12-15')
        assignment = self._assignment_repository.get_assignment_by_id(1)
        self.assertEqual(assignment.deadline, '2021-12-15')

    def test_generate_assignments(self):
        self._assignment_repository.generate_assignments()
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 10)

    def test_repository(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        assignment = Assignment('2', 'menu-driven', '2021-12-10')
        self._assignment_repository.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_repository.get_list_of_assignments()), 2)
