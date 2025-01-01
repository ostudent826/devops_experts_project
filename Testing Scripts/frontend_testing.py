from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

# Define the path to the temporary file
temp_file_path = os.path.join(os.getcwd(), "temp_id.txt")
driver = webdriver.Chrome()

try:
    # Read the ID from the temporary file
    with open(temp_file_path, "r") as temp_file:
        id = temp_file.read().strip()
    print(f"Retrieved ID: {id}")

    # Delete the temporary file after reading
    os.remove(temp_file_path)
    print(f"Temporary file {temp_file_path} deleted.")

    # Perform Selenium operations
    driver.get(f"http://localhost:5001/get_user_name/{id}")
    driver.implicitly_wait(0.5)

    # Locate the user name element in the table
    user_name_element = driver.find_element(By.XPATH, "//tr/td[2]")

    # Extract and print the user name
    if user_name_element:
        user_name = user_name_element.text
        print(f"User Name: {user_name}")
    else:
        print("User name element is empty.")

except FileNotFoundError:
    print(f"Temporary file {temp_file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    sleep(10)
    driver.quit()
