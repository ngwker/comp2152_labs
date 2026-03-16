
import random

# This is the Python file for the week
choices = ["Rock", "Paper", "Scissor"]
playerChoice = input("Enter your choice: (1=Rock ,2=Paper, 3=Scissor")
print(playerChoice)

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    playerChoice = choices[playerChoice - 1]
    playerChoice = choices[computerChoice - 1]

    print("You chose: ", playerChoice)
    print("Computer chose: ", computerChoice - 1)

    # Determine the winner using if/elif/else
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 0 and computerChoice == 2:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 1 and computerChoice == 0:
        print("Paper beats Rock - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!")
