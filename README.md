# DevopsExperts
Final Project - First Part


Libraries Used: pymysql, requests, json, flask, Selenium webdriver

![ksnip_20230108-123650](https://user-images.githubusercontent.com/58972577/211191607-ffb5a86b-e09d-4373-8a04-79e53341e2ec.png)

REST API (including tests)
DB - MySQL

MySQL credentials:

host='sql.freedb.tech'
port=3306
user='freedb_freedb_nir'
passwd='!Ryr3J%tY6MFF3a'
db='freedb_freedb_nir'


The REST API gateway will be: 127.0.0.1:5000/users/<USER_ID>

Example to use POST method:

Example: when posting the below JSON payload to 127.0.0.1:5000/users/1 
A new user will be created in the MySQL DB with the id 1 and the name john.
{“user_name”: “john”}


The Web interface is in: 127.0.0.1:5001/users/get_user_data/<USER_ID>

Example:
@app.route("/get_user_name")
def get_user_name(user_id):
user_name = get_user_name_from_db(user_id)
return "<H1 id='user'>" + user_name + "</H1>"
