#!/usr/bin/python3

""" module contain engine to store data using mysql """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

import os


class DBStorage:
    """ Class to store data using mysql """

    __engine = None
    __session = None

    def __init__(self):
        """ Constructor of the class
           dialect+driver://username:password@host:port/database
           dialct: mysql
           driver: mysqldb """
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        current = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, host, db),
            pool_pre_ping=True)

        if current == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """ query on the current database session (self.__session) all objects
           depending of the class name (argument cls) """

        if isinstance(cls, str):
            cls = eval(cls)

        if cls:
            objects = self.__session.query(cls)
        else:
            classes = [User, State, City, Place, Review, Amenity]
            objects = [
                obj for cls in classes for obj in self.__session.query(cls)
            ]

        return {
            "{}.{}".format(type(obj).__name__, obj.id): obj
            for obj in objects
        }

    def new(self, obj):
        """ add the object to the current database session (self.__session) """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ close the current session """
        self.__session.remove()
