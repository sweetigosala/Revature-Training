"""Area circumference of square , rectangle,circle"""
from math import pi

def area_square(side):
    """
    Area of a square
    :param side: side of square
    :return: area of square
    """
    return side*side


def area_circle(radius):
    """ Area of a circle
    :param radius: radius of circle
    :return: area of circle"""
    return pi*radius**2

def area_rectangle(length,width):
    """ Area of a rectangle
    :param side: side of rectangle
    :return: area of rectangle"""
    return length*width


def cir_circle(radius):
    """ Circumference of a square
    :param radius: radius of circle
    :return: circumference of square"""

    return 2*pi*radius