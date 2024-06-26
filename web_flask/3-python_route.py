#!/usr/bin/python3
"""Starts a Flask web application.
"""
from flask import Flask

my_web_app = Flask(__name__)


@my_web_app.route('/', strict_slashes=False)
def greet():
    """prints 'Hello HBNB!'."""
    return "Hello HBNB!"


@my_web_app.route('/hbnb', strict_slashes=False)
def greet_hbnb():
    """prints 'HBNB'."""
    return "HBNB"


@my_web_app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """prints 'C' followed by the value of <text>."""
    # modified_text = text.replace("_", " ")
    modified_text = ''.join([' ' if char == '_' else char for char in text])
    return "C {}".format(modified_text)


@my_web_app.route('/python/<text>', strict_slashes=False)
@my_web_app.route('/python/', strict_slashes=False)
def python_text(text="is cool"):
    modified_text = text.replace('_', ' ')
    return "Python {}".format(modified_text)


if __name__ == "__main__":
    my_web_app.run(host='0.0.0.0', port=5000)
