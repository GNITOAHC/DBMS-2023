from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/Youbike'
db = SQLAlchemy(app)

class User(db.Model):
    CardID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), nullable=False)
    Rent_bike_serial = db.Column(db.Integer, nullable=False)
    
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

class Rent_History(db.Model):
    Start_loc = db.Column(db.String(30), primary_key=True)
    Stop_loc = db.Column(db.String(30), primary_key=True)
    Bike_serial = db.Column(db.Integer, primary_key=True)
    User_cardID = db.Column(db.Integer, primary_key=True)
    History_serial = db.Column(db.Integer, primary_key=True)
    Cost = db.Column(db.Integer, nullable=False)
    Time = db.Column(db.Integer, nullable=False)

# Routes and other Flask code...

if __name__ == '__main__':
    app.run()
