import copy

from src.repository.grade_repository import GradeRepository
from src.repository.grade_repository import UserExceptionGrade
from datetime import datetime


class GradeService:
    def __init__(self, student_repository, assignment_repository):
        self.__grade_repository = GradeRepository()
        self.__student_repository = student_repository
        self.__assignment_repository = assignment_repository

    def get_list_of_grades(self):
        return self.__grade_repository.get_list_of_grades()

    def student_does_not_have_given_assignment(self, assignment_id, student_id):
        """
        This function checks if the student with the given id already has to do that assignment
        :param assignment_id:
        :param student_id:
        :return: True if student does not have that assignment, False otherwise
        """
        for grade in self.__grade_repository.get_list_of_grades():
            if grade.student_id == student_id and grade.assignment_id == assignment_id:
                return False
        return True

    def give_assignment_to_student(self, assignment_id, student_id):
        """
        This function makes the relation between a student and his assignments
        :param assignment_id:
        :param student_id:
        :return:
        """
        if not student_id.isnumeric() or float(student_id) != int(student_id):
            raise UserExceptionGrade('Invalid student id')
        if not assignment_id.isnumeric() or float(assignment_id) != int(assignment_id):
            raise UserExceptionGrade('Invalid assigment id')
        if not self.__student_repository.id_not_unique(student_id):
            raise UserExceptionGrade('Student id does not exist')
        if not self.__assignment_repository.id_not_unique(assignment_id):
            raise UserExceptionGrade('Assignment id does not exist')
        if not self.student_does_not_have_given_assignment(assignment_id, student_id):
            raise UserExceptionGrade('This student already has the given assignment')

        self.__grade_repository.give_assignment_to_student(assignment_id, student_id, 0)

    def give_assignment_to_group(self, assignment_id, group_number):
        """
        This function parses through the list of students
        If it finds a student in a certain group that doesn't already have that assignment, it calls the function
        give_assignment_to_student in order to add them to the list
        :param assignment_id:
        :param group_number:
        :return:
        """
        if not assignment_id.isnumeric() or float(assignment_id) != int(assignment_id):
            raise UserExceptionGrade('Invalid assigment id')
        if not self.__assignment_repository.id_not_unique(assignment_id):
            raise UserExceptionGrade('Assignment id does not exist')
        if not group_number.isnumeric() or float(group_number) != int(group_number):
            raise UserExceptionGrade('The group number must be a natural number')

        for student in self.__student_repository.get_list_of_students():
            if int(student.group) == int(group_number) and self.student_does_not_have_given_assignment(assignment_id, student.id):
                self.give_assignment_to_student(assignment_id, str(student.id))

    def get_list_ungraded_assignments(self):
        return self.__grade_repository.get_list_ungraded_assignments()

    def get_list_ungraded_assignments_of_student(self, student_id):
        return self.__grade_repository.get_list_ungraded_assignments_of_student(student_id)

    def grade_assignment(self, assignment_id_to_grade, student_id_to_grade, given_grade):
        if not given_grade.isnumeric() or given_grade.isnumeric() and int(given_grade) <= 1 or \
                given_grade.isnumeric() and int(given_grade) > 10:
            raise UserExceptionGrade('Grade must be a natural number between 1 and 10')
        if not assignment_id_to_grade.isnumeric() or float(assignment_id_to_grade) != int(assignment_id_to_grade):
            raise UserExceptionGrade('Assignment id must be a natural number')
        if not student_id_to_grade.isnumeric() or float(student_id_to_grade) != int(student_id_to_grade):
            raise UserExceptionGrade("Student id must be a natural number")
        if self.__student_repository.get_student_by_id(int(student_id_to_grade)) is None:
            raise UserExceptionGrade("There is no student with this id")
        if self.__grade_repository.get_grade_by_student_id(student_id_to_grade) is None:
            raise UserExceptionGrade("The student doesn't have the given assignment")

        for grade in self.get_list_ungraded_assignments():
            if int(grade.assignment_id) == int(assignment_id_to_grade) and \
                    int(grade.student_id) == int(student_id_to_grade):
                grade.grade_value = given_grade

    def remove_assignment_from_grades_by_id(self, user_command_assignment_id):
        self.__grade_repository.remove_assignment_from_grades_by_id(user_command_assignment_id)

    def remove_student_from_grades_by_id(self, user_command_student_id):
        self.__grade_repository.remove_student_from_grades_by_id(user_command_student_id)

    @staticmethod
    def get_grade(grade):
        return int(grade.grade_value)

    def get_list_of_students_with_given_assignment_ordered_by_grade(self, assignment_id):
        # All students who received a given assignment, ordered descending by grade.
        if not assignment_id.isnumeric() or float(assignment_id) != int(assignment_id):
            raise UserExceptionGrade('Assignment id must be a natural number')
        if self.__grade_repository.get_assignment_by_id(assignment_id) is None:
            raise UserExceptionGrade('There is no student who has this assignment')
        if self.__grade_repository.get_assignment_by_id(assignment_id) not in self.__grade_repository.get_list_graded_assignments():
            raise UserExceptionGrade('This assignment is not graded yet')

        list_of_graded_assignments = self.__grade_repository.get_list_graded_assignments()
        for grade in list_of_graded_assignments:
            if int(grade.assignment_id) != int(assignment_id):
                del grade
        return sorted(list_of_graded_assignments, key=self.get_grade, reverse=True)

    def late_assignment(self, assignment_id):
        current_date = datetime.today()
        assignment = self.__assignment_repository.get_assignment_by_id(assignment_id)
        assignment_deadline = assignment.deadline
        if current_date > assignment_deadline:
            return True
        else:
            return False

    def get_student_passed_deadline_assignments(self):
        # All students who are late in handing in at least one assignment.
        list_of_ungraded_assignments = self.get_list_ungraded_assignments()
        list_of_students_late_assignment = []
        for grade in list_of_ungraded_assignments:
            if self.__assignment_repository.get_assignment_by_id(grade.assignment_id) is not None and self.late_assignment(grade.assignment_id) is True:
                student = self.__student_repository.get_student_by_id(int(grade.student_id))
                if student is not None:
                    list_of_students_late_assignment.append(student)

        if len(list_of_students_late_assignment) == 0:
            raise UserExceptionGrade('All students have up to date assignments')

        return list_of_students_late_assignment

    def get_list_graded_assignments_of_student(self, student_id):
        return self.__grade_repository.get_list_graded_assignments_of_student(student_id)

    def get_average_of_student_grades(self, student_id):
        list_grades_of_student = self.get_list_graded_assignments_of_student(student_id)
        sum_of_grades = 0
        for grade in list_grades_of_student:
            sum_of_grades += int(grade.grade_value)

        average = sum_of_grades/len(list_grades_of_student)

        return average

    def get_list_average_grade_all_students(self):
        list_average_grade_all_students = []
        added_student_ids = []
        for grade in self.__grade_repository.get_list_graded_assignments():
            if grade.student_id not in added_student_ids:
                list_average_grade_all_students.append('student id: ' + grade.student_id + '     average grade: ' + str(self.get_average_of_student_grades(grade.student_id)))
                added_student_ids.append(grade.student_id)

        list_average_grade_all_students.sort(reverse=False)
        return copy.deepcopy(list_average_grade_all_students)
