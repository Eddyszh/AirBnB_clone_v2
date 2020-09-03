#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Return states instance list"""
            from models import storage
            from models.city import City
            objList = []
            for key, value in storage.all().items():
                try:
                    if value.state_id == self.id:
                        objList.append(value)
                except AttributeError:
                    pass
            return objList
