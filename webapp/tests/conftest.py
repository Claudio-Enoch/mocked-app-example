import pytest

from flask.testing import FlaskClient

from app import app


@pytest.fixture(scope="function", autouse=True)
def app_client() -> FlaskClient:
    with app.test_client() as client:
        yield client
