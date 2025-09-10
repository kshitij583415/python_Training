# Given a tuple, write a program to replace an element with a new value.



tup = (1, 2, 3, 4, 5)

tup = tuple(10 if i == 4 else i for i in tup)
print(tup)

# output
# (1, 2, 3, 10, 5)