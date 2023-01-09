"""
Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n.
Two prime numbers p and q are called twin if q - p = 2.
"""

from math import sqrt


# verifies if a given number is prime
def is_prime(x):
    if x < 2 or x % 2 == 0:
        return False
    if x == 2:
        return True
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


# searches for the pair of prime numbers, p and q, immediately larger than x which satisfy the condition q - p = 2
def search_twin(x):
    p = x + 1
    while True:
        if is_prime(p) and is_prime((p + 2)):
            return p
        p += 1


if __name__ == '__main__':
    print("insert number: ")
    n = input()
    n = int(n)
    p1 = search_twin(n)
    p2 = p1 + 2
    print("The twin numbers are ", p1, " and ", p1 + 2)
