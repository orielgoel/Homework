
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    # locate the webdriver
    driver = webdriver.Chrome(service=Service("/Users/oriel.goel/Downloads/chromedriver_mac64/chromedriver"))

    #open the site
    driver.get('http://127.0.0.1:5001/users/get_user_data/5')
except:
    print('no access to server')
#find the element
try:
    text_field = driver.find_element(By.XPATH, '//*[@id="user"]')
    print('User name is:', text_field.text)
except:
     print('username does not exist')


driver.quit()
