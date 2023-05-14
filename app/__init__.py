import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from datetime import timedelta

from config import DevelopmentConfig, ProductionConfig, TestingConfig

db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    api = Api(app)

    if os.getenv('FLASK_DEBUG') == '1':
        app.config.from_object(DevelopmentConfig)
        print("Development mode")
    elif os.getenv('FLASK_DEBUG') == '0':
        app.config.from_object(ProductionConfig)
        print("Production mode")
    else:
        app.config.from_object(TestingConfig)
        print("Testing mode")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_blueprints(app)

    # Access token will expire in 15 minutes
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
    # Refresh token will expire in 30 days
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

    return app

def register_blueprints(app):
    from app.api.auth import bp as auth_route
    app.register_blueprint(auth_route)
    from app.api.feed import bp as feed_route
    app.register_blueprint(feed_route)
    from app.api.user import bp as user_route
    app.register_blueprint(user_route)
