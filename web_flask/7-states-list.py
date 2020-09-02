#!/usr/bin/python3
''' script that runs Flask to response with Hello Holberton '''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' return list of states '''
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    ''' ends every process '''
    storage.close()


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
