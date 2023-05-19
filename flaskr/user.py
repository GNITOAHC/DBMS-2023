from flask import Blueprint, render_template, jsonify
from database import db


user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/')
def user_root():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM User")
    data = cursor.fetchall()
    cursor.close()

    return jsonify(data)