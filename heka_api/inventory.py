from flask import Blueprint, request
from .models import db, VaccineContainer, VaccineSchema

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/vaccines', methods=['GET'])
def get_vaccines():
  return "Vaccines"

@bp.route('/vaccines', methods=['POST'])
def post_vaccine():
  data = request.get_json()
  vaccine_schema = VaccineSchema()
  vaccine = vaccine_schema.load(data)
  return vaccine.__repr__()


@bp.route('/vaccines/<id>', methods=['GET'])
def get_vaccine():
  return "Vaccine"