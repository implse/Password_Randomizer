import string
import secrets

alphanumeric = string.ascii_letters + string.digits + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
password = "".join(secrets.choice(alphanumeric) for char in range(20))

print(password)
