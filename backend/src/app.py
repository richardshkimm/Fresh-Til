from datetime import datetime
import json

import db
from flask import Flask, request

DB = db.DatabaseDriver()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"


# your routes here


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
