from src.domain.entities import Grade


class UserExceptionGrade(Exception):
    pass


class GradeRepository:
    def __init__(self):
        self.__list_of_grades = []

    def get_list_of_grades(self):
        return self.__list_of_grades

    def get_assignment_by_id(self, id):
        for grade in self.__list_of_grades:
            if grade.assignment_id == id:
                return grade
        return None

    def get_grade_by_student_id(self, id):
        for grade in self.__list_of_grades:
            if grade.student_id == id:
                return grade
        return None

    def student_does_not_have_given_assignment(self, assignment_id, student_id):
        for grade in self.__list_of_grades:
            if grade.student_id == student_id and grade.assignment_id == assignment_id:
                return False
        return True

    def give_assignment_to_student(self, assignment_id, student_id, grade):
        self.__list_of_grades.append(Grade(assignment_id, student_id, grade))

    def get_list_graded_assignments(self):
        list_of_graded_assignments = []
        for grade in self.__list_of_grades:
            if grade.grade_value != 0:
                list_of_graded_assignments.append(grade)

        return list_of_graded_assignments

    def get_list_ungraded_assignments(self):
        list_of_ungraded_assignments = []
        for grade in self.__list_of_grades:
            if int(grade.grade_value) == 0:
                list_of_ungraded_assignments.append(grade)

        return list_of_ungraded_assignments

    def get_list_graded_assignments_of_student(self, student_id):
        if not student_id.isnumeric() or float(student_id) != int(student_id):
            raise UserExceptionGrade("Student id must be a natural number")

        list_of_graded_assignments_of_student = []
        for grade in self.__list_of_grades:
            if grade.grade_value != 0 and int(grade.student_id) == int(student_id):
                list_of_graded_assignments_of_student.append(grade)

        return list_of_graded_assignments_of_student

    def get_list_ungraded_assignments_of_student(self, student_id):
        if not student_id.isnumeric() or float(student_id) != int(student_id):
            raise UserExceptionGrade("Student id must be a natural number")

        list_of_ungraded_assignments_of_student = []
        for grade in self.__list_of_grades:
            if int(grade.grade_value) == 0 and int(grade.student_id) == int(student_id):
                list_of_ungraded_assignments_of_student.append(grade)

        return list_of_ungraded_assignments_of_student

    def remove_assignment_from_grades_by_id(self, assignment_id):
        if not assignment_id.isnumeric() or float(assignment_id) != int(assignment_id):
            raise UserExceptionGrade("Assignment id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_grades) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_grades[index_go_through_list].assignment_id) == int(assignment_id):
                self.__list_of_grades.pop(index_go_through_list)
                length_of_list = len(self.__list_of_grades) - 1
                index_go_through_list -= 1
            index_go_through_list += 1

    def remove_student_from_grades_by_id(self, student_id):
        if not student_id.isnumeric() or float(student_id) != int(student_id):
            raise UserExceptionGrade("Student id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self.__list_of_grades) - 1

        while index_go_through_list <= length_of_list:
            if int(self.__list_of_grades[index_go_through_list].student_id) == int(student_id):
                self.__list_of_grades.pop(index_go_through_list)
                length_of_list = len(self.__list_of_grades) - 1
                index_go_through_list -= 1
            index_go_through_list += 1
