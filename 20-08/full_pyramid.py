# full pyramid

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    num = 1
    for j in range(1, 2 * i):
        print(num, end="")
        num += 1
    print()

# output
# 5
#     1
#    123
#   12345
#  1234567
# 123456789