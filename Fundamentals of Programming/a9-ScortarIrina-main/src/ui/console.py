import configparser

from src.repository.grade_repo import GradeTextFileRepository, GradeRepositoryException, GradeBinaryFileRepository, \
    GradeRepository
from src.services.students_service import StudentService
from src.services.assignments_service import AssignmentService
from src.services.grades_service import GradeService
from src.repository.student_repo import StudentRepositoryException, StudentRepository, StudentTextFileRepository, StudentBinaryFileRepository
from src.repository.assignment_repo import AssignmentRepositoryException, AssignmentRepository, AssignmentTextFileRepository, AssignmentBinaryFileRepository
from src.services.undo_redo_service import UndoRedoService, UndoRedoExceptions


class Ui:

    def __init__(self):
        self._undo_redo_service = UndoRedoService()
        config = configparser.ConfigParser()
        config.read("settings.properties")
        self._repo = (config.get("CONFIG", "repository"))

        if self._repo == "inmemory":
            student = StudentRepository()
            assignment = AssignmentRepository()
            grade = GradeRepository()

        elif self._repo == "TextFiles":
            student = StudentTextFileRepository()
            assignment = AssignmentTextFileRepository()
            grade = GradeTextFileRepository()

        elif self._repo == "BinaryFiles":
            student = StudentBinaryFileRepository()
            assignment = AssignmentBinaryFileRepository()
            grade = GradeBinaryFileRepository()

        self._students_service = StudentService(student, self._undo_redo_service)
        self._assignments_service = AssignmentService(assignment, self._undo_redo_service)
        self._grades_service = GradeService(grade, student, assignment, self._undo_redo_service)

    @staticmethod
    def print_menu():
        print("\t0. Exit\n"
              "\t1. Add a student\n"
              "\t2. Remove student by id\n"
              "\t3. Add an assignment\n"
              "\t4. Remove assignment by id\n"
              "\t5. Update list of students\n"
              "\t6. Update list of assignments\n"
              "\t7. Print list of students\n"
              "\t8. Print list of assignments\n"
              "\t9. Give an assignment to a student\n"
              "\t10. Give an assignment to a group of students\n"
              "\t11. Print list of students with their corresponding assignments\n"
              "\t12. Grade student for a given assignment\n"
              "\t13. Statistics\n"
              "\t14. Undo\n"
              "\t15. Redo\n")

    @staticmethod
    def print_submenu_for_statistics():
        print('\t\t1. All students who received a given assignment, ordered descending by grade\n'
              '\t\t2. All students who are late in handing in at least one assignment\n'
              '\t\t3. Students with the best school situation, sorted in descending order of the average grade received for all graded assignments.\n')

    @staticmethod
    def print_submenu_for_update_student_by_id():
        print("\t\t1. Update name\n"
              "\t\t2. Update group\n")

    @staticmethod
    def print_submenu_for_update_assignment_by_id():
        print("\t\t1. Update description\n"
              "\t\t2. Update deadline\n")

    def display_list_of_students(self):
        students_service = self._students_service
        for i in students_service.get_list_of_students():
            print(str(i))

    def display_list_of_assignments(self):
        try:
            assignments_service = self._assignments_service
            for i in assignments_service.get_list_of_assignments():
                print(str(i))
        except ValueError as ve:
            print(str(ve))

    def display_list_of_grades(self):
        try:
            grades_service = self._grades_service
            for i in grades_service.get_list_of_grades():
                print(str(i))
        except ValueError as ve:
            print(str(ve))

    def add_new_student(self):
        try:
            user_command_id = input('\tstudent id: ')
            user_command_name = input('\tstudent name: ')
            user_command_group = input('\tstudent group: ')
            self._students_service.add_new_student(user_command_id, user_command_name, user_command_group)
        except StudentRepositoryException as ue:
            print(ue)

    def add_new_assignment(self):
        try:
            user_command_id = input('\tassignment id: ')
            user_command_description = input('\tassignment description: ')
            user_command_deadline = input('\tassignment deadline: ')
            self._assignments_service.add_new_assignment(user_command_id, user_command_description,
                                                         user_command_deadline)
        except AssignmentRepositoryException as ue:
            print(ue)

    def update_student_by_id(self):
        user_command_id = int(input('\tid of the student whose information you want to update: '))
        if not self._students_service.id_not_unique(user_command_id):
            print('There is no student with this id')
        else:
            self.print_submenu_for_update_student_by_id()
            user_option = input('\tChoose an option (1 or 2): ')
            if not user_option.isnumeric():
                print('Invalid input')
            else:
                user_option = int(user_option)
                if user_option == 1:
                    try:
                        user_command_name = input('\tUpdated name: ')
                        student = self._students_service.get_student_by_id(user_command_id)
                        self._students_service.update_name(user_command_id, user_command_name)
                    except StudentRepositoryException as ue:
                        print(ue)
                elif user_option == 2:
                    try:
                        user_command_group = input('\tUpdated group: ')
                        student = self._students_service.get_student_by_id(user_command_id)
                        self._students_service.update_group(user_command_id, user_command_group)
                    except StudentRepositoryException as ue:
                        print(ue)
                else:
                    print('\tInvalid input')

    def update_assignment_by_id(self):
        user_command_id = int(input('\tid of the assignment whose information you want to update: '))
        if not self._assignments_service.id_not_unique(user_command_id):
            print('There is no assignment with this id')
        else:
            self.print_submenu_for_update_assignment_by_id()
            user_option = input('\tChoose an option (1 or 2): ')
            if not user_option.isnumeric():
                print('Invalid input')
            else:
                user_option = int(user_option)
                if user_option == 1:
                    try:
                        user_command_description = input('\tUpdated description: ')
                        assignment = self._assignments_service.get_assignment_by_id(user_command_id)
                        self._assignments_service.update_description(user_command_id, user_command_description)
                    except StudentRepositoryException as ue:
                        print(ue)
                elif user_option == 2:
                    try:
                        user_command_deadline = input('\tUpdated deadline: ')
                        assignment = self._assignments_service.get_assignment_by_id(user_command_id)
                        self._assignments_service.update_deadline(user_command_id, user_command_deadline)
                    except ValueError as ve:
                        print(str(ve))
                else:
                    print('\tInvalid input')

    def remove_student_by_id(self):
        try:
            user_command_student_id = input('\tid of the student you want to remove: ')
            student = self._students_service.get_student_by_id(user_command_student_id)
            self._students_service.remove_student_by_id(user_command_student_id)
            # self._grades_service.remove_student_from_grades_by_id(user_command_student_id)
        except StudentRepositoryException as ue:
            print(ue)

    def remove_assignment_by_id(self):
        try:
            user_command_assignment_id = input('\tid of the assignment you want to remove: ')
            assignment = self._assignments_service.get_assignment_by_id(user_command_assignment_id)
            self._assignments_service.remove_assignment_by_id(user_command_assignment_id)
            # self._grades_service.remove_assignment_from_grades_by_id(user_command_assignment_id)
        except AssignmentRepositoryException as ue:
            print(ue)

    def give_assignment_to_student(self):
        try:
            user_command_student_id = input('\tid of the student you want to give an assignment to: ')
            user_command_assignment_id = input('\tid of the assignment you want to give: ')
            self._grades_service.give_assignment_to_student(user_command_assignment_id, user_command_student_id)
        except GradeRepositoryException as ue:
            print(ue)

    def give_assignment_to_group(self):
        try:
            user_command_group_number = input('\tgroup number you want to give an assignment to: ')
            user_command_assignment_id = input('\tid of the assignment you want to give: ')
            self._grades_service.give_assignment_to_group(user_command_assignment_id, user_command_group_number)
        except GradeRepositoryException as ue:
            print(ue)

    def grade_student_for_given_assignment(self):
        """
        Grade student for a given assignment. When grading, the program must allow the user to select the assignment
        that is graded, from the student’s list of ungraded assignments. A student’s grade for a given assignment cannot
        be changed
        """
        try:
            student_id_to_grade = input('\tStudent id you want to grade: ')
            if len(self._grades_service.get_list_ungraded_assignments_of_student(student_id_to_grade)) == 0:
                print("This student has no assignments")
            else:
                print('These are the ungraded assignments of chosen student: ')
                grades_service = self._grades_service
                for i in grades_service.get_list_ungraded_assignments_of_student(student_id_to_grade):
                    print('\t', str(i))
                assignment_id_to_grade = input('\n\tAssignment id you want to grade: ')
                given_grade = input('\tGrade you want to give: ')
                self._grades_service.grade_assignment(assignment_id_to_grade, student_id_to_grade, given_grade)
        except GradeRepositoryException as ue:
            print(str(ue))

    @staticmethod
    def print_statistics(list_for_statistic):
        for grade in list_for_statistic:
            print('\t\t' + str(grade))

    def make_statistics(self):
        self.print_submenu_for_statistics()
        user_option = input('\tChoose an option (1-3): ')

        if not user_option.isnumeric():
            print('Invalid input')

        elif int(user_option) == 1:
            # All students.bin who received a given assignment, ordered descending by grade.
            try:
                user_command_assignment_id = input('\n\tAssignment id to order by: ')
                list_for_statistics = self._grades_service.get_list_of_students_with_given_assignment_ordered_by_grade(user_command_assignment_id)
                print('\n\tStudents who received a given assignment, ordered descending by grade: ')
                self.print_statistics(list_for_statistics)
            except GradeRepositoryException as ue:
                print(ue)

        elif int(user_option) == 2:
            # All students.bin who are late in handing in at least one assignment.
            try:
                list_for_statistics = self._grades_service.get_student_passed_deadline_assignments()
                print('\n\tStudents who are late in handing in at least one assignment: ')
                self.print_statistics(list_for_statistics)
            except GradeRepositoryException as ue:
                print(ue)

        elif int(user_option) == 3:
            # Students with the best school situation, sorted in descending order of the average grade received for all graded assignments.
            try:
                list_for_statistics = self._grades_service.get_list_average_grade_all_students()
                print('\n\tStudents with the best school situation: ')
                self.print_statistics(list_for_statistics)
            except GradeRepositoryException as ue:
                print(ue)
        else:
            print('Invalid input')

    def start(self):

        self._students_service.generate_students()
        self._assignments_service.generate_assignments()

        while True:
            try:
                print('\nMenu options')
                self.print_menu()
                user_option = input('\nChoose an option (0-13): ')

                if not user_option.isnumeric():
                    print('Invalid input')
                else:
                    user_option = int(user_option)

                    # exit program
                    if user_option == 0:
                        return

                    # add a student
                    elif user_option == 1:
                        try:
                            self.add_new_student()
                        except ValueError as ve:
                            print(ve)

                    # remove student by id
                    elif user_option == 2:
                        try:
                            self.remove_student_by_id()
                        except ValueError as ve:
                            print(ve)

                    # add an assignment
                    elif user_option == 3:
                        try:
                            self.add_new_assignment()
                        except ValueError as ve:
                            print(ve)

                    # remove assignment by id
                    elif user_option == 4:
                        try:
                            self.remove_assignment_by_id()
                        except ValueError as ve:
                            print(ve)

                    # Update list of students
                    elif user_option == 5:
                        self.update_student_by_id()

                    # Update list of assignments
                    elif user_option == 6:
                        self.update_assignment_by_id()

                    # Print list of students
                    elif user_option == 7:
                        self.display_list_of_students()

                    # Print list of assignments
                    elif user_option == 8:
                        self.display_list_of_assignments()

                    # give assignment to a student
                    elif user_option == 9:
                        self.give_assignment_to_student()

                    # give assignments to a group of students.bin
                    elif user_option == 10:
                        self.give_assignment_to_group()

                    # print list of grades
                    elif user_option == 11:
                        self.display_list_of_grades()

                    # Grade student for a given assignment
                    elif user_option == 12:
                        self.grade_student_for_given_assignment()

                    # statistics
                    elif user_option == 13:
                        self.make_statistics()

                    # undo
                    elif user_option == 14:
                        try:
                            self._undo_redo_service.undo()
                        except UndoRedoExceptions as ure:
                            print(str(ure))

                    # redo
                    elif user_option == 15:
                        try:
                            self._undo_redo_service.redo()
                        except UndoRedoExceptions as ure:
                            print(str(ure))

                    else:
                        print('Invalid option')

                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            except ValueError as ve:
                print(str(ve))


console = Ui()
console.start()
