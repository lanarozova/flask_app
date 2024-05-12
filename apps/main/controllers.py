
from flask.views import MethodView
from flask import render_template, request, redirect, url_for

# from apps.validators.validators import validate_name, validate_email, validate_password_format, check_passwords_matching
from apps.main.exceptions import UserAlreadyRegisteredError, UserNotFoundError
from apps.temp_database.database import register_user, get_user
from apps.main.forms import RegistrationForm, LoginForm


class Registration(MethodView):

    def get(self):
        form = RegistrationForm()
        return render_template("main/registration.html", form=form)

    def post(self):
        form = RegistrationForm(request.form)
        try:
            if form.validate_on_submit():
                user_dict = {"name": form.name.data, "email": form.email.data, "password": form.password.data}
                register_user(user_dict)
                return render_template("main/registration_success.html")
            # else:
            #     return render_template("main/registration.html", form=form)
        except UserAlreadyRegisteredError as error:
            return render_template("main/registration.html", form=form, error=error)


class Login(MethodView):

    def get(self):
        form = LoginForm()
        return render_template("main/login.html", form=form)

    def post(self):
        form = LoginForm(request.form)
        try:
            if form.validate_on_submit():
                user_info = get_user(form.email.data, form.password.data)
                return render_template(
                    "main/user_account.html",
                    name=user_info["name"],
                    email=user_info["email"])
            else:
                render_template("main/login.html", form=form)
        except UserNotFoundError as error:
            return render_template("main/login.html", form=form, error=error)


class Home(MethodView):

    def get(self):
        return render_template("main/index.html")
