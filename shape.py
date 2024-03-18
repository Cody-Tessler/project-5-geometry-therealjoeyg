"""
DO NOT MODIFY THIS FILE.

The Shape class is an abstract class. We won't create an instance of it. 
We only use it as a parent class for other concrete classes.
You can think of it as a template for its children. 
It contains attributes and methods that should be implemented in child classes.

In other words, do NOT modify THIS file.
Implement the methods defined here in all classes that inherit from this class.
"""

class Shape:
    """
    This is a abstract class representing geometrical shape.
    """

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        pass

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        pass

    @classmethod
    def check_if_args_not_below_zero(cls, *args):
        """
        Check if any of args are not below 0

        Returns:
            bool: True if any of args are not below 0

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        if list(filter(lambda x: x < 0, args)):
            raise ValueError
        return True

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        pass