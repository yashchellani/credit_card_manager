from flask import Flask
import tests.db_test as db_test

app = Flask(__name__)

@app.route("/test-push")
def test_push():
    db = db_test.get_db()
    db_test.add_test_object(db, "1", "test", "test@gmail.com")
    return "<p>Added Test Object!</p>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(host="localhost", port=5000)