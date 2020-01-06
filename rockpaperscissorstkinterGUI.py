from Tkinter import *
from ttk import *
import random

player_score = 0
computer_score = 0
  
def play():
  picks = ["Rock", "Paper", "Scissors"]
  computer_pick = random.choice(picks)
  user_pick = human_pick.get()
  player_score = 0
  computer_score = 0

  if user_pick == computer_pick: #checks who wins
    result_set.set("Computer chose %s. It's a draw!" % (computer_pick)) 
  
  if user_pick == "Paper":
    if computer_pick == "Scissors":
      result_set.set("Computer chose scissors. You lose!")
      computer_score += 1
    elif computer_pick == "Rock":
      result_set.set("Computer chose rock. You win!")
      player_score += 1
  
  if user_pick == "Rock":
    if computer_pick == "Scissors":
      result_set.set("Computer chose scissors. You win!")
      player_score += 1
    elif computer_pick == "Paper":
      result_set.set("Computer chose paper. You lose!")
      computer_score += 1
  
  if user_pick == "Scissors":
    if computer_pick == "Rock":
      result_set.set("Computer chose rock. You lose!")
      computer_score += 1
    elif computer_pick == "Paper":
      result_set.set("Computer chose paper. You win!")
      player_score += 1
      
    return player_score, computer_score

root = Tk() # sets up root window
root.title ('Rock Paper Scissors') # adds title to the window 'Rock Paper Scissors'

mainframe = Frame(root, padding = '3 3 12 12') # sets up space between frame and window
mainframe.grid(column=0, row = 0, sticky=(N,W,E,S)) # choose grid layout, sticky uses Cardinal directions
mainframe.columnconfigure(0, weight=1) 
mainframe.rowconfigure(0,weight=1)

human_pick = StringVar()
computer_pick = StringVar()
result_set = StringVar()


human_pick.set("Rock")


Label(mainframe, text='Player').grid(column=1, row = 1, sticky = W)
Radiobutton(mainframe, text ='Rock', variable = human_pick, value = 'Rock').grid(column=1, row=2, sticky=W)
Radiobutton(mainframe, text ='Paper', variable = human_pick, value = 'Paper').grid(column=1, row=3, sticky=W)
Radiobutton(mainframe, text ='Scissors', variable = human_pick, value = 'Scissors').grid(column=1, row=4, sticky=W)

Label(mainframe, text='Computer').grid(column=3, row = 1, sticky = W)
Radiobutton(mainframe, text ='Rock', variable = computer_pick, value = 'Rock').grid(column=3, row=2, sticky=W)
Radiobutton(mainframe, text ='Paper', variable = computer_pick, value = 'Paper').grid(column=3, row=3, sticky=W)
Radiobutton(mainframe, text ='Scissors', variable = computer_pick, value = 'Scissors').grid(column=3, row=4, sticky=W)

Button(mainframe, text="Play", command = play).grid(column = 2, row = 7, sticky = W)

Label(mainframe, textvariable = result_set).grid(column = 1, row = 5, sticky =W, columnspan = 2)
Label(mainframe, text='Player Score: %d' % (player_score)).grid(column=3, row = 10, sticky = W)
Label(mainframe, text='Computer Score: %d' % (computer_score)).grid(column=1, row = 10, sticky = W)

# label - method to display text on window 
# mainframe - where the widget will go, in this case the mainframe
# text = 'Player' - input text for label
# grid - indicates the use of the grid system (row and column)
# sticky = W - text will be aligned with left side of window (West)

root.mainloop() # tells computer to run GUI

 
