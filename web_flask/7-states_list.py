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
    states_list = ""
    for state in states:
        states_list.append(f"<LI>{state.id}: <B>{state.name}<B>\n\n")

    return render_template("7-states_list.html", states=states_list)


@app.teardown_appcontext
def closing():
    storage.close()
