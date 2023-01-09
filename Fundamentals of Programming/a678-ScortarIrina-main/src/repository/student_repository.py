from src.domain.entities import Student
from random import randint
import random


class UserExceptionStudent(Exception):
    pass


class StudentRepository(object):
    def __init__(self):
        self.__list_of_students = []

    def generate_students(self):
        names = ["Irina", "Andrei", "Tudor", "Stefan", "Lucia", "Paul", "Monica", "Andreea", "Sonia", "Ioana",
                 "Victor", "Alex", "Maria", "Ana"]
        list_ids = random.sample(range(1, 200), 10)
        for i in range(10):
            self.__list_of_students.append(Student(list_ids[i], random.choice(names), randint(100, 999)))

    def get_list_of_students(self):
        return self.__list_of_students

    def get_student_by_id(self, id):
        for student in self.__list_of_students:
            if int(student.id) == int(id):
                return student
        return None

    def id_not_unique(self, id):
        for student in self.__list_of_students:
            if int(student.id) == int(id):
                return True
        return False

    def add_new_student(self, id, name, group):
        if self.id_not_unique(id):
            raise UserExceptionStudent("Id must be unique")
        elif type(id) is str and (not id.isnumeric() or float(id) != int(id)):
            raise UserExceptionStudent("Id must be a natural number")
        elif len(name) <= 0:
            raise UserExceptionStudent("Name must not be empty")
        elif not name.isalpha():
            raise UserExceptionStudent("Invalid name")
        elif type(group) is str and (not group.isnumeric() or float(group) != int(group) or int(group) < 100 or int(group) > 999):
            raise UserExceptionStudent("Group number must be an integer between 100 and 999")

        self.__list_of_students.append(Student(id, name, group))

    def remove_student_by_id(self, student_id):
        if type(student_id) is str and (not student_id.isnumeric() or float(student_id) != int(student_id)):
            raise UserExceptionStudent("Id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_students) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_students[index_go_through_list].id) == int(student_id):
                self.__list_of_students.pop(index_go_through_list)
                length_of_list = len(self.__list_of_students) - 1
                index_go_through_list -= 1
            index_go_through_list += 1

    def update_name(self, student_id, student_name):
        if len(student_name) <= 0:
            raise UserExceptionStudent("Name must not be empty")
        if not student_name.isalpha():
            raise UserExceptionStudent("Invalid name")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_students) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_students[index_go_through_list].id) == int(student_id):
                self.__list_of_students[index_go_through_list].name = student_name
                index_go_through_list = length_of_list
            index_go_through_list += 1

    def update_group(self, student_id, student_group):
        if not student_group.isnumeric() or float(student_group) != int(student_group) or int(student_group) < 100 or \
                int(student_group) > 999:
            raise UserExceptionStudent("Group number must be an integer between 100 and 999")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_students) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_students[index_go_through_list].id) == int(student_id):
                self.__list_of_students[index_go_through_list].group = student_group
                index_go_through_list = length_of_list
            index_go_through_list += 1
