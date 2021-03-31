import flask
import pymongo
import os
from bson import ObjectId

# accept arguments.
from flask import request

# flask applicaiton.
app = flask.Flask(__name__)

# Connecting to MongoDB database with specified collection.
# enviroment variable to ensure security.
mongoDB_url = os.environ.get('MONGO_URL')
mongoDB_connector = pymongo.MongoClient(mongoDB_url)
mongoDB_collection = mongoDB_connector["CobyBase"]["users"]

# default ping.
@app.route('/', methods=['GET'])
def ping():
    return { "resp": "Coby API is online!" }

# basic users http requests.
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def users():
    search_id = request.args.get('id')
    if request.method == "GET":
        # return specific user.
        if search_id:
            user = mongoDB_collection.find_one({"_id": ObjectId(search_id)})
            user["_id"] = str(user["_id"])
            return { "users": user }
        # return all users.
        else:
            users = list(mongoDB_collection.find())
            for user in users:
                user["_id"] = str(user["_id"])
            return { "users": users }