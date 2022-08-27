from flask import Flask
import utils.db_utils as db_utils
import service.creditcard_generator as cc_gen

app = Flask(__name__)

@app.route("/post/card-creation-request")
def test_push():
    db = db_utils.get_db()
    request = {
        "name": "test",
        "email": "test",
        "mobile number": 98877665,
        "status": "In Progress"
    }
    db_utils.post_request(db, request)
    return "<p>Added Test Object!</p>"

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

@app.route("/cc-gen")
def generate_creditcard():
    db = db_utils.get_db()
    data = cc_gen.generate_creditcard()
    return data
    
if __name__ == '__main__':
    app.run(host="localhost", port=5000)