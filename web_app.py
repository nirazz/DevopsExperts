from flask import Flask

from db_connector import fetch_user_name

app = Flask(__name__)


@app.route("/users/get_user_data/<user_id>")
def get_user_name(user_id):
    user_name = fetch_user_name(user_id)
    if user_name is None:
        return "<H1 id='error'>Error: User not found</H1>", 404
    else:
        return f"<H1 id='user'>Hello {user_name}!</H1>", 200


app.run(host='127.0.0.1', debug=True, port=5001)
