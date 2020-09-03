#!/usr/bin/python3
''' script that runs Flask to response with Hello Holberton '''
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(error):
    ''' ends every process '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' return list of states '''
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=all_states)


@app.route('/cities_by_states', strict_slashes=False)
def state_cities_list():
    ''' return list of states '''
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
