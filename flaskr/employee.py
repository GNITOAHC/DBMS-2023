from flask import Blueprint, render_template, jsonify, request, abort, url_for, redirect
from database import db

employee = Blueprint('employee', __name__, template_folder='templates')

@employee.route('/employee_root', methods=['GET'])
def employee_root():
    return render_template('employee_root.html')

@employee.route("/employee", methods=["GET"])
def employee_id():
    id = request.args.get("emp_id")

    # query data from db 
    cursor = db.connection.cursor()

    result = cursor.execute(
        f'''SELECT * FROM employee WHERE employee.Ssn = {id}'''
    )
    emp = result.fetchone()
    return render_template("employee/employee.html", name=emp.Name, sex=emp.Sex)

@employee.route("/employee/control", methods=["GET"])
def employee_control():
    id = request.args.get("emp_id")

    # query data from db 
    cursor = db.connection.cursor()

    result = cursor.execute(
        f'''select *\
        from location \
        where location.Control_Employee = {id}'''
    )
    return render_template("employee/employee_control.html", result=result, emp_id=id)

@employee.route("/employee/maintain", methods=["GET"])
def employee_maintain():
    id = request.args.get("emp_id")

    # query data from db
    cursor = db.connection.cursor()

    result = cursor.execute(
        f'''select *\
        from bike \
        where bike.Maintenance_Employee = {id}'''
    )
    return render_template("employee/employee_maintain.html", result=result, emp_id=id)

@employee.route("/employee/maintain/bike", methods=["GET"])
def employee_maintain_serial():
    id = request.args.get("emp_id")
    bike_serial = request.args.get("bike_serial")

    # query data from db
    cursor = db.connection.cursor()

    result = cursor.execute(
        f'''select *\
        from bike, location\
        where bike.Maintenance_Employee = {id} and bike.Serial_num = {bike_serial} and bike.Park_loc = location.Name '''
    )
    result = result.fetchone()
    return render_template("employee/employee_maintain_bike.html", r=result, emp_id=id, bike_serial=bike_serial)

@employee.route("/employee/userHistory", methods=["GET"])
def employee_user_history():
    id = request.args.get("emp_id")
    cardID = request.args.get("card_id")
    
    # query data from db
    cursor = db.connection.cursor()

    result = cursor.execute(
        f'''select *\
        from Rent_history \
        where Rent_history.User_cardID = {cardID} '''
    )
    return render_template("employee/employee_user_history.html", emp_id=id, r=result)

@employee.route("/employee/rentInfo", methods=["GET"])
def employee_rent_info():
    id = request.args.get("emp_id")
    rentSerial = request.args.get("rent_serial")

    # query data from db 
    cursor = db.connection.cursor()

    result = cursor.execute(
        f'''select *\
        from Rent_history \
        where Rent_history.History_serial = {rentSerial} '''
    )
    return render_template("employee/employee_rent_info.html", emp_id=id, r=result)
