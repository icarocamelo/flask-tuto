from flask import Flask
from flask import request
import sys

app = Flask(__name__)

app_version = "0.0.1"

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/echo')
def echo():
    value = request.args.get('value')

    return "Echoing... [" + value + "]"

@app.route('/version')
def version():
    return 'Version: ' + app_version

if __name__ == '__main__':
    debug = sys.argv[1]
    ssl = sys.argv[2]

    print ('Starting server... DEBUG enabled: ' + debug)

    if ssl == 'True':
        print ('SSL enabled')
        app.run(ssl_context='adhoc', debug = debug == 'True')       
    else:
        print ('DEBUG enabled: ' + debug == 'True')
        app.run(debug = debug == 'True')
