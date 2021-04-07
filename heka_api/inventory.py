from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from .models import db, VaccineContainer, VaccineSchema, Order, OrderSchema

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

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
    abort(409)
  return jsonify("Resource added successfully."), 200


@bp.route('/vaccines/<id>', methods=['GET'])
def get_vaccine(id):
  data = VaccineContainer.query.filter_by(id=id).first()
  if data is None:
    abort(404)
  schema = VaccineSchema()
  return jsonify(schema.dump(data)), 200


@bp.route('/orders/<id>', methods=['GET'])
def get_order(id):
  data = Order.query.filter_by(id=id).first()
  if data is None:
    abort(404)
  schema = OrderSchema()
  return jsonify(schema.dump(data)), 200

@bp.route('/orders', methods=['GET'])
def get_orders():
  data = Order.query.all()
  if data is None:
    abort(404)
  schema = OrderSchema(many=True)
  return jsonify(schema.dump(data)), 200


@bp.errorhandler(404)
def resource_not_found(error):
  return jsonify({"error": 404, "message": "Resource not found."}), 404


@bp.errorhandler(400)
def resource_not_found(error):
  return jsonify({"error": 400, "message": "Invalid request parameters or body."}), 400


@bp.errorhandler(409)
def resource_not_found(error):
  return jsonify({"error": 409, "message": "Existing duplicate"}), 409