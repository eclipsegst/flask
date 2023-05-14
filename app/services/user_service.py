from flask import abort, jsonify, g, url_for
from app.models.user import User
from app import db

def new_user(request):
    
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('user_route.get_user', id=user.id, _external=True)})

def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})
