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
