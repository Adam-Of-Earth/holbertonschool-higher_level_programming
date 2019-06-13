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

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update object's attributes"""
        if len(args) > 0:
            attrs = ('id', 'size', 'x', 'y')
            for name, value in zip(attrs, args):
                setattr(self, name, value)
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """dictionary of square"""
        dic = {
            "id": self.id,
            "size": self.__size,
            "x": self.x,
            "y": self.y}
        return dic
