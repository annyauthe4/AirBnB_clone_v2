#!/usr/bin/python3
"""
This program starts a Flask web application, display greetings
and accept user input to display text or set default.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns greeting."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return greeting."""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns greeting with user input."""
    return f"C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Returns greeting with user input or default."""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
