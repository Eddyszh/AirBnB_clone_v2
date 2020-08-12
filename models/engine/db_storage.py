#!/usr/bin/python3
"""DATABASE Module"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
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

    def __init__(self):
        """Costructor"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        tables = {"Amenity": Amenity, "City": City, "State": State,
                  "Place": Place, "Review": Review, "User": User}
        objDict = {}

        for key in tables:
            if cls is None or cls in tables:
                obj = self.__session.query(tables[cls]).all()
                for i in obj:
                    key = type(obj).__name__ + '.' + obj.id
                    objDict[key] = obj
        return objDict

    def new(self, obj):
        """Adds an object to the current database session"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()
