import hashlib

def make_password(password):
    return hashlib.md5(("9@^"+password+'$&').encode()).hexdigest()