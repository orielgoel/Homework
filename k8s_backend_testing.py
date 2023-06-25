import requests
import db_connector
import sys

user_id = sys.argv[1]
# user_id = 22

# Read the file contents
try:
    with open('k8s_url.txt', 'r') as file:  # Replace with the actual path to your file
      file_content = file.readline().strip()  # Strip any leading/trailing whitespace
except:
    raise Exception("test failed")

url = f'{file_content}/data/{user_id}'

#  Creating the user with a POST
post = requests.post(url, json={"user_name": "oriel"})
if post.status_code == 200:
    print('User Created:', post.json())
elif post.status_code == 500:
    print('response code 500:', post.json())
else:
    raise Exception("test failed")



# Checking the user exists with a GET
try:
    get = requests.get(f'{file_content}/data/{user_id}')
    if get.ok:
        print('User verified and exists:', get.json())
    else:
        print('response code 500:', get.json())
except:
    raise Exception("test failed")

#  Login to the DB and pull the name of the user
# print(add_user('22'))