from flask import Flask, render_template
from dotenv import load_dotenv
import os

from database import db


from manager import manager_blueprint
from user import user_blueprint
from api import api_blueprint
from employee import employee


app = Flask(
    __name__,
    static_url_path="/python",
    static_folder="static",
    template_folder="templates",
)
load_dotenv()

app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MYSQL_DB"] = "Youbike"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

db.init_app(app)


# root
@app.route("/")
def index():
    return render_template("homepage.html")


# register blueprint
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(api_blueprint, url_prefix="/api")
app.register_blueprint(employee, url_prefix="/employee")
app.register_blueprint(manager_blueprint, url_prefix="/manager")


# # error handler 404
# @app.errorhandler(404)
# def not_found_error(error):
#     app.logger.error(str(error))
#     return render_template("404.html"), 404


# # error handler 400
# @app.errorhandler(400)
# def parameter_not_found_error(error):
#     app.logger.error(str(error))
#     return render_template("400.html"), 400


# # error handler 500
# @app.errorhandler(500)
# def internal_server_error(error):
#     app.logger.error(str(error))
#     return render_template("500.html"), 500


# default error handler
@app.errorhandler(Exception)
def default_error_handler(error):
    app.logger.error(str(error))
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
