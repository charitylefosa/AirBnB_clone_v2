#!/usr/bin/python3
"""
A script to to load all cities of a State,
Ig storage engine is DBStorage, use cities relationship
Otherwise, use the public getter method cities.
After ech request remove the current method cities.
Declareamethod to handle @app.trardown_appcontext
Call in this method storage.close()
Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”

"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """A function that serves as the home route of the application.
    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays cities per state"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_context(ctx):
    """Displays cities per state"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
