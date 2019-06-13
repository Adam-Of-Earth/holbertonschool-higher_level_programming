#!/usr/bin/python3
"""module for square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method to return string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)
