from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

app = Flask(__name__)

from trainedModels import endpoints

@app.route("/c1/score")
def hello():
    testData = request.args.get('test').split(",")
    predections = endpoints.pageBugClassfier.predict([testData])
    print(predections[0].answer)
    return jsonify(predections[0].answer)

app.run(host="0.0.0.0")
