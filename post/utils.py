import secrets


def secret_token():
    return secrets.token_urlsafe(6)
