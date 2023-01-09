"""
Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the sequence
of natural numbers by replacing composed numbers with their prime divisors, without memorizing the
elements of the sequence
"""


from math import sqrt


def is_prime(x):
    if x < 2 or x % 2 == 0:
        return False
    if x == 2:
        return True
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

# The sequence is 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the sequence
# of natural numbers by replacing composed numbers with their prime divisors

def n_th_element_of_the_sequence(n):
    current_position = 1
    current_number = 2
    while current_position < n:
        divisor = 2
        copy_of_current_number = current_number
        while copy_of_current_number > 1:
            if copy_of_current_number % divisor == 0:
                current_position += 1
            while copy_of_current_number % divisor == 0:
                copy_of_current_number /= divisor
            if current_position != n:
                divisor += 1
            else:
                return divisor
        current_number += 1
    return 1


if __name__ == '__main__':
    print("Insert position: ")
    a = int(input())
    print(n_th_element_of_the_sequence(a))
