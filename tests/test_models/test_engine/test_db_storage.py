#!/usr/bin/python3
"""Module for testing db storage"""
import unittest
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy.orm import sessionmaker

@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "test in db storage")
class test_DbStorage(unittest.TestCase):
    def testAmenity(self):
        amenity = Amenity(name="Internet")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Cable")

    def testCity(self):
        city = City(name="Medellin")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Medellin")

    def testPlace(self):
        place = Place(name="House", number_rooms=2)
        if place.id in models.storage.all():
            self.assertTrue(place.name, "House")
            self.assertTrue(place.number_rooms, 2)

    def testReview(self):
        review = Review(text="School")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "School")

    def testState(self):
        state = State(name="Antioquia")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Antioquia")

    def testUser(self):
        user = User(name="Holberton")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Holberton")

    def tearDown(self):
        self.session.close()
        self.session.rollback()
