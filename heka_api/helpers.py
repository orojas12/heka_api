# UTILITY FUNCTIONS
from .models import db, VaccineContainer

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
    for vaccine in vaccine_data:
        available = VaccineContainer.query \
        .filter_by(order_id=None, manufacturer_id=vaccine['manufacturer_id']) \
        .limit(vaccine['quantity']).all()

    if len(available) < vaccine['quantity']:
        raise Exception("Not enough vaccine supply.")

    for vaccine in available:
        vaccine.order_id = order.id