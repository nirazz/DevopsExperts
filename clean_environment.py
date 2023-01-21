import requests

rest_session = requests.Session()
try:
    rest_session.get('http://127.0.0.1:5000/stop_server')
    rest_session.close()
except requests.exceptions.RequestException as e:
    print("Error stopping rest_server on port 5000:", e)

web_session = requests.Session()
try:
    web_session.get('http://127.0.0.1:5001/stop_server')
    web_session.close()
except requests.exceptions.RequestException as e:
    print("Error stopping web_server on port 5001:", e)