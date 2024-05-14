from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    name = StringField(
        label="Your name",
        validators=[DataRequired(), Length(2, 50)])

    email = EmailField(
        label="Your email",
        validators=[
            DataRequired(),
            Email()
        ])

    password = PasswordField(
        label="Your password",
        validators=[
            DataRequired()
        ]
    )
    repeat_password = PasswordField(
        label="Repeat your password",
        validators=[
            DataRequired(),
            EqualTo("password", "Passwords must match")
        ]
    )


class LoginForm(FlaskForm):
    email = EmailField(
        label="Your email",
        validators=[
            DataRequired(),
            Email()
        ])
    password = PasswordField(
        label="Your password",
        validators=[
            DataRequired()
        ])
