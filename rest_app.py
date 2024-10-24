# BackEND
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os
import signal
# DB config


"""
Tasks: improve code

1.Add it eacg method valid check:

if post body is exist V
if put body is exist V
if get body is empty
if delete what it need 

if get and user doesnt exist return error V

if post and user is already exist return error V

if put and user doenst exist error V

if delete and use doesnt exist error
"""

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'users'
}

app = Flask(__name__)
CORS(app)

# define URL Path

@app.route('/users/<int:id>', methods=['POST'])
def create_user(id):
    connection = None

    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if request.content_length == 0:
            return jsonify({
                "error": "body request is empty"
            }), 400

        request_data = request.get_json()

        if 'user_name' not in request_data:
            return jsonify({
                "error": "Missing user_name"
            }), 400

        user_name = request_data['user_name']

        data = (id, user_name, datetime.now())

        query = """INSERT INTO users (user_id, name, creation_date)
                   VALUES (%s, %s, %s);"""

        cursor.execute(query, data)

        connection.commit()

        result = cursor.fetchall()

        return jsonify({
            "status": "ok",
            "user_added": user_name
        }), 201



    except pymysql.IntegrityError as e:

        return jsonify({
            "status": "error",
            "reason": "id is already exist",
            "id": id
        }), 400

    except Exception as e:
        # General exception handler
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()


@app.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    connection = None

    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if request.content_length is not None:
            return jsonify({
                "error": "GET request cannot have body"
            }), 400

        if id == 0:
            # Execute DB command get all users from table users
            cursor.execute("SELECT * FROM users;")
            result = cursor.fetchall()

            return jsonify(result)

        query = (f"SELECT * FROM users WHERE user_id = %s")

        cursor.execute(query, id)
        query_response = cursor.fetchone()

        if cursor.rowcount == 0:

            return jsonify({
                "status": "error",
                "reason": "no such id",
                "the Id searched": id
            }), 500

        else:

            result = {
                "status": "ok",
                "user_name": query_response[1]
            }
            return jsonify(result), 200

    except Exception as e:

        # General exception handler

        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    finally:
        if connection:
            cursor.close()
            connection.close()


@app.route('/users/<int:id>', methods=['PUT'])
def modify_user(id):
    connection = None

    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if request.content_length == 0:
            return jsonify({
                "error": "body request is empty"
            }), 400

        request_data = request.get_json()
        user_name = request_data['user_name']

        query_is_user_exist = (f"SELECT * FROM users WHERE user_id = %s")

        cursor.execute(query_is_user_exist, id)

        if cursor.rowcount == 0:

            return jsonify({
                "status": "error",
                "reason": "no such id",
                "the Id searched": id
            }), 500

        else:
            query = "UPDATE `users` SET `name` = %s WHERE `user_id` = %s"

            cursor.execute(query, (user_name, id))

            connection.commit()

            return jsonify({
                "status": "ok",
                "user_name": user_name
            }), 200

    except Exception as e:
        print(f"Insert user error {e}")


    finally:
        if connection:
            cursor.close()
            connection.close()


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = None

    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if request.content_length is not None:
            return jsonify({
                "error": "DELETE request cannot have body"
            }), 400

        query = "DELETE FROM users WHERE user_id = %s;"

        # Add to look if user_id is exist before

        query_is_user_exist = (f"SELECT * FROM users WHERE user_id = %s")

        cursor.execute(query_is_user_exist, id)
        if cursor.rowcount == 0:

            return jsonify({
                "status": "error",
                "reason": "no such id",
                "the Id searched": id
            }), 500

        else:
            cursor.execute(query, (id))
            connection.commit()

        return jsonify({
            "message": f"User_ID {id} Deleted."
        }), 200

    except Exception as e:
        print(f"Insert user error {e}")


    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

if __name__ == '__main__':
    app.run(debug=True)
