# data = [(1, 2, 3), (3, 4), (2, 5, 6), (1, 4, 7)]
# Flatten all tuples into a single list without using itertools or list comprehension.
 
# Find the numbers that appear in at least 2 different tuples.
 
# Return the result as a tuple (sorted_common_numbers, count) where:
 
# sorted_common_numbers is a sorted list of those repeated numbers.
 
# count is how many such numbers exist.


from collections import OrderedDict


data = [(1, 2, 3), (3, 4), (2, 5, 6), (1, 4, 7)]
tp=()

for i in data:
    for j in i:
        tp=tp+(j,)
print(tp)


dic = OrderedDict()
l = []
cnt=0

for i in data:
    st = set(i)
    for j in st:
        dic[j] = dic.get(j, 0) + 1
    
for i in dic:
    if dic[i] >= 2:
        l.append(i)
        cnt+=1

ans = (l, cnt)
print(ans)


# output
# (1, 2, 3, 3, 4, 2, 5, 6, 1, 4, 7)
# ([1, 2, 3, 4], 4)