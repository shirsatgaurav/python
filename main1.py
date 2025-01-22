import random

# Fix the variable name from 'cumputer' to 'computer'
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Fix the dictionary keys for clarity and consistent naming
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the user's choice
you = youDict[youstr]

# Display choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Game logic for win, lose, or draw
if computer == you:
    print("It's a draw!")
else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    else:
        print("Something went wrong!")
