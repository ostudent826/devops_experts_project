from flask import Flask ,render_template
import os
import signal

app = Flask(__name__)


@app.route('/get_user_name/<int:id>', methods=['GET'])
def get_user_name(id):

    return render_template("htmltest.html",id=id)


@app.route('/stop_server')
def stop_server():
    print("rest_app - Stopped")
    os._exit(0)
    return 'Server stopped'





if __name__ == '__main__':
    app.run(port=5001,debug=True)