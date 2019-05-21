#!/usr/bin/python3
"""a class Square

Description of a square class

"""

class Square:
    """square shape

    infomation about the square and how to use it

    """

    def __init__(self, size):
        """Create a square size large

        size(int): how large the size wil be

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """finds the squares area"""
            return self.__size * self.__size
