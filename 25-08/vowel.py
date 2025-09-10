# Ask the user to enter a word and count how many vowels and consonants it contains.

st = input("Enter a string: ")

vowels = 'aeiouAEIOU'
vCount = 0
cCount = 0
for i in st:
    if i in vowels:
        vCount += 1
    else:
        cCount += 1

print(f"Number of vowels in the string is {vCount} and consonants is {cCount}")

# output
# Enter a string: hello world
# Number of vowels in the string is 3 and consonants is 8