import requests
import db_connector
user_id = 3

#  Creating the user with a POST
post = requests.post(f'http://127.0.0.1:5000/data/{user_id}', json={"user_name": "oriel"})
if post.ok:
    print('User Created:', post.json())
else:
        print('response code 500:', post.json())


# Checking the user exists with a GET
try:
    get = requests.get(f'http://127.0.0.1:5000/data/{user_id}')
    if get.ok:
        print('User verified and exists:', get.json())
    else:
        print('response code 500:', get.json())
except:
    print('No access to server with GET')

#  Login to the DB and pull the name of the user
# print(add_user(user_id))