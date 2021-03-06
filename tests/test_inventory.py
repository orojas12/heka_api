import pytest
from heka_api import create_app
from heka_api.models import db, VaccineContainer
import json

@pytest.fixture(scope="module")
def client():
    app = create_app(TESTING=True)
    with app.test_client() as client:
        yield client
        VaccineContainer.query.filter_by(id="06aec48a-952b-4f2f-b375-00df5d923870").delete()
        db.session.commit()

def test_vaccines_post(client):
    response = client.post('/inventory/vaccines', json={
            "id": "06aec48a-952b-4f2f-b375-00df5d923870",
            "order_id": 4,
            "manufacturer_id": 1,
            "dist_center": 2
        }
    )
    assert response.status_code == 200

def test_duplicate_vaccines_post(client):
    response = client.post('/inventory/vaccines', json={
            "id": "06aec48a-952b-4f2f-b375-00df5d923870",
            "order_id": 4,
            "manufacturer_id": 1,
            "dist_center": 2
        }
    )
    assert response.status_code == 409

def test_not_found(client):
    vaccines_response = client.get('/inventory/vaccines/-1')
    assert vaccines_response.status_code == 404
    orders_response = client.get('/inventory/orders/-1')
    assert orders_response.status_code == 404
    order_vaccines_response = client.get('/inventory/orders/-1/vaccines')
    assert order_vaccines_response.status_code == 404
    customers_response = client.get('/inventory/customers/-1')
    assert customers_response.status_code == 404
    manufacturers_response = client.get('/inventory/manufacturers/-1')
    assert manufacturers_response.status_code == 404

def test_orders_get(client):
    order_response = client.get('/inventory/orders/1')
    assert order_response.status_code == 200
    orders_response = client.get('/inventory/orders')
    assert orders_response.status_code == 200
    order_vaccines_response = client.get('/inventory/orders/1/vaccines')
    assert order_vaccines_response.status_code == 200


# def test_orders_post(client):
#     response = client.post('/inventory/orders', json={
            
#         }
#     )

def test_customers_get(client):
    response = client.get('/inventory/customers/1')
    assert response.status_code == 200
    response = client.get('/inventory/customers')
    assert response.status_code == 200