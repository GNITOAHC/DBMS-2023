from flask import Flask

from database import db

from user import user_blueprint


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'YOUR_PASSWORD'
app.config['MYSQL_DB'] = 'Youbike'
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)

# register blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')


if __name__ == '__main__':
    app.run()
