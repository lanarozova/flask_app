from os import path
from apps.accounts.exceptions import UserAlreadyRegisteredError, UserNotFoundError
import re
import json

# users_db = "users.json"
users_db = path.join("apps", "temp_database", "users.json")

users_db_fields = ["user_id", "email", "password", "name"]


def generate_id():
    with open(users_db) as f:
        db_data = json.load(f)
        if db_data["users"]:
            users_ids = []
            for key in db_data["users"]:
                users_ids.append(int(key))
            return max(users_ids) + 1
        else:
            return 1


def is_user_registered(new_user_dict):
    with open(users_db) as f:
        db_data = json.load(f)
        for user in db_data["users"].values():
            if new_user_dict["email"] == user["email"]:
                return True
        return False


def update_users_db(user_id, new_user_dict):

    with open(users_db, "r+") as f:
        db_data = json.load(f)
        db_data["users"][user_id] = new_user_dict
        f.seek(0)
        json.dump(db_data, f, indent=4)


def register_user(user_dict):
    if is_user_registered(user_dict):
        raise UserAlreadyRegisteredError
    else:
        user_id = generate_id()
        update_users_db(user_id, user_dict)


def get_user(email, password):
    user_login_details = ", ".join([email, password])
    with open(users_db) as f:
        db_data = json.load(f)
        for user in db_data["users"].values():
            if user["email"] == email and user["password"] == password:
                return user
        raise UserNotFoundError("Your email or password or both are incorrect.")


if __name__ == "__main__":
    # user_dict = {"name": "John", "email": "john@gm.co", "password": "fgH138@ng0"}
    # register_user(user_dict)
    another_user = {"name": "Emily", "email": "emily2@gm.co", "password": "emilY38@ng0"}
    register_user(another_user)
    print(is_user_registered(another_user))
