#!/usr/bin/python3
"""module for class Rectangle"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation for Rectangle class
        args:
        widht(int): width of rectangle
        height(int): height of rectangle
        x(int):coradinate
        y(int):coradinate
        id(int): id of object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
