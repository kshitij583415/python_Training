# Factorial Calculation
# Input an integer N and compute its factorial using a for loop.

n = int(input("Enter a number: "))
fact=1
for i in range(1, n + 1):
    fact *= i
print(fact)

# output
# Enter a number: 5
# 120