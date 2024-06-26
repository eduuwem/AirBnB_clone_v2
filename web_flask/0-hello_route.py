#!/usr/bin/python3
"""Starts a Flask web application.
"""
from flask import Flask

my_web_app = Flask(__name__)


@my_web_app.route('/', strict_slashes=False)
def greet():
    """prints Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    my_web_app.run(host='0.0.0.0', port=5000)
