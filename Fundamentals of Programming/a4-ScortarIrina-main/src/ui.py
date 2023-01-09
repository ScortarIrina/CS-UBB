"""
  User interface module
"""

import functions
import copy


list_of_utilities = ['water', 'heating', 'electricity', 'gas', 'other']


def print_possible_commands():
    print('\nPOSSIBLE COMMANDS:')
    print('\tadd <apartment> <type> <amount>')
    print('\tremove <apartment>')
    print('\tremove <start apartment> to <end apartment>')
    print('\tremove <type>')
    print('\treplace <apartment> <type> with <amount>')
    print('\tlist')
    print('\tlist <apartment>')
    print('\tlist [ < | = | > ] <amount>')
    print('\tsum <type>')
    print('\tmax <apartment>')
    print('\tsort apartment')
    print('\tsort type')
    print('\tfilter <type>')
    print('\tfilter <value>')
    print('\tundo')
    print('\texit\n')


def display_maximum_amount_per_each_expense_type_for_given_apartment(list_of_apartments_expenses, command_apartment):
    if not command_apartment.isnumeric() and float(command_apartment) != int(command_apartment):
        raise ValueError('Invalid apartment number')
    else:
        for i in list_of_utilities:
            expense_amount = functions.get_maximum_amount_per_given_expense_type_for_given_apartment(list_of_apartments_expenses, int(command_apartment), i)
            if expense_amount == 0:
                print(i, ': -')
            else:
                print(i, ': ', expense_amount)


def get_user_command():
    return input("Give command: ")


def display_expenses_with_different_properties(list_of_apartments_expenses, command_parameters):
    """
    Based on the length of the list formed of split command_parameters, displays expenses having different properties
    :param list_of_apartments_expenses:
    :param command_parameters:
    :return:
    """
    if command_parameters is None:
        print_all_apartments(list_of_apartments_expenses)

    else:
        try:
            list_of_parameters = command_parameters.split()

            if len(list_of_parameters) == 1:

                if list_of_parameters[0].isnumeric() and float(list_of_parameters[0]) == int(list_of_parameters[0]):
                    apartment_number = int(list_of_parameters[0])
                    display_all_expenses_for_given_apartment(list_of_apartments_expenses, apartment_number)

                else:
                    raise ValueError("Invalid input")

            elif len(list_of_parameters) == 2:

                if list_of_parameters[1].isnumeric() and float(list_of_parameters[1]) == int(list_of_parameters[1]) and \
                        list_of_parameters[0] == '<':
                    utility_amount = int(list_of_parameters[1])
                    display_apartments_total_expenses_less_than_given_amount(list_of_apartments_expenses, utility_amount)

                elif list_of_parameters[1].isnumeric() and float(list_of_parameters[1]) == int(list_of_parameters[1]) and \
                        list_of_parameters[0] == '=':
                    utility_amount = int(list_of_parameters[1])
                    display_apartments_total_expenses_equal_to_given_amount(list_of_apartments_expenses, utility_amount)

                elif list_of_parameters[1].isnumeric() and float(list_of_parameters[1]) == int(list_of_parameters[1]) and \
                        list_of_parameters[0] == '>':
                    utility_amount = int(list_of_parameters[1])
                    display_apartments_total_expenses_greater_than_given_amount(list_of_apartments_expenses, utility_amount)

                else:
                    raise ValueError("Invalid input")

        except ValueError as ve:
            print(str(ve))


