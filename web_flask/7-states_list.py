#!/usr/bin/python3
"""
List of states
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def closing(exc):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
