"""
## Problem Statement
Implement a menu-driven console application that provides the following functionalities:
1. Read a list of complex numbers (in `z = a + bi` form) from the console.
2. Display the entire list of numbers on the console.
3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of the
properties from the list provided below.
4. Exit the application.

**The source code will include:**
- Specifications for the functions related to point 3 above.
- 10 complex numbers already available at program startup.

### Sequence Properties
The sequence (consists of):
1. Numbers with a strictly increasing real part.
2. Contains at most 3 distinct values.
"""

# function that reads complex numbers from the console
# reads real and imaginary part separately
def read_complex_number(list_of_complex_numbers):
    real_part = int(input("Input real part of complex number: "))
    imaginary_part = int(input("Input imaginary part of complex number: "))
    list_of_complex_numbers.append([real_part, imaginary_part]) # add the new number to the list


# prints the options of the menu after each iteration
def print_menu_options():
    print("1. Read a complex number.\n"
          "2. Display the entire list of numbers on the console.\n"
          "3. Display on the console the longest sequence of numbers with a strictly increasing real part.\n"
          "4. Display on the console the longest sequence which contains at most 3 distinct values.\n"
          "5. Exit the application.")


# prints the entire (and updates) list of complex numbers
def display_entire_list_of_numbers(list_of_complex_numbers):
    print(list_of_complex_numbers)


# returns the real part of a complex number as an int
def get_real_part_of_complex_number(list):
    return list[0]


# returns the imaginary part of a complex number as an int
def get_imaginary_part_of_complex_number(list):
    return list[1]


def display_longest_sequence_strictly_increasing_real_part(list_of_complex_numbers):
    length_of_largest_sequence = 0
    start_position_of_largest_sequence = 0

    length_of_current_sequence = 1
    start_position_of_current_sequence = 0

    for i in range(1, len(list_of_complex_numbers)):
        real_part_current_number = get_real_part_of_complex_number(list_of_complex_numbers[i])
        real_part_previous_number = get_real_part_of_complex_number(list_of_complex_numbers[i-1])

        if real_part_current_number <= real_part_previous_number:
            if length_of_largest_sequence < length_of_current_sequence:
                length_of_largest_sequence = length_of_current_sequence
                start_position_of_largest_sequence = start_position_of_current_sequence
            else:
                pass
            length_of_current_sequence = 1
            start_position_of_current_sequence = i
        elif real_part_current_number > real_part_previous_number:
            length_of_current_sequence += 1

    print("The longest sequence of numbers with strictly increasing real part is ")
    for i in range(start_position_of_largest_sequence, start_position_of_largest_sequence + length_of_largest_sequence):
        real_part = get_real_part_of_complex_number((list_of_complex_numbers[i]))
        imaginary_part = get_imaginary_part_of_complex_number((list_of_complex_numbers[i]))
        print('z=', real_part, '+', imaginary_part, 'i')


def complex_numbers_are_equal(real_part_1, real_part_2, imaginary_part_1, imaginary_part_2):
    return real_part_1 == real_part_2 and imaginary_part_1 == imaginary_part_2


def display_longest_sequence_at_most_3_distinct_values(list_of_complex_numbers):
    length_of_largest_sequence = 0
    start_position_of_largest_sequence = 0

    length_of_current_sequence = 3
    start_position_of_current_sequence = 0

    real_part_number_1 = get_real_part_of_complex_number(list_of_complex_numbers[0])
    imaginary_part_number_1 = get_imaginary_part_of_complex_number(list_of_complex_numbers[0])
    real_part_number_2 = get_real_part_of_complex_number(list_of_complex_numbers[1])
    imaginary_part_number_2 = get_imaginary_part_of_complex_number(list_of_complex_numbers[1])
    real_part_number_3 = get_real_part_of_complex_number(list_of_complex_numbers[2])
    imaginary_part_number_3 = get_imaginary_part_of_complex_number(list_of_complex_numbers[2])

    for i in range(3, len(list_of_complex_numbers)):
        real_part_current_number = get_real_part_of_complex_number(list_of_complex_numbers[i])
        imaginary_part_current_number = get_imaginary_part_of_complex_number(list_of_complex_numbers[i])
        if complex_numbers_are_equal(real_part_current_number, real_part_number_1, imaginary_part_current_number, imaginary_part_number_1) or complex_numbers_are_equal(real_part_current_number, real_part_number_2, imaginary_part_current_number, imaginary_part_number_2) or complex_numbers_are_equal(real_part_current_number, real_part_number_3, imaginary_part_current_number, imaginary_part_number_3):
            length_of_current_sequence += 1
            if length_of_current_sequence > length_of_largest_sequence:
                length_of_largest_sequence = length_of_current_sequence
                start_position_of_largest_sequence = start_position_of_current_sequence
        else:
            length_of_current_sequence = 3
            start_position_of_current_sequence += 1
            real_part_number_1 = real_part_number_2
            imaginary_part_number_1 = imaginary_part_number_2
            real_part_number_2 = real_part_number_3
            imaginary_part_number_2 = imaginary_part_number_3
            real_part_number_3 = real_part_current_number
            imaginary_part_number_3 = imaginary_part_current_number

    for i in range(start_position_of_largest_sequence, start_position_of_largest_sequence + length_of_largest_sequence):
        real_part = get_real_part_of_complex_number((list_of_complex_numbers[i]))
        imaginary_part = get_imaginary_part_of_complex_number((list_of_complex_numbers[i]))
        print('z=', real_part, '+', imaginary_part, 'i')


def run_menu():
    list_of_complex_numbers = [[1, 2], [3, -3], [0, 3], [1, 2], [-8, 2], [-2, 3], [4, 7], [11, 0], [12, 2], [6, -5]]
    menu_options = {
        1: read_complex_number,
        2: display_entire_list_of_numbers,
        3: display_longest_sequence_strictly_increasing_real_part,
        4: display_longest_sequence_at_most_3_distinct_values
    }
    while True:
        print_menu_options()
        option = input("Choose an option (1 to 5): ")
        if option == "5":
            break
        option = int(option)

        menu_options[option](list_of_complex_numbers)


if __name__ == '__main__':
    run_menu()
    # print(list_of_complex_numbers)
