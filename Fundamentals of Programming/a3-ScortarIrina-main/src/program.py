"""
Each expense is stored using the following elements:
    - apartment (number of apartment, positive integer)
    - amount (positive integer)
    - type (from one of the predefined categories:
                * water
                * heating
                * electricity
                * gas
                * other)
"""

"""
  Write non-UI functions below 
  Non-UI functions
        - there will be no print/input calls here
        - these functions will not call other functions that use print/input
        - these functions communicate via parameters & return type and value
"""

list_of_utilities = ['water', 'heating', 'electricity', 'gas', 'other']


def split_command_into_parameters(user_command):
    """
    Split the user's command into the command word and parameters

    :param user_command: Command input by user
    :return: A tuple of (<command word>, <command parameters>) in lowercase
    """
    user_command = user_command.strip()  # eliminate the spaces at the beginning and at the end of the input string
    tokens = user_command.split(maxsplit=1)

    command_word = tokens[0].lower() if len(tokens) > 0 else None
    if command_word != 'add' and command_word != 'remove' and command_word != 'replace' and command_word != 'list' and command_word != 'exit':
        raise ValueError("Invalid command word: ", command_word)

    command_parameter = tokens[1].lower() if len(tokens) == 2 else None

    return command_word, command_parameter


def test_split_command_into_parameters():
    assert split_command_into_parameters('exit') == ('exit', None)
    assert split_command_into_parameters('add 1 gas 100') == ('add', '1 gas 100')
    assert split_command_into_parameters('remove 1') == ('remove', '1')


# test_split_command_into_parameters()


def get_parameters_for_add_function(command_parameters):
    try:
        list_of_parameters = command_parameters.split()
        command_apartment_number = list_of_parameters[0]
        command_utility_type = list_of_parameters[1]
        command_utility_amount = list_of_parameters[2]

        if not command_apartment_number.isnumeric() or float(command_apartment_number) != int(command_apartment_number):
            raise ValueError("Invalid apartment number: ", command_apartment_number)

        if command_utility_type not in list_of_utilities:
            raise ValueError("Invalid utility type: ", command_utility_type)

        if not command_utility_amount.isnumeric() or float(command_utility_amount) != int(command_utility_amount):
            raise ValueError("Invalid amount: ", command_utility_amount)

        return int(command_apartment_number), command_utility_type, int(command_utility_amount)

    except ValueError as ve:
        print(str(ve))


def test_get_parameters_for_add_function():
    assert get_parameters_for_add_function('1 gas 10') == (1, 'gas', 10)


# test_get_parameters_for_add_function()


def replace_amount_of_given_expense_type_for_given_apartment(list_of_apartments_expenses, apartment_number, apartment_utility, utility_amount):
    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['type'] == apartment_utility and list_of_apartments_expenses[i]['ap.no'] == apartment_number:
            list_of_apartments_expenses[i].update({'amount': utility_amount})
    return list_of_apartments_expenses


def test_replace_amount_of_given_expense_type_for_given_apartment():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}]
    assert replace_amount_of_given_expense_type_for_given_apartment(test_apartment_list, 1, 'gas', 100) == [{'ap.no': 1, 'type': 'gas', 'amount': 100}]


# test_replace_amount_of_given_expense_type_for_given_apartment()


def get_total_expenses_of_an_apartment(list_of_apartments_expenses, apartment_number):
    total_value_expenses = 0
    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['ap.no'] == apartment_number:
            total_value_expenses += list_of_apartments_expenses[i]['amount']
    return total_value_expenses


def test_get_total_expenses_of_an_apartment():
    test_list_of_apartments = [{'ap.no': 1, 'type': "heating", 'amount': 80},
                               {'ap.no': 1, 'type': "gas", 'amount': 10},
                               {'ap.no': 2, 'type': "electricity", 'amount': 40},
                               {'ap.no': 2, 'type': "heating", 'amount': 100},
                               {'ap.no': 3, 'type': "gas", 'amount': 60},
                               {'ap.no': 3, 'type': "other", 'amount': 20},
                               {'ap.no': 4, 'type': "gas", 'amount': 10},
                               {'ap.no': 5, 'type': "water", 'amount': 90},
                               {'ap.no': 5, 'type': "heating", 'amount': 80},
                               {'ap.no': 5, 'type': "electricity", 'amount': 100}]
    assert get_total_expenses_of_an_apartment(test_list_of_apartments, 1) == 90


