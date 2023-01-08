import requests
import pymysql

# Step 1: POST the JSON payload to the API
user_name = "john"  # or any other username
payload = {"user_name": user_name}
url = "http://127.0.0.1:5000/users/1"
response = requests.post(url, json=payload)

# Step 2: Send a GET request and check the response
get_response = requests.get(url)
assert get_response.status_code == 200
assert get_response.json()['user_name'] == payload["user_name"]

# Step 3: Connect to the database and check the data
schema_name = 'freedb_freedb_nir'
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_nir', passwd='!Ryr3J%tY6MFF3a', db=schema_name)
cursor = conn.cursor()
cursor.execute("SELECT * FROM freedb_freedb_nir.users WHERE user_id=1")
result = cursor.fetchone()
if result[1] == user_name:
    print("User found in database")
else:
    raise Exception("User not found in database")
