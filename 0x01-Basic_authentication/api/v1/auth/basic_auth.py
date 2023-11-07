#!/usr/bin/env python3
"""
6. Basic auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """a class BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """BasicAuth that returns the Base64 part
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ecode_base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_base64 = base64.b64decode(base64_authorization_header)
            return decoded_base64.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """used to extract users credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if not (":" in decoded_base64_authorization_header):
            return None, None
        else:
            name, password = decoded_base64_authorization_header.split(":")
            return name, password
