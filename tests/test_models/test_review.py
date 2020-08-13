#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.base_model import BaseModel
import os
import unittest
import pep8


class test_review(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        cls.my_review = Review()
        cls.my_review.place_id = "Medellin"
        cls.my_review.user_id = "Holberton"
        cls.my_review.text = "Text"

    @classmethod
    def tearDownClass(cls):
        del cls.my_review
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_review(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_subclass(self):
        self.assertTrue(issubclass(self.my_review.__class__, BaseModel), True)

    def test_attributes(self):
        self.assertTrue('place_id' in self.my_review.__dict__)
        self.assertTrue('user_id' in self.my_review.__dict__)
        self.assertTrue('text' in self.my_review.__dict__)
        self.assertTrue('id' in self.my_review.__dict__)
        self.assertTrue('created_at' in self.my_review.__dict__)
        self.assertTrue('updated_at' in self.my_review.__dict__)

    def test_attributes_str(self):
        self.assertEqual(type(self.my_review.place_id), str)
        self.assertEqual(type(self.my_review.user_id), str)
        self.assertEqual(type(self.my_review.text), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test skip")
    def test_save(self):
        """ """
        self.my_review.save()
        self.assertNotEqual(self.my_review.created_at, self.my_review.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dic' in dir(self.my_review), True)

if __name__ == "__main__":
    unittest.main()
