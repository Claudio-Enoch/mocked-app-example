import os

import requests

from flask import jsonify, abort

from app import app
from app.model import WeatherModel


@app.route("/weather/<string:location>")
def weather(location):
    # use ip api
    ip_response = requests.get("http://ip.jsontest.com")
    if ip_response.status_code != 200:
        abort(404)
    ip = ip_response.json()["ip"]

    # use weather api
    access_key = os.environ.get("ACCESS_KEY")
    weather_response = requests.get(f"http://api.weatherstack.com/current?query={location}&access_key={access_key}")
    if weather_response.status_code != 200:
        abort(404)

    # model response and return json
    weather_model = WeatherModel(weather_json=weather_response.json(), location=location, ip=ip)
    return jsonify(weather_model.get_json())
