from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from .models import db, VaccineContainer, VaccineSchema, Order, OrderSchema, Customer, CustomerSchema, Manufacturer, ManufacturerSchema
from uuid import uuid4

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

## INSERT MORE VACCINES (TESTING ONLY!!! DO NOT DEPLOY THIS ROUTE!)
@bp.route('/vaccines/insert', methods=['POST'])
def make_more_vaccines():
  for _ in range(3):
    db.session.add(VaccineContainer(id=uuid4(), manufacturer_id=1, dist_center=1))
    db.session.add(VaccineContainer(id=uuid4(), manufacturer_id=2, dist_center=1))
    db.session.add(VaccineContainer(id=uuid4(), manufacturer_id=3, dist_center=1))
  db.session.commit()
  return jsonify("Vaccines created successfully."), 200

### VACCINES ###
@bp.route('/vaccines', methods=['GET'])
def get_vaccines():
  data = db.session.query(VaccineContainer).all()
  schema = VaccineSchema(many=True)
  return jsonify(schema.dump(data)), 200

@bp.route('/vaccines', methods=['POST'])
def post_vaccine():
  data = request.get_json()
  vaccine_schema = VaccineSchema()
  vaccine = vaccine_schema.load(data)
  try:
    db.session.add(vaccine)
    db.session.commit()
  except IntegrityError:
    db.session.rollback()
    abort(409, description="Duplicate resource already exists.")
  return jsonify("Resource added successfully."), 200

@bp.route('/vaccines/<id>', methods=['GET'])
def get_vaccine(id):
  data = VaccineContainer.query.filter_by(id=id).first()
  if not data:
    abort(404, description="Vaccine with id of {} does not exist.".format(id))
  schema = VaccineSchema()
  return jsonify(schema.dump(data)), 200


### ORDERS ###
@bp.route('/orders', methods=['GET'])
def get_orders():
  data = Order.query.all()
  if not data:
    abort(404, description="Error while getting orders")
  schema = OrderSchema(many=True)
  return jsonify(schema.dump(data)), 200

@bp.route('/orders', methods=['POST'])
def create_order():
  data = request.get_json()
  schema = OrderSchema()
  order = schema.load(data)
  db.session.add(order)
  db.session.commit()
  return jsonify("Order created successfully."), 200

@bp.route('/orders/<id>', methods=['GET'])
def get_order(id):
  data = Order.query.filter_by(id=id).first()
  if not data:
    abort(404, description="Order with id of {} does not exist.".format(id))
  schema = OrderSchema()
  return jsonify(schema.dump(data)), 200

@bp.route('/orders/<id>/vaccines', methods=['GET'])
def get_order_vaccines(id):
  data = VaccineContainer.query.filter_by(order_id=id).all()
  if not data:
    abort(404, "No vaccines have been added to this order.")
  schema = VaccineSchema(many=True)
  return jsonify(schema.dump(data)), 200

@bp.route('/orders/<order_id>/vaccines', methods=['POST'])
def add_vaccines_to_order(order_id):
  vaccine_orders = request.get_json()
  for vaccine_order in vaccine_orders:
    available_vaccines = VaccineContainer.query.filter_by(
        order_id=None,
        manufacturer_id=vaccine_order['manufacturer_id']
      ).limit(vaccine_order['quantity']).all()
    if len(available_vaccines) < vaccine_order['quantity']:
      abort(404, description="Not enough supply.")
    for vaccine in available_vaccines:
      vaccine.order_id = order_id
  db.session.commit()
  return jsonify("Vaccines added to order."), 200


### CUSTOMERS ###
@bp.route('/customers', methods=['GET'])
def get_customers():
  data = Customer.query.all()
  if not data:
    abort(404, "Error while getting customers.")
  schema = CustomerSchema(many=True)
  return jsonify(schema.dump(data)), 200

@bp.route('/customers', methods=['POST'])
def create_customer():
  data = request.get_json()
  schema = CustomerSchema()
  customer = schema.load(data)
  try:
    db.session.add(customer)
    db.session.commit()
  except IntegrityError:
    db.session.rollback()
    abort(409, "Customer already exists.")
  return jsonify("Customer created successfully."), 200

@bp.route('/customers/<id>', methods=['GET'])
def get_customer(id):
  data = Customer.query.filter_by(id=id).first()
  if not data:
    abort(404, "Customer with id of {} does not exist.".format(id))
  schema = CustomerSchema()
  return jsonify(schema.dump(data)), 200


### MANUFACTURERS ###
@bp.route('/manufacturers', methods=['GET'])
def get_manufacturers():
  data = Manufacturer.query.all()
  if not data:
    abort(404, "Error while getting manufacturers.")
  schema = ManufacturerSchema(many=True)
  return jsonify(schema.dump(data)), 200

@bp.route('/manufacturers/<id>', methods=['GET'])
def get_manufacturer(id):
  data = Manufacturer.query.filter_by(id=id).first()
  if not data:
    abort(404, "Manufacturer with id of {} does not exist.".format(id))
  schema = ManufacturerSchema()
  return jsonify(schema.dump(data)), 200


### ERROR HANDLERS ###
@bp.errorhandler(404)
def resource_not_found(description):
  return jsonify(error=str(description)), 404

@bp.errorhandler(400)
def bad_request(description):
  return jsonify(error=str(description)), 400

@bp.errorhandler(409)
def conflict(description):
  return jsonify(error=str(description)), 409