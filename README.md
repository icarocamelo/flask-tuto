# Basic REST API with Flask
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Install all dependencies
- pip install -r requirements.txt

## Update depedencies from code
- pip freeze > requirements.txt

## Install SSL certificate (optional)
- pip install pyopenssl

## Export FLASK_APP env variable
- export FLASK_APP=app/server.py

## Run server
- python app/server.py DEBUG SSL

- Example: python app/server.py True True

## Useful resources
- Flask HTTP auth
    - https://flask-httpauth.readthedocs.io/en/latest/
    - http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/
    - https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

