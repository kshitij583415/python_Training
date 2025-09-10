# Dictionary methods


d = {'a': 1, 'b': 2}
print(d.get('a'))        
print(d.get('c', 0))     

d = {'a': 1, 'b': 2}
val = d.pop('a')
print(val)             
print(d)  

d = {'x': 10, 'y': 20}
item = d.popitem()
print(item)             
print(d) 

d = {'a': 1}
d.update({'b': 2, 'c': 3})
print(d) 

d = {'a': 1}
d.clear()
print(d)


arr = [1, 2, 3]
for i in enumerate(arr):
    print(i)


# output
# 1
# 0
# 1
# {'b': 2}
# ('y', 20)
# {'x': 10}
# {'a': 1, 'b': 2, 'c': 3}
# {}
# (0, 1)
# (1, 2)
# (2, 3)