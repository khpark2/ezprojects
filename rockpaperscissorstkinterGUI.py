# game with GUI

from Tkinter import *
from ttk import *
import random

root = Tk() # sets up root window
root.title ('Rock Paper Scissors') # adds title to the window 'Rock Paper Scissors'

mainframe = Frame(root, padding = '3 3 12 12') # sets up space between frame and window
mainframe.grid(column=0, row = 0, sticky=(N,W,E,S)) # choose grid layout, sticky uses Cardinal directions
mainframe.columnconfigure(0, weight=1) 
mainframe.rowconfigure(0,weight=1)

Label(mainframe, text='Player').grid(column=1, row = 1, sticky = W) 

# label - method to display text on window 
# mainframe - where the widget will go, in this case the mainframe
# text = 'Player' - input text for label
# grid - indicates the use of the grid system (row and column)
# sticky = W - text will be aligned with left side of window (West)

root.mainloop() # tells computer to run GUI
