import re
from apps.validators.exceptions import EmailValidationError, NameValidationError, PasswordInvalidFormatError, PasswordsDontMatchError


def validate_email(email: str) -> str:
    match = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email)
    if match.group():
        return email.lower()
    else:
        raise EmailValidationError


def validate_name(name: str) -> str:
    if re.match(r"[a-zA-Z]+[a-zA-Z-]+[a-zA-Z-]", name):
        name = name.split()
        if len(name) == 2:
            return f"{name[0].lower().capitalize()} {name[1].lower().capitalize()}"
        else:
            return name[0].lower().capitalize()
    else:
        raise NameValidationError


def validate_password_format(password):
    if not re.fullmatch(r'[A-Za-z0-9@!#$%^&*()_\-+=]{8,}', password):
        raise PasswordInvalidFormatError(
            "Password must contain at least eight characters, "
            "at least one uppercase letter, one lowercase letter, one number and one special character:"
        )
    else:
        return password


def check_passwords_matching(password_1, password_2):
    if password_1 == password_2:
        return password_1
    else:
        raise PasswordsDontMatchError("Passwords don't match.")


if __name__ == "__main__":
    print(validate_email("svitlaroza@gm.co"))
    print(validate_name("George-njrg"))
    print(validate_password_format("1701L!an"))