def execute_modification_for_remove(command_parameters, list_of_apartments_expenses, all_versions_list_of_apartments_expenses):
    """
    Executes modifications on the list by removing or replacing elements
    :param command_parameters:
    :param list_of_apartments_expenses:
    :return:
    """
    if command_parameters is None:
        print("Invalid input")
    else:
        try:
            list_of_parameters = command_parameters.split()

            if len(list_of_parameters) == 1:

                if list_of_parameters[0].isnumeric():
                    apartment_number = int(list_of_parameters[0])
                    functions.remove_expenses_for_given_apartment(list_of_apartments_expenses, apartment_number)

                elif list_of_parameters[0] in list_of_utilities:
                    apartment_utility = list_of_parameters[0]
                    functions.remove_expenses_for_given_utility(list_of_apartments_expenses, apartment_utility)

                else:
                    raise ValueError("Invalid input: ", list_of_parameters[0])

            elif len(list_of_parameters) == 3:

                start_apartment = list_of_parameters[0]
                if not start_apartment.isnumeric() or float(start_apartment) != int(start_apartment):
                    raise ValueError("Invalid start apartment number: ", start_apartment)
                else:
                    start_apartment = int(start_apartment)

                connective_word = list_of_parameters[1]
                if connective_word != 'to':
                    raise ValueError("Invalid connective word: ", connective_word)

                end_apartment = list_of_parameters[2]
                if not end_apartment.isnumeric() or float(end_apartment) != int(end_apartment):
                    raise ValueError("Invalid end apartment number: ", end_apartment)
                else:
                    end_apartment = int(end_apartment)
                functions.remove_expenses_in_range_of_two_apartments(list_of_apartments_expenses, start_apartment, end_apartment)

            copy_list_of_apartments_expenses = copy.deepcopy(list_of_apartments_expenses)
            all_versions_list_of_apartments_expenses.append(copy_list_of_apartments_expenses)

        except ValueError as ve:
            print(str(ve))


def execute_modification_for_replace(command_parameters, list_of_apartments_expenses, all_versions_list_of_apartments_expenses):
    if command_parameters is None:
        print("Invalid input")
    else:
        try:
            list_of_parameters = command_parameters.split()

            if len(list_of_parameters) == 4:

                if list_of_parameters[0].isnumeric() and float(list_of_parameters[0]) == int(list_of_parameters[0]) and \
                        list_of_parameters[1] in list_of_utilities and list_of_parameters[2] == 'with' and \
                        list_of_parameters[3].isnumeric() and float(list_of_parameters[3]):
                    apartment_number = int(list_of_parameters[0])
                    apartment_utility = list_of_parameters[1]
                    utility_amount = int(list_of_parameters[3])
                    functions.replace_amount_of_given_expense_type_for_given_apartment(list_of_apartments_expenses, apartment_number, apartment_utility, utility_amount)

                copy_list_of_apartments_expenses = copy.deepcopy(list_of_apartments_expenses)
                all_versions_list_of_apartments_expenses.append(copy_list_of_apartments_expenses)

            else:
                raise ValueError("Invalid input")

        except ValueError as ve:
            print(str(ve))


def execute_modification_for_filter(list_of_apartments_expenses, command_parameters, all_versions_list_of_apartments_expenses):
    if command_parameters is None:
        print("Invalid input")

    else:
        try:
            if command_parameters in list_of_utilities:
                functions.modify_list_for_filter_by_expense_type(list_of_apartments_expenses, command_parameters)

            elif command_parameters.isnumeric() and float(command_parameters) == int(command_parameters):
                functions.modify_list_for_filter_by_expense_amount(list_of_apartments_expenses, int(command_parameters))

            copy_list_of_apartments_expenses = copy.deepcopy(list_of_apartments_expenses)
            all_versions_list_of_apartments_expenses.append(copy_list_of_apartments_expenses)

        except ValueError as ve:
            print(str(ve))


def add_new_transaction(command_parameters, list_of_apartments_expenses, all_versions_list_of_apartments_expenses):
    if command_parameters is None:
        raise ValueError("Invalid input")

    else:
        try:
            command_apartment_number, command_utility_type, command_expense_amount = functions.get_parameters_for_add_function(command_parameters)
            list_of_apartments_expenses.append({'ap.no': command_apartment_number, 'type': command_utility_type, 'amount': command_expense_amount})

            copy_list_of_apartments_expenses = copy.deepcopy(list_of_apartments_expenses)
            all_versions_list_of_apartments_expenses.append(copy_list_of_apartments_expenses)

        except ValueError as ve:
            print(str(ve))


