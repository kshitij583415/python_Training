# 1️⃣ Prime Number Finder (For Loop + If + Break)
# Write a program that:
 
# Takes an integer input n.
 
# Checks whether n is a prime number.
 
# Uses a for loop to check divisibility and a break statement to stop when a factor is found.
 
# Prints "Prime" if it’s prime, otherwise "Not Prime"


n = int(input("Enter a no: "))
flag=0
for i in range(2, n):
    if (n % i == 0):
        flag = 1
        break
if flag == 0:
    print("Prime")
else:
    print("Not Prime")

# output
# Enter a no: 4
# Not Prime