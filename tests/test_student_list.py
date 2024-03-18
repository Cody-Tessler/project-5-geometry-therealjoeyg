import unittest
import math
from os import listdir

from circle import Circle
from equilateral_triangle import EquilateralTriangle
from pentagon import Pentagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from shape_list import ShapeList
from main import handle_fifth_menu_option

class ShapeListTester(unittest.TestCase):
    def test_largest_perimeter(self):
        sl = ShapeList()
        p = Pentagon(3)
        s = Square(5)
        t = Triangle(2, 4, 5)
        c = Circle(3)
        sl.add_shape(p)
        sl.add_shape(s)
        sl.add_shape(t)
        sl.add_shape(c)
        self.assertIs(sl.get_largest_shape_by_perimeter(), s)

    def test_largest_area(self):
        sl = ShapeList()
        p = Pentagon(3)
        s = Square(5)
        t = Triangle(2, 4, 5)
        c = Circle(3)
        sl.add_shape(p)
        sl.add_shape(s)
        sl.add_shape(t)
        sl.add_shape(c)
        self.assertIs(sl.get_largest_shape_by_area(), c)


def main():
    unittest.TextTestRunner(verbosity=2)
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
