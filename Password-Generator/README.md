# Password Generator

A simple Python CLI program that generates a random password of the
length you choose. The password mixes lowercase letters, uppercase
letters, digits and symbols.

## Features
- You choose the password length
- Uses lowercase, uppercase, digits and symbols
- Asks again if the input is not a number, or is zero or negative
- Password generation is in a separate function

## How to Run

python password_generator.py

## Sample Output

Enter the length of the password: abc
Please enter a valid integer.
Enter the length of the password: 0
Please enter a positive integer.
Enter the length of the password: 12
Your password: k9#Tq2!mPz@L


## Note
This project is for practice. The `random` module is not designed for real security. For real passwords, Python's `secrets` module is the better choice.

## Author
Md. Majharul Islam Porbo  
Portfolio: [porbo.cyou](https://porbo.cyou)
