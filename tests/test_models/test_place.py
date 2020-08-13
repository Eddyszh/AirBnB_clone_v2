#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.base_model import BaseModel
import os
import unittest
import pep8


class test_Place(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        cls.my_place = Place()
        cls.my_place.city_id = "Medellin"
        cls.my_place.user_id = "Holberton"
        cls.my_place.name = "School"
        cls.my_place.description = "Academy"
        cls.my_place.number_rooms = 0
        cls.my_place.number_bathrooms = 0
        cls.my_place.max_guest = 0
        cls.my_place.price_by_night = 0
        cls.my_place.latitude = 0.0
        cls.my_place.longitude = 0.0
        cls.my_place.amnity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.my_place
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_place(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_subclass(self):
        self.assertTrue(issubclass(self.my_place.__class__, BaseModel), True)

    def test_attributes(self):
        self.assertTrue('city_id' in self.my_place.__dict__)
        self.assertTrue('user_id' in self.my_place.__dict__)
        self.assertTrue('name' in self.my_place.__dict__)
        self.assertTrue('description' in self.my_place.__dict__)
        self.assertTrue('number_rooms' in self.my_place.__dict__)
        self.assertTrue('number_bathrooms' in self.my_place.__dict__)
        self.assertTrue('max_guest' in self.my_place.__dict__)
        self.assertTrue('price_by_night' in self.my_place.__dict__)
        self.assertTrue('latitude' in self.my_place.__dict__)
        self.assertTrue('longitude' in self.my_place.__dict__)
        self.assertTrue('amenity_ids' in self.my_place.__dict__)
        self.assertTrue('id' in self.my_place.__dict__)
        self.assertTrue('created_at' in self.my_place.__dict__)
        self.assertTrue('updated_at' in self.my_place.__dict__)

    def test_attributes_str(self):
        self.assertEqual(type(self.my_place.city_id), str)
        self.assertEqual(type(self.my_place.user_id), str)
        self.assertEqual(type(self.my_place.name), str)
        self.assertEqual(type(self.my_place.description), str)
        self.assertEqual(type(self.my_place.number_rooms), str)
        self.assertEqual(type(self.my_place.number_bathrooms), str)
        self.assertEqual(type(self.my_place.max_guest), str)
        self.assertEqual(type(self.my_place.price_by_night), str)
        self.assertEqual(type(self.my_place.latitude), str)
        self.assertEqual(type(self.my_place.longitude), str)
        self.assertEqual(type(self.my_place.amenity_ids), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test skip")
    def test_save(self):
        """ """
        self.my_place.save()
        self.assertNotEqual(self.my_place.created_at, self.my_place.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dic' in dir(self.my_place), True)

if __name__ == "__main__":
    unittest.main()
