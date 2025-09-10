# list comphrehension


arr=[1,2,3,4,5,6,7,8,9,10]

list1 = [x ** 2 for x in arr if x % 2 == 0]

print(list1)


# zip

l1 = ["apple", "banana", "cherry"]
l2 = [1, 2, 3]

t = zip(l1, l2)

print(list(t))

# map

numbers = [1, 2, 3, 4, 5]

result = map(str, numbers)  
print(list(result))  


# output
# [4, 16, 36, 64, 100]
# [('apple', 1), ('banana', 2), ('cherry', 3)]
# ['1', '2', '3', '4', '5']