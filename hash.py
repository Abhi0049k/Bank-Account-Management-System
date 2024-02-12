from bcrypt import *

def hash_password(password):
    hash = hashpw(password.encode("utf-8"), gensalt(rounds=4))
    return hash


def verify_password(password, hashed_password):
    result = checkpw(password.encode("utf-8"), hashed_password)
    return result

