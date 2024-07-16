 from flask import Flask
 from flask import request
 from werkzeug.utils import secure_filename
 app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f'/var/www/uploads/{secure_filename(f.filename)}')
