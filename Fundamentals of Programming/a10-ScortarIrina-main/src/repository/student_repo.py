import random
from random import randint

from domain.data_structure import Iterable
from src.domain.student import Student
import pickle


class StudentRepositoryException(Exception):
    pass


class StudentRepository(object):
    def __init__(self):
        self._list_of_students = Iterable()

    def generate_student(self):
        names = ["Irina", "Andrei", "Tudor", "Stefan", "Lucia", "Paul", "Monica", "Andreea", "Sonia", "Ioana",
                 "Victor", "Alex", "Maria", "Ana"]
        id_list = []
        id = random.randint(100, 900)
        name = random.choice(names)
        group = randint(100, 999)

        if id not in id_list:
            id_list.append(id)
            self.add_new_student(str(id), name, str(group))

    def get_list_of_students(self):
        return self._list_of_students.get_list()

    def get_student_by_id(self, id):
        for student in self._list_of_students:
            if int(student.id) == int(id):
                return student
        return None

    def id_not_unique(self, id):
        for student in self._list_of_students:
            if int(student.id) == int(id):
                return True
        return False

    def add_new_student(self, id, name, group):
        self._list_of_students.append(Student(id, name, group))

    def remove_student_by_id(self, student_id):
        if type(student_id) is str and (not student_id.isnumeric() or float(student_id) != int(student_id)):
            raise StudentRepositoryException("Id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self._list_of_students) - 1

        while index_go_through_list <= length_of_list:
            if int(self._list_of_students[index_go_through_list].id) == int(student_id):
                self._list_of_students.pop(index_go_through_list)
                length_of_list = len(self._list_of_students) - 1
                index_go_through_list -= 1
            index_go_through_list += 1

    def update_name(self, student_id, student_name):
        if type(student_id) is str and (not student_id.isnumeric() or float(student_id) != int(student_id)):
            raise StudentRepositoryException("Id must be a natural number")
        if len(student_name) <= 0:
            raise StudentRepositoryException("Name must not be empty")
        if not student_name.isalpha():
            raise StudentRepositoryException("Invalid name")

        for student in self._list_of_students:
            if int(student.id) == int(student_id):
                student.name = student_name
                return student

    def update_group(self, student_id, student_group):
        if type(student_id) is str and (not student_group.isnumeric() or float(student_group) != int(student_group) or
                                        int(student_group) < 100 or int(student_group) > 999):
            raise StudentRepositoryException("Group number must be an integer between 100 and 999")

        index_go_through_list = 0
        length_of_list = len(self._list_of_students) - 1

        while index_go_through_list <= length_of_list:
            if int(self._list_of_students[index_go_through_list].id) == int(student_id):
                self._list_of_students[index_go_through_list].group = student_group
                index_go_through_list = length_of_list
            index_go_through_list += 1


class StudentTextFileRepository(StudentRepository):
    def __init__(self):
        super().__init__()
        self._file_name = r"C:\Users\Irina\Desktop\PycharmProjects\a9-ScortarIrina\src\Files\TextFiles\students.txt"
        self._clear_file()
        # self._load_file()

    # function which reads from the list
    # def _load_file(self):
    #     file = open(self._file_name, "rt")
    #
    #     for line in file.readlines():
    #         __id, _name, _group = line.split(maxsplit=2, sep=',')
    #         self.add_new_student(str(__id), str(_name), str(_group).rstrip())
    #
    #     file.close()

    # function which writes to the list
    def _save_file(self):
        file = open(self._file_name, "wt")

        for student in self._list_of_students:
            file.write('student id: ' + str(student.id) + '     name: ' + student._name + '     group: ' + str(student._group) + "\n")

        file.close()

    # function clears list every time the program restarts
    def _clear_file(self):
        file = open(self._file_name, "wb")
        file.truncate()
        file.close()

    def id_not_unique(self, id):
        return super(StudentTextFileRepository, self).id_not_unique(id)

    # def get_student_by_id(self, id):
    #     return super(StudentTextFileRepository, self).get_student_by_id(id)

    def get_list_of_students(self):
        return super(StudentTextFileRepository, self).get_list_of_students()

    def add_new_student(self, __id, _name, _group):
        super(StudentTextFileRepository, self).add_new_student(__id, _name, _group)
        self._save_file()

    def remove_student_by_id(self, __id):
        super(StudentTextFileRepository, self).remove_student_by_id(__id)
        self._save_file()

    # def update_name(self, student_id, student_name):
    #     super(StudentTextFileRepository, self).update_name(student_id, student_name)
    #     self._save_file()
    #
    # def update_group(self, student_id, student_group):
    #     super(StudentTextFileRepository, self).update_group(student_id, student_group)
    #     self._save_file()

    def generate_student(self):
        super(StudentTextFileRepository, self).generate_student()
        self._save_file()


class StudentBinaryFileRepository(StudentRepository):
    def __init__(self):
        super().__init__()
        self._file_name = r"C:\Users\Irina\Desktop\PycharmProjects\a9-ScortarIrina\src\Files\BinaryFiles\students.bin"
        self._clear_file()
        # self._load_file()

    # function which reads from the list
    # def _load_file(self):
    #     try:
    #         file = open(self._file_name, "rb")  # rb = read binary
    #         self._list_of_students = pickle.load(file)
    #         file.close()
    #     except EOFError:
    #         pass
    #     file.close()

    # function which writes to the list
    def _save_file(self):
        file = open(self._file_name, "wb")  # wb = write binary
        pickle.dump(self._list_of_students, file)
        file.close()

    # function clears list every time the program restarts
    def _clear_file(self):
        file = open(self._file_name, "wb")
        file.truncate()
        file.close()

    def add_new_student(self, id, name, group):
        super(StudentBinaryFileRepository, self).add_new_student(id, name, group)
        self._save_file()

    def remove_student_by_id(self, id):
        super(StudentBinaryFileRepository, self).remove_student_by_id(id)
        self._save_file()

    # def update_name(self, student_id, student_name):
    #     super(StudentBinaryFileRepository, self).update_name(student_id, student_name)
    #     self._save_file()

    def update_group(self, student_id, student_group):
        super(StudentBinaryFileRepository, self).update_group(student_id, student_group)
        self._save_file()

    def generate_student(self):
        super(StudentBinaryFileRepository, self).generate_student()
        self._save_file()

    def id_not_unique(self, id):
        return super(StudentBinaryFileRepository, self).id_not_unique(id)

    def get_student_by_id(self, id):
        return super(StudentBinaryFileRepository, self).get_student_by_id(id)

    def get_list_of_students(self):
        return super(StudentBinaryFileRepository, self).get_list_of_students()
