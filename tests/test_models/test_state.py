#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel
import os
import unittest
import pep8


class test_state(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        cls.my_state = State()
        cls.my_state.name = "Antioquia"

    @classmethod
    def tearDownClass(cls):
        del cls.my_state
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_state(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_subclass(self):
        self.assertTrue(issubclass(self.my_state.__class__, BaseModel), True)

    def test_attributes(self):
        self.assertTrue('name' in self.my_state.__dict__)
        self.assertTrue('id' in self.my_state.__dict__)
        self.assertTrue('created_at' in self.my_state.__dict__)
        self.assertTrue('updated_at' in self.my_state.__dict__)

    def test_attributes_str(self):
        self.assertEqual(type(self.my_state.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test skip")
    def test_save(self):
        """ """
        self.my_state.save()
        self.assertNotEqual(self.my_state.created_at, self.my_state.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.my_state), True)

if __name__ == "__main__":
    unittest.main()
