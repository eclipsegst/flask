from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from app import db
from app.models.user import User

bp = Blueprint('auth_route', __name__, url_prefix='/api/auth')

@bp.route('/register', methods=['POST'])
def register():
    if request.is_json:
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if username and password:
            user = User.query.filter_by(username=username).first()

            if user is None:
                user = User(username=username, password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                access_token = create_access_token(identity=username)
                refresh_token = create_refresh_token(identity=username)
                return {"access_token": access_token, "refresh_token": refresh_token}, 201
            else:
                return {"msg": "Username is already taken."}, 400

    return {"msg": "Request should be JSON."}, 400

@bp.route('/login', methods=['POST'])
def login():
    if request.is_json:
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if username and password:
            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                access_token = create_access_token(identity=username)
                refresh_token = create_refresh_token(identity=username)
                return {"access_token": access_token, "refresh_token": refresh_token}, 200
            else:
                return {"msg": "Invalid credentials."}, 401

    return {"msg": "Request should be JSON."}, 400

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token)

@bp.route('/resource/protected')
@jwt_required()
def get_resource():
    current_user = get_jwt_identity()
    return jsonify({'data': 'Hello, %s!' % current_user})
