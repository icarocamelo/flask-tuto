from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def echo():
    value = request.args.get('value')

    return "Echoing... [" + value + "]"


if __name__ == '__main__':
    app.run(debug = True)