# 3️⃣ Multiplication Table Skipping a Number (For + If + Continue/Break)
# Write a program that:
 
# Takes a number n from the user.
 
# Prints the multiplication table from 1 to 10.
 
# If the multiplication result becomes greater than 50, break the loop.
 
# If the multiplier is 5, skip that iteration using continue.


n = int(input("Enter a number: "))

for i in range(1, 11):
    if n == 5:
        continue
    if n * i > 50:
        break
    print(n * i)

# output
# Enter a number: 7
# 7
# 14
# 21
# 28
# 35
# 42
# 49