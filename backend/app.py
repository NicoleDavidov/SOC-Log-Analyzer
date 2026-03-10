from flask import Flask, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/alerts")
def get_alerts():
    path = os.path.join(BASE_DIR, "output", "alerts.json") 
    with open(path) as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/risk-scores")
def get_risk_scores():
    path = os.path.join(BASE_DIR, "output", "risk_scores.json")
    with open(path) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)