from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/fruits", methods=["GET"])
def fruits():
    list = ["apple", "banana", "cherry", "zebra-cakes"]
    return jsonify(list)

if __name__ == "__main__":
    app.run()
