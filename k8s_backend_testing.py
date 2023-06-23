import requests
import db_connector
import sys

user_id = sys.argv[1]


# Read the file contents
with open('k8s_url.txt', 'r') as file:  # Replace with the actual path to your file
    file_content = file.readline().strip()

#  Creating the user with a POST
url = f'{file_content}/data/{user_id}'
post = requests.post(url, json={"user_name": "oriel"})
if post.ok:
    print('User Created:', post.json())
else:
        print('response code 500:', post.json())


# Checking the user exists with a GET
try:
    get = requests.get(f'{file_content}/data/{user_id}')
    if get.ok:
        print('User verified and exists:', get.json())
    else:
        print('response code 500:', get.json())
except:
    print('No access to server with GET')

#  Login to the DB and pull the name of the user
# print(add_user(user_id))