"""
Services:
    - add student
    - print all students
    - filter
    - undo
"""

from src.domain.student import Student
from random import randint
import random
import copy


class Services:

    def __init__(self):
        self.__list_of_students = []
        self.__stack_of_lists_of_students = []

    def generate_students(self):
        names = ["Irina", "Andrei", "Tudor", "Stefan", "Lucia", "Paul", "Monica", "Andreea", "Sonia", "Ioana", "Victor", "Alex", "Maria", "Ana"]
        ids = random.sample(range(1, 200), 10)
        for i in range(10):
            self.__list_of_students.append(Student(ids[i], random.choice(names), randint(100, 999)))
        self.__stack_of_lists_of_students.append(copy.deepcopy(self.__list_of_students))

    def get_list_of_students(self):
        return self.__list_of_students

    def id_not_unique(self, id):
        for student in self.__list_of_students:
            if student.id == id:
                return True
        return False

    def add_new_student(self, id, name, group):
        """
        This function adds a new student (id, name, group) to the list of students
        User input => every new student

        :param id: id of the student
        :param name: name of the student
        :param group: group of the student
        :return:
        """
        if self.id_not_unique(id):
            raise ValueError("Id must be unique")
        if not id.isnumeric() or float(id) != int(id):
            raise ValueError("Id must be a natural number")
        if len(name) <= 0:
            raise ValueError("Name must not be empty")
        if not name.isalpha():
            raise ValueError("Invalid name")
        if not group.isnumeric() or float(group) != int(group) or int(group) < 100 or int(group) > 999:
            raise ValueError("Group number must be an integer between 100 and 999")

        self.__list_of_students.append(Student(id, name, group))
        self.__stack_of_lists_of_students.append(copy.deepcopy(self.__list_of_students))

    def filter_list(self, user_command_group):
        if int(user_command_group) < 100 or int(user_command_group) > 999:
            raise ValueError("Group number must be in range 100-999")
        index_go_through_list = 0
        length_of_list = len(self.__list_of_students) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_students[index_go_through_list].group) == int(user_command_group):
                self.__list_of_students.pop(index_go_through_list)
                length_of_list = len(self.__list_of_students) - 1
                index_go_through_list -= 1
            index_go_through_list += 1
        self.__stack_of_lists_of_students.append(copy.deepcopy(self.__list_of_students))

    def undo_last_operation(self):
        length_stack = len(self.__stack_of_lists_of_students) - 1
        self.__stack_of_lists_of_students.pop(length_stack)
        self.__list_of_students = copy.deepcopy(self.__stack_of_lists_of_students[length_stack - 1])

    def undo(self):
        if len(self.__stack_of_lists_of_students) == 1:
            raise ValueError("Cannot undo operation")
        else:
            self.undo_last_operation()
