import copy

from src.services.undo_redo_service import Operation, Call


class AssignmentService:

    def __init__(self, repository, undo_redo_service):
        self._assignment_repository = repository
        self._undo_redo = undo_redo_service

    def generate_assignments(self):
        for assignment in range(10):
            self._assignment_repository.generate_assignments()

    def get_list_of_assignments(self):
        return self._assignment_repository.get_list_of_assignments()

    def id_not_unique(self, id):
        return self._assignment_repository.id_not_unique(id)

    def get_assignment_by_id(self, id):
        return copy.deepcopy(self._assignment_repository.get_assignment_by_id(id))

    def add_new_assignment(self, id, description, deadline):
        if self._assignment_repository.id_not_unique(id) is False:
            self._assignment_repository.add_new_assignment(id, description, deadline)
        else:
            raise ValueError("Assignment id must be unique")

    def remove_assignment_by_id(self, assignment_id):
        assignment = self.get_assignment_by_id(assignment_id)
        self._undo_redo.add(Operation(Call(self.add_new_assignment, assignment.id, assignment.description, assignment.deadline),
                                      Call(self.remove_assignment_by_id, assignment_id)))
        self._assignment_repository.remove_assignment_by_id(assignment_id)

    def update_description(self, assignment_id, assignment_description):
        assignment = self.get_assignment_by_id(assignment_id)
        self._undo_redo.add(Operation(Call(self.update_description, assignment.id, assignment.description),
                                      Call(self.update_description, assignment_id, assignment_description)))
        self._assignment_repository.update_description(assignment_id, assignment_description)

    def update_deadline(self, assignment_id, assignment_deadline):
        assignment = self.get_assignment_by_id(assignment_id)
        self._undo_redo.add(Operation(Call(self.update_deadline, assignment.id, str(assignment.deadline)),
                                      Call(self.update_deadline, assignment_id, str(assignment_deadline))))
        self._assignment_repository.update_deadline(assignment_id, assignment_deadline)