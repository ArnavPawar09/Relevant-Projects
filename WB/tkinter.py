"""
Tkinter
"""

from tkinter import *

# -> Creating a window 

window = Tk() 
window.geometry("700x500") # size of the window
window.title("Example") # Title displayed at top left

# -> Background 

window.config(background = "white") # can also use HEX values for colours

# -> Creating Labels & customisations

label = Label(window,
              text = "Hello World",
              font = ('Aerial',20,'bold'),
              fg = 'yellow',
              bg='black',
              relief = RAISED, # border, Can also use SUNKEN
              bd = 5, # border width
              padx = 50, # space b/w text and x axis
              pady = 50) # space b/w text and y axis

label.pack() # shows label at top center by default
label.place(x=0, y=0) # shows label at a given position


window.mainloop() # show the window, Listen for events


