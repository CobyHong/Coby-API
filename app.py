import flask
import pymongo
import os

# accept arguments.
from flask import request

# flask applicaiton.
app = flask.Flask(__name__)

# Connecting to MongoDB database with specified collection.
# enviroment variable to ensure security.
# mongoDB_url = os.environ.get('MONGO_URL')
# mongoDB_connector = pymongo.MongoClient(str(mongoDB_url))
# mongoDB_collection = mongoDB_connector["CobyBase"]["users"]

@app.route('/', methods=['GET'])
def ping():
    return { "resp": "Coby API is online!" }

@app.route('/users', methods=['GET'])
def users():
    return { "users": "This is a test"}