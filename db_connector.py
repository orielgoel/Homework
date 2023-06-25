import pymysql
import json

HOST = '194.233.173.71'
PORT = 3306
USER = 'sql7615502'
PASSWORD = 'asdasd321321fgdfg3333'
DB = 'Project'
#  This function will check if a user id exist on the DB and returns the name if it exists
def get_user(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute(f"SELECT name from {DB}.users WHERE id = {user_id};")
        # Fetch all rows from the result set
        rows = cursor.fetchall()
        # Convert the rows to a list of dictionaries
        results = []
        for row in rows:
            result = {}
            for i, col in enumerate(cursor.description):
                result[col[0]] = row[i]
            results.append(result)
        # get only the name key
        name = result['name']
        return name

    except Exception as e:
        return 'failure'
    finally:
        cursor.close()
        conn.close()

# Debug
# print(get_user(111))


#  This function will add a user and will error if it exists
def add_user(user_id,user_name):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute(f"INSERT into {DB}.users (name, id) VALUES ('{user_name}', '{user_id}')")
        # Commit the change in the DB
        conn.autocommit(True)
        cursor.close()
        conn.close()
        return user_name

    except Exception as e:
        return 'failure'
# This function will update a username if the ID exists
def put_user(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute(f"UPDATE users SET name = '{user_name}' WHERE id = {user_id};")

        # Check if any rows were updated
        if cursor.rowcount == 0:
            # No rows were updated, handle the error
            return 'failure'
        else:
            # Rows were updated, commit the transaction
            conn.commit()
            return user_name
    finally:
        cursor.close()
        conn.close()
#  This function will remove a user if the ID exists
def delete_user(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute(f"DELETE from users WHERE id = {user_id};")

        # Check if any rows were updated
        if cursor.rowcount == 0:
            # No rows were updated, handle the error
            return 'failure'
        else:
            # Rows were updated, commit the transaction
            conn.commit()
            return user_id
    finally:
        cursor.close()
        conn.close()