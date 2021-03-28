from flask import Blueprint

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/vaccines', methods=['GET'])
def get_vaccines():
  return "Vaccines"

@bp.route('/vaccines', methods=['POST'])
def post_vaccine():
  return "Post vaccine"
  

@bp.route('/vaccines/<id>', methods=['GET'])
def get_vaccine():
  return "Vaccine"