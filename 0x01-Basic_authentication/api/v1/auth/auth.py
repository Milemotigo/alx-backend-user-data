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
        - path and excluded_paths
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path = path + '/'
        for p in excluded_paths:
            if not p.endswith('/'):
                p = p + '/'
        return False if path in excluded_paths else True

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
