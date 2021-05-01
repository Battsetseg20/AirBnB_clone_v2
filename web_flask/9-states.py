#!/usr/bin/python3
"""
Starts Flask web app
"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page """
    states = storage.all(State)
    id = None
    return render_template("9-states.html", states=states, id=id)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page """
    states = storage.all(State)
    id = 'State.' + str(id)
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
