# Continue Statement Example
# Print numbers from 1 to 10, but skip printing 5.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# output
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
