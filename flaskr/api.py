from flask import Blueprint, render_template, jsonify, request, abort, url_for, redirect
from database import db


api_blueprint = Blueprint('api', __name__, template_folder='templates')

# renting api
@api_blueprint.route("/user/rent")
def user_rent_api():
    # get cardId and bike serial from request arguments
    card_id = request.args.get("card_id")
    bike_serial = request.args.get("bike_serial")
    if card_id is None or bike_serial is None:
        abort(400, "Parameter not found")

    # query data from db
    cursor = db.connection.cursor()
    # query user data
    cursor.execute(f'''
        SELECT * FROM User
        WHERE CardID = {card_id};
    ''')
    row_headers=[x[0] for x in cursor.description]
    result = cursor.fetchone()
    if result is None:
        abort(404, "User not found")
    user = dict(zip(row_headers, result))
    
    if user is None:  # if user not exist
        print("User not found")
        abort(404, "User not found")
    elif user.Rent_bike_serial is not None:  # if user already rent a bike
        print("User can't rent")
        abort(404, "User can't rent")
    bike = db.session.get(Bike, int(bike_serial))  # get the bike by pk
    if bike is None:  # if bike not exist
        print("Bike not found")
        abort(404, "Bike not found")
    elif bike.Is_using is True or bike.Is_broken is True:  # if bike is not avalible
        print("Bike is not avalible")
        abort(404, "Bike is not avalible")

    # update db data
    bike.Is_using = True
    user.Rent_bike_serial = bike_serial
    db.session.commit()

    # redirct to user homepage
    return redirect(url_for("user_root", card_id=card_id))