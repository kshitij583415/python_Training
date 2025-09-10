# 2]. Write a function that takes three numbers and returns the largest.


def largest():
    a, b, c = map(int, input().split())
    return max(a, b, c)

print(largest())


# output
# 4 3 1
# 4