
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()
