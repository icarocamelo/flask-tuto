# Basic REST API with Flask and Mongodb
Simple REST API with SSL and Basic HTTP Authentication

## Install all dependencies
- pip install -r requirements.txt

## Update depedencies from code
- pip freeze > requirements.txt

## Export FLASK_APP env variable
- export FLASK_APP=app/server.py

## Mongodb
    1. Install mongodb using Docker (https://hub.docker.com/_/mongo/)
    2. Create user
        - db.users.insertOne({'name':'admin', 'password':'admin'})
    3. Check creation
        - db.users.find()

## Run server
- python app/server.py DEBUG SSL

- Example: python app/server.py True True

## Useful resources
- Flask
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- Flask HTTP auth
    - https://flask-httpauth.readthedocs.io/en/latest/
    - http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/
    - https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

