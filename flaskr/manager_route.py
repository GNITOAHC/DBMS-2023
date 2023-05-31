from flask import Blueprint, render_template, jsonify, request, abort, url_for, redirect
from database import db


manager_blueprint = Blueprint('manager', __name__, template_folder='templates')



@manager_blueprint.route('/manager/check_subordinates', methods=['GET'])
def check_subordinates():
    result = db.session.execute("SELECT * FROM Employee;")
    employees = result.fetchall()
    return render_template('subordinates.html', employees=employees)

@manager_blueprint.route('/manager/click_subordinate/<int:ssn>')
def click_subordinate(ssn):
    result = db.session.execute("""
        SELECT Bike.Serial_num, Location.Name
        FROM Employee
        JOIN Bike ON Bike.Maintenance_Employee = Employee.Ssn
        JOIN Location ON Location.Control_Employee = Employee.Ssn
        WHERE Employee.Ssn = :emp_id;
        """, {"emp_id": ssn})
    employees = result.fetchall()
    return render_template('click_subordinate.html', employees=employees)


