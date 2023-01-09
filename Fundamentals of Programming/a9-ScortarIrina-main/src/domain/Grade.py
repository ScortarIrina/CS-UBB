class Grade:
    def __init__(self, __assignment_id, __student_id, _grade_value):
        self.__assignment_id = __assignment_id
        self.__student_id = __student_id
        self._grade_value = _grade_value

    @property
    def assignment_id(self):
        return self.__assignment_id

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, value):
        self._grade_value = value

    def __str__(self):
        return 'ASSIGNMENT ID: ' + str(self.__assignment_id) + '     STUDENT ID: ' + str(self.__student_id) + \
            '     GRADE VALUE: ' + str(self._grade_value)
