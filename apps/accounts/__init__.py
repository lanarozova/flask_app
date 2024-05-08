from flask import Blueprint


accounts = Blueprint("accounts", __name__)


from apps.accounts import routes

