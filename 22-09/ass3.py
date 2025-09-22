with open("file1.txt", "r") as f:
    data = f.read() 
    print(data)

with open("file1.txt", "r") as f:
    data1 = f.readline()
    data2 = f.readline()
    print(data1)
    print(data2)

with open("file1.txt", "r") as f:
    data = f.readlines()
    print(data)

with open("file1.txt", "r") as f:
    data = f.read(2)
    print(data)


# read reads the entire file at once, readline reads one line at a time, readlines reads all lines and returns them as a list, read(n) reads n characters from the file.