from apps.accounts import accounts
from apps.accounts.controllers import Registration, Login, Home


registration_view = Registration.as_view("registration")
accounts.add_url_rule("/accounts/registration", view_func=registration_view, methods=["GET", "POST"])

login_view = Login.as_view("login")
accounts.add_url_rule("/accounts/login", view_func=login_view, methods=["GET", "POST"])

home_view = Home.as_view("home")
accounts.add_url_rule("/accounts/home", view_func=home_view, methods=["GET"])
accounts.add_url_rule("/accounts/", view_func=home_view, methods=["GET"])


