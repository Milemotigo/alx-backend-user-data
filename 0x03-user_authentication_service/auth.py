#!/usr/bin/env python3
""" basic authentication
"""
from user import User
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
    
    def register_user(self, email: str, password: str) -> User:
        pass
