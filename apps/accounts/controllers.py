
from flask.views import MethodView
from flask import render_template, request, redirect, url_for

from apps.validators.validators import validate_name, validate_email, validate_password_format, check_passwords_matching
from apps.accounts.exceptions import UserAlreadyRegisteredError, UserNotFoundError
from apps.temp_database.database import register_user, get_user


class Registration(MethodView):

    def get(self):
        return render_template("accounts/registration.html")

    def post(self):
        try:
            name = validate_name(request.form.get("name"))
            email = validate_email(request.form.get("email"))
            password = request.form.get("password")
            repeat_password = request.form.get("repeat_password")
            password = validate_password_format(check_passwords_matching(password, repeat_password))
            user_dict = {"name": name, "email": email, "password": password}
            register_user(user_dict)
        except UserAlreadyRegisteredError as error:
            return render_template(
                "accounts/registration.html",
                error=error,
                name=request.form.get("name"),
                email=request.form.get("email"))

        return render_template("accounts/registration_success.html")


class Login(MethodView):

    def get(self):
        return render_template("accounts/login.html")

    def post(self):
        try:
            email = validate_email(request.form.get("email"))
            password = validate_password_format(request.form.get("password"))
            user_info = get_user(email, password)
            return render_template(
                "accounts/user_account.html",
                name=user_info["name"],
                email=user_info["email"])
        except UserNotFoundError as error:
            return render_template("accounts/login.html", error=error)


class Home(MethodView):

    def get(self):
        return render_template("accounts/index.html")
