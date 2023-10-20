# Abstract
# 1. Method = A method that has a signature (declaration), but no implementation, that is left for the child class
# 2. Class = A class which contains one or more abstract methods
# Derived class must override abstract methods


# To define an abstract class or abstract method
# we must first import these modules
from abc import ABC, abstractclassmethod


# Vehicle is extending AbstractClass
class Vehicle(ABC):
    # And here we use the abstractclassmethod decorator
    @abstractclassmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("Car is driving")


class Motorcycle(Vehicle):
    def go(self):
        print("Bike is riding?")


# The following would raise an exception
# > vehicle = Vehicle()
# > vehicle.go()

car = Car()
car.go()  # Car is driving

bike = Motorcycle()
bike.go()  # Bike is riding?
