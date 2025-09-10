# check prime no from 1 to n 

def checkPrime(n):
    i = 2
    while (i < n):
        if (n % i == 0):
            return False
        i += 1
    return True

n = int(input("Enter the no: "))

if (n < 2):
    print("Not a prime")
else:
    i = 2
    while (i <= n):
        if (checkPrime(i)):
            print(f"{i} is a prime number")
        else:
            print(f"{i} is not a prime number")
        i += 1

# output     
# Enter the no: 7
# 2 is a prime number
# 3 is a prime number
# 4 is not a prime number
# 5 is a prime number
# 6 is not a prime number
# 7 is a prime number