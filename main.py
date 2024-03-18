"""
This is the entrance of the program.

YOU DO NOT NEED TO MODIFY THIS FILE.
"""

import sys
import os

from shape_list import ShapeList
from texttable import Texttable
from circle import Circle
from equilateral_triangle import EquilateralTriangle
from pentagon import Pentagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle

OPTION_TITLE_INDEX = 0
OPTION_FUNCTION_INDEX = 1


def handle_first_menu_option(shapes):
    """
    This feature allows user to add new shape to shapes list.
    User is able to choose what kind of shapes he/she wants to add.
    The user should specify attributes that a given shape requires.

    :param shapes: ShapeList -> object of ShapeList class
    """
    SHAPE_NAME_INDEX = 0
    PARAMETERS_STARTING_INDEX = 1
    PAR_A_INDEX = 0
    PAR_B_INDEX = 1
    PAR_C_INDEX = 2

    user_input = ask_for_shape_input()
    try:
        shape_info = user_input.split(',')
        if shape_info[SHAPE_NAME_INDEX] == 't':
            t_check = [int(v) for v in shape_info[1:]]

            if t_check[PAR_A_INDEX] + t_check[PAR_B_INDEX] < t_check[PAR_C_INDEX] or \
               t_check[PAR_B_INDEX] + t_check[PAR_C_INDEX] < t_check[PAR_A_INDEX] or \
               t_check[PAR_C_INDEX] + t_check[PAR_A_INDEX] < t_check[PAR_B_INDEX]:
                print('\nInvalid triangle.')
                raise ValueError
        shape_name = shape_info[SHAPE_NAME_INDEX]
        shape_args = [int(i) for i in shape_info[PARAMETERS_STARTING_INDEX:]]
        new_shape = SHAPE_TYPES[shape_name](*shape_args)
        shapes.add_shape(new_shape)
        print('\n{} added successfully!\n'.format(str(new_shape)))
    except:
        print('\nWrong input!\n')


def handle_second_menu_option(shapes):
    """
    This feature should print table containing all shapes added to the list.

    :param shapes: ShapeList -> object of ShapeList class
    """
    print(shapes.get_shapes_table())


def handle_third_menu_option(shapes):
    """
    This feature prints shape with the largest perimeter from a list.

    :param shapes: ShapeList -> object of ShapeList class
    """
    print(shapes.get_largest_shape_by_perimeter())
    print('\n')


def handle_fourth_menu_option(shapes):
    """
    This feature prints shape with the largest area from a list.

    :param shapes: ShapeList -> object of ShapeList class
    """
    print(shapes.get_largest_shape_by_area())
    print('\n')


def handle_fifth_menu_option(shapes):
    """
    This feature should allow user to choose shape type and print it's formulas (perimeter, area).

    :param shapes: ShapeList -> object of ShapeList class
    """
    for shape_type in ['c', 't', 'et', 'r', 's', 'p']:
        print_shape_formulas(SHAPE_TYPES[shape_type])


def handle_seventh_menu_option(shapes):
    """
    Exits the program.
    """
    sys.exit()
    
    
def ask_for_shape_type():
    """
    Ask user for input about shape he want to choose.

    :return: string -> string with shape shortcut
    """
    shape = input('Choose shape type:\n' + ' Circle (c)\n' + ' Triangle (t)\n' + ' Equilateral Triangle (et)\n' +
                  ' Rectangle (r)\n' + ' Square (s)\n' + ' Pentagon (p)\n ').lower()
    return shape


def ask_for_shape_input():
    """
    Ask user for shape formula and return it as a string.

    :return: string -> formula for create a shape as a string
    """
    user_input = input('Enter data in the following syntax:\n' +
                       ' Circle -> c,<radius>\n' +
                       ' Triangle -> t,<a>,<b>,<c>\n' +
                       ' Equilateral Triangle -> et,<a>\n' +
                       ' Rectangle -> r,<a>,<b>\n' +
                       ' Square -> s,<a>\n' +
                       ' Pentagon -> p,<a>\n ').lower()
    return user_input


def print_menu_options():
    """
    Print options in console to represent menu
    """
    print(' (1) Add new shape\n' +
          ' (2) Show all shapes\n' +
          ' (3) Show shape with the largest perimeter\n' +
          ' (4) Show shape with the largest area\n' +
          ' (5) Show formulas\n' +
          ' (0) Exit program')


def print_shape_formulas(shape):
    """
    Print formula of area and perimeter for a given shape.

    :param shape: Shape -> object of Shape class
    """
    print(shape.__name__)
    print(f'P = {shape.get_perimeter_formula()}')
    print(f'A = {shape.get_area_formula()}')
    print()


SHAPE_TYPES = {'c': Circle,
               't': Triangle,
               'et': EquilateralTriangle,
               'r': Rectangle,
               's': Square,
               'p': Pentagon}

OPTIONS = {
    '1': ['Add new shape', handle_first_menu_option],
    '2': ['Show all shapes', handle_second_menu_option],
    '3': ['Show shape with the largest perimeter', handle_third_menu_option],
    '4': ['Show shape with the largest area', handle_fourth_menu_option],
    '5': ['Show formulas', handle_fifth_menu_option],
    '0': ['Exit program', handle_seventh_menu_option]}


def main():
    SYS_CLEAR = 'clear'
    os.system(SYS_CLEAR)
    print('''
    :'######:::'########::'#######::'##:::::::'########::::'###::::'########::'##::: ##:
    '##... ##:: ##.....::'##.... ##: ##::::::: ##.....::::'## ##::: ##.... ##: ###:: ##:
    ##:::..::: ##::::::: ##:::: ##: ##::::::: ##::::::::'##:. ##:: ##:::: ##: ####: ##:
    ##::'####: ######::: ##:::: ##: ##::::::: ######:::'##:::. ##: ########:: ## ## ##:
    ##::: ##:: ##...:::: ##:::: ##: ##::::::: ##...:::: #########: ##.. ##::: ##. ####:
    ##::: ##:: ##::::::: ##:::: ##: ##::::::: ##::::::: ##.... ##: ##::. ##:: ##:. ###:
    . ######::: ########:. #######:: ########: ########: ##:::: ##: ##:::. ##: ##::. ##:
    :......::::........:::.......:::........::........::..:::::..::..:::::..::..::::..::        
    ''')

    shapes = ShapeList()
    while True:
        print('What do you want to do?')
        print_menu_options()
        user_input = input("Type number of option: ")
        if (user_input not in OPTIONS):
            os.system('')
        else:
            os.system(SYS_CLEAR)
            OPTIONS[user_input][OPTION_FUNCTION_INDEX](shapes)


if __name__ == "__main__":
    main()
