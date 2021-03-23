from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
  return "Hello World!"