# fac using function and recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter a number: "))
result = fact(num)
print(f"The factorial of {num} is {result}")

# output
# Enter a number: 5 
# The factorial of 5 is 120