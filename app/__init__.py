from flask import Flask
from flask_restful import Resource, Api

def create_api():
    app = Flask(__name__)
    api = Api(app)

    if app.config['FLASK_ENV'] == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif app.config['FLASK_ENV'] == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.ProductionConfig')

    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/')
    return app
