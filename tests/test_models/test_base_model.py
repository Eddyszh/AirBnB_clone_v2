#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8


class test_basemodel(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        cls.my_base_model = BaseModel()
        cls.my_base_model.name = "Holberton"
        cls.my_base_model.number = 13

    @classmethod
    def tearDownClass(cls):
        del cls.my_base_model
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8_base_model(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.my_base_model, BaseModel))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test skip")
    def test_save(self):
        """ """
        self.my_base_model.save()
        self.assertNotEqual(
            self.my_base_model.created_at, self.my_base_model.updated_at)

    def test_to_dict(self):
        """ """
        my_base_model_dict = self.my_base_model.to_dict()
        self.assertEqual(self.my_base_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(my_base_model_dict['created_at'], str)
        self.assertIsInstance(my_base_model_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
    # def __init__(self, *args, **kwargs):
    #     """ """
    #     super().__init__(*args, **kwargs)
    #     self.name = 'BaseModel'
    #     self.value = BaseModel

    # def setUp(self):
    #     """ """
    #     pass

    # def tearDown(self):
    #     try:
    #         os.remove('file.json')
    #     except:
    #         pass

    # def test_default(self):
    #     """ """
    #     i = self.value()
    #     self.assertEqual(type(i), self.value)

    # @unittest.skipIf(
    #     os.getenv('HBNB_TYPE_STORAGE') == 'db', "won't work in db")
    # def test_kwargs(self):
    #     """ """
    #     i = self.value()
    #     copy = i.to_dict()
    #     new = BaseModel(**copy)
    #     self.assertFalse(new is i)

    # @unittest.skipIf(
    #     os.getenv('HBNB_TYPE_STORAGE') == 'db', "won't work in db")
    # def test_kwargs_int(self):
    #     """ """
    #     i = self.value()
    #     copy = i.to_dict()
    #     copy.update({1: 2})
    #     with self.assertRaises(TypeError):
    #         new = BaseModel(**copy)

    # @unittest.skipIf(
    #     os.getenv('HBNB_TYPE_STORAGE') == 'db', "won't work in db")
    # def test_save(self):
    #     """ Testing save """
    #     i = self.value()
    #     i.save()
    #     key = self.name + "." + i.id
    #     with open('file.json', 'r') as f:
    #         j = json.load(f)
    #         self.assertEqual(j[key], i.to_dict())

    # def test_str(self):
    #     """ """
    #     i = self.value()
    #     self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
    #                      i.__dict__))

    # def test_todict(self):
    #     """ """
    #     i = self.value()
    #     n = i.to_dict()
    #     self.assertEqual(i.to_dict(), n)

    # def test_kwargs_none(self):
    #     """ """
    #     n = {None: None}
    #     with self.assertRaises(TypeError):
    #         new = self.value(**n)

    # @unittest.skipIf(
    #     os.getenv('HBNB_TYPE_STORAGE') != 'db', "work in db")
    # def test_kwargs_one(self):
    #     """ """
    #     n = {'Name': 'test'}
    #     with self.assertRaises(KeyError):
    #         new = self.value(**n)

    # def test_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.id), str)

    # def test_created_at(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.created_at), datetime.datetime)

    # def test_updated_at(self):
    #     """ """
    #     first = self.value()
    #     self.assertEqual(type(first.updated_at), datetime.datetime)
    #     n = first.to_dict()
    #     second = BaseModel(**n)
    #     self.assertFalse(first.created_at == second.updated_at)
