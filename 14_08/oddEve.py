#odd even game

import random

def batting(target=None):
    score = 0
    while True:
        player_choice = int(input("Enter your run (1-6): "))
        if player_choice not in range(1, 7):
            print("Invalid! Choose between 1 to 6.")
            continue
        comp_choice = random.randint(1, 6)
        print(f"Computer bowls: {comp_choice}")
        if player_choice == comp_choice:
            print("OUT!")
            break
        else:
            score += player_choice
            print(f"Your score: {score}")
            if target is not None and score > target:
                print("You have chased the target!")
                break
    return score

def bowling(target=None):
    score = 0
    while True:
        player_choice = int(input("Enter your bowl (1-6): "))
        if player_choice not in range(1, 7):
            print("Invalid! Choose between 1 to 6.")
            continue
        comp_choice = random.randint(1, 6)
        print(f"Computer bats: {comp_choice}")
        if player_choice == comp_choice:
            print("OUT!")
            break
        else:
            score += comp_choice
            print(f"Computer score: {score}")
            if target is not None and score > target:
                print("Computer has chased the target!")
                break
    return score

def choose():
    choice = int(input("Choose between 1 for batting and 2 for bowling: "))
    if choice not in [1, 2]:
        print("Invalid choice! Thank you for playing")
        return
    if choice == 1:
        print("You chose batting first")
        print("\n--- First Innings ---")
        player_score = batting()
        print(f"\nYour total score: {player_score}")
        print("\n--- Second Innings (Computer Chasing) ---")
        comp_score = bowling(target=player_score)
        if comp_score > player_score:
            print(f"Computer scored {comp_score}, Computer wins!")
        elif comp_score == player_score:
            print("Match tied!")
        else:
            print("You win!")
    else:
        print("You chose bowling first")
        print("\n--- First Innings ---")
        comp_score = bowling()
        print(f"\nComputer total score: {comp_score}")
        print("\n--- Second Innings (You Chasing) ---")
        player_score = batting(target=comp_score)
        if player_score > comp_score:
            print(f"You scored {player_score}, You win!")
        elif player_score == comp_score:
            print("Match tied!")
        else:
            print("Computer wins!")

def computer_toss_choice():
    if random.choice([1, 2]) == 1:
        print("Computer chose batting first")
        comp_score = bowling()
        print(f"Computer scored {comp_score}")
        print("\n--- Your turn to chase ---")
        player_score = batting(target=comp_score)
        if player_score > comp_score:
            print("You win!")
        elif player_score == comp_score:
            print("Match tied!")
        else:
            print("Computer wins!")
    else:
        print("Computer chose bowling first")
        player_score = batting()
        print(f"You scored {player_score}")
        print("\n--- Computer chasing ---")
        comp_score = bowling(target=player_score)
        if comp_score > player_score:
            print("Computer wins!")
        elif comp_score == player_score:
            print("Match tied!")
        else:
            print("You win!")

print("Welcome to odd even game, you have to choose a number between 1 to 6")
print("It's toss time")
toss = int(input("Choose between 1 for odd and 2 for even: "))

if toss not in [1, 2]:
    print("Invalid choice! Thank you for playing")
else:
    n = int(input("Enter your number for toss (1-6): "))
    com = random.randint(1, 6)
    print(f"Computer chose {com} for toss")
    total = n + com
    if toss == 2:
        if total % 2 == 0:
            print("You won the toss!")
            choose()
        else:
            print("Computer won the toss!")
            computer_toss_choice()
    else:
        if total % 2 != 0:
            print("You won the toss!")
            choose()
        else:
            print("Computer won the toss!")
            computer_toss_choice()


# Welcome to odd even game, you have to choose a number between 1 to 6
# It's toss time
# Choose between 1 for odd and 2 for even: 1
# Enter your number for toss (1-6): 7
# Computer chose 4 for toss
# You won the toss!
# Choose between 1 for batting and 2 for bowling: 1
# You chose batting first

# --- First Innings ---
# Enter your run (1-6): 3
# Computer bowls: 6
# Your score: 3
# Enter your run (1-6): 2
# Computer bowls: 6
# Your score: 5
# Enter your run (1-6): 6
# Computer bowls: 5
# Your score: 11
# Enter your run (1-6): 1
# Computer bowls: 4
# Your score: 12
# Enter your run (1-6): 2
# Computer bowls: 1
# Your score: 14
# Enter your run (1-6): 2
# Computer bowls: 3
# Your score: 16
# Enter your run (1-6): 4
# Computer bowls: 5
# Your score: 20
# Enter your run (1-6): 3
# Computer bowls: 1
# Your score: 23
# Enter your run (1-6): 2
# Computer bowls: 3
# Your score: 25
# Enter your run (1-6): 3
# Computer bowls: 2
# Your score: 28
# Enter your run (1-6): 1
# Computer bowls: 6
# Your score: 29
# Enter your run (1-6): 3
# Computer bowls: 5
# Your score: 32
# Enter your run (1-6): 2
# Computer bowls: 3
# Your score: 34
# Enter your run (1-6): 2
# Computer bowls: 4
# Your score: 36
# Enter your run (1-6): 2
# Computer bowls: 2
# OUT!

# Your total score: 36

# --- Second Innings (Computer Chasing) ---
# Enter your bowl (1-6): 4
# Computer bats: 6
# Computer score: 6
# Enter your bowl (1-6): 3
# Computer bats: 2
# Computer score: 8
# Enter your bowl (1-6): 3
# Computer bats: 4
# Computer score: 12
# Enter your bowl (1-6): 3
# Computer bats: 6
# Computer score: 18
# Enter your bowl (1-6): 3
# Computer bats: 4
# Computer score: 22
# Enter your bowl (1-6): 3
# Computer bats: 5
# Computer score: 27
# Enter your bowl (1-6): 3
# Computer bats: 5
# Computer score: 32
# Enter your bowl (1-6): 3
# Computer bats: 2
# Computer score: 34
# Enter your bowl (1-6): 3
# Computer bats: 4
# Computer score: 38
# Computer has chased the target!
# Computer scored 38, Computer wins!