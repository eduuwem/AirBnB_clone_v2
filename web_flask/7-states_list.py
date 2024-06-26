#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

my_web_app = Flask(__name__)


@my_web_app.route("/states_list", strict_slashes=False)
def states_list():
    """prints an HTML page with a list of all State objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@my_web_app.teardown_appcontext
def teardown(exc):
    """close the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    my_web_app.run(host="0.0.0.0", port=5000)
