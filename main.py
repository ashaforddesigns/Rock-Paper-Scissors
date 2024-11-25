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

    
def game(userResponse):
    # initilizing variables
    RPS = ["rock", "paper", "scissors"]
    compResponse = random.choice(RPS)
    global compScore, userScore, MSG #you must make it global in order to be acessed by the gui
    
    # tied
    if compResponse == userResponse:
        MSG.set("It's a draw this round")
    # the user wins
    elif (compResponse == "rock" and userResponse == "paper") or (compResponse == "paper" and userResponse == "scissors") or (compResponse == "scissors" and userResponse == "rock"):
        MSG.set(f"You win this round! I chose {compResponse}") # you must use an f string so everything stays a string, no variables
        userScore.set(userScore.get() + 1)
    # the user loses
    else:
        MSG.set(f"You lost this round! I chose {compResponse}")
        compScore.set(compScore.get() + 1)

def resetGame():
    MSG.set("")
    compScore.set(0)
    userScore.set(0)



root = Tk()
root.title("Rock, Paper, Scissors, SHOOT!")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))


#center this thing later
MSG = StringVar() # this is a TKinter message. to retrieve it you must use the .get() fuction
ttk.Label(mainFrame, textvariable=MSG).grid(column=0, row=0,columnspan=3) 


ttk.Label(mainFrame, text="Make your move").grid(column=0, row=1, columnspan=3)


Rock = StringVar(value="Rock")
rockButton = ttk.Button(mainFrame, command=lambda: game("rock"), textvariable=Rock, width=4) #if you dont add lambda the game run the fuction immediately
rockButton.grid(column=0, row=2) 

Paper = StringVar(value="Paper")
PaperButton = ttk.Button(mainFrame, command=lambda: game("paper"), textvariable=Paper, width=5)
PaperButton.grid(column=1, row=2)

Scissors = StringVar(value="Scissors")
ScissorsButton = ttk.Button(mainFrame, command=lambda: game("scissors"), textvariable=Scissors, width=8)
ScissorsButton.grid(column=2, row=2)

ttk.Label(mainFrame, text="My Score").grid(column=0, row=3, columnspan=2)
ttk.Label(mainFrame, text="Your Score").grid(column=1, row=3, columnspan=2)

compScore = IntVar()
compScore.set(0)
ttk.Label(mainFrame, textvariable=compScore).grid(column=0,row=4, columnspan=2)


userScore = IntVar()
userScore.set(0)
ttk.Label(mainFrame, textvariable=userScore).grid(column=1,row=4, columnspan=2)

reset = StringVar()
ttk.Button(mainFrame, text="Reset", command=lambda: resetGame(), width=8).grid(column=1, row=5)
root.mainloop()




