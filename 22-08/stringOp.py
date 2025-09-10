# String Operations

s1 = "Hello"
s2 = "Kshitij"

print(s1 + ' ' + s2)
print(s1[1])
print(s2[3])

print(s1[1:4] + s2[0:5:2])

s3 = "ello"

print(s3 in s1)

if s3 in s1:
    print(s1[0::2])
else:
    print(s2[1::2])

# output
# Hello Kshitij
# e             
# hitij
# True  
# Hlo
# hitij
