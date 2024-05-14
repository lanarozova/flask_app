
from flask.views import MethodView
from flask import render_template, request, redirect, url_for

from apps.main.forms import RegistrationForm, LoginForm
from apps.main.repositories import UserRepository, RoleRepository
from apps.main.data_objects.dto.user import NewUserDTO

from apps.main.exceptions import UserAlreadyRegisteredError, UserNotFoundError
from apps.validators.exceptions import PasswordInvalidFormatError, NameValidationError

user_repository = UserRepository()
role_repository = RoleRepository()


class Registration(MethodView):

    def get(self):
        form = RegistrationForm()
        return render_template("main/registration.html", form=form)

    def post(self):
        form = RegistrationForm(request.form)
        try:
            if form.validate_on_submit():
                role_dto = role_repository.get_user_role()
                user_dto = NewUserDTO(
                    name=form.name.data,
                    email=form.email.data,
                    password=form.password.data,
                    is_active=False,
                    role_id=role_dto.id
                )
                print(user_dto)
                user_repository.add_user(user_dto)

                return render_template("main/registration_success.html")
        except UserAlreadyRegisteredError as e:
            form.email.errors.append(e)
        except PasswordInvalidFormatError as e:
            form.password.errors.append(e)
        except NameValidationError as e:
            form.name.errors.append(e)

        return render_template("main/registration.html", form=form)


class Login(MethodView):

    def get(self):
        form = LoginForm()
        return render_template("main/login.html", form=form)

    def post(self):
        form = LoginForm(request.form)
        try:
            if form.validate_on_submit():
                if user_repository.check_user_password(form.email.data, form.password.data):
                    user = user_repository.get_user_by_email(form.email.data)
                    return render_template(
                    "main/user_account.html",
                        name=user.name,
                        email=user.email)
            else:
                return render_template("main/login.html", form=form)
        except UserNotFoundError as error:
            return render_template("main/login.html", form=form, error=error)


class Home(MethodView):

    def get(self):
        return render_template("main/index.html")
