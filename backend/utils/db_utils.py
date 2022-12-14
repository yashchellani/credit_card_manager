from bson.json_util import dumps
import pymongo
import os
from dotenv import load_dotenv

def get_db():
    load_dotenv()
    client = pymongo.MongoClient(os.getenv("MONGO_CONNECTION"))
    db = client["management-system"]
    return db

def post_request(db, request):
    db["card-creation-requests"].insert_one(request)
    return "Post Request Success", 200

def get_rejected_requests(db):
    rejected_requests = db["card-creation-requests"].find({"$or":[{"status": "Failed"}, {"status": "In Progress"}]})
    return dumps(list(rejected_requests))

def get_all_requests(db):
    all_requests = db["card-creation-requests"].find()
    return dumps(list(all_requests))

def get_cardcreation_history(db):
    cardcreation_history = db["card-creation-history"].find()
    return dumps(list(cardcreation_history))

def post_creditcard_history(db, credit_card):
    db["card-creation-history"].insert_one(credit_card)
    return "Post Credit Card Success", 200
