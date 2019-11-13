# ----------------------------------------------------------------------------
# Name:         tax
# Purpose:      sales tax calculator
#
# Author:       Andrew Tran
# Date:         04/15/2019
# ----------------------------------------------------------------------------
"""
A simple sales tax calculator assuming a 9.25% tax rate

Prompt the user for the cost of three individual items.
Print the subtotal, sales tax, and total cost of the items.
"""

TAX_RATE = 9.25 / 100  # tax rate constant: 9.25%


user_input = input('Please enter the price of the first item in $: ')
first_item_cost = float(user_input)  # convert input string to number

user_input = input('Please enter the price of the second item in $: ')
second_item_cost = float(user_input)  # convert input string to number

user_input = input('Please enter the price of the third item in $: ')
third_item_cost = float(user_input)  # convert input string to number


# calculate the subtotal, sales tax, and total cost of each item
subtotal_amount = first_item_cost + second_item_cost + third_item_cost
sales_tax_amount = subtotal_amount * TAX_RATE
total_cost_amount = subtotal_amount + sales_tax_amount

# convert all values to formatted strings prefixed with $ sign
# contain commas and restricted to 2 decimal places
subtotal = f'${subtotal_amount:,.2f}'
sales_tax = f'${sales_tax_amount:,.2f}'
total_cost = f'${total_cost_amount:,.2f}'

# format all output strings (right aligned)
subtotal_output = f'SUBTOTAL:{subtotal:>14}'
sales_tax_output = f'SALES TAX:{sales_tax:>13}'
total_cost_output = f'TOTAL:{total_cost:>17}'

print(subtotal_output)
print(sales_tax_output)
print(total_cost_output)
