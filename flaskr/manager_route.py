from flask import Blueprint, render_template, jsonify, request, abort, url_for, redirect
from database import db

manager_blueprint = Blueprint('manager', __name__, template_folder='templates')



@manager_blueprint.route('/manager/check_subordinates', methods=['GET'])
def check_subordinates():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Employee;")
    result = cursor.fetchall()
    print(result)
    return render_template('subordinates.html', employees=result)

@manager_blueprint.route('/manager/click_subordinate', methods=['GET'])
def click_subordinate():
    ssn = request.args.get("ssn")
    cursor = db.connection.cursor()
    cursor.execute(f"""
        SELECT Bike.Serial_num, Location.Name
        FROM Employee
        JOIN Bike ON Bike.Maintenance_Employee = Employee.Ssn
        JOIN Location ON Location.Control_Employee = Employee.Ssn
        WHERE Employee.Ssn = {ssn};
        """)
    result = cursor.fetchall()
    print(result)
    return render_template('click_subordinate.html', employees=result)


