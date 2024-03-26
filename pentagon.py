from shape import Shape
import math

class Pentagon(Shape):

    def __init__(self, a):
        """
        Constructs a Pentagon object

        :param a: float -> side length of regular pentagon
        """

        self.check_if_args_not_below_zero(a)
        self.a = a

    def get_area(self):
        """
        Calculates pentagon area using formula: 1/4 * sqrt( 5( 5 + 2sqrt(5) )) a^2 

        :return:float -> area of the regular pentagon
        """
        return 1/4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.a**2

    def get_perimeter(self):
        """
        Calculates perimeter of regular pentagon using formula: 5a

        # : return: float -> perimeter of the triangle
        """
        return 5 * self.a

    def __str__(self):
        return f'Pentagon, a={self.a:0.2f}'

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Pentagon as a string.

        :return: string
        """
        return '1/4sqrt(5(5+2sqrt(5))a^2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Pentagon as a string.

        :return: string
        """
        return '5a'
