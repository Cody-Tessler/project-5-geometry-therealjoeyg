"""
The EquilateralTriangle class is implemented for you.
It inherits from Triangle.
"""

from triangle import Triangle

class EquilateralTriangle(Triangle):

    def __init__(self, a):
        """
        Constructs an EquilateralTriangle object

        :param a: float -> side of triangle
        """
        super().__init__(a, a, a)
        

    def __str__(self):
        """
        Returns a formatted string with details about EquilateralTriangle.

        :return: string
        """
        return f'EquilateralTriangle, a = {self.a:0.2f}'
        
        
