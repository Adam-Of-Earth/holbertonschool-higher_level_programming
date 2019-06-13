#!/usr/bin/python3
"""module to test base"""

import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def test_idCount(self):
        b1 = Base()
        b2 = Base()
        b3 = base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_0Args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_multArgs(self):
        b1 = Base(5)
        self.assertEqual(b1.id, 5)

    
