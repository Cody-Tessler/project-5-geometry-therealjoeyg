from shape import Shape

class Circle(Shape):

    def __init__(self, r):
        ...

    def get_area(self):
        return 0

    def get_perimeter(self):
        return 0

    def __str__(self):
        return "TODO"

    @classmethod
    def get_area_formula(cls):
        return "TODO"

    @classmethod
    def get_perimeter_formula(cls):
        return "TODO"
