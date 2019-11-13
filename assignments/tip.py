# ----------------------------------------------------------------------------
# Name:         tip
# Purpose:      tip calculator
#
# Author:       Andrew Tran
# Date:         04/15/2019
# ----------------------------------------------------------------------------
"""
Tip calculator assuming a 20% tip rate

Prompt the user for the cost of their meal.
Print the tip amount and the total cost.
"""

TIP_RATE = 20 / 100  # tip rate constant: 20%


def get_input():
    """
    Prompt the user for the cost of their meal
    Parameter: None
    Returns: (float) the user input as a float
    """
    user_input = input('Please enter the cost of your meal in $: ')
    number = float(user_input)  # convert the input string to a number
    return number


def get_tip(amount):
    """
    Compute and format the tip corresponding to the given amount
    Parameter: amount (float)
    Returns: (string) formatted tip with 2 decimals and $ sign
    """
    tip = TIP_RATE * amount
    formatted_tip = f'${tip:.2f}'  # format the string
    return formatted_tip


def get_total(amount):
    """
    Compute the total cost of the meal including the tip
    Parameter: amount (float)
    Returns: (string) formatted total cost with 2 decimals and $ sign
    """
    total = amount * (1 + TIP_RATE)
    formatted_total = f'${total:.2f}'  # format the string
    return formatted_total


def main():
    cost = get_input()
    tip = get_tip(cost)
    total = get_total(cost)
    print(f'Tip Amount:{tip:>8}')
    print(f'Total Cost:{total:>8}')


if __name__ == '__main__':
    main()
