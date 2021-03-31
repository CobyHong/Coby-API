import flask

# accept arguments
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return { "resp": "Coby API is online!" }

@app.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        user = request.args.get('id')
        return { "users": 1 }
    else:
        return { "users": 2 }
