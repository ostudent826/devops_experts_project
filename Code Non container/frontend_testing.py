from os.path import exists
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


from selenium.webdriver.common.by import By

try:
    driver.get("http://localhost:5001/get_user_name/3")

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


