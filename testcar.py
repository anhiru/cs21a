# ----------------------------------------------------------------------------
# Name:         testcar
# Purpose:      create tests for car using Python unit testing framework
#
# Author:       Andrew Tran
# Date:         06/19/2019
# ----------------------------------------------------------------------------
"""
Module to test certain methods from the car module

A test case is an individual unit of testing.
A test case checks for specific responses to a particular set of inputs.

The unittest module provides a base class, TestCase,
which may be used to create new test cases.
Defining a test case involves defining a subclass of TestCase.
"""
import unittest
import car


# create a new test case to test the Car class
# test case TestCar is a subclass of unittest.TestCase
class TestCar(unittest.TestCase):
    """
    Test case for the normal execution of Car methods
    """
    def setUp(self) -> None:
        """
        Create three cars for testing

        The first car has a fuel efficiency of 20 miles/gallon,
        initial mileage of 1000 miles and 9 gallons of fuel in the tank.
        The second car has a fuel efficiency of 30 miles/gallon,
        initial mileage of 5000 miles and 2 gallons of fuel in the tank
        The third car has a fuel efficiency of 24 miles/gallon,
        initial mileage of 0 miles and an empty gas tank.
        """
        # save the 3 car objects as instance variables
        # so we can access them in the test methods
        self.first_car = car.Car('Porsche', '911', 20, 1000, 9)
        self.second_car = car.Car('Honda', 'Civic', 30, 2000, 2)
        self.third_car = car.Car('Honda', 'Pilot', 24)

    def test_drive(self):
        """
        Test the drive method in the Car class

        :return: None
        """
        # driving when there is enough gas in the tank
        self.first_car.drive(100)
        self.assertEqual(self.first_car.mileage, 1100)
        self.assertEqual(self.first_car.gas_in_tank, 4)

        # driving when there is not enough gas in the tank
        self.second_car.drive(200)
        self.assertEqual(self.second_car.gas_in_tank, 0)
        self.assertEqual(self.second_car.mileage, 2060)

        # driving when there is no gas in the tank
        self.third_car.drive(20)
        self.assertEqual(self.third_car.gas_in_tank, 0)
        self.assertEqual(self.third_car.mileage, 0)

        # if the result is NOT equal to the one we provided,
        # an assertion exception is raised but is NOT reported on
        # until the end of the tests

    def test_add_gas(self):
        """
        Test the add_gas method in the Car class

        :return: None
        """
        self.first_car.add_gas(3)
        self.assertEqual(self.first_car.gas_in_tank, 12)

        # the method returns a Car object
        # check that the object returned by the add_gas method
        # is an instance of the Car class
        self.assertIsInstance(self.second_car.add_gas(10), car.Car)
        self.third_car.add_gas(5)
        self.assertEqual(self.third_car.gas_in_tank, 5)

        # the mileage is not affected
        self.assertEqual(self.third_car.mileage, 0)
