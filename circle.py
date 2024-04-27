from shape import Shape
import math
# Part 3
class Circle(Shape):

    def __init__(self, r):
        """
        Constructs a Circle object

        :param r: float -> radius of triangle
        """
        self.check_if_args_not_below_zero(r)
        self.r = r

    def get_area(self):
        """
        Calculates circle area using formula: pi * r^2

        :return: float -> area of the circle
        """
        return math.pi * self.r**2

    def get_perimeter(self):
        """
        Calculates perimeter of circle using formula: 2 * pi * r

        :return: float -> perimeter of the circle
        """

        return 2 * math.pi * self.r

    def __str__(self):
        return f'Circle, r={self.r:0.2f}'

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Circle as a string.

        :return: string
        """
        return 'pi * r^2 where r is the radius of the circle'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Circle as a string.

        :return: string
        """
        return '2 * pi * r where r is the radius of the circle'

