"""
Generate the largest prime number smaller than a given natural number n. If such a number does not exist, a message
should be displayed.
"""

from math import sqrt


def is_prime(number_to_check):
    # verifies if a given number is prime
    if number_to_check == 2:
        return True
    if number_to_check < 2 or number_to_check % 2 == 0:
        return False
    for i in range(3, int(sqrt(number_to_check)) + 1, 2):
        if number_to_check % i == 0:
            return False
    return True


def largest_prime_smaller(x):
    x -= 1
    while True:
        if x < 2:  # if there isn't any prime nr smaller than n then the functions returns "false"
            return False
        if is_prime(x):  # otherwise, it returns the first prime number it finds (the search starts from n-1
            return x
        x -= 1


if __name__ == '__main__':
    print("insert number: ")
    n = input()
    n = int(n)
    aux = largest_prime_smaller(n)
    if aux:
        print(aux)
    else:
        print("There is no such number")
