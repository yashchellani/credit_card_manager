import pymongo

def get_db():
    client = pymongo.MongoClient("mongodb+srv://root:Password123@cardiff.j1mmrzt.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    return db

def add_test_object(db, id, name, email):
    test_object = {'id': id, 'name': name, 'email': email}
    return db.test.insert_one(test_object)

    