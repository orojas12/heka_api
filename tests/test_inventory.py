import pytest
from heka_api import create_app
import json

@pytest.fixture
def client():
    app = create_app(TESTING=True)
    with app.test_client() as client:
        yield client

def test_vaccines_post(client):
    response = client.post('/inventory/vaccines', json={
            "id": "06aec48a-952b-4f2f-b375-00df5d923870",
            "order_id": 4,
            "manufacturer_id": 1,
            "dist_center": 2
        }
    )

    assert response.data == ("<VaccineContainer id=06aec48a-952b-4f2f-b375-00df5d923870, order_id=4, " +
        "manufacturer_id=1, dist_center=2>").encode('utf8')