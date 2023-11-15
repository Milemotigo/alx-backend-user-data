#!/usr/bin/env python3
"""DB module.
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    # def find_user_by(self, **kwargs) -> User:
    #     """Finds a user based on a set of filters.
    #     """
    #     fields, values = [], []
    #     for key, value in kwargs.items():
    #         if hasattr(User, key):
    #             fields.append(getattr(User, key))
    #             values.append(value)
    #         else:
    #             raise InvalidRequestError()
    #     result = self._session.query(User).filter(
    #         tuple_(*fields).in_([tuple(values)])).first()
    #     if result is None:
    #         raise NoResultFound()
    #     return result
    def find_user_by(self, **kwargs) -> User:
        """Finds a user based on a set of filters.
        """
        query = None
        for key, value in kwargs.items():
            if hasattr(User, key):
                filter = getattr(User, key) == value
                query = self._session.query(User).filter(filter)
                user = query.first()
                if user:
                    return user
                else:
                    raise NoResultFound()
        if query is None:
            raise InvalidRequestError()

    def update_user(self, user_id: int, **kwargs) -> None:
        """upadate users in the database"""
        if user_id == User.id:
            user_to_update = self.find_user_by(user_id=id)
            if user_to_update is None:
                raise ValueError()
            for key, value in kwargs.items():
                if hasattr(user_to_update, key):
                    new_att = setattr(user_to_update, key, value)
                    self._session.add(new_att)
                    self._session.commit()
        return None
