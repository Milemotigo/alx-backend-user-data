#!/usr/bin/env python3
"""session_auth"""
from api.v1.auth.auth import Auth
import os

switch_value = os.getenv('SWITCH_VALUE')


class SessioAuth(Auth):
    pass