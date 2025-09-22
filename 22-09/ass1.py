# open example
f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# with open example
with open("file.txt", "r") as f:
    data = f.read()
    print(data)

# output:
# Hello my name is kshitij singh
# Hello my name is kshitij singh

# diff between open and with open is with open automatically closes the file while open requires us to manually close the file.