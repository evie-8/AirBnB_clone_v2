#!/usr/bin/python3
<<<<<<< HEAD
"""db storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    '''database storage engine for mysql storage'''
    __engine = None
    __session = None
=======
"""Module for database storage"""


from sqlalchemy import create_engine
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, Session, scoped_session
import os


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    classes = {
            "State": State,
            "City": City
            # "User": User,
            # "Place": Place,
            # "Review": Review,
            # "Amenity": Amenity
         }

    def __init__(self):
        """Constructor for class DBStorage"""
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db),
                                      pool_pre_ping=True)
        if (os.environ.get('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        (self.__session) all objects"""

        dicts = {}
        if cls in self.classes.keys():
            for row in self.__session.query(self.classes[cls]).all():
                name = self.classes[cls].__name__
                key = f"{name}.{row.id}"
                dicts[key] = row
        else:
            t = []
            for k, v in self.classes.items():
                t .append(self.__session.query(v).all())
            for rows in t:
                for row in rows:
                    name = type(row).__name__
                    key = f"{name}.{row.id}"
                    dicts[key] = row
        return dicts

    def new(self, obj):
        """creating a new object"""
        self.__session.add(obj)

    def save(self):
        """commiting our changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete current database session if not none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all database tables"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        sessions = scoped_session(Session)
        self.__session = sessions
>>>>>>> de054e02cca2f4bcb0a7185a2468a28c1f596336
