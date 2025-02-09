#!/usr/bin/python3
"""
This module starts a web application that allows external
IPs and listen on port 5000. It renders greetings.
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns greeting."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
