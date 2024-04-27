"""
Implement this class.
Recall that every square is a rectangle.
Therefore the Square class should inherit from the Rectangle class.
Do NOT implement the get_area() and get_perimeter() methods here.
Those methods should be inherited from the parent class.
"""
# Part 3
from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, a):
        """
        Constructs a Square object

        :param a: float -> side of square
        """
        super().__init__(a,a)

    def __str__(self):
        """
        Returns a formatted string with details about Square.

        :return: string
        """
        return f'Square, a = {self.a:0.2f}'