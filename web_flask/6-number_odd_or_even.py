#!/usr/bin/python3
''' script that runs Flask to response with Hello Holberton '''
from flask import Flask, render_template
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
    text = 'C {}'.format(text.replace("_", " "))
    return text


@app.route('/python',  strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_len(text='is_cool'):
    ''' return value to display '''
    text = 'Python {}'.format(text.replace("_", " "))
    return text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    ''' return value to display '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' return value to display '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_template(n):
    ''' return value to display '''
    if (n % 2) == 0:
        type_n = 'even'
    else:
        type_n = 'odd'
    return render_template('6-number_odd_or_even.html',
                           number=n, type_n=type_n)


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
