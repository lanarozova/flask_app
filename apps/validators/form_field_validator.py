import re
from apps.validators.exceptions import EmailValidationError, NameValidationError, PasswordInvalidFormatError, PasswordsDontMatchError


def validate_email(email: str) -> str:
    match = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email)
    if match.group():
        return email.lower()
    else:
        raise EmailValidationError("Incorrect email format.")


def validate_name(name: str) -> str:
    pattern = r"[a-zA-Z]+[a-zA-Z-]"
    name = name.split()
    if len(name) == 2:
        if re.match(pattern, name[0]) and re.match(pattern, name[1]):
            return f"{name[0].lower().capitalize()} {name[1].lower().capitalize()}"
    else:
        if re.match(pattern, name[0]):
            return name[0].lower().capitalize()
    raise NameValidationError("Name must consist of at least 2 latin letters and can include hyphens or spaces.")


def validate_password_format(password):
    pw_validated = (len(password) < 9
                    and re.match(r'[A-Z]', password)
                    and re.match(r'[0-9]]', password)
                    and re.match(r'[@!#$%^&*()_\-+=]', password))

    if not pw_validated:
        raise PasswordInvalidFormatError(
            "Password must contain at least eight characters, "
            "at least one uppercase letter, one lowercase letter, one number and one special character."
        )
    return password


def check_passwords_matching(password_1, password_2):
    if password_1 == password_2:
        return password_1
    else:
        raise PasswordsDontMatchError("Passwords don't match.")
