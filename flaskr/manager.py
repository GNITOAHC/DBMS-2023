from flask import Blueprint, render_template, jsonify, request, abort, url_for, redirect
from database import db

manager_blueprint = Blueprint("manager", __name__, template_folder="templates")


@manager_blueprint.route("/manager/check_subordinates", methods=["GET"])
def check_subordinates():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Employee;")
    result = cursor.fetchall()
    return render_template("manager/subordinates.html", employees=result)


@manager_blueprint.route("/manager/click_subordinate", methods=["GET"])
def click_subordinate():
    ssn = request.args.get("ssn")
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
        SELECT Bike.Serial_num, Location.Name
        FROM Employee
        JOIN Bike ON Bike.Maintenance_Employee = Employee.Ssn
        JOIN Location ON Location.Control_Employee = Employee.Ssn
        WHERE Employee.Ssn = {ssn};
        """
    )
    result = cursor.fetchall()
    return render_template("manager/click_subordinate.html", employees=result)

@manager_blueprint.route('/bike/<int:serial_num>', methods=['DELETE'])
def delete_bike(serial_num):
    cursor = db.connection.cursor()
    cursor.execute(
        f"""
        DELETE
        FROM Bike
        WHERE Serial_num = {serial_num};
        """
    )
    cursor.execute(
        f"""
        UPDATE Rent_History
        SET Bike_serial = NULL
        WHERE Bike_serial = {serial_num};
        """
    )
    db.connection.commit()
    return ''
