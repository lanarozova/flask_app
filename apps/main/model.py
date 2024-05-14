import bcrypt
from sqlalchemy import Enum
from sqlalchemy.orm import validates


from apps.db import db
from apps.validators.form_field_validator import validate_email, validate_password_format, validate_name
from apps.enums import RolesNamesEnum


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(255), unique=True)
    is_active = db.Column(db.Boolean, default=False)
    _hashed_password = db.Column("hashed_password", db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="RESTRICT"))

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email}>"

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password: str):
        print("setting pw")
        validate_password_format(password)
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self._hashed_password = hashed_password.decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self._hashed_password.encode("utf-8"))

    @validates("name")
    def validate_name(self, key, name):
        return validate_name(name)

    @validates("email")
    def validate_email(self, key, email):
        return validate_email(email)


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(Enum(RolesNamesEnum), unique=True)
    users = db.relationship("UserModel", backref="role", lazy="dynamic")

    @validates("name")
    def validate_name(self, key, value):
        if value not in RolesNamesEnum.list():
            raise ValueError(f"Invalid role name: {value}. Allowed values are: {RolesNamesEnum.list()}")
        return value

    def __repr__(self):
        return f"<Role(name={self.name}>"
