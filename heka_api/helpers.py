# UTILITY FUNCTIONS
from .models import db, Vaccine

def separate_order_vaccine_data(order_data):
    vaccine_data = []
    for key in order_data:
        if key == 'vaccines':
            vaccine_data = order_data.pop('vaccines')
            break
    
    if not vaccine_data:
        raise Exception("Order is missing vaccines.")
    
    return [order_data, vaccine_data]

def add_vaccines_to_order(vaccine_data, order):
    available = []
    for item in vaccine_data:
        results = Vaccine.query \
        .filter_by(order_id=None, manufacturer_id=item['manufacturer_id']) \
        .limit(item['quantity']).all()

        if len(results) < item['quantity']:
            raise Exception("Not enough vaccine supply.")

        available.extend(results)

    for vaccine in available:
        vaccine.order_id = order.id