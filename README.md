# Basic REST API with Flask
Simple REST API with SSL and Basic HTTP Authentication

## Install all dependencies
- pip install -r requirements.txt

## Update depedencies from code
- pip freeze > requirements.txt

## Export FLASK_APP env variable
- export FLASK_APP=app/server.py

## Run server
- python app/server.py DEBUG SSL

- Example: python app/server.py True True

## Dependencies
- pip install flask-httpauth

## Useful resources
- Flask
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- Flask HTTP auth
    - https://flask-httpauth.readthedocs.io/en/latest/
    - http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/
    - https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

