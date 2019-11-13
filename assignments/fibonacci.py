# ----------------------------------------------------------------------------
# Name :        fibonacci
# Purpose:      fibonacci number calculator
#
# Author:       Andrew Tran
# Date:         05/04/2019
# ----------------------------------------------------------------------------
"""
A simple fibonacci number calculator using recursion and range

Prompt the user for a positive 'stop' case integer.
Print the fibonacci number of the given integer.
"""


def fibonacci(n):
    """
    Compute the fibonacci number of a non-negative integer

    :param n: number (int)
    :return: fibonacci number (int)
    """
    # base case: 0 or 1
    if n <= 1:
        return n

    # else: recursive rule
    return fibonacci(n - 1) + fibonacci(n - 2)


# prompt user for a positive integer
valid_input = False
while not valid_input:
    number = int(input('Please enter a positive integer: '))
    if number >= 0:
        valid_input = True

# compute fibonacci number of user-entered integer
fib = [0, 1]
for i in range(2, number + 1):
    fib.append(fib[-2] + fib[-1])

# print fibonacci results
print(f'In one year, there will be {fib[-1]} pairs of rabbits.')
print(f'In one year, there will be {fibonacci(number)} pairs of rabbits.')
