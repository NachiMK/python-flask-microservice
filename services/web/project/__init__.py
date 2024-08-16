import os
from flask import Flask, jsonify, request, send_file, render_template, session, send_from_directory
from flask_session import Session
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
app.config['SESSION_PERMANENT'] = False

# Initialize the session
Session(app)
socketio = SocketIO(app)


@app.route("/")
def hello():
    return "Hello World from Python Flask Gunicorn Nginx Docker Compose!"


@app.route('/health')
def healthCheck():
    return jsonify({"status": "ok"})


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


if __name__ == '__main__':
    print("Starting Flask application...")
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    socketio.run(app, debug=True)
