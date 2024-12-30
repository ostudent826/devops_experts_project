# BackEND
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os
import signal

# Database configuration
DB_CONFIG = {
    'host': 'mysql_container',
    'port': 3307,
    'user': 'admin',
    'password': '123456',
    'database': 'users'
}

app = Flask(__name__)
CORS(app)


# Define the API routes

@app.route('/users/<int:id>', methods=['POST'])
def create_user(id):
    connection = None
    # Endpoint to create a new user
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Validate that the request body is not empty
        if request.content_length == 0:
            return jsonify({"error": "Body request is empty"}), 400

        # Extract data from the request
        request_data = request.get_json()

        # Ensure the 'user_name' field exists in the request
        if 'user_name' not in request_data:
            return jsonify({"error": "Missing user_name"}), 400

        # Prepare the data for the query
        user_name = request_data['user_name']
        data = (id, user_name, datetime.now())

        # SQL query to insert a new user
        query = """INSERT INTO users (user_id, name, creation_date)
                   VALUES (%s, %s, %s);"""
        cursor.execute(query, data)

        # Commit the transaction
        connection.commit()

        # Respond with success
        return jsonify({"status": "ok", "user_added": user_name}), 201

    # Handle duplicate primary key (IntegrityError)
    except pymysql.IntegrityError:
        return jsonify({"status": "error", "reason": "id is already exist", "id": id}), 400

    # General error handling
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    # Ensure the database connection is properly closed
    finally:
        if connection:
            cursor.close()
            connection.close()


@app.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    connection = None
    # Endpoint to retrieve users
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Ensure GET requests do not contain a body
        if request.content_length is not None:
            return jsonify({"error": "GET request cannot have body"}), 400

        # Retrieve all users if id = 0
        if id == 0:
            cursor.execute("SELECT * FROM users;")
            result = cursor.fetchall()
            return jsonify(result)

        # Retrieve a specific user by id
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, id)
        query_response = cursor.fetchone()

        # Handle case where no user is found
        if cursor.rowcount == 0:
            return jsonify({"status": "error", "reason": "no such id", "the Id searched": id}), 500

        # Respond with the user's information
        result = {"status": "ok", "user_name": query_response[1]}
        return jsonify(result), 200

    # General error handling
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    # Ensure the database connection is properly closed
    finally:
        if connection:
            cursor.close()
            connection.close()


@app.route('/users/<int:id>', methods=['PUT'])
def modify_user(id):
    connection = None
    # Endpoint to update a user's information
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Validate that the request body is not empty
        if request.content_length == 0:
            return jsonify({"error": "Body request is empty"}), 400

        # Extract data from the request
        request_data = request.get_json()
        user_name = request_data['user_name']

        # Check if the user exists
        query_is_user_exist = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query_is_user_exist, id)

        # Handle case where the user does not exist
        if cursor.rowcount == 0:
            return jsonify({"status": "error", "reason": "no such id", "the Id searched": id}), 500

        # Update the user's name
        query = "UPDATE `users` SET `name` = %s WHERE `user_id` = %s"
        cursor.execute(query, (user_name, id))
        connection.commit()

        # Respond with success
        return jsonify({"status": "ok", "user_name": user_name}), 200

    # General error handling
    except Exception as e:
        print(f"Update user error {e}")

    # Ensure the database connection is properly closed
    finally:
        if connection:
            cursor.close()
            connection.close()


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = None
    # Endpoint to delete a user
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Ensure DELETE requests do not contain a body
        if request.content_length is not None:
            return jsonify({"error": "DELETE request cannot have body"}), 400

        # Check if the user exists
        query_is_user_exist = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query_is_user_exist, id)

        # Handle case where the user does not exist
        if cursor.rowcount == 0:
            return jsonify({"status": "error", "reason": "no such id", "the Id searched": id}), 500

        # Delete the user
        query = "DELETE FROM users WHERE user_id = %s;"
        cursor.execute(query, (id,))
        connection.commit()

        # Respond with success
        return jsonify({"message": f"User_ID {id} Deleted."}), 200

    # General error handling
    except Exception as e:
        print(f"Delete user error {e}")

    # Ensure the database connection is properly closed
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/users/flush', methods=['DELETE'])
def flush_users():
    connection = None
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Delete all rows from the users table
        query = "DELETE FROM users;"
        cursor.execute(query)
        connection.commit()

        # Respond with success
        return jsonify({"message": "All users deleted successfully."}), 200

    # General error handling
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    # Ensure the database connection is properly closed
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/stop_server')
def stop_server():
    print("rest_app - Stopped")
    os._exit(0)
    return 'Server stopped'


if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0',port=5000,debug=True)
