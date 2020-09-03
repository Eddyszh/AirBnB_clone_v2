#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display c followed by text"""
    return 'C {}'.format(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Display python followed by text"""
    return 'Python {}'.format(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display n is a number"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Display a HTML page if n is integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
