from flask import Flask, render_template, request, abort, redirect, url_for

from database import db

from user import user_blueprint


app = Flask(
    __name__,
    static_url_path='/python',
    static_folder='static',
    template_folder='templates'
)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'YOUR_PASSWORD'
app.config['MYSQL_DB'] = 'Youbike'
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)

# root
@app.route("/")
def index():
    return "Youbike"

# register blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')

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


# # default error handler
# @app.errorhandler(Exception)
# def default_error_handler(error):
#     app.logger.error(str(error))
#     return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
