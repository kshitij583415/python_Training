# flatten a nested list [1, [2, [3, 4], 5], 6] --> [1, 2, 3, 4, 5, 6]

def flatten(l):
    ls = []
    for i in l:
        if isinstance(i, list):
            ls.extend(flatten(i))
        else:
            ls.append(i)
    return ls


l = [1, [2, [3, 4], 5], 6]
ls = flatten(l)
print(ls)

# lis = [1, 2, 3, 4, 5, 6,8,9,1]
# lis.append(1)
# lis.extend([10, 11])

# print(lis)

# output
# [1, 2, 3, 4, 5, 6]