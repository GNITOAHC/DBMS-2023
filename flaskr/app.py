from flask import Flask, render_template, request, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import os

import logging

# 創建flask
# 當前__name__表示目前.py名字
app = Flask(
    __name__,
    static_url_path="/python",
    static_folder="static",
    template_folder="templates",
)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/Youbike"
app.config["SECRET_KEY"] = os.urandom(24)
db = SQLAlchemy(app)
Session = sessionmaker(bind=db.engine)


# 配置日志记录
app.logger.setLevel(logging.DEBUG)  # 设置日志级别
console_handler = logging.StreamHandler()  # 创建控制台日志处理程序
console_handler.setLevel(logging.DEBUG)  # 设置控制台日志级别
app.logger.addHandler(console_handler)  # 添加控制台日志处理程序到应用程序的日志记录器中


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


@app.route("/")
def index():
    return "Youbike"


@app.route("/user")
def user_root():
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")

    session = Session()  # 创建Session对象
    user = session.get(User, int(card_id))  # 使用Session对象执行查询
    session.close()  # 关闭Session

    if user is None:
        abort(404, "User not found")
    return render_template("user_root.html", user=user)


@app.route("/user/profile")
def user_profile():
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")

    session = Session()  # 创建Session对象
    user = session.get(User, int(card_id))  # 使用Session对象执行查询
    ensures = (
        session.query(Ensurance).filter_by(CardID=int(card_id)).all()
    )  # 使用Session对象执行筛选查询
    session.close()  # 关闭Session

    if user is None:
        abort(404, "User not found")
    return render_template("user_profile.html", user=user, ensures=ensures)


@app.route("/user/history")
def user_history():
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")

    session = Session()  # 创建Session对象
    user = session.get(User, int(card_id))  # 使用Session对象执行查询
    histories = (
        session.query(Rent_history).filter_by(User_cardID=int(card_id)).all()
    )  # 使用Session对象执行筛选查询
    session.close()  # 关闭Session

    if user is None:
        abort(404, "User not found")
    return render_template("user_history.html", user=user, histories=histories)


@app.route("/user/rent", methods=["POST", "GET"])
def user_rent():
    card_id = request.args.get("card_id")
    if card_id is None:
        abort(400, "Parameter not found")

    if request.method == "POST":
        bike_serial = request.form["bsf"]
        return redirect(
            url_for("user_rent_api", bike_serial=bike_serial, card_id=card_id)
        )
    else:
        session = Session()  # 创建Session对象
        user = session.get(User, int(card_id))  # 使用Session对象执行查询
        session.close()  # 关闭Session
        if user is None:
            abort(404, "User not found")
        return render_template("user_rent.html", user=user)


@app.route("/api/user/rent")
def user_rent_api():
    card_id = request.args.get("card_id")
    bike_serial = request.args.get("bike_serial")
    if card_id is None or bike_serial is None:
        abort(400, "Parameter not found")

    user = db.session.get(User, int(card_id))  # 使用Session对象执行查询
    if user is None:
        abort(404, "User not found")
    elif user.Rent_bike_serial is not None:
        abort(404, "User can't rent")

    bike = db.session.get(Bike, int(bike_serial))  # 使用Session对象执行查询
    if bike is None:
        abort(404, "Bike not found")
    elif bike.Is_using is True or bike.Is_broken is True:
        abort(404, "Bike is not avalible")

    bike.Is_using = True
    user.Rent_bike_serial = bike_serial
    db.session.commit()
    return redirect(url_for("user_root", card_id=card_id))


@app.route("/user/return", methods=["POST", "GET"])
def user_return():
    return "Return "


@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(str(error))
    return render_template("404.html"), 404


@app.errorhandler(400)
def parameter_not_found_error(error):
    app.logger.error(str(error))
    return render_template("400.html"), 400


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error(str(error))
    return render_template("500.html"), 500


@app.errorhandler(Exception)
def default_error_handler(error):
    app.logger.error(str(error))
    return render_template("500.html"), 500


if __name__ == "__main__":
    # 啟動 flask 程序
    app.run()
