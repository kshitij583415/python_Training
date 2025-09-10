# rhombus

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * n)


print()


for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if (i == 1 or i == n):
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*")
        
# output
# 5
#     *****
#    *****
#   *****
#  *****
# *****

#     *****
#    *   *
#   *   *
#  *   *
# *****
