from flask import Flask

def create_app():
  app = Flask(__name__)

  app.config.from_object('heka-api.default_config.py')
  app.config.from_envvar('APP_CONFIG_FILE')

  from . import routes
  app.register_blueprint(routes.bp)