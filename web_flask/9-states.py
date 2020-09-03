#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
"""starts a Flask web application"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_li():
    """Display a HTML page"""
    classes = {'State': State}
    states = storage.all(classes["State"]).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_li():
    """Display a HTML page"""
    classes = {'State': State}
    states = storage.all(classes["State"]).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page"""
    classes = {'State': State}
    states = storage.all(classes["State"])
    key = "State.{}".format(id)
    if key in states:
        state = states[key]
    else:
        state = None
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