def print_all_apartments(list_of_apartments_expenses):
    for i in range(len(list_of_apartments_expenses)):
        print(list_of_apartments_expenses[i])


def display_all_expenses_for_given_apartment(list_of_apartments_expenses, apartment_number):
    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['ap.no'] == apartment_number:
            print(list_of_apartments_expenses[i])


def display_apartments_total_expenses_less_than_given_amount(list_of_apartments_expenses, utility_amount):
    highest_number_apartment = functions.get_highest_number_apartment(list_of_apartments_expenses)

    for i in range(1, highest_number_apartment + 1):
        total_expenses_of_an_apartment = functions.get_total_expenses_of_an_apartment(list_of_apartments_expenses, i)
        if total_expenses_of_an_apartment < utility_amount:
            print(i)


def display_apartments_total_expenses_equal_to_given_amount(list_of_apartments_expenses, utility_amount):
    highest_number_apartment = functions.get_highest_number_apartment(list_of_apartments_expenses)

    for i in range(1, highest_number_apartment + 1):
        total_expenses_of_an_apartment = functions.get_total_expenses_of_an_apartment(list_of_apartments_expenses, i)
        if total_expenses_of_an_apartment == utility_amount:
            print(i)


def display_apartments_total_expenses_greater_than_given_amount(list_of_apartments_expenses, utility_amount):
    highest_number_apartment = functions.get_highest_number_apartment(list_of_apartments_expenses)

    for i in range(1, highest_number_apartment + 1):
        total_expenses_of_an_apartment = functions.get_total_expenses_of_an_apartment(list_of_apartments_expenses, i)
        if total_expenses_of_an_apartment > utility_amount:
            print(i)


def display_total_amount_for_expenses_having_given_type(list_of_apartments_expenses, command_type):
    if command_type not in list_of_utilities:
        raise ValueError("Invalid expense type: ", command_type)
    else:
        print(functions.total_amount_for_expenses_having_given_type(list_of_apartments_expenses, command_type))


def display_apartments_for_sort_by_total_amount_of_expenses(list_of_apartments_expenses):
    dictionary_of_apartments_vs_total_expenses = {}

    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['ap.no'] not in dictionary_of_apartments_vs_total_expenses:
            current_apartment_number = list_of_apartments_expenses[i]['ap.no']
            total_expenses_current_apartment = functions.get_total_expenses_of_an_apartment(list_of_apartments_expenses, list_of_apartments_expenses[i]['ap.no'])
            dictionary_of_apartments_vs_total_expenses[current_apartment_number] = total_expenses_current_apartment

    list_of_expenses_amount_ascending = sorted(dictionary_of_apartments_vs_total_expenses.values())

    for i in range(len(list_of_expenses_amount_ascending)):
        for key, value in dictionary_of_apartments_vs_total_expenses.items():
            if list_of_expenses_amount_ascending[i] == value:
                print('apartment number:', key, '        total amount:', value)


def display_type_for_sort_by_total_amount(list_of_apartments_expenses):
    dictionary_of_utilities = {'water': 0, 'heating': 0, 'electricity': 0, 'gas': 0, 'other': 0}

    for i in list_of_utilities:
        total_expenses = functions.get_total_expenses_of_given_type(list_of_apartments_expenses, i)
        dictionary_of_utilities[i] = total_expenses

    list_of_expenses_amount_ascending = sorted(dictionary_of_utilities.values())

    for i in range(len(list_of_expenses_amount_ascending)):
        for key, value in dictionary_of_utilities.items():
            if list_of_expenses_amount_ascending[i] == value:
                print('expense type:', key, '        total amount:', value)