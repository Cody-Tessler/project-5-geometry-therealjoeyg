from shape import Shape
# Part 3
class Rectangle(Shape):

    def __init__(self, a, b):
        """
        Constructs a Rectangle object

        :param a: float -> length of rectangle
        :param b: float -> width of rectangle
        """
        self.check_if_args_not_below_zero(a, b)
        self.a = a
        self.b = b 

    def get_area(self):
        """
        Calculates rectangle area using formula: lw

        :return: float -> area of the rectangle
        """
        return self.a * self.b

    def get_perimeter(self):
        """
        Calculates perimeter of rectangle using formula: 2a+2b

        # :return: float -> perimeter of the rectangle
        """
        return 2 * self.a + 2 * self.b

    def __str__(self):
        return f'Rectangle, a={self.a:0.2f}, b={self.b:0.2f}'

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Rectangle as a string.

        :return: string
        """
        return 'ab'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Rectangle as a string.

        :return: string
        """
        return '2a+2b'

