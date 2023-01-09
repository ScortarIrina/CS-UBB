from src.domain.entities import Assignment
import random
import datetime


class UserExceptionAssignment(Exception):
    pass


class AssignmentRepository:
    def __init__(self):
        self.__list_of_assignments = []

    def generate_assignments(self):
        descriptions = ["test functions", "modular programming", "layered architecture", "procedural programming",
                        "command-based ui", "menu-driven ui", "classes", "exceptions"]

        deadlines = []
        generated_deadline = datetime.datetime.strptime("2021-11-02", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2021-11-10", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2021-12-20", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2021-11-17", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2022-01-14", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2022-01-23", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2022-01-29", "%Y-%m-%d")
        deadlines.append(generated_deadline)
        generated_deadline = datetime.datetime.strptime("2022-02-16", "%Y-%m-%d")
        deadlines.append(generated_deadline)

        list_ids = random.sample(range(1, 200), 10)

        for i in range(10):
            self.__list_of_assignments.append(Assignment(list_ids[i], random.choice(descriptions), random.choice(deadlines)))

    def get_list_of_assignments(self):
        return self.__list_of_assignments

    def id_not_unique(self, id):
        for assignment in self.__list_of_assignments:
            if int(assignment.id) == int(id):
                return True
        return False

    def get_assignment_by_id(self, id):
        for assignment in self.__list_of_assignments:
            if int(assignment.id) == int(id):
                return assignment
        return None

    def add_new_assignment(self, id, description, deadline):
        if self.id_not_unique(id):
            raise UserExceptionAssignment('Id must be unique')
        elif type(id) is str and (not id.isnumeric() or float(id) != int(id)):
            raise UserExceptionAssignment('Id must be a natural number')
        elif len(description) <= 0:
            raise UserExceptionAssignment('Description must not be empty')

        self.__list_of_assignments.append(Assignment(id, description, deadline))

    def remove_assignment_from_assignments_by_id(self, assignment_id):
        if type(id) is str and (not assignment_id.isnumeric() or float(assignment_id) != int(assignment_id)):
            raise UserExceptionAssignment("Id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_assignments) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_assignments[index_go_through_list].id) == int(assignment_id):
                self.__list_of_assignments.pop(index_go_through_list)
                length_of_list = len(self.__list_of_assignments) - 1
                index_go_through_list -= 1
            index_go_through_list += 1

    def update_description(self, assignment_id, assignment_description):
        if len(assignment_description) <= 0:
            raise UserExceptionAssignment("Description must not be empty")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_assignments) - 1
        while index_go_through_list <= length_of_list:
            if int(self.__list_of_assignments[index_go_through_list].id) == int(assignment_id):
                self.__list_of_assignments[index_go_through_list].description = assignment_description
                index_go_through_list = length_of_list
            index_go_through_list += 1

    def update_deadline(self, assignment_id, assignment_deadline):
        datetime.datetime.strptime(assignment_deadline, "%Y-%m-%d")
        index_go_through_list = 0
        length_of_list = len(self.__list_of_assignments) - 1
        while index_go_through_list <= length_of_list:
            if int(self.__list_of_assignments[index_go_through_list].id) == int(assignment_id):
                self.__list_of_assignments[index_go_through_list].deadline = assignment_deadline
                index_go_through_list = length_of_list
            index_go_through_list += 1