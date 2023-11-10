#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def get_user_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({"error": "email missing"}), 400

    if password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    if users[0].is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), session_id)
        return res

    return jsonify({"error": "wrong password"}), 401
