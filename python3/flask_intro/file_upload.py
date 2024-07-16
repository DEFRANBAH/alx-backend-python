# module to uploasd thne file on th server system

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        saved = request.files['the_file']
        saved.save('/var/www/uploads/uploaded_file.txt')

