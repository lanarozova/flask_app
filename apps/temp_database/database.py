from os import path
from apps.accounts.exceptions import UserAlreadyRegisteredError, UserNotFoundError


users_db = path.join("apps", "temp_database", "users.txt")
users_db_fields = ["user_id", "email", "password", "name"]


def generate_id():
    with open(users_db) as f:
        lines = f.readlines()
        if lines:
            return int(lines[-1].split(", ")[0]) + 1
        else:
            return 1


def is_user_registered(user_str):
    with open(users_db) as f:
        content = f.read()
        if user_str in content:
            return True
        else:
            return False


def register_user(user_str):
    if is_user_registered(user_str):
        raise UserAlreadyRegisteredError
    else:
        user_id = str(generate_id())
        with open(users_db, "a") as f:
            f.write(user_id + ", " + user_str + "\n")


def get_user(email, password):
    user_login_details = ", ".join([email, password])
    with open(users_db) as f:
        for line in f.readlines():
            if user_login_details in line:
                return line.split(", ")
        raise UserNotFoundError