# test_get_total_expenses_of_an_apartment()


def get_highest_number_apartment(list_of_apartments_expenses):
    highest_number_apartment = 0
    for i in range(len(list_of_apartments_expenses)):
        if int(list_of_apartments_expenses[i]['ap.no']) > highest_number_apartment:
            highest_number_apartment = int(list_of_apartments_expenses[i]['ap.no'])
    return highest_number_apartment


def test_get_highest_number_apartment():
    test_list_of_apartments = [{'ap.no': 1, 'type': "heating", 'amount': 80},
                               {'ap.no': 1, 'type': "gas", 'amount': 10},
                               {'ap.no': 2, 'type': "electricity", 'amount': 40},
                               {'ap.no': 2, 'type': "heating", 'amount': 100},
                               {'ap.no': 3, 'type': "gas", 'amount': 60},
                               {'ap.no': 3, 'type': "other", 'amount': 20},
                               {'ap.no': 4, 'type': "gas", 'amount': 10},
                               {'ap.no': 5, 'type': "water", 'amount': 90},
                               {'ap.no': 5, 'type': "heating", 'amount': 80},
                               {'ap.no': 5, 'type': "electricity", 'amount': 100}]
    assert get_highest_number_apartment(test_list_of_apartments) == 5


# test_get_highest_number_apartment()


def remove_expenses_for_given_apartment(list_of_apartments_expenses, apartment_number):
    index_go_through_list = 0
    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[index_go_through_list]['ap.no'] == apartment_number:
            del list_of_apartments_expenses[index_go_through_list]
            index_go_through_list -= 1
        index_go_through_list += 1
    return list_of_apartments_expenses


def test_remove_expenses_for_given_apartment():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}]
    assert remove_expenses_for_given_apartment(test_apartment_list, 1) == []


# test_remove_expenses_for_given_apartment()


def remove_expenses_for_given_utility(list_of_apartments_expenses, apartment_utility):
    index_go_through_list = 0
    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[index_go_through_list]['type'] == apartment_utility:
            del list_of_apartments_expenses[index_go_through_list]
            index_go_through_list -= 1
        index_go_through_list += 1
    return list_of_apartments_expenses


def test_remove_expenses_for_given_utility():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}]
    assert remove_expenses_for_given_utility(test_apartment_list, 'gas') == []


# test_remove_expenses_for_given_utility()


def remove_expenses_in_range_of_two_apartments(list_of_apartments_expenses, start_apartment, end_apartment):
    for i in range(len(list_of_apartments_expenses) - 1, -1, -1):
        if start_apartment <= list_of_apartments_expenses[i]['ap.no'] <= end_apartment:
            del list_of_apartments_expenses[i]
    return list_of_apartments_expenses


def test_remove_expenses_in_range_of_two_apartments():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 2, 'type': 'gas', 'amount': 10}, {'ap.no': 3, 'type': 'gas', 'amount': 10}]
    assert remove_expenses_in_range_of_two_apartments(test_apartment_list, 1, 2) == [{'ap.no': 3, 'type': 'gas', 'amount': 10}]


# test_remove_expenses_in_range_of_two_apartments()


"""
  Write the command-driven UI below
  UI functions
        - "talk" to the program's user
        - rely on the non-UI functions to solve the requirements
"""


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


def execute_modification_for_remove(command_parameters, list_of_apartments_expenses):
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
                    list_of_apartments_expenses = remove_expenses_for_given_apartment(list_of_apartments_expenses, apartment_number)
                elif list_of_parameters[0] in list_of_utilities:
                    apartment_utility = list_of_parameters[0]
                    list_of_apartments_expenses = remove_expenses_for_given_utility(list_of_apartments_expenses, apartment_utility)
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
                list_of_apartments_expenses = remove_expenses_in_range_of_two_apartments(list_of_apartments_expenses, start_apartment, end_apartment)
        except ValueError as ve:
            print(str(ve))


