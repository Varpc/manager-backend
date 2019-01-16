# -*- coding: utf-8 -*-

import os
from flask import Flask
from manager.settings import config
from manager.extensions import db
from manager.apis import apis


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprint(app)

    @app.route('/')
    def index():
        return '<h1>Hello</h1>'

    return app


def register_extensions(app: Flask):
    db.init_app(app)


def register_blueprint(app: Flask):
    app.register_blueprint(apis, url_prefix='/api')
