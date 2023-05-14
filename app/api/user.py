from flask import Blueprint, request
from app.services.user_service import new_user, get_user_by_id

bp = Blueprint('user_route', __name__)

@bp.route("/api/users", methods=['POST'])
def signup():
    return new_user(request)

@bp.route('/api/users/<int:id>')
def get_user(id):
    return get_user_by_id(id)
