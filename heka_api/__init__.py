from flask import Flask
import pprint

def create_app(**test_config):
	app = Flask(__name__)

	app.config.from_object('heka_api.default_config')
	app.config.from_envvar('YOURAPPLICATION_SETTINGS', silent=True)

	if test_config is not None:
		app.config.from_mapping(**test_config)

	from .models import db, ma
	db.init_app(app)
	ma.init_app(app)

	from . import api
	app.register_blueprint(api.bp)

	return app
