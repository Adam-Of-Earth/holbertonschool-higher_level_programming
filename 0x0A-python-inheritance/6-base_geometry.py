#!/usr/bin/python3
"""creates a BaseDeometry class"""


class BaseGeometry:
    """base class"""
    def area(self):
        """gets area"""
        raise(Exception("area() is not implemented"))
