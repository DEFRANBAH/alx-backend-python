@app.route('/me')
def me_api():
    user = get_current_user()
    return {
            "theme": user.theme,
            "username": user.username,
            "image":url_for('image', filename=user.image),
            }

@app.route('/users')
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
    
