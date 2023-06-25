import requests
import db_connector
import sys

user_id = sys.argv[1]
#  Creating the user with a POST
post = requests.post(f'http://127.0.0.1:5000/data/{user_id}', json={"user_name": "oriel"})
if post.status_code == 200:
    print('User Created:', post.json())
elif post.status_code == 500:
    print('response code 500:', post.json())
else:
    raise Exception("test failed")

import requests
import db_connector
import sys

user_id = sys.argv[1]
#  Creating the user with a POST
post = requests.post(f'http://127.0.0.1:5000/data/{user_id}', json={"user_name": "oriel"})
if post.status_code == 200:
    print('User Created:', post.json())
elif post.status_code == 500:
    print('response code 500:', post.json())
else:
    raise Exception("test failed")



# Checking the user exists with a GET
try:
    get = requests.get(f'http://127.0.0.1:5000/data/{user_id}')
    if get.ok:
        print('User verified and exists:', get.json())
    else:
        print('response code 500:', get.json())
except:
    raise Exception("test failed")

#  Login to the DB and pull the name of the user
# print(add_user('22'))

# Checking the user exists with a GET
try:
    get = requests.get(f'http://127.0.0.1:5000/data/{user_id}')
    if get.ok:
        print('User verified and exists:', get.json())
    else:
        print('response code 500:', get.json())
except:
    raise Exception("test failed")

#  Login to the DB and pull the name of the user
# print(add_user('22'))