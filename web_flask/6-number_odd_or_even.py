#!/usr/bin/python3
"""
This program starts a Flask web application, display greetings
and uses Jinja to render HTNL page if number.
"""


from flask import Flask, render_template
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
    """Return C with user input."""
    return f"C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is cool'):
    """Return greeting with input or default."""
    return f"Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Returns n and a text."""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_html_page(n):
    """Render html page if n is a number."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Renders HTML if n is int and checks if odd or even."""
    if n % 2 == 0:
        check_even = 'even'
    else:
        check_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           check_even=check_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
