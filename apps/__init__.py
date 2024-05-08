from flask import Flask, current_app
from flask_bootstrap import Bootstrap

from apps.settings import config
from apps.accounts import accounts


def create_app(config_name: str = "default") -> Flask:
    if config_name not in config:
        raise RuntimeError(f"Invalid configuration name: {config_name}")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(accounts)

    Bootstrap(app)

    return app
