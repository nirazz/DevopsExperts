import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("/home/nir-raz/Downloads/chromedriver"))

driver.get("http://127.0.0.1:5001/users/get_user_data/1")
# Test if the "user" element exists and print its text
try:
    H1_element = driver.find_element(By.ID, value="user")
    time.sleep(5)
    user_name = H1_element.text
    print(f"Hello Username: {user_name}")
except NoSuchElementException:
    print("Error: element with id 'user' not found")
