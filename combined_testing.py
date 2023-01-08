import time
import requests
import pymysql
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Step 1: POST the JSON payload to the API
user_name = "Nir"  # or any other username
payload = {"user_name": user_name}
url = "http://127.0.0.1:5000/users/2"
response = requests.post(url, json=payload)

# Step 2: Send a GET request and check the response
get_response = requests.get(url)
try:
    assert get_response.json()['user_name'] == payload["user_name"]
except AssertionError:
    raise Exception("GET request response does not match expected data")

# Step 3: Connect to the database and check the data
schema_name = 'freedb_freedb_nir'
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_nir', passwd='!Ryr3J%tY6MFF3a',
                       db=schema_name)
cursor = conn.cursor()
# cursor.execute("SELECT * FROM freedb_freedb_nir.users WHERE id=%s", response.json()['user_id'])
cursor.execute("SELECT * FROM freedb_freedb_nir.users WHERE user_id=2")
result = cursor.fetchone()
try:
    assert result[1] == "Nir"
except AssertionError:
    raise Exception("Data not found in database")

# Step 4: Start a Selenium Webdriver session
driver = webdriver.Chrome()

# Step 5: Navigate to web interface URL using the new user idcursor.execute("SELECT * FROM freedb_freedb_nir.users WHERE user_id=2")
# driver.get("http://localhost:5001//users/get_user_data/" + response.json()['user_id'])
driver.get("http://127.0.0.1:5001/users/get_user_data/2")

# Step 6: Check that the username is correct
try:
    user_name_element = driver.find_element(By.ID, value="user")
    time.sleep(5)
    assert user_name_element.text == "Hello Nir!"
    print(f"Passed Tests: {user_name_element.text}")
except NoSuchElementException:
    print("Error: element with id 'user' not found")
except AssertionError:
    raise Exception("Username does not match expected value")

# If all steps are successful, close the browser
driver.quit()
