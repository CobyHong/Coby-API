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
@app.route('/users', methods=['GET', 'PUT', 'POST', 'DELETE'])
def users():
    search_id = request.args.get('id')
    search_name = request.args.get('name')
    search_desc = request.args.get('desc')

    if request.method == "GET":
        if search_id:
            user = mongoDB_collection.find_one({"_id": ObjectId(search_id)})
            if user:
                user["_id"] = str(user["_id"])
                return { "users": user }, 201
            return flask.jsonify({"error": "User not found"}), 404
        else:
            users = list(mongoDB_collection.find())
            if users:
                for user in users:
                    user["_id"] = str(user["_id"])
                return { "users": users }, 201
            return flask.jsonify({"error": "users list empty"}), 404

    if request.method == "PUT":
        target_id = {"_id": ObjectId(search_id)}
        if search_name and search_desc:
            update_id = { "$set": { "name": search_name, "desc": search_desc } }
            resp = mongoDB_collection.update_one(target_id, update_id)
            if resp:
                return flask.jsonify({"success": "user updated"}), 204
        return flask.jsonify({"error": "cannot update user"}), 404
        
    if request.method == "POST":
        new_user = request.get_json()
        resp = mongoDB_collection.insert(new_user)
        if resp:
            return flask.jsonify({"success": "user added"}), 204
        return flask.jsonify({"error": "user insert failed"}), 404

    if request.method == "DELETE":
        if search_id:
            resp = mongoDB_collection.remove({"_id": ObjectId(search_id)})
            if resp['n'] == 1:
                return flask.jsonify({"success": "user removed"}), 204
            return flask.jsonify({"error": "user not found"}), 404
