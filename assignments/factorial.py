# ----------------------------------------------------------------------------
# Name :        factorial
# Purpose:      factorial calculator
#
# Author:       Andrew Tran
# Date:         04/20/2019
# ----------------------------------------------------------------------------
"""
A simple factorial calculator using range and recursion

Prompt the user for a positive 'stop' case integer.
Print the product of all the numbers
from 1 up to and including the given integer.
"""


def fact(n):
    """
    Compute the factorial of a non-negative integer

    :param n: number (int)
    :return: factorial (int)
    """
    if n == 0:
        return 1

    return n * fact(n - 1)


# prompt user for a positive integer
valid_input = False
while not valid_input:
    number = int(input('Please enter a positive integer: '))
    if number >= 0:
        valid_input = True

# compute factorial of user-entered integer
result = 1  # initialize the factorial result to 1
for i in range(2, number + 1):  # omit 0 but include number
    result *= i

# print factorial results
print('\nFactorial using while loop:', result)
print('Factorial using recursion:', fact(number))
