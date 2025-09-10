# 2️⃣ Guess the Number Game (While + If + Break)
# Write a program that:
 
# Randomly selects a number between 1 and 50.
 
# Repeatedly asks the user to guess the number.
 
# If the guess is correct, prints "You guessed it!" and exits using break.
 
# If the guess is too high or too low, prints a hint and lets the user try again.
 
# Uses a while loop for continuous guessing.

import random

no = random.randint(1, 50)
while True:
    i = int(input("Enter a no to guess in the range of 1 to 50: "))
    
    if i < 1 or i > 50:
        print("Please enter a valid no within range of 1 to 50")
    elif i == no:
        print("You guessed it right!")
        break
    elif i < no:
        print("Try a higher no")
    else:
        print("Try a lower no")

# output
# Enter a no to guess in the range of 1 to 50: 4
# Try a lower no
# Enter a no to guess in the range of 1 to 50: 2
# Try a higher no
# Enter a no to guess in the range of 1 to 50: 3
# You guessed it right!



