# 2.	Write a Python program that takes a string input from the user and checks whether it is a palindrome

st = input("Enter a string: ")
if st==st[::-1]:
    print(f"{st} is a palindrome")
else:
    print(f"{st} is not a palindrome")

# output
# Enter a string: aba
# aba is a palindrome