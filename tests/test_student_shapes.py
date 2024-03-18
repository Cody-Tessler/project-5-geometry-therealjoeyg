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

class CircleTester(unittest.TestCase):

    def test_constructor(self):
        c = Circle(3)
        self.assertEqual(c.r, 3, "Wrong radius")

    def test_value_error(self):
        with self.assertRaises(ValueError,
                               msg="Circle radius can't be negative"):
            Circle(-1)

    def test_area(self):
        r = 3
        c = Circle(r)
        area = math.pi * r ** 2
        self.assertEqual(c.get_area(), area)

    def test_perimeter(self):
        r = 3
        c = Circle(r)
        perimeter = 2 * math.pi * r
        self.assertEqual(c.get_perimeter(), perimeter)


class RectangleTester(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(2, 3)
        self.assertEqual((r.a, r.b), (2, 3))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

    def test_area(self):
        a = 2
        b = 3
        r = Rectangle(a, b)
        area = a * b
        self.assertEqual(r.get_area(), area)

    def test_perimeter(self):
        a = 2
        b = 3
        r = Rectangle(a, b)
        perimeter = 2*a + 2*b
        self.assertEqual(r.get_perimeter(), perimeter)


class SquareTester(unittest.TestCase):

    def test_constructor(self):
        s = Square(2)
        self.assertEqual((s.a, s.b), (2, 2))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)
            Square(-90)

    def test_area(self):
        a = 2
        s = Square(a)
        area = a**2
        self.assertEqual(s.get_area(), area)

    def test_perimeter(self):
        a = 2
        s = Square(a)
        perimeter = a*4
        self.assertEqual(s.get_perimeter(), perimeter)

class PentagonTester(unittest.TestCase):

    def test_constructor(self):
        p = Pentagon(2)
        self.assertEqual(p.a, 2)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Pentagon(-1)
            Pentagon(-90)

    def test_area(self):
        a = 2
        p = Pentagon(a)
        area = a**2 * math.sqrt(5*(5+2*math.sqrt(5)))/4
        self.assertEqual(p.get_area(), area)

    def test_perimeter(self):
        a = 2
        p = Pentagon(a)
        perimeter = 5*a
        self.assertEqual(p.get_perimeter(), perimeter)


def main():
    unittest.TextTestRunner(verbosity=2)
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
