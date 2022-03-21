import re


def is_email_valid(email: str) -> bool:
    """
    Check email using regex, return boolean.
    """
    if not email:
        return False

    email_regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )

    return re.fullmatch(email_regex, email)
