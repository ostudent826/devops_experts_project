"""Download mySQL to win10"""

import os
import platform
import subprocess
from time import sleep

import requests
import sys


# def download_mysql_installer():
#     url = "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.30.0.msi"  # Adjust the version as needed
#     response = requests.get(url)
#     print(response.content)
#     download_path =r"C:\Users\shaam\Downloads\mysql\mysql-installer.msi"
#
#     try:
#         with open(download_path, "wb") as f:
#             f.write(response.content)
#     except Exception as e:
#         print(f"Installation Failed {e}")
#
#     print("Downloaded MySQL installer.")

#irrelevant
# def install_mysql_windows():
#     installer_path = r"C:\Users\shaam\Downloads\mysql\mysql-installer.msi"
#
#     try:
#         # Install the MySQL server
#         subprocess.call(['msiexec', '/i', installer_path])
#         print("MySQL server installed.")
#     except Exception as e:
#         print(f"Installation failed: {e}")


def start_mysql_windows():
    try:
        # Start the MySQL service
        subprocess.call(['net', 'start', 'MySQL80'])
        print("MySQL service started.")
    except Exception as e:
        print(f"Failed to start MySQL service: {e}")


def close_app():
    print("Closing the application.")
    sys.exit()


if __name__ == "__main__":
    if platform.system() == "Windows":
       # download_mysql_installer()
      #  install_mysql_windows()
         start_mysql_windows()
         sleep(15)
         close_app()  # Call to close the application
    else:
        print("This script only supports Windows.")