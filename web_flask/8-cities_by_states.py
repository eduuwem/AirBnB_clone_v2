#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

my_web_app = Flask(__name__)


@my_web_app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """prints an HTML page with a list of all states and related cities.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@my_web_app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    my_web_app.run(host="0.0.0.0", port=5000)
