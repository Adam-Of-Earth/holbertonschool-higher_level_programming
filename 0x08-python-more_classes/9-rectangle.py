#!/usr/bin/python3
"""class defineing a rectangle"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize rectangle

        Args:
        height(int): rectangle height
        width(int): rectangel width
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """draws the rectangle
        returns: (string)image of rectangle"""
        ret = []
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            ret.append(str(self.print_symbol) * self.__width)
        return '\n'.join(ret)

    def __repr__(self):
        """rep of the rectangle
        return: (str)representation of rectangle"""
        return "{}({}, {})".format(
            type(self).__name__,
            self.__width,
            self.__height
        )

    def __del__(self):
        """messege when deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """finds largest rectangle
        returns: rect_1 unlsess rect_2 > rect_1"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of rectangle")
        return rect_2 if rect_2.area() >= rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        """creates a square of size"""
        return cls(size, size)
