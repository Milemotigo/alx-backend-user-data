#!/usr/bin/env python3
""" basic authentication
"""
from user import User
from sqlalchemy.orm.exc import NoResultFound
from db import DB
import bcrypt
import uuid
from typing import Union


def _generate_uuid() -> str:
    """
    return a string representation of a new UUID
    """
    return str(uuid.uuid4())


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

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        '''
        It should expect email and password required
        arguments and return a boolean.
        '''
        user = None
        try:
            user = self._db.find_user_by(email=email)

            if user:
                get_user = user.hashed_password
                return bcrypt.checkpw(password.encode('utf-8'), get_user)
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """Creates a new session for a user.
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        if user is None:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Retrieves a user based on a given session ID.
        """
        user = None
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """this method destroys a session with the given id"""
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """16. Generate reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                user.reset_token = _generate_uuid()
                return user.reset_token
        except ValueError:
            return

    def update_password(self, reset_token: str, password: str) -> None:
        """find the corresponding
        user and update the password
        """
        user = self._db.find_user_by(reset_token)
        if user is None:
            raise ValueError
        new_hashed = _hash_password(password)
        self.update_password(user, new_hashed, reset_token=None)

