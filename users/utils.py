import re

from django.core.exceptions import ValidationError


class UsernameValidationError(ValidationError):
    pass


def validate_username(username):
    regex = "^[a-zA-Z0-9_\.-@+]+$"
    match = re.match(regex, username)
    if match:
        return match
    else:
        raise UsernameValidationError("Username is invalid.")
