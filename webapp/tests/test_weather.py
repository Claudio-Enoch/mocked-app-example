def test_weather_denver(app_client):
    response = app_client.get("/weather/denver").json
    assert response["ip"] == "1.1.1.1"
    assert response["weather"] == "Partly cloudy"
    assert response["location"] == "Denver, United States of America"
    assert response["success"] is True


def test_weather_fake_location(app_client):
    response = app_client.get("/weather/fakeplace").json
    assert response["ip"] == "1.1.1.1"
    assert response["weather"] is None
    assert response["location"] == "fakeplace"
    assert response["success"] is False
