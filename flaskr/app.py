from flask import Flask, render_template

# 創建flask
# 當前__name__表示目前.py名字
app = Flask(
    __name__,
    static_url_path="/python",
    static_folder="static",
    template_folder="templates",
)


@app.route("/")
def index():
    return "Youbike"


@app.route("/user/<int:card_id>")
def user_root(card_id):
    return render_template("user_root.html", card_id=card_id)


@app.route("/user/<int:card_id>/profile")
def user_profile(card_id):
    return "User name " + str(card_id)


@app.route("/user/<int:card_id>/history")
def user_history(card_id):
    return "History " + str(card_id)


@app.route("/user/<int:card_id>/rent")
def user_rent(card_id):
    return "rent " + str(card_id)


@app.route("/user/<int:card_id>/return")
def user_return(card_id):
    return "Return " + str(card_id)


if __name__ == "__main__":
    # 啟動 flask 程序
    app.run()
