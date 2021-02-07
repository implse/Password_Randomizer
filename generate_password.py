import string
import secrets

alphanumeric = string.ascii_letters + string.digits
symbols = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
password = "".join(secrets.choice(alphanumeric + symbols) for char in range(20))

print(password)
