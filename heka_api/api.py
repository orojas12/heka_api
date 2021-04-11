from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from .models import db, VaccineContainer, VaccineSchema, Order, OrderSchema, Customer, CustomerSchema, Manufacturer, ManufacturerSchema
from uuid import uuid4
from .helpers import separate_order_vaccine_data, add_vaccines_to_order

bp = Blueprint('api', __name__, url_prefix='/api')

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
	orders = Order.query.all()

	if not orders:
		abort(404, description="No orders found in database.")
    
	schema = OrderSchema(many=True)
	return jsonify(schema.dump(orders)), 200

@bp.route('/orders', methods=['POST'])
def create_order():
	schema = OrderSchema()
	json = request.get_json()
	
	try:
		[order_data, vaccine_data] = separate_order_vaccine_data(json)
		order = schema.load(order_data)
		order.id = uuid4()
		add_vaccines_to_order(vaccine_data, order)
	except Exception as error:
		db.session.rollback()
		abort(400, description="Order could not be processed: " + error.__str__())
	except ValidationError:
		db.session.rollback()
		abort(400, description="Invalid order data.")

	db.session.add(order)
	db.session.commit()
	return jsonify("Order created successfully."), 200

@bp.route('/orders/<id>', methods=['GET'])
def get_order(id):
	order = Order.query.filter_by(id=id).first()

	if not order:
		abort(404, description="Order with id of {} does not exist.".format(id))

	vaccines = VaccineContainer.query.filter_by(order_id=id).all()

	if not vaccines:
		abort(404, description="No vaccines have been added to this order.")

	order.vaccines = vaccines
	schema = OrderSchema()
	return jsonify(schema.dump(order)), 200


### CUSTOMERS ###
@bp.route('/customers', methods=['GET'])
def get_customers():
	data = Customer.query.all()
	if not data:
		abort(404, description="Error while getting customers.")
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
		abort(409, description="Customer already exists.")
	return jsonify("Customer created successfully."), 200

@bp.route('/customers/<id>', methods=['GET'])
def get_customer(id):
	data = Customer.query.filter_by(id=id).first()
	if not data:
		abort(404, description="Customer with id of {} does not exist.".format(id))
	schema = CustomerSchema()
	return jsonify(schema.dump(data)), 200


### MANUFACTURERS ###
@bp.route('/manufacturers', methods=['GET'])
def get_manufacturers():
	data = Manufacturer.query.all()
	if not data:
		abort(404, description="Error while getting manufacturers.")
	schema = ManufacturerSchema(many=True)
	return jsonify(schema.dump(data)), 200

@bp.route('/manufacturers/<id>', methods=['GET'])
def get_manufacturer(id):
	data = Manufacturer.query.filter_by(id=id).first()
	if not data:
		abort(404, description="Manufacturer with id of {} does not exist.".format(id))
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