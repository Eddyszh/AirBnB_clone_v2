#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Displays Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Display c followed by text"""
    return 'C {}'.format(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    """Display python followed by text"""
    return 'Python {}'.format(text).replace("_", " ")


@app.route('/number/<int:n>')
def is_number(n):
    """Display n is a number"""
    return '{:d} is a number'.format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
