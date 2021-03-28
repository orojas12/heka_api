import pytest
from heka-api import heka-api

@pytest.fixture
def client():
    app = create_app()
    app.test_client()
