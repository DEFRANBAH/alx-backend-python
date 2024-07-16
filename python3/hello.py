#module to run flask as object application on WSGI
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! this is just an example server</p>"
