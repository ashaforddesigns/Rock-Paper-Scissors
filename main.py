from tkinter import *
from tkinter import ttk
import random

# documentation answer
# # creates the window and the title for it
# root = Tk()
# root.title("Rock, Paper, Scissors, SHOOT!") 

# # creates the frame where all widgets will be held
# mainframe = ttk.Frame(root, padding="3 3 12 12") 
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1) # frame will fill the whole size of the window if resized (column then row)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # this entry makes a variable called "feet"
# feet_entry.grid(column=2, row=1, sticky=(W, E)) #places it in the grid

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) # this is a label that takes the variable "meters" and puts it into it and then places it into the grid with the .grid fuction (does it all at the same time)
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5) #adds padding on all of the children of the mainframe
# feet_entry.focus() # automatically highlights and get ready for an answer for this label
# root.bind("<Return>", calculate) # says the return key on the keyboard is the same as hitting the calculate button
# root.mainloop()

root = Tk()
root.title("Rock, Paper, Scissors, SHOOT!")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainFrame, text="Let's play rock, paper, scissors!").grid(column=0, row=0)
ttk.Label(mainFrame, text="Make your moover").grid(column=0, row=1)


Rock = StringVar()
rockButton = ttk.Button(mainFrame, text="Rock", textvariable=Rock)
rockButton.grid(column=0, row=2, sticky=(W, E))

Paper = StringVar()
PaperButton = ttk.Button(mainFrame, text="Paper", textvariable=Paper)
PaperButton.grid(column=1, row=2, sticky=(W, E))

Scissors = StringVar()
ScissorsButton = ttk.Button(mainFrame, text="Scissors", textvariable=Scissors)
ScissorsButton.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainFrame, text="My Score").grid(column=0, row=3)
ttk.Label(mainFrame, text="Your Score").grid(column=0, row=3)

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

