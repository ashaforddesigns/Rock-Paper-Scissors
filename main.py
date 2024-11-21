import tkinter as tk
import random

# initilizing variables
userResponse = input("Rock, Paper or Scissors? (press (q) to quit): ")
RPS = ["rock", "paper", "scissors"]
compResponse = random.choice(RPS)
compScore = 0
userScore = 0
#game scenarios
while userResponse is not "q":
    # tied
    if compResponse == userResponse:
        print("It's a draw this round")
    # the user wins
    elif (compResponse == "rock" and userResponse == "paper") or (compResponse == "paper" and userResponse == "scissors") or (compResponse == "scissors" and userResponse == "rock"):
        print("You win this round! I chose", compResponse)
        userScore+=1
    # the user loses
    else:
        print("You lost this round! I chose", compResponse)
        compScore+=1
    
    userResponse = input("Rock, Paper or Scissors? (press (q) to quit): ")
    compResponse = random.choice(RPS)
    print("The score is currently: ", "Me - ", compScore, "You - ", userScore)

# end screen
print("The final score is: Me -", compScore, "You - ", userScore)
if compScore > userScore:
    print("I have won! Sorry buddy")
elif compScore == userScore:
    print("The game ended in a tie :0 Rematch?")
else:
    print("Congratulations! You beat me.")

