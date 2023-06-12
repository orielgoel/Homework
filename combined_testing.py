import requests
from db_connector import get_user
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Set this ID for creating a new user, increment by 1 each time of running
user_id = 10


#  BACKEND TESTING
#  Creating the user with a POST
post = requests.post(f'http://127.0.0.1:5000/data/{user_id}', json={"user_name": "oriel"})
if post.ok:
    print('User Created:', post.json())
else:
    raise Exception("test failed")


# Checking the user exists with a GET
try:
    get = requests.get(f'http://127.0.0.1:5000/data/{user_id}')
    if get.ok:
        print('User verified and exists:', get.json())
    else:
        raise Exception("test failed")
except:
    raise Exception("test failed")

#  Login to the DB and pull the name of the user
print('pymysql found username:', get_user(user_id))



#  FRONT-END SELENIUM TESTING
try:
    # locate the webdriver
    driver = webdriver.Chrome(service=Service("/Users/oriel.goel/Downloads/chromedriver_mac64/chromedriver"))

    #open the site
    driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
except:
    raise Exception("test failed")
#find the element
try:
    text_field = driver.find_element(By.XPATH, '//*[@id="user"]')
    print('Selenium found username:', text_field.text)
except:
     raise Exception("test failed")


driver.quit()
