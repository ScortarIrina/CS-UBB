from src.repository.assignment_repository import AssignmentRepository


class AssignmentService:

    def __init__(self):
        self.__assignment_repository = AssignmentRepository()

    def generate_assignments(self):
        self.__assignment_repository.generate_assignments()

    def get_list_of_assignments(self):
        return self.__assignment_repository.get_list_of_assignments()

    def id_not_unique(self, id):
        return self.__assignment_repository.id_not_unique(id)

    def get_assignment_by_id(self, id):
        return self.__assignment_repository.get_assignment_by_id(id)

    def add_new_assignment(self, id, description, deadline):
        self.__assignment_repository.add_new_assignment(id, description, deadline)

    def remove_assignment_from_assignments_by_id(self, assignment_id):
        self.__assignment_repository.remove_assignment_from_assignments_by_id(assignment_id)

    def update_description(self, assignment_id, assignment_description):
        self.__assignment_repository.update_description(assignment_id, assignment_description)

    def update_deadline(self, assignment_id, assignment_deadline):
        self.__assignment_repository.update_deadline(assignment_id, assignment_deadline)