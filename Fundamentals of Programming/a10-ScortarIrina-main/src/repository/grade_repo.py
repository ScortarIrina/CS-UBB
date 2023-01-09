import pickle

from domain.data_structure import Iterable
from src.domain.grade import Grade


class GradeRepositoryException(Exception):
    pass


class GradeRepository:
    def __init__(self):
        self._list_of_grades = Iterable()

    def get_list_of_grades(self):
        return self._list_of_grades.get_list()

    def get_assignment_by_id(self, id):
        for grade in self._list_of_grades:
            if grade.assignment_id == id:
                return grade
        return None

    def get_grade_by_student_id(self, id):
        for grade in self._list_of_grades:
            if grade.student_id == id:
                return grade
        return None

    def student_does_not_have_given_assignment(self, assignment_id, student_id):
        for grade in self._list_of_grades:
            if grade.student_id == student_id and grade.assignment_id == assignment_id:
                return False
        return True

    def give_assignment_to_student(self, assignment_id, student_id, grade):
        self._list_of_grades.append(Grade(assignment_id, student_id, grade))

    # def delete_assignment_of_student(self, assignment_id, student_id):
    #     for grade in self._list_of_grades:
    #         if grade.assignment_id == assignment_id and grade.student_id == student_id:
    #             deleted_grade = grade
    #             del self._list_of_grades[grade]
    #             return deleted_grade

    def get_list_graded_assignments(self):
        list_of_graded_assignments = []
        for grade in self._list_of_grades:
            if grade.grade_value != 0:
                list_of_graded_assignments.append(grade)

        return list_of_graded_assignments

    def get_list_ungraded_assignments(self):
        list_of_ungraded_assignments = []
        for grade in self._list_of_grades:
            if int(grade.grade_value) == 0:
                list_of_ungraded_assignments.append(grade)

        return list_of_ungraded_assignments

    def get_list_graded_assignments_of_student(self, student_id):
        if type(student_id) is str and (not student_id.isnumeric() or float(student_id) != int(student_id)):
            raise GradeRepositoryException("Id must be a natural number")

        list_of_graded_assignments_of_student = []
        for grade in self._list_of_grades:
            if grade.grade_value != 0 and int(grade.student_id) == int(student_id):
                list_of_graded_assignments_of_student.append(grade)

        return list_of_graded_assignments_of_student

    def get_list_ungraded_assignments_of_student(self, student_id):
        if type(student_id) is str and (not student_id.isnumeric() or float(student_id) != int(student_id)):
            raise GradeRepositoryException("Id must be a natural number")

        list_of_ungraded_assignments_of_student = []
        for grade in self._list_of_grades:
            if int(grade.grade_value) == 0 and int(grade.student_id) == int(student_id):
                list_of_ungraded_assignments_of_student.append(grade)

        return list_of_ungraded_assignments_of_student

    def remove_assignment_from_grades_by_id(self, assignment_id):
        index_go_through_list = 0
        length_of_list = len(self._list_of_grades) - 1

        while index_go_through_list <= length_of_list:
            if int(self._list_of_grades[index_go_through_list].assignment_id) == int(assignment_id):
                self._list_of_grades.pop(index_go_through_list)
                length_of_list = len(self._list_of_grades) - 1
                index_go_through_list -= 1
            index_go_through_list += 1

    def remove_student_from_grades_by_id(self, student_id):
        if type(student_id) is str and (not student_id.isnumeric() or float(student_id) != int(student_id)):
            raise GradeRepositoryException("Id must be a natural number")

        index_go_through_list = 0
        length_of_list = len(self._list_of_grades) - 1

        while index_go_through_list <= length_of_list:
            if int(self._list_of_grades[index_go_through_list].student_id) == int(student_id):
                self._list_of_grades.pop(index_go_through_list)
                length_of_list = len(self._list_of_grades) - 1
                index_go_through_list -= 1
            index_go_through_list += 1


