"""
  Program functionalities module
"""
import copy

list_of_utilities = ['water', 'heating', 'electricity', 'gas', 'other']
possible_commands = ['add', 'remove', 'replace', 'list', 'sum', 'max', 'sort', 'filter', 'undo', 'exit']


def split_command_into_parameters(user_command):
    """
    Split the user's command into the command word and parameters
    :param user_command: Command input by user
    :return: A tuple of (<command word>, <command parameters>) in lowercase
    """
    user_command = user_command.strip()  # eliminate the spaces at the beginning and at the end of the input string
    tokens = user_command.split(maxsplit=1)

    command_word = tokens[0].lower() if len(tokens) > 0 else None
    if command_word not in possible_commands:
        raise ValueError("Invalid command word: ", command_word)

    command_parameter = tokens[1].lower() if len(tokens) == 2 else None

    return command_word, command_parameter


def test_split_command_into_parameters():
    assert split_command_into_parameters('exit') == ('exit', None)
    assert split_command_into_parameters('add 1 gas 100') == ('add', '1 gas 100')
    assert split_command_into_parameters('remove 1') == ('remove', '1')


# test_split_command_into_parameters()


def get_parameters_for_add_function(command_parameters):
    list_of_parameters = command_parameters.split()
    if len(list_of_parameters) == 3:
        try:
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

    else:
        raise ValueError("Invalid input")


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


def get_total_expenses_of_given_type(list_of_apartments_expenses, expense_type):
    total_value_expenses = 0

    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['type'] == expense_type:
            total_value_expenses += int(list_of_apartments_expenses[i]['amount'])

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


def get_maximum_amount_per_given_expense_type_for_given_apartment(list_of_apartments_expenses, command_apartment, command_type):
    max_amount = 0

    for i in range(len(list_of_apartments_expenses)):
        if list_of_apartments_expenses[i]['ap.no'] == command_apartment and \
                list_of_apartments_expenses[i]['type'] == command_type and \
                list_of_apartments_expenses[i]['amount'] > max_amount:
            max_amount = list_of_apartments_expenses[i]['amount']

    return max_amount


def test_get_maximum_amount_per_given_expense_type_for_given_apartment():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 1, 'type': 'gas', 'amount': 11}, {'ap.no': 1, 'type': 'heating', 'amount': 110}]
    assert get_maximum_amount_per_given_expense_type_for_given_apartment(test_apartment_list, 1, 'gas') == 11
    assert get_maximum_amount_per_given_expense_type_for_given_apartment(test_apartment_list, 1, 'heating') == 110
    assert get_maximum_amount_per_given_expense_type_for_given_apartment(test_apartment_list, 1, 'other') == 0


# test_get_maximum_amount_per_given_expense_type_for_given_apartment()


def total_amount_for_expenses_having_given_type(list_of_apartments_expenses, command_type):
    try:
        amount = 0
        for i in range(len(list_of_apartments_expenses)):
            if list_of_apartments_expenses[i]['type'] == command_type:
                amount += list_of_apartments_expenses[i]['amount']
        return amount
    except ValueError as ve:
        print(str(ve))


def test_total_amount_for_expenses_having_given_type():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 1, 'type': 'gas', 'amount': 11}, {'ap.no': 1, 'type': 'heating', 'amount': 110}]
    assert total_amount_for_expenses_having_given_type(test_apartment_list, 'gas') == 21
    assert total_amount_for_expenses_having_given_type(test_apartment_list, 'electricity') == 0


# test_total_amount_for_expenses_having_given_type()


def modify_list_for_filter_by_expense_type(list_of_apartments_expenses, command_type):
    """
     Keep in the list only expenses for given utility
    """
    for i in range(len(list_of_apartments_expenses) - 1, -1, -1):
        if list_of_apartments_expenses[i]['type'] != command_type:
            del list_of_apartments_expenses[i]

    return list_of_apartments_expenses


def test_modify_list_for_filter_by_expense_type():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 1, 'type': 'gas', 'amount': 11}, {'ap.no': 1, 'type': 'heating', 'amount': 110}]
    assert modify_list_for_filter_by_expense_type(test_apartment_list, 'gas') == [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 1, 'type': 'gas', 'amount': 11}]


# test_modify_list_for_filter_by_expense_type()


def modify_list_for_filter_by_expense_amount(list_of_apartments_expenses, command_amount):
    """
     Keep in the list only expenses smaller than given amount
    """
    for i in range(len(list_of_apartments_expenses) - 1, -1, -1):
        if list_of_apartments_expenses[i]['amount'] >= command_amount:
            del list_of_apartments_expenses[i]

    return list_of_apartments_expenses


def test_modify_list_for_filter_by_expense_amount():
    test_apartment_list = [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 1, 'type': 'gas', 'amount': 11}, {'ap.no': 1, 'type': 'heating', 'amount': 110}]
    assert modify_list_for_filter_by_expense_amount(test_apartment_list, 100) == [{'ap.no': 1, 'type': 'gas', 'amount': 10}, {'ap.no': 1, 'type': 'gas', 'amount': 11}]


# test_modify_list_for_filter_by_expense_amount()


def undo_last_operation(all_versions_list_of_apartments_expenses):
    length_list_versions_index = len(all_versions_list_of_apartments_expenses) - 1
    all_versions_list_of_apartments_expenses.pop(length_list_versions_index)
    return copy.deepcopy(all_versions_list_of_apartments_expenses[length_list_versions_index - 1])


def test_undo_last_operation():
    test_apartment_list = [[{'ap.no': 1, 'type': 'gas', 'amount': 10}], [{'ap.no': 1, 'type': 'gas', 'amount': 11}], [{'ap.no': 1, 'type': 'heating', 'amount': 110}]]
    assert undo_last_operation(test_apartment_list) == [{'ap.no': 1, 'type': 'gas', 'amount': 11}]


# test_undo_last_operation()


def undo(all_versions_list_of_apartments_expenses):
    if len(all_versions_list_of_apartments_expenses) == 1:
        raise ValueError("Cannot undo operation")
    else:
        return undo_last_operation(all_versions_list_of_apartments_expenses)

def test_undo():
    test_apartment_list = [[{'ap.no': 1, 'type': 'gas', 'amount': 10}], [{'ap.no': 1, 'type': 'gas', 'amount': 11}], [{'ap.no': 1, 'type': 'heating', 'amount': 110}]]
    assert undo(test_apartment_list) == [{'ap.no': 1, 'type': 'gas', 'amount': 11}]


# test_undo()