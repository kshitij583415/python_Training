
# logical operators in Python



a = 5
b = 0
c = 10



if a > 0 and c > a:
    print("Both a > 0 and c > a are True")


print("a and c:", a and c)    
print("b and c:", b and c)    



if a < 0 or b == 0:
    print("Either a < 0 or b == 0 is True")


print("a or c:", a or c)     
print("b or c:", b or c)      



if not b:
    print("b is falsy, so 'not b' is True")


print("not a:", not a)       
print("not b:", not b)        



result = not (a and b) or (c and a)
print("Result of combined expression:", result)




# Order of Precedence of Logical Operators

def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False


if order(-1) or order(5) or order(10):
    print("Atleast one of the number is positive")

# output
# Both a > 0 and c > a are True
# a and c: 10
# b and c: 0
# Either a < 0 or b == 0 is True
# a or c: 5
# b or c: 10
# b is falsy, so 'not b' is True
# not a: False
# not b: True
# Result of combined expression: True
# Method called for value: -1
# Method called for value: 5
# Atleast one of the number is positive