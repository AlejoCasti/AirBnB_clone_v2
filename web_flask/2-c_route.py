#!/usr/bin/python3
''' script that runs Flask to response with Hello Holberton '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    ''' return value to display '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' return value to display '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_len(text):
    ''' return value to display '''
    text = text.replace("_", " ")
    text = 'C {}'.format(text)
    return text


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
