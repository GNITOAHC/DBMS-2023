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
    user = cursor.fetchone()
    if user is None:
        abort(404, "User not found")

    if user is None:  # if user not exist
        print("User not found")
        abort(404, "User not found")
    elif user['Rent_bike_serial'] is not None:  # if user already rent a bike
        print("User can't rent")
        abort(404, "User can't rent")
    
    # query bike data
    cursor.execute(f'''
        SELECT * FROM Bike
        WHERE Serial_num = {bike_serial}
    ''')
    bike = cursor.fetchone()
    if bike is None:  # if bike not exist
        print("Bike not found")
        abort(404, "Bike not found")
    elif bike['Is_using'] is True or bike['Is_broken'] is True:  # if bike is not avalible
        print("Bike is not avalible")
        abort(404, "Bike is not avalible")

    # update db data
    cursor.execute(f'''
        UPDATE Bike
        SET Is_using = 1
        WHERE Serial_num = {bike_serial};
    ''')
    db.connection.commit()
    cursor.execute(f'''
        UPDATE User
        SET Rent_bike_serial = {bike_serial}
        WHERE CardID = {card_id};
    ''')
    db.connection.commit()

    # redirct to user homepage
    return redirect(url_for("user.user_root", card_id=card_id))