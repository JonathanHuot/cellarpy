from settings import settings
import hashlib


hashpassword = lambda text: hashlib.sha512(settings["secret"]["salt"] + text).hexdigest()
