# ----------------------------------------------------------------------------
# Name:         employee
# Purpose:      class definitions for the Employee class
#
# Author:       Andrew Tran
# Date:         05/25/2019
# ----------------------------------------------------------------------------
"""
Module to describe employees using object composition
"""
from account import Account


# use from employee import Employee
class Employee(object):
    """
    Represent an employee

    Arguments:
    name: employee's name (str)

    Attributes:
    name: employee's name (str)
    job: employee's job description (str)
    account: employee's bank account (Account)
    """
    def __init__(self, name):
        self.name = name
        self.job = ''
        self.account = Account(name)


def main():
    new_hire = Employee('Alex')
    new_hire.account.deposit(500)
    print(new_hire.account)


if __name__ == '__main__':
    main()
