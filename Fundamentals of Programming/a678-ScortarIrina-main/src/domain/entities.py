"""
Classes for:

    ~ Student: student_id, name, group
    ~ Assignment: assignment_id, description, deadline
    ~ Grade: assignment_id, student_id, grade_value
"""
import datetime


class Student:
    def __init__(self, id, name, group):
        if type(id) is str:
            id = int(id)
        if type(group) is str:
            group = int(group)
        self.__id = id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        self.__group = value

    def __str__(self):
        return 'ID: ' + str(self.__id) + '     NAME: ' + str(self.__name) + '     GROUP: ' + str(self.__group)


class Assignment:
    def __init__(self, id, description, deadline):
        if type(deadline) == str:
            deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d')
        if type(id) == str:
            id = int(id)

        self.__id = id
        self.__description = description
        self.__deadline = deadline

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, value):
        self.__deadline = value

    def __str__(self):
        return 'ID: ' + str(self.__id) + '     DESCRIPTION: ' + str(self.__description) + '     DEADLINE: ' + \
               str(self.__deadline)


class Grade:
    def __init__(self, assignment_id, student_id, grade_value):
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def assignment_id(self):
        return self.__assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        self.__assignment_id = value

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, value):
        self.__grade_value = value

    def __str__(self):
        return 'ASSIGNMENT ID: ' + str(self.__assignment_id) + '     STUDENT ID: ' + str(self.__student_id) + \
            '     GRADE VALUE: ' + str(self.__grade_value)
