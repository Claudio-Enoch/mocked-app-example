import requests

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ip")
def index():
    response = requests.get("http://ip.jsontest.com")
    return jsonify(response.json())
