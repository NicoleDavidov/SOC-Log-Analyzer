from flask import Flask, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

@app.route("/alerts")
def get_alerts():
    path = os.path.join(OUTPUT_DIR, "alerts.json")
    with open(path) as f:
        return jsonify(json.load(f))

@app.route("/risk-scores")
def get_risk_scores():
    path = os.path.join(OUTPUT_DIR, "risk_scores.json")
    with open(path) as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)