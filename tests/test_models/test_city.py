#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
import os
import unittest
import pep8


class test_City(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        cls.my_city = City()
        cls.my_city.name = "Medellin"
        cls.my_city.state_id = "Ant"

    @classmethod
    def tearDownClass(cls):
        del cls.my_city
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_city(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_subclass(self):
        self.assertTrue(issubclass(self.my_city.__class__, BaseModel), True)

    def test_attributes(self):
        self.assertTrue('name' in self.my_city.__dict__)
        self.assertTrue('state_id' in self.my_city.__dict__)
        self.assertTrue('id' in self.my_city.__dict__)
        self.assertTrue('created_at' in self.my_city.__dict__)
        self.assertTrue('updated_at' in self.my_city.__dict__)

    def test_attributes_str(self):
        self.assertEqual(type(self.my_city.name), str)
        self.assertEqual(type(self.my_city.state_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test skip")
    def test_save(self):
        """ """
        self.my_city.save()
        self.assertNotEqual(self.my_city.created_at, self.my_city.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.my_city), True)

if __name__ == "__main__":
    unittest.main()
