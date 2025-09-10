# Given a sentence as input, count the number of words in it with and without using the built-in split() function.

st = input("Enter a string:")
words = 0
st = st.strip()
s=False
for i in st:
    if i.isspace() and s==False:
        words += 1
        s = True
    else:
        s = False
print(f"Number of words in the string is {words+1}")

# output
# Enter a string: hello world
# Number of words in the string is 2