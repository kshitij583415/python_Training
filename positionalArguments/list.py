# how to use positional arguments in list

def add(a, b, c):
    print(a + b + c)

nums = [1, 2, 3]
add(*nums)

# output
# 6