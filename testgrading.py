# ----------------------------------------------------------------------------
# Name:         testgrading
# Purpose:      create tests for grading using Python unit testing framework
#
# Author:       Andrew Tran
# Date:         06/19/2019
# ----------------------------------------------------------------------------
"""
Module to test certain methods from the grading module
"""
import unittest
import grading


class TestGrading(unittest.TestCase):
    """
    Test case for the normal execution of grading functions
    """
    # test case does not include any fixtures
    # we do not define any setUp or tearDown methods
    def test_is_passing(self):
        """
        Test the is_passing function in the grading module

        :return: None
        """
        # test a passing grade
        self.assertTrue(grading.is_passing(85))

        # test a failing grade
        self.assertFalse(grading.is_passing(50))

        # test a borderline passing grade and specify a message
        self.assertTrue(grading.is_passing(70),
                        'Borderline grade not identified as passing')
