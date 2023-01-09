class Student:

    def __init__(self, id, name, group):  # constructor for the fields
        self.__id = id
        self.__name = name
        self.__group = group

    # check if id is unique
    @property
    def id(self):
        return self.__id

    def set_id(self, new_student_id):
        if not new_student_id.isnumeric() or float(new_student_id) != int(new_student_id):
            raise ValueError("The id must be a positive integer number")
        self.__id = new_student_id

    @property
    def name(self):
        return self.__name

    def set_name(self, new_student_name):
        if not new_student_name.isalpha():
            raise ValueError("The name must be a string of letters")
        self.__name = new_student_name

    @property
    def group(self):
        return self.__group

    def set_group(self, new_student_group):
        if not new_student_group.isnumeric() or float(new_student_group) != int(new_student_group) or int(new_student_group) == 0:
            raise ValueError("The group must be a positive integer number")
        self.__group = new_student_group

    def __str__(self):
        return 'id: ' + str(self.__id) + '     name: ' + str(self.__name) + '     group: ' + str(self.__group)

    def __int__(self):
        return int(self.__group)


