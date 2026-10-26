import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

characters = lowercase + uppercase + digits + punctuation


def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


while True:
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if length <= 0:
        print("Please enter a positive integer.")
        continue

    break

print("Your password:", generate_password(length))