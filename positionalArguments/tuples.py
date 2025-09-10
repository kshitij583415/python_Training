# positional arguments in tuples

def multiply(a, b, c):
    print(a * b * c)

t = (2, 3, 4)
multiply(*t)

# output
# 24