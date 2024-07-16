
from flask import Flask
from markupsafe import escape
from flask import url_for 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/users/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {escape(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='kevin ochola'))
    print(url_for('show_post', post_id=1))
    print(url_for('show_subpath', subpath='a/b/c'))

