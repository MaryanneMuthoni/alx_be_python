#  Solidify your understanding of class methods and static methods in Python
#+ Create a Python script named class_static_methods_demo.py. 
#+ In this script, define a class Calculator that includes both a class method and a static method to perform calculations

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


