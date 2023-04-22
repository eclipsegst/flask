from flask import Blueprint, request, jsonify, g
from app.services.user_service import new_user, get_user_by_id
from app import auth
from app.models import User

user_route = Blueprint('user_route', __name__)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@user_route.route("/api/users", methods=['POST'])
def signup():
    return new_user(request)

@user_route.route('/api/users/<int:id>')
def get_user(id):
    return get_user_by_id(id)
