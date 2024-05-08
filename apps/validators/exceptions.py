class EmailValidationError(Exception):
    pass


class NameValidationError(Exception):
    pass

class PasswordInvalidFormatError(Exception):
    pass

class PasswordsDontMatchError(Exception):
    pass