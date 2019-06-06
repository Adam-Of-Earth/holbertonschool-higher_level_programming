#!/usr/bin/python3
"""creates a BaseDeometry class"""


class BaseGeometry:
    """base class"""
    def area(self):
        """gets area"""
        raise(Exception("area() is not implemented"))

    def integer_validator(self, name, value):
        """validate int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle (BaseGeometry):
    """A rectangle with height and width"""

    def __init__(self, width, height):
        """instantiate of a rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """creates a representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return rectangle's area"""
        return self.__width * self.__height
