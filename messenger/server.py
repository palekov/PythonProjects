from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/status')
def status():
    return {
        'status': 'OK',
        'name': 'sk-messanger',
        'time': datetime.now()
    }

app.run()