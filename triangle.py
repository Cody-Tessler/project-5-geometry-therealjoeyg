"""
The Triangle class is completed for you. Model your implementations of the other classes after this one.

The docstring is using the reST style.
Read up on other types of docstring styles here: https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats
The classes you implement should use docstrings with a matching style.
"""

from shape import Shape
import math

class Triangle(Shape):

    def __init__(self, a, b, c):
        """
        Constructs a Triangle object

        :param a: float -> first side of triangle
        :param b: float -> second side of triangle
        :param c: float -> third side of triangle
        """
        self.check_if_args_not_below_zero(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """
        Calculates triangle area using formula: sqrt(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2

        :return: float -> area of the triangle
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        """
        Calculates perimeter of triangle using formula: a+b+c

        # :return: float -> perimeter of the triangle
        """
        return self.a + self.b + self.c

    def __str__(self):
        return f'Triangle, a={self.a:0.2f}, b={self.b:0.2f}, c={self.c:0.2f}'

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Triangle as a string.

        :return: string
        """
        return 'sqrt(s(s-a)(s-b)(s-c)) where s=(a+b+c)/2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Triangle as a string.

        :return: string
        """
        return 'a+b+c'
