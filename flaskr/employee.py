from flask import Blueprint, render_template, request, abort
from database import db

employee = Blueprint("employee", __name__, template_folder="templates")


@employee.route("/employee_root", methods=["GET"])
def employee_root():
    return render_template("employee/employee_root.html")


@employee.route("/", methods=["GET"])
def employee_id():
    id = request.args.get("emp_id")

    # query data from db
    cursor = db.connect.cursor()

    cursor.execute(
        f"""
        SELECT * FROM Employee
        WHERE Ssn = {id};
    """
    )
    emp = cursor.fetchone()
    if emp is None:
        abort(404, "Employee not found")
    cursor.close()
    return render_template("employee/employee.html", emp=emp)


@employee.route("/control", methods=["GET"])
def employee_control():
    id = request.args.get("emp_id")

    # query data from db
    cursor = db.connect.cursor()

    cursor.execute(
        f"""
        SELECT * FROM Location
        WHERE Control_Employee = {id};
    """
    )
    result = cursor.fetchall()
    cursor.close()
    return render_template("employee/employee_control.html", result=result, emp_id=id)


@employee.route("/maintain", methods=["GET"])
def employee_maintain():
    id = request.args.get("emp_id")

    # query data from db
    cursor = db.connect.cursor()

    cursor.execute(
        f"""
        SELECT * FROM Bike
        WHERE Maintenance_Employee = {id}
    """
    )
    result = cursor.fetchall()
    cursor.close()
    return render_template("employee/employee_maintain.html", result=result, emp_id=id)


@employee.route("/maintain/bike", methods=["GET"])
def employee_maintain_serial():
    id = request.args.get("emp_id")
    bike_serial = request.args.get("bike_serial")

    # query data from db
    cursor = db.connect.cursor()

    cursor.execute(
        f"""
        SELECT * FROM Bike, Location
        WHERE Bike.Maintenance_Employee = {id} and Bike.Serial_num = {bike_serial} and Bike.Park_loc = Location.Name
    """
    )
    result = cursor.fetchone()
    cursor.close()
    return render_template(
        "employee/employee_maintain_bike.html",
        r=result,
        emp_id=id,
        bike_serial=bike_serial,
    )


@employee.route("/userHistory", methods=["GET"])
def employee_user_history():
    id = request.args.get("emp_id")
    cardID = request.args.get("card_id")
    if cardID is None:
        cardID = 000

    # query data from db
    cursor = db.connect.cursor()

    cursor.execute(
        f"""
        SELECT * FROM Rent_history
        WHERE User_cardID = {cardID}
    """
    )
    result = cursor.fetchall()
    row = cursor.rowcount
    cursor.close()
    return render_template(
        "employee/employee_user_history.html", emp_id=id, r=result, row=row
    )


@employee.route("/rentInfo", methods=["GET"])
def employee_rent_info():
    id = request.args.get("emp_id")
    rentSerial = request.args.get("rent_serial")
    if rentSerial is None:
        rentSerial = 000

    # query data from db
    cursor = db.connect.cursor()

    cursor.execute(
        f"""
        SELECT * FROM Rent_history
        WHERE History_serial = {rentSerial}
    """
    )
    result = cursor.fetchall()
    row = cursor.rowcount
    cursor.close()
    return render_template(
        "employee/employee_rent_info.html", emp_id=id, r=result, row=row
    )
