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

