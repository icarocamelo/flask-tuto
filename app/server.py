from flask import Flask
from flask import request

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
    app.run(debug = True)