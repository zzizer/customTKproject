import bcrypt

def hash_password(password: str) -> str:
    """
    Hashes a plaintext password.
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(provided_password: str, stored_hashed_password: str) -> bool:
    """
    Verifies a password by comparing it with the stored hashed password.
    """
    return bcrypt.checkpw(provided_password.encode(), stored_hashed_password.encode())