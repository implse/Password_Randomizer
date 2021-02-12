import string
import secrets

alphanumeric = string.ascii_letters + string.digits
symbols = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


while True:
    try:
        ask_user = input("How many characters do you want in your password: ")
        password_length = int(ask_user)
        if password_length > 0:
            break
        else:
            print("Number can't be negative or zero, try again\n")
            continue
    except:
        print("Input must be an integer, try again\n")
        continue


password = "".join(secrets.choice(alphanumeric + symbols) for char in range(password_length))
print(password)
