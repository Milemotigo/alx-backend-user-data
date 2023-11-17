#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort, redirect, make_response
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


# @app.route("/sessions", methods=['DELETE'], strict_slashes=False)
# def logout():
#     """Delete a session"""
#     session_id = request.cookies.get('session_id')
#     user = AUTH.get_user_from_session_id(session_id)
#     if user:
#         AUTH.destroy_session(user.id)
#         return redirect('/')
#     else:
#         abort(403)
@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """DELETE /sessions
    Return:
        - Redirects to home route.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile() -> str:
    """GET /profile
    Return:
        - The user's profile information.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return(jsonify({"email": user.email}))
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """Get reset password token
    Return:
    """
    email = request.form.get(email)
    reset_token = AUTH.get_reset_password_token(email)
    if reset_token:
        abort(403)
    return(jsonify({"email": email, "reset_token": reset_token})), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """Update password end-point"""
    try:
        email = request.form.get(email)
        reset_token = request.form.get(reset_token)
        new_password = request.form.get(new_password)
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
