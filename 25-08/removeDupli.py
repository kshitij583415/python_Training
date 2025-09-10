# Write a program that removes duplicate characters while keeping only the first occurrence.
 

st = input("Enter a string: ")
dupli = []
for i in st.split():
    if i not in dupli:
        dupli.append(i)   
print(" ".join(dupli))


# output
# Enter a string: hello hello world
# hello world   