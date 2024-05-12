from flask import Blueprint


main = Blueprint("/", __name__)


from apps.main import routes

