from apps.main import main
from apps.main.controllers import Registration, Login, Home


registration_view = Registration.as_view("registration")
main.add_url_rule("/registration", view_func=registration_view, methods=["GET", "POST"])

login_view = Login.as_view("login")
main.add_url_rule("/login", view_func=login_view, methods=["GET", "POST"])

home_view = Home.as_view("home")
main.add_url_rule("/home", view_func=home_view, methods=["GET"])
main.add_url_rule("/", view_func=home_view, methods=["GET"])


