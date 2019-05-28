#!/usr/bin/python3
"""class defineing a rectangle"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize rectangle

        Args:
        height(int): rectangle height
        width(int): rectangel width
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, val):
        """sets height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise TypeError("height must be >= 0")
        self.__height = val

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self,val):
        """sets width"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise TypeError("width must be >= 0")
        self.__width = val

    def area(self):
        """finds area of rectangle
        return: area(int)"""
        return self.__height * self.__width

    def perimeter(self):
        """finds perimeter of rectangle
        return: perimeter(int)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
