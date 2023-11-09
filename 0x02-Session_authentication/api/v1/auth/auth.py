#!/usr/bin/env python3
""" Auth class
"""
from flask import Flask, request
from typing import List, TypeVar
import os


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
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(
            self,
            request=None
            ) -> str:
        """
        returns None
        - request will be the Flask request object
        """
        authorized_header = request.headers.get('Authorization')
        if request is None:
            return None
        return authorized_header

    def current_user(
            self,
            request=None
            ) -> TypeVar('User'):
        ''' Current User
        '''
        request = Flask(__name__)
        return None

    def session_cookie(self, request=None):
        """Returns a cookie from the server"""
        if request is None:
            return None
        _my_session_id = os.getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
