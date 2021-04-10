import users, sqlite3
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from flask_limiter import Limiter


app = Flask(__name__)
app.config["SECRET_KEY"] = "token_key"
conn = sqlite3.connect("testdb.db", check_same_thread=False)
Limiter(app, global_limits=["5 per minute"])
conn.execute(
    "create table If not exists users( user_id text PRIMARY KEY,password text)"
)
cursor = conn.cursor()


@app.route("/signup", methods=["POST"])
def user_signup():
    data = request.get_json()
    if users.signUp(data):
        return jsonify({"message": "user is created"})
    else:
        return jsonify({"message": "user failed to create"})


@app.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    if users.login(data):
        return jsonify({"message": "login successful", "access_token": genToken(data)})
    else:
        return jsonify({"message": "login failed"})


@app.route("/verify", methods=["GET"])
def verify():
    token = request.args.get("token")
    return decode(token)


def genToken(data):
    token = jwt.encode(
        {
            "user": data["user"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        },
        app.config["SECRET_KEY"],
    )
    return token


def decode(token):
    value = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
    if users.checkToken(value):
        return jsonify({"meassage": "token is varified"})
    else:
        return jsonify({"meassage": "token is is not valid"})


if (__name__) == "__main__":

    app.run(host="localhost", port="3000", debug=True)
