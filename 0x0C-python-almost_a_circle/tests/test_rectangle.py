#!/usr/bin/python3


import unittest
import io


class TestRectangleClass(unittest.TestCase):
    def Test_int(self):
        r1 = Rectangle(5, 100)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 720)

    def test_isSubclass(self):
        r1 = Rectangle(5, 100)
        self.assertTrue(issubclass(Rectangle, Base)

    
