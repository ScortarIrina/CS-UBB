import pickle

from src.domain.Assignment import Assignment
import random
import datetime


class AssignmentRepositoryException(Exception):
    pass


class AssignmentRepository(object):
    def __init__(self):
        self._list_of_assignments = []

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

        list_ids = []
        id = random.randint(100, 900)
        description = random.choice(descriptions)
        deadline = random.choice(deadlines)

        if id in list_ids:
            pass
        else:
            list_ids.append(id)
            self.add_new_assignment(str(id), description, deadline)

    def get_list_of_assignments(self):
        return self._list_of_assignments

    def id_not_unique(self, id):
        for assignment in self._list_of_assignments:
            if int(assignment.id) == int(id):
                return True
        return False

    def get_assignment_by_id(self, id):
        for assignment in self._list_of_assignments:
            if int(assignment.id) == int(id):
                return assignment
        return None

    def add_new_assignment(self, id, description, deadline):
        self._list_of_assignments.append(Assignment(id, description, deadline))

    def remove_assignment_by_id(self, assignment_id):
        if type(id) is str and (not assignment_id.isnumeric() or float(assignment_id) != int(assignment_id)):
            raise AssignmentRepositoryException("Id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self._list_of_assignments) - 1

        while index_go_through_list <= length_of_list:
            if int(self._list_of_assignments[index_go_through_list].id) == int(assignment_id):
                self._list_of_assignments.pop(index_go_through_list)
                length_of_list = len(self._list_of_assignments) - 1
                index_go_through_list -= 1
            index_go_through_list += 1

    def update_description(self, assignment_id, assignment_description):
        if type(assignment_id) is str and len(assignment_description) <= 0:
            raise AssignmentRepositoryException("Description must not be empty")

        index_go_through_list = 0
        length_of_list = len(self._list_of_assignments) - 1
        while index_go_through_list <= length_of_list:
            if int(self._list_of_assignments[index_go_through_list].id) == int(assignment_id):
                self._list_of_assignments[index_go_through_list].description = assignment_description
                index_go_through_list = length_of_list
            index_go_through_list += 1

    def update_deadline(self, assignment_id, assignment_deadline):
        datetime.datetime.strptime(assignment_deadline, "%Y-%m-%d")
        index_go_through_list = 0
        length_of_list = len(self._list_of_assignments) - 1
        while index_go_through_list <= length_of_list:
            if int(self._list_of_assignments[index_go_through_list].id) == int(assignment_id):
                self._list_of_assignments[index_go_through_list].deadline = assignment_deadline
                index_go_through_list = length_of_list
            index_go_through_list += 1

    def __len__(self):
        return len(self._list_of_assignments)

    def __getitem__(self, item):
        return self._list_of_assignments[item]


class AssignmentTextFileRepository(AssignmentRepository):
    def __init__(self):
        super().__init__()
        self._file_name = r"C:\Users\Irina\Desktop\PycharmProjects\a9-ScortarIrina\src\Files\TextFiles\assignments.txt"
        self._clear_file()
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")

        for line in file.readlines():
            __id, _description, _deadline = line.split(maxsplit=2, sep=',')
            self.add_new_assignment(str(__id), str(_description), str(_deadline).rstrip())

        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt")

        for assignment in self._list_of_assignments:
            file.write(str(assignment.id) + ',' + assignment.description + ',' + str(assignment.deadline) + "\n")

        file.close()

    def _clear_file(self):
        file = open(self._file_name, "wt")
        file.truncate()
        file.close()

    def remove_assignment_by_id(self, assignment_id):
        super(AssignmentTextFileRepository, self).remove_assignment_by_id(assignment_id)
        self._save_file()

    def update_description(self, assignment_id, assignment_description):
        super(AssignmentTextFileRepository, self).update_description(assignment_id, assignment_description)
        self._save_file()

    def update_deadline(self, assignment_id, assignment_deadline):
        super(AssignmentTextFileRepository, self).update_deadline(assignment_id, assignment_deadline)
        self._save_file()

    def add_new_assignment(self, __id, _description, _deadline):
        super(AssignmentTextFileRepository, self).add_new_assignment(__id, _description, _deadline)
        self._save_file()

    def id_not_unique(self, id):
        return super(AssignmentTextFileRepository, self).id_not_unique(id)

    def get_assignment_by_id(self, id):
        return super(AssignmentTextFileRepository, self).get_assignment_by_id(id)

    def generate_assignments(self):
        super(AssignmentTextFileRepository, self).generate_assignments()
        self._save_file()
        
    def get_list_of_assignments(self):
        return super(AssignmentTextFileRepository, self).get_list_of_assignments()


class AssignmentBinaryFileRepository(AssignmentRepository):
    def __init__(self):
        super().__init__()
        self._file_name = r"C:\Users\Irina\Desktop\PycharmProjects\a9-ScortarIrina\src\Files\BinaryFiles\assignments.bin"
        self._clear_file()
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "rb")
            for assignment in pickle.load(file):
                self.add_new_assignment(assignment.id, assignment.description, assignment.deadline)
            file.close()
        except EOFError:
            pass

        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")
        pickle.dump(self._list_of_assignments, file)
        file.close()

    def _clear_file(self):
        file = open(self._file_name, "wb")
        file.truncate()
        file.close()

    def add_new_student(self, id, name, group):
        super(AssignmentBinaryFileRepository, self).add_new_assignment(id, name, group)
        self._save_file()

    def remove_assignment_by_id(self, id):
        super(AssignmentBinaryFileRepository, self).remove_assignment_by_id(id)
        self._save_file()

    def update_description(self, assignment_id, assignment_description):
        super(AssignmentBinaryFileRepository, self).update_description(assignment_id, assignment_description)
        self._save_file()

    def update_deadline(self, assignment_id, assignment_deadline):
        super(AssignmentBinaryFileRepository, self).update_deadline(assignment_id, assignment_deadline)
        self._save_file()

    def id_not_unique(self, id):
        return super(AssignmentBinaryFileRepository, self).id_not_unique(id)

    def get_assignment_by_id(self, id):
        return super(AssignmentBinaryFileRepository, self).get_assignment_by_id(id)

    def generate_assignments(self):
        super(AssignmentBinaryFileRepository, self).generate_assignments()
        self._save_file()

    def get_list_of_assignments(self):
        return super(AssignmentBinaryFileRepository, self).get_list_of_assignments()
