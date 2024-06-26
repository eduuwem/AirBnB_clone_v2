#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

my_web_app = Flask(__name__)


@my_web_app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all State
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@my_web_app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@my_web_app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    my_web_app.run(host="0.0.0.0", port=5000)
