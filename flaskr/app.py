from flask import Flask, render_template, request, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

import logging

app = Flask(
    __name__,  # the name of the current file
    static_url_path="/python",  # access static file via /python/filename
    static_folder="static",  # the folder where static files at
    template_folder="templates",  # the folder where templates files at
)
# db config
app.app_context().push()
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:password@localhost/Youbike"  # mod by your self
db = SQLAlchemy(app)
Session = sessionmaker(bind=db.engine)
# add console log
app.logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
app.logger.addHandler(console_handler)


# ORM made by Neo
class User(db.Model):
    CardID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), nullable=False)
    Rent_bike_serial = db.Column(db.Integer, nullable=True)


class Bike(db.Model):
    Serial_num = db.Column(db.Integer, primary_key=True)
    Factory = db.Column(db.String(60), nullable=False)
    Is_broken = db.Column(db.Boolean, nullable=False)
    Is_using = db.Column(db.Boolean, nullable=False)
    Maintenance_record = db.Column(db.Integer, nullable=False)
    Maintenance_Employee = db.Column(db.Integer, nullable=False)
    Park_loc = db.Column(db.String(20), nullable=False)


class Location(db.Model):
    Name = db.Column(db.String(20), primary_key=True)
    Street = db.Column(db.String(30), nullable=False)
    District = db.Column(db.String(30), nullable=False)
    City = db.Column(db.String(30), nullable=False)
    Control_Employee = db.Column(db.Integer, nullable=False)


class Employee(db.Model):
    Ssn = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), nullable=False)
    Sex = db.Column(db.String(10), nullable=False)


class Ensurance(db.Model):
    CardID = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.Integer, primary_key=True)
    Amount = db.Column(db.Integer, nullable=False)


class Rent_history(db.Model):
    Start_loc = db.Column(db.String(30), primary_key=True)
    Stop_loc = db.Column(db.String(30), primary_key=True)
    Bike_serial = db.Column(db.Integer, primary_key=True)
    User_cardID = db.Column(db.Integer, primary_key=True)
    History_serial = db.Column(db.Integer, primary_key=True)
    Cost = db.Column(db.Integer, nullable=False)
    Time = db.Column(db.Integer, nullable=False)


# start of the flask router


# root
@app.route("/")
def index():
    return "Youbike"


# homepage for user
@app.route("/user")
def user_root():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")
    # access the copy of db via orm
    session = Session()
    user = session.get(User, int(card_id))
    session.close()
    if user is None:
        abort(404, "User not found")

    return render_template("user_root.html", user=user)


# user profile page
@app.route("/user/profile")
def user_profile():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")
    # access the copy of db via orm
    session = Session()
    user = session.get(User, int(card_id))  # get user by pk
    ensures = (
        session.query(Ensurance).filter_by(CardID=int(card_id)).all()
    )  # get ensurances by attibute cardId
    session.close()
    if user is None:
        abort(404, "User not found")

    return render_template("user_profile.html", user=user, ensures=ensures)


# user history page
@app.route("/user/history")
def user_history():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")
    # access the copy of db via orm
    session = Session()
    user = session.get(User, int(card_id))  # get user by pk
    histories = (
        session.query(Rent_history).filter_by(User_cardID=int(card_id)).all()
    )  # get histories by attibute cardId
    session.close()
    if user is None:
        abort(404, "User not found")

    return render_template("user_history.html", user=user, histories=histories)


# get and post the renting info
@app.route("/user/rent", methods=["POST", "GET"])
def user_rent():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")
    # post: redirect to renting api
    if request.method == "POST":
        bike_serial = request.form["bsf"]
        return redirect(
            url_for("user_rent_api", bike_serial=bike_serial, card_id=card_id)
        )
    # get: generate the form to gather the renting info
    else:
        # access the copy of db via orm
        session = Session()
        user = session.get(User, int(card_id))
        session.close()
        if user is None:
            abort(404, "User not found")
        return render_template("user_rent.html", user=user)


# renting api
@app.route("/api/user/rent")
def user_rent_api():
    # get cardId and bike serial from request arguments
    card_id = request.args.get("card_id")
    bike_serial = request.args.get("bike_serial")
    if card_id is None or bike_serial is None:
        abort(400, "Parameter not found")
    # access db physically via orm
    user = db.session.get(User, int(card_id))  # get user by pk
    if user is None:  # if user not exist
        abort(404, "User not found")
    elif user.Rent_bike_serial is not None:  # if user already rent a bike
        abort(404, "User can't rent")
    bike = db.session.get(Bike, int(bike_serial))  # get the bike by pk
    if bike is None:  # if bike not exist
        abort(404, "Bike not found")
    elif bike.Is_using is True or bike.Is_broken is True:  # if bike is not avalible
        abort(404, "Bike is not avalible")
    # update db data
    bike.Is_using = True
    user.Rent_bike_serial = bike_serial
    db.session.commit()

    # redirct to user homepage
    return redirect(url_for("user_root", card_id=card_id))


# get and post the returning info
@app.route("/user/return", methods=["POST", "GET"])
def user_return():
    # TODO:
    return "Return "


# error handler 404
@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(str(error))
    return render_template("404.html"), 404


# error handler 400
@app.errorhandler(400)
def parameter_not_found_error(error):
    app.logger.error(str(error))
    return render_template("400.html"), 400


# error handler 500
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error(str(error))
    return render_template("500.html"), 500


# default error handler
@app.errorhandler(Exception)
def default_error_handler(error):
    app.logger.error(str(error))
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run()
