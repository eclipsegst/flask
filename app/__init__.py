import os

from flask import Flask, g
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()

def create_api():
    app = Flask(__name__)
    api = Api(app)
    mode = os.environ.get('MODE')
    print(mode)

    if mode == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif mode == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.ProductionConfig')
    app.config['SECRET_KEY'] = 'a long secret key'
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.feed import feed_route
    app.register_blueprint(feed_route)
    from app.api.user import user_route
    app.register_blueprint(user_route)
    from app.api.auth import auth_route
    app.register_blueprint(auth_route)

    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/')
    return app

from app import api, services, models
