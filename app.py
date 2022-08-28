from flask import Flask
import utils.db_utils as db_utils
import service.creditcard_generator as cc_gen
import random

app = Flask(__name__)


@app.route("/post/card-creation-request/")
def post_cardcreationrequest():
    db = db_utils.get_db()
    if random.random() <= 0.8:
        # Approved Request
        request = {
            "name": "Michael B. Jordan",
            "email": "test",
            "nric url": "https://www.google.com",
            "self portrait": "https://www.google.com",
            "gender": "Male",
            "marital status": "Single",
            "nationality": "Singaporean",
            "address": "1 Ang Mo Kio Ave 3, #22-442 Singapore 123451",
            "mobile number": 98877665,
            "date of birth": "1 June 1990",
            "credit score": 720,
            "status": "Approved"
        }
        db_utils.post_request(db, request)

        # Issue Credit Card
        credit_card = cc_gen.generate_creditcard()
        credit_card["name"] = request["name"]
        credit_card["email"] = request["email"]
        credit_card["card type"] = "Virtual"
        credit_card["credit balance"] = 0
        credit_card["date created"] = "28 August 2022"
        db_utils.post_creditcard_history(db, credit_card)

        return "<p>Request Approved, Card Issued</p>"
    else:
        # Rejected Request
        request = {
            "name": "Louis Hamilton",
            "email": "test",
            "nric url": "https://www.google.com",
            "self portrait": "https://www.google.com",
            "gender": "Male",
            "marital status": "Single",
            "nationality": "Singaporean",
            "address": "1 Ang Mo Kio Ave 3, #22-442 Singapore 123451",
            "mobile number": 98877665,
            "date of birth": "1 June 1990",
            "credit score": 720,
            "status": "Rejected"
        }
        db_utils.post_request(db, request)
        return "<p>Request Rejected, Manual Review Needed</p>"
    

# Get All Rejected/In-Progress Card Creation Requests
@app.route("/get/rejected-requests/")
def get_rejectedrequests():
    db = db_utils.get_db()
    return db_utils.get_rejected_requests(db)

# Get All Historical Card Creation Requests
@app.route("/get/all-requests/")
def get_allrequests():
    db = db_utils.get_db()
    return db_utils.get_all_requests(db)  

@app.route("/get/card-creation-history/")
def get_cardcreationhistory():
    db = db_utils.get_db()
    return db_utils.get_cardcreation_history(db)

@app.route("/cc-gen/")
def generate_creditcard():
    db = db_utils.get_db()
    data = cc_gen.generate_creditcard()
    return data
    
if __name__ == '__main__':
    app.run(host="localhost", port=5000)