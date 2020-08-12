#!/usr/bin/python3
"""DATABASE Module"""
from base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage():
    """DataBase Storage class"""
    __engine = None
    __session = None

    __tables = {"Ameninity": Amenity, "City": City, "Place": Place,
          "Review": Review, "State": State, "User": User}

    def __init__(self):
        """Costructor"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("localhost")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB), pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        objDict = {}
        for key in self.__tables:
            if cls is None or cls in self.__tables:
                obj = self.__session.query(self.__tables[cls]).all()
                for i in obj:
                    key = type(obj).__name__ + '.' + obj.id
                    objDict[key] = obj
        return objDict

    def new(self, obj):
        """Adds an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=false)
        Session  = scoped_session(session_factory)
        self.__session = Session()
