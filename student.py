# ----------------------------------------------------------------------------
# Name:         student
# Purpose       contains the class definitions for students
#
# Author:       Andrew Tran
# Date:         05/25/2019
# ----------------------------------------------------------------------------
"""
Module to describe students in a college setting
"""


class Student(object):
    """
    Represent a student

    Arguments:
    name: student name (str)
    sid: student id - 8 digits (int)

    Attributes:
    name: student name (str)
    sid: student id - 8 digits (int)
    """
    # class variable
    number_of_students = 0

    def __init__(self, name, sid):
        self.name = name
        if self.valid(sid):
            self.sid = sid
        else:
            self.sid = 0

    @staticmethod
    def valid(id):
        """
        A valid student ID starts with 2018

        :param id: inputted ID to be checked (int)
        :return: True if the ID is valid, False otherwise (bool)
        """
        return id // 10000 == 2018

    @classmethod
    def update_count(cls):
        cls.number_of_students += 1  # increment the class variable


def main():
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    print(maze_size)


if __name__ == '__main__':
    main()
