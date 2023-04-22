import os

from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

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
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.feed import feed_route
    app.register_blueprint(feed_route)

    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/')
    return app

from app import api, services, models
