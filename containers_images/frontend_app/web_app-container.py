from flask import Flask ,render_template
import os
import signal

app = Flask(__name__)


@app.route('/get_user_name/<int:id>', methods=['GET'])
def get_user_name(id):

    return render_template("htmltest.html",id=id)


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'







if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
