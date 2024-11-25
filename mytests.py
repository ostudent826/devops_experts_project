import pymysql

# Example DB_CONFIG structure
DB_CONFIG = {
    'host': 'localhost',  # MySQL server host
    'user': 'root',  # Your MySQL username
    'password': '123456',  # Your MySQL password
    'database': 'users'  # Database to connect to
}


def test():
    connection = None
    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        user_id = 14  # Change to the correct user_id you want to update
        new_name = 'sa'  # New name to update


        # Proceed to update the record
        sql_query = "UPDATE `users` SET `name` = %s WHERE `user_id` = %s"
        cursor.execute(sql_query, (new_name, user_id))
        connection.commit()


    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            # Close the connection
            connection.close()


# Call the test function
#test()

if __name__ == "__main__":
    test()
