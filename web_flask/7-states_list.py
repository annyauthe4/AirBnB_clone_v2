#!/usr/bin/python3
"""
This program starts a Flask web application and displays an HTML
page for list of states fetched from a database.
"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Fetches data from database and render it on HTML."""
    states = sorted(list(storage.all("State").values(), key=lambda x: x.name))
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
