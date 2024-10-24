import pymysql

# Replace these with your MySQL server credentials
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456'
}


def create_database(db_name):
    """Create a new database in MySQL."""
    connection = None
    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Query to check if the database exists
        cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{db_name}'")

        cursor_result = cursor.fetchone()

        if cursor_result:
            print(f"Database '{db_name}' already exists.")

        else:
            # Create a new database
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database '{db_name}' created successfully!")


    except Exception as e:
        print(f"The error '{e}' occurred")

    finally:
        if connection:
            cursor.close()
            connection.close()

def create_table(db_name):

    # Database name
    db_name = "users"

    #Create Table Syntax
    create_table_syntax = """
            CREATE TABLE `users` (
    	    user_id INT AUTO_INCREMENT PRIMARY KEY,
    	    name VARCHAR(50) NOT NULL,
    	    creation_date VARCHAR(50) NOT NULL
            ) 
            AUTO_INCREMENT=1 ;
            """
    connection = None

    try:
        # Connect to MySQL server
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Connect to Users Database
        cursor.execute(f"USE {db_name}")
        cursor.execute(create_table_syntax)

        print("Table created successfully!")

    # Error handler
    except Exception as e:
        print(f"Error at creation table :  {e}")

    # Close connection to database
    finally:
        if connection:
            cursor.close()
            connection.close()



if __name__ == '__main__':

    db_name = "users"
    create_database(db_name)  # Replace with your desired database name
    create_table(db_name)
