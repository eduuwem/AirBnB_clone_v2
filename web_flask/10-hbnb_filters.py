#!/usr/bin/python3
"""Starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

my_web_app = Flask(__name__)


@my_web_app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """prints the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@my_web_app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    my_web_app.run(host="0.0.0.0", port=5000)
