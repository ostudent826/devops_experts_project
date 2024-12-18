import json
from random import randint
import requests
import pymysql
import names
import tempfile
import os


headers = {"Content-Type": "application/json"}

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'users'
}

#Add user to DB
def add_user_post(username,id):
    json_data = {"user_name": username}
    url = f"http://localhost:5000/users/{id}"
    try:

        send_request_post = requests.post(url,json=json_data,headers=headers)


        if send_request_post.status_code == 200:
            print("Success:", send_request_post.json())
        else:
            print(f"Failed with status code: {send_request_post.status_code}")
            print("Response:", send_request_post.text)

    except Exception as e:
        print(f"Error: {e}")

#Check if user added
def check_user_added(id):
    url = f"http://localhost:5000/users/{id}"
    try:

        send_request_get = requests.get(url,headers=headers)

        if send_request_get.status_code == 200:
            print("Success used added:", send_request_get.json())
        else:
            print(f"Failed with status code: {send_request_get.status_code}")
            print("Response:", send_request_get.text)

    except Exception as e:
        print(f"Error: {e}")

#Check if user exist in db
def query_db_user(id):

    connection = None

    try:


        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()


        query = (f"SELECT * FROM users WHERE user_id = %s")

        cursor.execute(query, id)
        query_response = cursor.fetchone()

        if cursor.rowcount == 0:
            response = {
                "status": "error",
                "reason": "no such id",
                "the Id searched": id
            }
            return json.dumps(response)

        else:

            result = {

                "status": "ok",

                "user_name": query_response

            }
            return print("Query from data base get user name: "+json.dumps(result["user_name"][1]))

    except Exception as e:
        print(f"Error : {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()



if __name__ == '__main__':

    id = randint(1, 5)
    print(f"Generated ID: {id}")

    # Create a temporary file in the current directory
    temp_file_path = os.path.join(os.getcwd(), "temp_id.txt")

    # Write the ID to the temporary file
    with open(temp_file_path, "w") as temp_file:
        temp_file.write(str(id))

    # Perform operations
    add_user_post(names.get_full_name(), id)
    check_user_added(id)
    query_db_user(id)

