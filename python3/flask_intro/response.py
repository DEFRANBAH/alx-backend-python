
from flask import Flask, request, make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    response = make_response(render_template('error.html'), 404)
    response.headers['X-Something'] = 'A value'
    return response
