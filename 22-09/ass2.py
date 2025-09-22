arr = ["This\n", "is", "a", "python", "assignment"]

with open("file1.txt", "w") as f:
    for item in arr:
        f.write(item)
        
with open("file2.txt", "w") as f:
    f.writelines(arr)


# write writes the entire string at once while writelines writes a list of strings to the file.