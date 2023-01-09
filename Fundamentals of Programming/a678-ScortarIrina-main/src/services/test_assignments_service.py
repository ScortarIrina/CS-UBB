import unittest
from src.domain.entities import Assignment
from src.services.assignments_service import AssignmentService


class AssignmentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._assignment_service = AssignmentService()

    def tearDown(self) -> None:
        pass

    def test_generate_assignments(self):
        self._assignment_service.generate_assignments()
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 10)

    def test_get_list_of_assignments(self):
        assignment1 = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment1.id, assignment1.description, assignment1.deadline)
        assignment2 = Assignment('2', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment2.id, assignment2.description, assignment2.deadline)
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 2)

    def test_id_not_unique(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertTrue(self._assignment_service.id_not_unique('1'))

    def test_get_assignment_by_id(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(str(self._assignment_service.get_assignment_by_id('1')), str(assignment))

    def test_update_description(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_service.update_description(1, 'command-driven')
        assignment = self._assignment_service.get_assignment_by_id(1)
        self.assertEqual(assignment.description, 'command-driven')

    def test_update_deadline(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_service.update_deadline(1, '2021-12-1')
        assignment = self._assignment_service.get_assignment_by_id(1)
        self.assertEqual(assignment.deadline, '2021-12-1')

    def test_remove_assignment_from_assignments_by_id(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self._assignment_service.remove_assignment_from_assignments_by_id('1')
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 0)

    def test_add_new_assignment(self):
        assignment = Assignment('1', 'menu-driven', '2021-12-10')
        self._assignment_service.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
        self.assertEqual(len(self._assignment_service.get_list_of_assignments()), 1)
