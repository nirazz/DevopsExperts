import pymysql


def add_user(user_id, username):
    schema_name = 'freedb_freedb_nir'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_nir', passwd='!Ryr3J%tY6MFF3a', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (user_name, user_id) VALUES ('{username}', {user_id})")

    cursor.close()
    conn.close()

# Test:
# add_user(30, "Nir")

def update_user(user_id, username):
    schema_name = 'freedb_freedb_nir'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_nir', passwd='!Ryr3J%tY6MFF3a', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Updating the username and id in the users table
    cursor.execute(f"UPDATE {schema_name}.users SET user_name='{username}', user_id={user_id} WHERE user_id={user_id}")

    cursor.close()
    conn.close()

# Test:
# update_user(30, "Niv")
def delete_user(user_id):
    schema_name = 'freedb_freedb_nir'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_nir', passwd='!Ryr3J%tY6MFF3a', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Deleting the user data
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id={user_id}")

    cursor.close()
    conn.close()

# Test:
# delete_user(2, 'Jack')

def fetch_user_name(user_id):
    schema_name = 'freedb_freedb_nir'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_freedb_nir', passwd='!Ryr3J%tY6MFF3a', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Fetching the username
    cursor.execute(f"SELECT user_name FROM {schema_name}.users WHERE user_id={user_id}")

    # Fetch the username
    user_name = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return user_name

#Test:
# nm = fetch_user_name(1)
# print(nm)