from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

app = Flask(__name__)

@app.route("/sections")
def hello():
    return 'Hello, World!'

app.run(host="0.0.0.0",port=5001)
