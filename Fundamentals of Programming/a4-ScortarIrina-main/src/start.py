"""
  Start the program by running this module
"""

import functions
import ui
import copy

possible_commands = ['add', 'remove', 'replace', 'list', 'sum', 'max', 'sort', 'filter', 'undo', 'exit']


def start_command_ui():
    list_of_apartments_expenses = [{'ap.no': 1, 'type': "heating", 'amount': 80},
                                   {'ap.no': 2, 'type': "electricity", 'amount': 40},
                                   {'ap.no': 2, 'type': "heating", 'amount': 100},
                                   {'ap.no': 3, 'type': "gas", 'amount': 60},
                                   {'ap.no': 1, 'type': "gas", 'amount': 10},
                                   {'ap.no': 3, 'type': "other", 'amount': 20},
                                   {'ap.no': 5, 'type': "heating", 'amount': 80},
                                   {'ap.no': 4, 'type': "gas", 'amount': 10},
                                   {'ap.no': 5, 'type': "water", 'amount': 90},
                                   {'ap.no': 5, 'type': "electricity", 'amount': 100}]

    all_versions_list_of_apartments_expenses = []
    copy_list_of_apartments_expenses = copy.deepcopy(list_of_apartments_expenses)
    all_versions_list_of_apartments_expenses.append(copy_list_of_apartments_expenses)

    while True:
        ui.print_possible_commands()
        user_command = ui.get_user_command()
        try:
            # Parse user command into command word and parameters
            command_word, command_parameters = functions.split_command_into_parameters(user_command)

            # Call the correct function for the given command
            if command_word not in possible_commands:
                print("Invalid command word")
            elif command_word == 'exit':
                return
            elif command_word == 'add' and command_parameters:
                ui.add_new_transaction(command_parameters, list_of_apartments_expenses, all_versions_list_of_apartments_expenses)
            elif command_word == 'remove':
                ui.execute_modification_for_remove(command_parameters, list_of_apartments_expenses, all_versions_list_of_apartments_expenses)
            elif command_word == 'replace':
                ui.execute_modification_for_replace(command_parameters, list_of_apartments_expenses, all_versions_list_of_apartments_expenses)
            elif command_word == 'list':
                ui.display_expenses_with_different_properties(list_of_apartments_expenses, command_parameters)
            elif command_word == 'sum':
                ui.display_total_amount_for_expenses_having_given_type(list_of_apartments_expenses, command_parameters)
            elif command_word == 'max':
               ui.display_maximum_amount_per_each_expense_type_for_given_apartment(list_of_apartments_expenses, command_parameters)
            elif command_word == 'sort':
                if command_parameters == 'apartment':
                    # display the list of apartments sorted ascending by total amount of expenses
                    ui.display_apartments_for_sort_by_total_amount_of_expenses(list_of_apartments_expenses)
                elif command_parameters == 'type':
                    # display the total amount of expenses for each type, sorted ascending by amount of money
                    ui.display_type_for_sort_by_total_amount(list_of_apartments_expenses)
                else:
                    raise ValueError('Invalid word: ', command_parameters)
            elif command_word == 'filter':
                ui.execute_modification_for_filter(list_of_apartments_expenses, command_parameters, all_versions_list_of_apartments_expenses)
            elif command_word == 'undo':
                list_of_apartments_expenses = functions.undo(all_versions_list_of_apartments_expenses)
            print('\n')
        except ValueError as ve:
            print(str(ve))


start_command_ui()
