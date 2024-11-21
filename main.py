import tkinter as tk
import random

# game logic
userResponse = input("Rock, Paper or Scissors? (press (q) to quit): ")

RPS = ["rock", "paper", "scissors"]
compResponse = random.choice(RPS)

#scenarios

while True:
    if userResponse == "q":
        break
    # tied
    if compResponse == userResponse:
        print("It's a tie! :0")
    # the user wins
    elif (compResponse == "rock" and userResponse == "paper") or (compResponse == "paper" and userResponse == "scissors") or (compResponse == "scissors" and userResponse == "rock"):
        print("You win! I chose", compResponse)
    # the user loses
    else:
        print("You lost! I chose", compResponse)



    #TESTING PURPOSES--delete later   
    print("FOR TESTING:", userResponse, compResponse)

#GOALS:
#plays until user hits "q"...
#tracks wins somehow...

# while True:
#     if userResponse == "q":
#         break
