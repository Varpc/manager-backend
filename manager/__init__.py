# -*- coding: utf-8 -*-

import os
import click
from flask import Flask
from manager.settings import config
from manager.extensions import db
from manager.apis import apis
from manager.crawler.crawlers import crawler_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprint(app)
    register_commands(app)

    @app.route('/')
    def index():
        return 'true'

    return app


def register_extensions(app: Flask):
    db.init_app(app)


def register_blueprint(app: Flask):
    app.register_blueprint(apis, url_prefix='/api')
    app.register_blueprint(crawler_bp, url_prefix='/update')


def register_commands(app: Flask):
    @app.cli.command()
    def forge():
        from manager.fakes import root_fake, user_fake, post_fake
        click.echo("Drop database")
        db.drop_all()
        click.echo("Create new databases")
        db.create_all()

        click.echo('generate root data')
        root_fake()

        click.echo('generate user and problems data')
        user_fake()

        click.echo('generate post data')
        post_fake()

        click.echo("Done")
