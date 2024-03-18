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


class TriangleTester(unittest.TestCase):

    def test_constructor(self):
        t = Triangle(2, 4, 5)
        self.assertEqual((t.a, t.b, t.c), (2, 4, 5))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 1, 1)

    def test_area(self):
        a = 2
        b = 4
        c = 5
        t = Triangle(a, b, c)
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        self.assertEqual(t.get_area(), area)

    def test_perimeter(self):
        a = 2
        b = 4
        c = 5
        t = Triangle(a, b, c)
        perimeter = a + b + c
        self.assertEqual(t.get_perimeter(), perimeter)


class EquilateralTriangleTester(unittest.TestCase):

    def test_constructor(self):
        t = EquilateralTriangle(2)
        self.assertEqual((t.a, t.b, t.c), (2, 2, 2))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            EquilateralTriangle(-1)

    def test_area(self):
        a = b = c = 2
        t = EquilateralTriangle(a)
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        self.assertEqual(t.get_area(), area)

    def test_perimeter(self):
        a = 2
        t = EquilateralTriangle(a)
        perimeter = 3*a
        self.assertEqual(t.get_perimeter(), perimeter)

class ShapeListTester(unittest.TestCase):

    def test_constructor(self):
        sl = ShapeList()
        self.assertIsInstance(sl.shapes, list)

    def test_add_shape(self):
        sl = ShapeList()
        c = Circle(2)
        sl.add_shape(c)
        self.assertEqual(sl.shapes[0], c)

    def test_type_error(self):
        sl = ShapeList()
        with self.assertRaises(TypeError, msg="Invalid Shape"):
            sl.add_shape("dupa")

    def test_shapes_table(self):
        sl = ShapeList()
        s = Square(4)
        sl.add_shape(s)
        self.assertIsInstance(sl.get_shapes_table(), str)

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

def main():
    unittest.TextTestRunner(verbosity=2)
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
