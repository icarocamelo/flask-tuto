from flask import Flask
from flask import request
from flask_httpauth import HTTPBasicAuth
from pymongo import MongoClient
import sys

app = Flask(__name__)
auth = HTTPBasicAuth()
client = MongoClient("mongodb://172.17.0.2:27017")
db = client.test

app_version = "0.0.1"

@auth.get_password
def get_pw(username):
    for u in db.users.find():
        if username in u['name']:
            return username
    return None

@app.route('/')
@app.route('/index')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

@app.route('/echo')
@auth.login_required
def echo():
    value = request.args.get('value')

    return "Echoing... [" + value + "]"

@app.route('/version')
@auth.login_required
def version():
    return 'Version: ' + app_version

@app.route('/users')
@auth.login_required
def get_users():
    result = ''
    for u in db.users.find():
        result = result + u['name'] + '\n'
    return result

if __name__ == '__main__':
    debug = sys.argv[1]
    ssl = sys.argv[2]

    print ('Starting server...')

    if ssl == 'True':
        print ('SSL enabled')
        app.run(ssl_context='adhoc', debug = debug == 'True')       
    else:
        print ('DEBUG enabled: ' + debug == 'True')
        app.run(debug = debug == 'True')
