# ----------------------------------------------------------------------------
# Name:         car
# Purpose:      describe a car
#
# Author:       Andrew Tran
# Date:         06/19/2019
# ----------------------------------------------------------------------------
"""
Module to outline a Car class
"""


class Car(object):
    """
    Represent a car in my virtual world

    Arguments:
    make: car make (string)
    model: car model (string)
    fuel_efficiency: fuel efficiency in miles per gallon (float)
    mileage: current mileage on car in miles, defaults to 0 (float, optional)
    gas: current gas in the tank in gallons, defaults to 0 (float, optional)

    Attributes:
    make: car make (string)
    model: car model (string)
    fuel_efficiency: fuel efficiency in miles per gallon (float)
    mileage: current mileage on the car in miles (float)
    gas_in_tank: current gas in the tank in gallons (float)
    """

    def __init__(self,  make,  model, fuel_efficiency, mileage=0, gas=0):
        self.make = make
        self.model = model
        self.fuel_efficiency = fuel_efficiency
        self.mileage = mileage
        self.gas_in_tank = gas

    def add_gas(self, amount):
        """
        Add gas to the car.

        :param amount: the amount of gas to be added in gallons (float)
        :return: the updated Car object (Car)
        """
        self.gas_in_tank += amount
        return self

    def drive(self, distance):
        """
        Drive a car a given distance, if possible.
        If there is not enough gas, drive as much as possible.

        :param distance: the distance to be driven in miles (float)
        :return: the updated Car object (Car)
        """
        max_distance = self.fuel_efficiency * self.gas_in_tank

        if distance <= max_distance:  # we can drive the distance
            self.mileage += distance
            self.gas_in_tank = (self.gas_in_tank -
                                distance / self.fuel_efficiency)
        else:   # not enough gas
            self.mileage += max_distance  # drive as far as possible
            self.gas_in_tank = 0

        return self
