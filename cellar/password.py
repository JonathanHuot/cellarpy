import hashlib


def hashpassword(text, salt):
    return hashlib.sha512("{0}|{1}".format(salt, text).encode('utf-8')).hexdigest()
