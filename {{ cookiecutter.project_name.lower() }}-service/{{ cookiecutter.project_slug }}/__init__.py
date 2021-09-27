from flask import Flask

from . import blueprints, commands, config, middleware


def setup_metrics(app):
    pass


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    commands.init_app(app)
    middleware.init_app(app)
    blueprints.init_app(app)

    setup_metrics(app)

    return app
