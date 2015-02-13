import hashlib


hashpassword = lambda text, salt: hashlib.sha512(salt + text).hexdigest()
