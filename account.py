# ----------------------------------------------------------------------------
# Name:         account
# Purpose:      contains the class definitions for bank accounts
#
# Author:       Andrew Tran
# Date:         05/25/2019
# ----------------------------------------------------------------------------
"""
Module to describe and manipulate bank accounts using inheritance
"""


# use: from account import Account
class Account(object):
    """
    Represent a bank account

    Arguments:
    account_holder: account holder's name (str)

    Attributes:
    holder: account holder's name (str)
    balance: account balance in dollars (float)
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        super().__setattr__('balance', 0)

    def __str__(self):
        return f'{self.holder}: ${self.balance}'

    def __setattr__(self, name, value):
        if name == 'balance':
            print('This is a read-only attribute.')
        else:
            super().__setattr__(name, value)

    def deposit(self, amount):
        """
        Deposit the given amount into the account

        :param amount: the amount to be deposited in dollars (float)
        :return: the updated account object (Account)
        """
        super().__setattr__('balance', self.balance + amount)
        return self

    def withdraw(self, amount):
        """
        Withdraw the amount from the account if possible

        :param amount: the amount to be withdrawn in dollars (float)
        :return: True if the withdrawal is successful, False otherwise (bool)
        """
        if self.balance >= amount:
            super().__setattr__('balance', self.balance - amount)
            return True
        else:
            return False


# use: from account import SavingsAccount
class SavingsAccount(Account):
    """
    Represent a savings bank account with a withdrawal fee

    Arguments:
    account_holder: account holder's name (str)

    Attributes:
    holder: account holder's name (string)
    balance: account balance in dollars (float)
    """
    # class variable
    fee = 1

    def withdraw(self, amount):
        """
        Withdraw the amount + the fee from the account if possible

        :param amount: the amount to be withdrawn in dollars (float)
        :return: True if withdrawal is successful, False otherwise (bool)
        """
        if self.balance >= amount + self.fee:
            self.balance -= amount + self.fee
            return True
        else:
            return False


# use: from account import PremiumAccount
class PremiumAccount(Account):
    """
    Represent a premium interest bearing bank account

    Arguments:
    account_holder: account holder's name (str)
    rate: interest rate (float)

    Attributes:
    holder: account holder's name (str)
    balance: account balance in dollars (float)
    interest_rate: interest rate (float)
    """
    def __init__(self, account_holder, rate):
        self.interest_rate = rate
        Account.__init__(self, account_holder)


# use: from account import PremiumSavingsAccount
class PremiumSavingsAccount(PremiumAccount, SavingsAccount):
    """
    Represent a premium interest bearing bank account with a withdrawal fee
    """


def main():
    a = SavingsAccount('Alice')
    b = Account('Billy')
    print(b.balance)
    b.balance = 20
    print(a.balance)


if __name__ == '__main__':
    main()
