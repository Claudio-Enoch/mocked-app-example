# Mocked App Example
Demo application with mocked 3rd party dependencies and tests.  

# Getting Started
- require docker-compose 1.27+
- run application with mocked service `docker-compose up`
  - navigate browser to **localhost:5000/weather/denver
- run application tests `docker-compose run webapp pytest -v`
- run webapp without mocking `docker build -t app webapp && docker run -p 5000:5050 app`
  - navigate browser to **localhost:5000/weather/<location_name>

# Notes
.env file has been purposefully included in the repo for demo purposes
