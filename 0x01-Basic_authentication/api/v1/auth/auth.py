#!/usr/bin/env python3
""" Auth class
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth:
    ''' A Class to manage the API authentication.
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """that returns False
        - path and excluded_paths"""
        if path is None:
            return True
        return False

    def authorization_header(
            self,
            request=None
            ) -> str:
        """
        returns None
        - request will be the Flask request object
        """
        if request is None:
            return None

    def current_user(
            self,
            request=None
            ) -> TypeVar('User'):
        ''' Current User
        '''
        request = Flask(__name__)
        return None
