# Calculator Class:

# Static Method - add(a, b): Returns the sum of two numbers. Use the @staticmethod decorator.
# Class Method - multiply(cls, a, b): Returns the product of two numbers. Use the @classmethod decorator and ensure it prints a class attribute named calculation_type before performing the multiplication.


class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
