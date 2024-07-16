from flask  import Flask
from flask import request
from flask import make_response
app = Flask(__name__)


#accessing cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not raise KeyError

#setting cookies
@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username)', 'admin')
    return resp
