#!/usr/bin/python3
"""
This program starts a Flask web application, displays greeting
and takes user input to be displayed.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns greeting."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns greeting."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns C with input text."""
    return f"C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_cool(text='is cool'):
    """Return python with user input or default."""
    return f"Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Return input n is a number."""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
