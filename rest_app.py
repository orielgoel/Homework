from flask import Flask, request
from db_connector import add_user, get_user, delete_user, put_user

app = Flask(__name__)
print("hello from inside docker")
# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # add_user(user_id, user_name)
        if add_user(user_id, user_name) == 'failure':
            return {'status': 'error', 'reason': 'id already exists'}, 500  # status code
        else:
          return {'status': 'OK', 'user_name': user_name, 'user_id': user_id}, 200  # status code
    elif request.method == 'GET':
        if get_user(user_id) == 'failure':
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            return {'user_id': user_id, 'user_name': get_user(user_id)}, 200  # status code
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # add_user(user_id, user_name)
        if put_user(user_id, user_name) == 'failure':
            return {'status': 'error', 'reason': 'no such id or same username'}, 500  # status code
        else:
            return {'status': 'OK', 'user_updated': user_name}, 200  # status code
    elif request.method == 'DELETE':
        if delete_user(user_id) == 'failure':
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            return {'status': 'error', 'user_deleted': user_id}, 200  # status code

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


app.run(host='0.0.0.0', debug=True, port=5000)