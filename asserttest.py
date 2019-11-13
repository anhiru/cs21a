# ----------------------------------------------------------------------------
# Name:         asserttest
# Purpose:      test assert statements with the -O flag
#
# Author:       Andrew Tran
# Date:         06/19/2019
# ----------------------------------------------------------------------------
"""
Include an assertion that is always False

We can use an assertion at the start of a function to check for valid input
and after a function call to check for valid output.
"""


def main():
    # calculate_grade(95, 80, 95)
    amount = 300
    assert amount >= 0, 'invalid amount'
    print(amount)
    # reach this statement with 'python -O asserttest.py' in terminal


def calculate_grade(homework, midterm, final):
    """
    Compute the overall numeric grade for the course based on the weights

    :param homework: points received in the homework category (int/float)
    :param midterm: points received on the midterm (int/float)
    :param final: points received on the final (int/float)
    :return: overall numeric grade for the course (float)
    """
    assert 0 <= homework <= 100, 'invalid grade'
    assert 0 <= midterm <= 100, 'invalid grade'
    assert 0 <= final <= 100, 'invalid grade'
    grade = final * 0.5 + homework * 0.7 + midterm * 0.1
    assert 0 <= grade <= 100, 'invalid grade computation'
    return grade


if __name__ == '__main__':
    main()
