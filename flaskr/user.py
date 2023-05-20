from flask import Blueprint, render_template, jsonify, request, abort, url_for, redirect
from database import db


user_blueprint = Blueprint('user', __name__, template_folder='templates')

# @user_blueprint.route('/')
# def user_root():
#     cursor = db.connection.cursor()
#     cursor.execute("SELECT * FROM User")
#     data = cursor.fetchall()
#     cursor.close()

#     return jsonify(data)

# homepage for user
@user_blueprint.route("/")
def user_root():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")
        
    # query data from db
    cursor = db.connection.cursor()
    cursor.execute(f'''
        SELECT * FROM User
        WHERE CardID = {card_id};
    ''')
    row_headers=[x[0] for x in cursor.description]
    result = cursor.fetchone()
    if result is None:
        abort(404, "User not found")
    cursor.close()

    return render_template("user_root.html", user=dict(zip(row_headers, result)))


# user profile page
@user_blueprint.route("/profile")
def user_profile():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
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

    # query user's ensurance data
    cursor.execute(f'''
        SELECT * FROM Ensurance
        WHERE CardID = {card_id};
    ''')
    row_headers=[x[0] for x in cursor.description]
    results = cursor.fetchall()
    ensures = []
    for result in results:
        ensures.append(dict(zip(row_headers, result)))

    cursor.close()

    return render_template("user_profile.html", user=user, ensures=ensures)


# user history page
@user_blueprint.route("/history")
def user_history():
    # get cardId from request arguments
    card_id = request.args.get("card_id")
    if card_id is None:
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

    # query user's rent_history data
    cursor.execute(f'''
        SELECT * FROM Rent_history
        WHERE User_cardID = {card_id};
    ''')
    row_headers=[x[0] for x in cursor.description]
    results = cursor.fetchall()
    histories = []
    for result in results:
        histories.append(dict(zip(row_headers, result)))

    cursor.close()

    return render_template("user_history.html", user=user, histories=histories)


# # get and post the renting info
# @app.route("/user/rent", methods=["POST", "GET"])
# def user_rent():
#     # get cardId from request arguments
#     card_id = request.args.get("card_id")
#     if card_id is None:
#         abort(400, "Parameter not found")
#     # post: redirect to renting api
#     if request.method == "POST":
#         bike_serial = request.form["bsf"]
#         return redirect(
#             url_for("user_rent_api", bike_serial=bike_serial, card_id=card_id)
#         )
#     # get: generate the form to gather the renting info
#     else:
#         # access the copy of db via orm
#         session = Session()
#         user = session.get(User, int(card_id))
#         session.close()
#         if user is None:
#             abort(404, "User not found")
#         return render_template("user_rent.html", user=user)


# # renting api
# @app.route("/api/user/rent")
# def user_rent_api():
#     # get cardId and bike serial from request arguments
#     card_id = request.args.get("card_id")
#     bike_serial = request.args.get("bike_serial")
#     if card_id is None or bike_serial is None:
#         abort(400, "Parameter not found")
#     # access db physically via orm
#     user = db.session.get(User, int(card_id))  # get user by pk
#     if user is None:  # if user not exist
#         abort(404, "User not found")
#     elif user.Rent_bike_serial is not None:  # if user already rent a bike
#         abort(404, "User can't rent")
#     bike = db.session.get(Bike, int(bike_serial))  # get the bike by pk
#     if bike is None:  # if bike not exist
#         abort(404, "Bike not found")
#     elif bike.Is_using is True or bike.Is_broken is True:  # if bike is not avalible
#         abort(404, "Bike is not avalible")
#     # update db data
#     bike.Is_using = True
#     user.Rent_bike_serial = bike_serial
#     db.session.commit()

#     # redirct to user homepage
#     return redirect(url_for("user_root", card_id=card_id))


# # get and post the returning info
# @app.route("/user/return", methods=["POST", "GET"])
# def user_return():
#     # TODO:
#     return "Return "