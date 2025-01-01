from flask import Flask ,render_template
import os
import signal

app = Flask(__name__)

@app.route('/get_user_name/<int:id>', methods=['GET'])
def get_user_name(id):
    # Render the frontend page with the provided user ID
    # The page (frontend.html) will send backend requests to fetch and display user data
    return render_template("frontend.html", id=id)

@app.route('/stop_server')
def stop_server():
    print("rest_app - Stopped")
    os._exit(0)
    return 'Server stopped'





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
