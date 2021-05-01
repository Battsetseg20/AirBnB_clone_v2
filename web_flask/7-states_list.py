#!/usr/bin/python3
"""
Starts a Flask web application:
Web application must be listening on 0.0.0.0, port 5000
Use storage for fetching data from the storage engine:
    (FileStorage or DBStorage)
    => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
Routes:
     /states_list:
         H1 tag: “States”
         UL tag: with the list of all State objects present in DBStorage
         LI rag: description of one State: <state.id>: <B><state.name></B>
Use the option strict_slashes=False in route def
"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays a HTML page contaby states"""
    state_dict = storage.all(State).values()
    return render_template('7-states_list.html', states=state_dict)


@app.teardown_appcontext
def remove_session(exception):
    """Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
