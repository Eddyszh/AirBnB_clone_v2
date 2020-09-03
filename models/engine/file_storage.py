#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objDict = {}
        if cls is not None:
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    objDict[key] = obj
            return objDict
        return self.__objects

    def delete(self, obj=None):
        """Deletes an object from __object dictionary if exist"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if (key, obj) in self.__objects.items():
                self.__objects.pop(key)
            self.save()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """method for deserializing the JSON file to objects"""
        self.reload()
