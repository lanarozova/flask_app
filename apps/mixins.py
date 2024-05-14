from flask import current_app
from flask_sqlalchemy import SQLAlchemy


class DBMixin:
    @staticmethod
    def _get_db() -> SQLAlchemy:
        return current_app.db
