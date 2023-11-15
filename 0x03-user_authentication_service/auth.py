#!/usr/bin/env python3
""" basic authentication
"""
from user import User
import bycrypt

class Auth:    
    def _hash_password(password: str) -> str:
        """returned bytes is a salted hash of the input password"""
        