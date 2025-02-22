#!/usr/bin/python3
"""
listening on 0.0.0.0, port 5000
Fetch data from db storage
@app.teardown_appcontext
Routes:
/cities_by_states
"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    """List all cities by states"""
    states = storage.all(State).values()
    result = []
    for state in sorted(states, key=lambda x: x.name):
        result.append([state, state.cities])
    return render_template("8-cities_by_states.html", result=result)


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
