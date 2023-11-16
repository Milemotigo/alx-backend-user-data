#!/usr/bin/env python3
""" basic authentication
"""
from user import User
from sqlalchemy.orm.exc import NoResultFound
from db import DB
import bcrypt


def _hash_password(password: str) -> str:
    """returned bytes is a salted hash of the input password"""
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    # def register_user(self, email: str, password: str) -> User:
    #     user = self._db.find_user_by(email=email)
    #     if user:
    #         raise ValueError(f"User {email} already exists")
    #     else:
    #         raise NoResultFound()
    #     pw = _hash_password(password)
    #     new_user = self._db.add_user(email, pw)
    #     return new_user
    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")

    def valid_login(email: str, password: str) -> boolean:
        '''
        It should expect email and password required
        arguments and return a boolean.
        '''
        user = self._db.find_user_by(email=email)
        if bcrypt.checkpw(user.password, password):
            return True
        else:
            return false

