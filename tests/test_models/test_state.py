#!/usr/bin/python3
"""Test State"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Teststate(unittest.TestCase):
    def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """ class test"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """class"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        my_state.name = "Antioquia"
        self.assertEqual(my_state.name, 'Antioquia')

    def test_state_type(self):
        """ test state type """
        my_state = State()
        self.assertEqual(type(my_state.name), str)
        self.assertNotEqual(type(my_state.name), int)

    def test_attribute(self):
        """ state test """
        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))
        self.assertFalse(hasattr(my_state, "area"))

    def test_value(self):
        """ test value """
        my_state = State()
        self.assertEqual(my_state.name, "")
        self.assertFalse(my_state.name, "on fire")
