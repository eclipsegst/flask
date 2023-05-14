# flask
This is a simple Flask REST API. It contains the following features:
- User registration
- User authentication
- Use token to access protected resources
- Use local or remote database (PostgreSQL)

## Project Structure
- `run.py` - the app entry point
- `config.py` - the app configuration
- `requirements.txt` - the app dependencies
- `migrations/` - the database migrations
- `.env` - the environment variables, you need to create your local .env file, see below setup
- app/
  - `__init__.py` - the app package, `create_app()`
  - api/
    - `auth.py` - the authentication api
    - `user.py` - the user api
    - `feed.py` - the feed api
  - services/
    - `user_service.py` - the user service
    - `feed_service.py` - the feed service
  - models/
    - `user.py` - the user model
    - `feed.py` - the feed model

## Setup Evnironment

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

Create local .env file and set environment variable, e.g.
```bash
FLASK_DEBUG=1
DATABASE_URL=postgresql://db_username:db_password@127.0.0.1:5432/db_name
JWT_SECRET_KEY=your-secret-key
```
- **FLASK_DEBUG**: if set to 1, the app will run in debug mode, if set to 0, the app will run in production mode, otherwise, the app will run in test mode.
- **DATABASE_URL**: the database url, check `config.py` for more details.
- **JWT_SECRET_KEY**: the secret key for JWT.

## Database migrations

Initialize and then migrate a local database

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```
or with environment variable
```bash
env FLASK_APP=run.py FLASK_DEBUG=1 flask db init
env FLASK_APP=run.py FLASK_DEBUG=1 flask db migrate
env FLASK_APP=run.py FLASK_DEBUG=1 flask db upgrade
```
Note: For production database, use `FLASK_DEBUG=0` instead.

## Run app

```bash
python run.py
```
or
```
flask run
```

### API call examples

**Register a new user**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"test","password":"test"}' http://localhost:5000/api/auth/register
```

**Log in as a user**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"test","password":"test"}' http://localhost:5000/api/auth/login
```

**Refresh token**
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NDAzMTQzMSwianRpIjoiODA4MDU2OGUtMTZiNC00NmMzLWFjMmYtZDE3MzFhNGEyMjQwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJ0ZXN0MSIsIm5iZiI6MTY4NDAzMTQzMSwiZXhwIjoxNjg2NjIzNDMxfQ.NKbXfcHJ_--7OjNtV9qxjOhJ9tnySK8BKjf01w7AZWg" -i -X POST http://127.0.0.1:5000/api/auth/refresh
```

**Access protected resources with token**
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NDAzMzA1NywianRpIjoiNDkzN2U3Y2EtYmQ0NS00Y2Y0LWE0OWYtNDZmNWI0MjM0NWM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QxIiwibmJmIjoxNjg0MDMzMDU3LCJleHAiOjE2ODQwMzM5NTd9.xanehglkDtepPcp9yPpm_-gIVTjhy4lVtTxDmqqpk3Q" -i -X GET http://127.0.0.1:5000/api/auth/resource/protected
```
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NDAzMzA1NywianRpIjoiNDkzN2U3Y2EtYmQ0NS00Y2Y0LWE0OWYtNDZmNWI0MjM0NWM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QxIiwibmJmIjoxNjg0MDMzMDU3LCJleHAiOjE2ODQwMzM5NTd9.xanehglkDtepPcp9yPpm_-gIVTjhy4lVtTxDmqqpk3Q" -i -X GET http://127.0.0.1:5000/api/feed/protected
```

## Refrences
- [cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful): Flask cookiecutter template for builing APIs with flask-restful, including JWT auth, cli, tests, swagger, docker and more
- [https://github.com/JahnelGroup/flask-api](https://github.com/JahnelGroup/flask-api)
- [https://github.com/miguelgrinberg/REST-auth](https://github.com/miguelgrinberg/REST-auth)
- [https://github.com/Toxe/python-flask-rest-jwt](https://github.com/Toxe/python-flask-rest-jwt)
- [https://github.com/juliensalinas/python-flask-api-authentication](https://github.com/juliensalinas/python-flask-api-authentication)
