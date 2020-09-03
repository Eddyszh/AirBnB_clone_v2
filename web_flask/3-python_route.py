#!/usr/bin/python3
from flask import Flask
"""starts a Flask web application"""
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
