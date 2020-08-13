#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel
import os
import unittest
import pep8


class test_User(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        cls.my_user = User()
        cls.my_user.first_name = "Holberton"
        cls.my_user.last_name = "School"
        cls.my_user.email = "test@holberton.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        del cls.my_user
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_user(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_subclass(self):
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_attributes(self):
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)

    def test_attributes_str(self):
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.last_name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test skip")
    def test_save(self):
        """ """
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dic' in dir(self.my_user), True)

if __name__ == "__main__":
    unittest.main()
