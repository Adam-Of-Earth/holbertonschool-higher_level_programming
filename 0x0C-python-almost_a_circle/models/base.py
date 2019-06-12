#!/usr/bin/python3
"""base class module"""


import json
import os.path


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of init method
        Args: id(int): id of object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """returns a decoded JSON string"""
        if json_string is None or len(json_string) < 1:
            return[]
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance of a class from a dictionary"""
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """load a list of instances from a JSON file"""
        if not os.path.exists(cls.__name__ + 'json'):
            return []
        with open(cls.__name__ + '.json', 'rt') as file:
            objects = cls.from_json_string(file.read())
        return [cls.create(**d)for d in objects]

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a SJON sting to a file"""
        if list_objs is None:
            list_objs = []
        list_objs = [b.to_dictionary() for b in list_objs]
        list_objs = cls.to_json_string(list_objs)
        with open(cls.__name__ + ".json", "wt") as myFile:
            myFile.write(list_objs)

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of 'list_dictionarries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
