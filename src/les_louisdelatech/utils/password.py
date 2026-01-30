import hashlib
import secrets
import string


def generate_password() -> str:
    # Avoid non-printable ASCII and Discord/Markdown pitfalls. A long, alnum-only
    # password is strong while remaining copy/paste-friendly for end users.
    alphabet = string.ascii_letters + string.digits
    length = secrets.SystemRandom().randint(20, 30)
    return "".join(secrets.choice(alphabet) for _ in range(length))


def hash_password(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()
