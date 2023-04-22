# flask
This is a simple Flask REST API. It contains the following features:
- User registration
- User authentication
- Use token to access protected resources
- Use local or remote database (PostgreSQL)

## Structure
- `api.py` - the REST API
- `models.py` - the database models
- `config.py` - the app configuration
- app/
  - `__init__.py` - the app package, `create_api()`
  - api/
    - `auth.py` - the authentication api
    - `user.py` - the user api
    - `feed.py` - the feed api
  - services/
    - `user_service.py` - the user service
    - `feed_service.py` - the feed service

## Setup Evnironment

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

Create local .env file and set environment variable, e.g.
```bash
MODE="development"
```
## Database migrations
Update `config.py` with your database settings.

Initialize and then migrate a local database

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```
or with environment variable
```bash
env FLASK_APP=api.py flask db init
env FLASK_APP=api.py flask db migrate
env FLASK_APP=api.py flask db upgrade
```
## Run app

```bash
python app.py
```

## Run api
```bash
python api.py
```

### Examples

#### Create a new user

```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user01","password":"password"}' http://127.0.0.1:5000/api/users
```

#### Access protected resources
  
```bash
curl -u user01:password -i -X GET http://127.0.0.1:5000/api/resource
```

#### Get a token

```bash
curl -u user01:password -i -X GET http://127.0.0.1:5000/api/token
```
```
{
  "duration": 600,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjgyMTkyOTI4LjA1NzY4Mn0._QI6RmByhHKn9DR10FAz3TYgTdD8b0CqoM57cGA4bRM"
}
```
#### Access protected resources with token

```bash
curl -u eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjgyMTkyOTI4LjA1NzY4Mn0._QI6RmByhHKn9DR10FAz3TYgTdD8b0CqoM57cGA4bRM:x -i -X GET http://127.0.0.1:5001/api/resource
```
Note: there's `:x` after the token, this is because the token is not a valid username/password pair for basic auth.

## Refrences
- [https://github.com/JahnelGroup/flask-api](https://github.com/JahnelGroup/flask-api)
- [https://github.com/miguelgrinberg/REST-auth](https://github.com/miguelgrinberg/REST-auth)
- [https://github.com/Toxe/python-flask-rest-jwt](https://github.com/Toxe/python-flask-rest-jwt)
- [https://github.com/juliensalinas/python-flask-api-authentication](https://github.com/juliensalinas/python-flask-api-authentication)
