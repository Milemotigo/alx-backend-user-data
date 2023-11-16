#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def msg():
    """ return jsonify({"message": "Bienvenue"})
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def create_user() -> str:
    """Add a user at this endpoint"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 404


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """implements the login """
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        if not AUTH.valid_login(email, password):
            abort(401)
    except ValueError:
        return None
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
