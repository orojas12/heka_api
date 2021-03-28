import pytest
from heka_api import heka_api

@pytest.fixture
def client():
    app = heka_api.create_app(TESTING=True)
    with app.test_client() as client:
        yield client
