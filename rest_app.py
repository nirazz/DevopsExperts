from flask import Flask, request
from werkzeug.exceptions import BadRequest
from db_connector import add_user, update_user, fetch_user_name, delete_user

app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            # Check if the user_id exists in the database
            user_name = fetch_user_name(user_id)
            if user_name is None:
                # If the user_id is not found in the database, return an error message and a 404 status code
                return {'error': 'user not found'}, 404
            else:
                return {'user_id': user_id, 'user_name': user_name}, 200  # status code
        except Exception as e:
            # If any exception is raised, return an error message and a 500 status code
            return {'error': 'server error: {}'.format(e)}, 500

    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            add_user(user_id, user_name)
            return {'user id': user_id, 'user name': user_name, 'status': 'user added'}, 200  # status code
        except BadRequest as e:
            # If the request does not contain a JSON payload, return an error message and a 400 status code
            return {'error': 'invalid request: {}'.format(e)}, 400
        except Exception as e:
            # If any other exception is raised, return an error message and a 500 status code
            return {'error': 'server error: {}'.format(e)}, 500

    elif request.method == 'PUT':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            update_user(user_id, user_name)
            return {'user id': user_id, 'user name': user_name, 'status': 'updated'}, 200
        except BadRequest as e:
            # If the request does not contain a JSON payload, return an error message and a 400 status code
            return {'error': 'invalid request: {}'.format(e)}, 400
        except Exception as e:
            # If any other exception is raised, return an error message and a 500 status code
            return {'error': 'server error: {}'.format(e)}, 500

    elif request.method == 'DELETE':
        # If the user id is not found in the users' dictionary, return an error message and a 404 status code
        if not fetch_user_name(user_id):
            return {'error': 'user not found'}, 404  # status code
        # If the user id is found, remove the user from the dictionary and return a success message and a 200 status code
        else:
            user_name = fetch_user_name(user_id)
            delete_user(user_id)
            return {'user id': user_id, 'user name': user_name, 'status': 'deleted'}, 200


app.run(host='127.0.0.1', debug=True, port=5000)
