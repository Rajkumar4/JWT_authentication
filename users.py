from flask_sqlalchemy import SQLAlchemy
from app import conn, cursor as cr
import uuid
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import logging



def signUp(data):
    if data["user"] == "" or data["password"] == "":
        logging.error("either user or password is empty")
        return false
    encoded = generate_password_hash(data["password"])
    cr.execute(
        "insert into users (user_id,password)VALUES(?,?)",
        (data["user"], encoded),
    )
    conn.commit()
    logging.info("User " + data["user"] + " is created")
    return True


def login(data):
    if data["user"] == "" or data["password"] == "":
        logging.error("either user or password is empty")
        return False
    try:
        cr.execute("select password from users where user_id=?", (data["user"],))
    except:
        logging.error("user_id is not found")
        return False
    row = cr.fetchall()
    for ls in row:
        try:
            check_password_hash(ls[0], data["password"])
        except:
            logging.error("wrong password")
            return false
    return True


def checkToken(value):
    if value["user"] == "":
        logging.error("User not found in token")
        return False
    cr.execute("select * from users where user_id=?", (value["user"],))
    row = cr.fetchall()
    if len(row) == 1:
        return True
    else:
        return False