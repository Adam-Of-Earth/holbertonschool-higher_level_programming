#!/usr/bin/python3
"""a class Square

Description of a square class

"""


class Square:
    """square shape

    infomation about the square and how to use it

    """
    @property
    def size(self):
        """int: returns size of square"""
        return self.__size

    @size.setter
    def size(self, val=0):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        """finds the squares area"""
        return self.__size * self.__size

    def __init__(self, size=0):
        """Create a square size large

        size(int): how large the size wil be

        """

        self.size = size
    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
