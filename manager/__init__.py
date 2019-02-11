# -*- coding: utf-8 -*-

import os
import click
from flask import Flask, render_template
from manager.settings import config
from manager.extensions import db
from manager.apis import apis
from manager.crawler.crawlers import crawler_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__, static_url_path='')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprint(app)
    register_commands(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


def register_extensions(app: Flask):
    """注册程序所需的扩展"""
    db.init_app(app)


def register_blueprint(app: Flask):
    """注册程序蓝本"""
    app.register_blueprint(apis, url_prefix='/api')
    app.register_blueprint(crawler_bp, url_prefix='/update')


def register_commands(app: Flask):
    """注册程序所需的命令行命令"""
    @app.cli.command()
    def forge():
        """
        用于生成程序所需的虚拟数据，不可在生产环境中使用
        :return: None
        """
        from manager.fakes import root_fake, user_fake, post_fake, group_fake
        click.echo("Drop database")
        db.drop_all()
        click.echo("Create new databases")
        db.create_all()

        click.echo('generate root data')
        root_fake()

        click.echo('generate user and problems data')
        user_fake()

        click.echo('generate group data')
        group_fake()

        click.echo('generate post data')
        post_fake()

        click.echo("Done")
