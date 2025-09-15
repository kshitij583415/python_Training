s = ('a', 'b', 3, 6, 'i', 7, 'c', 'z')

cnt = 0
ans = []

for i in s:
    if isinstance(i, int):
        ans.append(i)
        cnt = i + 1
    else:
        ans.append(cnt)
        cnt += 1

print(tuple(ans))

# ouput
# (0, 1, 3, 6, 7, 7, 8, 9)
