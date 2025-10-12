#  Enhance your understanding of polymorphism in Python by creating a set 
#+ of classes that demonstrate method overriding and polymorphic behavior
#  Create a Python script named polymorphism_demo.py. 
#+ In this script, define a base class Shape with a method area() and derived classes Rectangle and Circle, 
#+ each overriding the area() method to calculate their respective areas.

import math

class Shape:
    def area(self):
        raise NotImplementedError('derived classes need to override this method')

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
