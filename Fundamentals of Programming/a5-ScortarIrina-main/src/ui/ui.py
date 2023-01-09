from src.services.services import Services
from src.tests.tests import TestFunctions


class Ui:

    def __init__(self):
        self.__services = Services()

    @staticmethod
    def print_menu():
        print("\t1. Add a student\n"
              "\t2. Display the list of students\n"
              "\t3. Filter the list so that students in a given group are deleted from the list\n"
              "\t4. Undo\n"
              "\t5. Exit\n")

    def display_list_of_students(self):
        services = self.__services
        for i in services.get_list_of_students():
            print(str(i))

    def add_new_student(self):
        user_command_id = input('\tstudent id: ')
        user_command_name = input('\tstudent name: ')
        user_command_group = input('\tstudent group: ')
        self.__services.add_new_student(user_command_id, user_command_name, user_command_group)

    def start(self):

        self.__services.generate_students()

        while True:
            try:
                print('\nMenu options:')
                self.print_menu()
                user_option = input('Choose an option (1-5): ')

                if not user_option.isnumeric():
                    print("Invalid input")
                else:
                    user_option = int(user_option)

                    # add a student
                    if user_option == 1:
                        try:
                            self.add_new_student()
                        except ValueError as ve:
                            print(ve)

                    # display list of students
                    elif user_option == 2:
                        self.display_list_of_students()

                    # filter
                    elif user_option == 3:
                        try:
                            user_command_group = input('\tstudent group: ')
                            self.__services.filter_list(user_command_group)
                        except ValueError as ve:
                            print(ve)

                    # undo
                    elif user_option == 4:
                        self.__services.undo()

                    # exit
                    elif user_option == 5:
                        return

            except ValueError as ve:
                print(str(ve))


test_functions = TestFunctions()
console = Ui()
console.start()
