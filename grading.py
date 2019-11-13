# ----------------------------------------------------------------------------
# Name:         grading
# Purpose:      miscellaneous functions used for grading
#
# Author:       Andrew Tran
# Date:         06/19/2019
# ----------------------------------------------------------------------------
"""
Module that contains various grading functions (to be tested)
"""
PASSING_GRADE = 70  # minimum grade required to pass a course


def is_passing(grade):
    """
    Determine whether a specified grade is enough to pass a course

    :param grade: a numeric grade between 0 and 100, inclusive (float)
    :return: True if the grade is passing, False otherwise (boolean)
    """
    return grade >= PASSING_GRADE
