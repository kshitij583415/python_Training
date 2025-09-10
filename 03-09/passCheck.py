# 3]. Write a function that checks if a password is strong (at least 8 chars, contains uppercase, lowercase, number, and symbol).


import re

reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"

def passValidator(password):
    if(re.match(reg, password)):
        return True
    return False

print(passValidator(input("Enter a password ")))

# Enter a password heloo2e$K
# True