class GradeTextFileRepository(GradeRepository):
    def __init__(self):
        super().__init__()
        self._file_name = r"C:\Users\Irina\Desktop\PycharmProjects\a10-ScortarIrina\src\files\text_files\grades.txt"
        self._clear_file()

    # function to write to file
    def _save_file(self):
        file = open(self._file_name, "wt")

        for grade in self._list_of_grades:
            file.write("assignment id: " + str(grade.assignment_id) + '     student id: ' + str(grade.student_id) + '     grade:' + str(grade.grade_value) + "\n")

        file.close()

    def _clear_file(self):
        file = open(self._file_name, "wt")
        file.truncate()
        file.close()

    def get_list_of_grades(self):
        return super(GradeTextFileRepository, self).get_list_of_grades()

    def get_assignment_by_id(self, id):
        return super(GradeTextFileRepository, self).get_assignment_by_id(id)

    def get_grade_by_student_id(self, id):
        return super(GradeTextFileRepository, self).get_grade_by_student_id(id)

    def student_does_not_have_given_assignment(self, assignment_id, student_id):
        return super(GradeTextFileRepository, self).student_does_not_have_given_assignment(assignment_id, student_id)

    def give_assignment_to_student(self, assignment_id, student_id, grade):
        super(GradeTextFileRepository, self).give_assignment_to_student(assignment_id, student_id, grade)
        self._save_file()

    # def get_list_graded_assignments(self):
    #     return super(GradeTextFileRepository, self).get_list_graded_assignments()
    #
    # def get_list_ungraded_assignments(self):
    #     return super(GradeTextFileRepository, self).get_list_ungraded_assignments()

    def get_list_graded_assignments_of_student(self, student_id):
        return super(GradeTextFileRepository, self).get_list_graded_assignments_of_student(student_id)

    # def get_list_ungraded_assignments_of_student(self, student_id):
    #     return super(GradeTextFileRepository, self).get_list_ungraded_assignments_of_student(student_id)

    def remove_assignment_from_grades_by_id(self, assignment_id):
        super(GradeTextFileRepository, self).remove_assignment_from_grades_by_id(assignment_id)
        self._save_file()

    def remove_student_from_grades_by_id(self, student_id):
        super(GradeTextFileRepository, self).remove_student_from_grades_by_id(student_id)
        self._save_file()

    # def delete_assignment_of_student(self, assignment_id, student_id):
    #     super(GradeTextFileRepository, self).delete_assignment_of_student(assignment_id, student_id)
    #     self._save_file()


class GradeBinaryFileRepository(GradeRepository):
    def __init__(self):
        super().__init__()
        self._file_name = r"C:\Users\Irina\Desktop\PycharmProjects\a10-ScortarIrina\src\files\text_files\grades.bin"
        self._clear_file()

    def _save_file(self):
        file = open(self._file_name, "wb")
        pickle.dump(self._list_of_grades, file)
        file.close()

    def _clear_file(self):
        file = open(self._file_name, "wt")
        file.truncate()
        file.close()

    def get_list_of_grades(self):
        return super(GradeBinaryFileRepository, self).get_list_of_grades()

    def get_assignment_by_id(self, id):
        return super(GradeBinaryFileRepository, self).get_assignment_by_id(id)

    def get_grade_by_student_id(self, id):
        return super(GradeBinaryFileRepository, self).get_grade_by_student_id(id)

    def student_does_not_have_given_assignment(self, assignment_id, student_id):
        return super(GradeBinaryFileRepository, self).student_does_not_have_given_assignment(assignment_id, student_id)

    def give_assignment_to_student(self, assignment_id, student_id, grade):
        super(GradeBinaryFileRepository, self).give_assignment_to_student(assignment_id, student_id, grade)
        self._save_file()

    def get_list_graded_assignments(self):
        return super(GradeBinaryFileRepository, self).get_list_graded_assignments()

    def get_list_ungraded_assignments(self):
        return super(GradeBinaryFileRepository, self).get_list_ungraded_assignments()

    def get_list_graded_assignments_of_student(self, student_id):
        return super(GradeBinaryFileRepository, self).get_list_graded_assignments_of_student(student_id)

    def get_list_ungraded_assignments_of_student(self, student_id):
        return super(GradeBinaryFileRepository, self).get_list_ungraded_assignments_of_student(student_id)

    def remove_assignment_from_grades_by_id(self, assignment_id):
        super(GradeBinaryFileRepository, self).remove_assignment_from_grades_by_id(assignment_id)
        self._save_file()

    def remove_student_from_grades_by_id(self, student_id):
        super(GradeBinaryFileRepository, self).remove_student_from_grades_by_id(student_id)
        self._save_file()

