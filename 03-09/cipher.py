# Write a Python program using a nested function to perform simple text encryption and decryption.
# Create a main function cipher(text, mode) that takes:
# text (string to process)
# mode ("encrypt" or "decrypt").
# Inside cipher(), define two inner functions:
# encrypt(text) → shifts each character by +3 in ASCII.
# decrypt(text) → shifts each character by -3 in ASCII.
# Based on the mode, call the inner function and return the result.


def encrypt(text):
    txt=""
    for i in range(0, len(text)):
        txt= txt+chr(ord(text[i]) + 3)
    return txt

def decrypt(text):
    txt=""
    for i in range(0, len(text)):
        txt =txt+ chr(ord(text[i]) - 3)
    return txt


def cipher(text, mode):
    if (mode == 'encrypt'):
        return encrypt(text)
    elif (mode == 'decrypt'):
        return decrypt(text)


mode = input()
text = input()

if mode == 'encrypt':
    print(cipher(text, 'encrypt'))
elif mode == 'decrypt':
    print(cipher(text, 'decrypt'))


# output
# encrypt
# hello 
# khoor