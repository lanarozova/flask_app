from flask import Flask, current_app
from flask_bootstrap import Bootstrap

from apps.settings import config
from apps.main import main
from apps.db import db, migrate
from apps.main.model import Role, UserModel


def create_app(config_name: str = "default") -> Flask:
    if config_name not in config:
        raise RuntimeError(f"Invalid configuration name: {config_name}")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print(app.config["SECRET_KEY"])

    app.register_blueprint(main)

    Bootstrap(app)

    # sqlalchemy
    db.init_app(app)
    migrate.init_app(app, db)
    app.db = db

    # add variables to context
    # @app.shell_context_processors
    # def make_shell_context():
    #     return {"db": db, "UserModel": UserModel, "Role": Role, "migrate": migrate}

    return app
