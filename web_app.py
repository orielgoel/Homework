from flask import Flask, render_template
from db_connector import add_user, get_user, delete_user, put_user
import signal
import os

app = Flask(__name__)


@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user_name(user_id):

    if get_user(user_id) == 'failure':
        return "<H1 id='error'>" 'no such id:' + user_id + "</H1>"
    else:
        return "<H1 id='user'>" + get_user(user_id) + "</H1>"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5001)