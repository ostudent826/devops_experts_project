import json
from random import randint

import requests
import pymysql
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import names


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
            print("Success Used Added:", send_request_get.json())
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

def flush_DB():
    requests.delete("http://localhost:5000/users/flush")
    print("All the DB users flushed")


driver = webdriver.Chrome()



def selenium_fron_test(id):
    try:
        driver.get(f"http://localhost:5001/get_user_name/{id}")

        driver.implicitly_wait(0.5)

        # Assuming the user name is inside a <td> element without needing 'data.user_name'
        user_name_element = driver.find_element(By.XPATH, "//tr/td[2]")

        # Extract the text from the <td> element

        if user_name_element:

            user_name = user_name_element.text
            print(f"User Name: {user_name}")
        else:
            print(" empty")


    except Exception as e:
        print(f"An error occurred: {e}")


    except Exception as e:
        print(f"Error {e}")

    finally:
        sleep(3)
        driver.quit()

if __name__ == '__main__':

    id = randint(1,100)
    add_user_post(names.get_full_name(), id)
    check_user_added(id)
    query_db_user(id)
    selenium_fron_test(id)
    sleep(10)
    flush_DB()



