import flask
import pymongo
import os

# accept arguments.
from flask import request

# flask applicaiton.
app = flask.Flask(__name__)

# Connecting to MongoDB database with specified collection.
# enviroment variable to ensure security.
mongoDB_url = os.environ.get('MONGO_URL')
mongoDB_connector = pymongo.MongoClient(mongoDB_url)
mongoDB_collection = mongoDB_connector["CobyBase"]["users"]

@app.route('/', methods=['GET'])
def ping():
    return { "resp": "Coby API is online!" }

@app.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        user = request.args.get('id')
        return { "users": 1 }
    else:
        users= list(mongoDB_collection.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return {"users": users}
