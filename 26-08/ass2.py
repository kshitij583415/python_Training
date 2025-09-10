# students = [
# ("Alice", ["Math", "Science", "History"]),
# ("Bob", ["Math", "English", "Science"]),
# ("Charlie", ["Biology", "Math", "History"]),
# ("David", ["Math", "Science", "Biology"]),
# ]
 
# Tasks:
 
# Find the set of subjects that are common to all students.
 
# Find the set of unique subjects taken by exactly one student only.
 
# Convert the result into a list of tuples of the form:
 
# ("Common", [...]) for common subjects
 
# ("Unique", [...]) for unique subjects
# where subjects inside the lists should be sorted alphabetically.
 


students = [
("Alice", ["Math", "Science", "History","Abc"]),
("Bob", ["Math", "English", "Science","Abc"]),
("Charlie", ["Biology", "Math", "History","Science","Abc"]),
("David", ["Math", "Science", "Biology","Abc"]),
]

dic = {}
cnt=0

for _, c in students:
    cnt+=1
    for i in c:
        dic[i] = dic.get(i, 0) + 1

l1 = []
l2 = []

for i in dic:
    if dic[i] >= cnt:
        print(f"Unique subject is: {i}")
        l1.append(i)
    if dic[i] == 1:
        print(f"Subject taken by only one student is: {i}")
        l2.append(i)

l1.sort()
l2.sort()
comm = ("Common", l1)
uniq = ("Unique", l2)

print(comm)
print(uniq)


# Unique subject is: Math
# Unique subject is: Science
# Unique subject is: Abc
# Subject taken by only one student is: English
# ('Common', ['Abc', 'Math', 'Science'])
# ('Unique', ['English'])