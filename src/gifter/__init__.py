import os

from flask import Flask

from gifter.api.gifter_api import gifter_api
from gifter.api.whoami_api import whoami_api
from gifter.models import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.register_blueprint(gifter_api)
    app.register_blueprint(whoami_api)
    db.init_app(app)
    return app
