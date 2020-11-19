class WeatherModel:

    def __init__(self, weather_json: dict, location: str, ip: str):
        self.weather_json = weather_json
        self.location = location
        self.ip = ip

    def get_json(self):
        if self.weather_json.get("success") is False:
            return dict(success=False, weather=None, location=self.location, ip=self.ip)
        weather = self.weather_json["current"]["weather_descriptions"][0]
        location = self.weather_json["request"]["query"]
        return dict(success=True, weather=weather, location=location, ip=self.ip)