def execute_modification_for_replace(command_parameters, list_of_apartments_expenses):
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
                    list_of_apartments_expenses = replace_amount_of_given_expense_type_for_given_apartment(list_of_apartments_expenses, apartment_number, apartment_utility, utility_amount)
            else:
                raise ValueError("Invalid input")
        except ValueError as ve:
            print(str(ve))


def display_all_expenses_for_given_apartment(list_of_apartments_expenses, apartment_number):
    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['ap.no'] == apartment_number:
            print(list_of_apartments_expenses[i])


def display_apartments_total_expenses_less_than_given_amount(list_of_apartments_expenses, utility_amount):
    highest_number_apartment = get_highest_number_apartment(list_of_apartments_expenses)
    for i in range(1, highest_number_apartment + 1):
        total_expenses_of_an_apartment = get_total_expenses_of_an_apartment(list_of_apartments_expenses, i)
        if total_expenses_of_an_apartment < utility_amount:
            print(i)


def display_apartments_total_expenses_equal_to_given_amount(list_of_apartments_expenses, utility_amount):
    highest_number_apartment = get_highest_number_apartment(list_of_apartments_expenses)
    for i in range(1, highest_number_apartment + 1):
        total_expenses_of_an_apartment = get_total_expenses_of_an_apartment(list_of_apartments_expenses, i)
        if total_expenses_of_an_apartment == utility_amount:
            print(i)


def display_apartments_total_expenses_greater_than_given_amount(list_of_apartments_expenses, utility_amount):
    highest_number_apartment = get_highest_number_apartment(list_of_apartments_expenses)
    for i in range(1, highest_number_apartment + 1):
        total_expenses_of_an_apartment = get_total_expenses_of_an_apartment(list_of_apartments_expenses, i)
        if total_expenses_of_an_apartment > utility_amount:
            print(i)


def add_new_transaction(command_parameters, list_of_apartments_expenses):
    if command_parameters is None:
        print("Invalid input")
    else:
        try:
            command_apartment_number, command_utility_type, command_expense_amount = get_parameters_for_add_function(command_parameters)
            list_of_apartments_expenses.append({'ap.no': command_apartment_number, 'type': command_utility_type, 'amount': command_expense_amount})
        except ValueError as ve:
            print(str(ve))


def print_all_apartments(list_of_apartments_expenses):
    for i in range(len(list_of_apartments_expenses)):
        print(list_of_apartments_expenses[i])


def start_command_ui():
    list_of_apartments_expenses = [{'ap.no': 1, 'type': "heating", 'amount': 80},
                                   {'ap.no': 1, 'type': "gas", 'amount': 10},
                                   {'ap.no': 2, 'type': "electricity", 'amount': 40},
                                   {'ap.no': 2, 'type': "heating", 'amount': 100},
                                   {'ap.no': 3, 'type': "gas", 'amount': 60},
                                   {'ap.no': 3, 'type': "other", 'amount': 20},
                                   {'ap.no': 4, 'type': "gas", 'amount': 10},
                                   {'ap.no': 5, 'type': "water", 'amount': 90},
                                   {'ap.no': 5, 'type': "heating", 'amount': 80},
                                   {'ap.no': 5, 'type': "electricity", 'amount': 100}]

    possible_commands = ['add', 'remove', 'replace', 'list', 'exit']

    while True:
        user_command = input("Give a command: ")
        try:
            # Parse user command into command word and parameters
            command_word, command_parameters = split_command_into_parameters(user_command)

            # Call the correct function for the given command
            if command_word not in possible_commands:
                print("Invalid command word")
            elif command_word == 'exit':
                return
            elif command_word == 'add' and command_parameters:
                add_new_transaction(command_parameters, list_of_apartments_expenses)
            elif command_word == 'remove':
                execute_modification_for_remove(command_parameters, list_of_apartments_expenses)
            elif command_word == 'replace':
                execute_modification_for_replace(command_parameters, list_of_apartments_expenses)
            elif command_word == 'list':
                display_expenses_with_different_properties(list_of_apartments_expenses, command_parameters)
            else:
                print("Invalid input: ")
        except ValueError as ve:
            print(str(ve))


if __name__ == '__main__':
    start_command_ui()
