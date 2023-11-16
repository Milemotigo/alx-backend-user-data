#!/usr/bin/env python3

from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def msg():
    """ return jsonify({"message": "Bienvenue"})
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """add a user in this end point"""
    email = request.form.get(email)
    password = request.form.get(password)
    #user = AUTH._db.find_user_by(email)
    #if user:
    #   return jsonify({"message": "email already registered"}), 404
    #AUTH.register_user(email=email, password=password)
    #return ({"email": email, "message": "user created"}), 201
    try:
        AUTH.register_user(email=email, password=password)
        return ({"email": email, "message": "user created"}), 201
    except ValueError():
        return jsonify({"message": "email already registered"}), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
