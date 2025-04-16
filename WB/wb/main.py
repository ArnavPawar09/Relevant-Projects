"""
White Board
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

#-----------------------------------------
# -> CREATING A WINDOW
win = Tk()
win.resizable(False, False)
win.title("White Board")
win.geometry("1260x640")
win.config(background = "#f2f3f5")

current_x = 0
current_y = 0
COLOR = "black"
    
#--------------------------------------------
# -> Defining functions
def position(work) :
    global current_x, current_y
    
    current_x = work.x
    current_y = work.y
    
def Line(work):
    global current_x, current_y
    
    area.create_line((current_x, current_y, work.x, work.y), width = get_currentValue(),
                     fill = COLOR,capstyle=ROUND, smooth=TRUE)
    current_x, current_y = work.x, work.y
    
def showColor(new):
    global COLOR 
    
    COLOR = new

def clear():
    area.delete("all")
    color_list()
    area.config(bg="white")
    
def bg():
    global COLOR
    
    page_color=COLOR
    area.config(bg=page_color)
    
#------------------------------------------------
# -> COLOR PALETTE
color = Canvas(win, bg = "#c4cccf", width = 40, height = 500)
color.place(x = 30, y = 30)

def color_list():
    id = color.create_rectangle((8,8,35,35), fill = "black")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("black"))
    
    id = color.create_rectangle((8,40,35,68), fill = "gray")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("gray"))
    
    id = color.create_rectangle((8,73,35,101), fill = "brown")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("brown"))
    
    id = color.create_rectangle((8,105,35,134), fill = "red")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("red"))
    
    id = color.create_rectangle((8,138,35,167), fill = "orange")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("orange"))
    
    id = color.create_rectangle((8,171,35,200), fill = "yellow")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("yellow"))
    
    id = color.create_rectangle((8,204,35,233), fill = "green")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("green"))
    
    id = color.create_rectangle((8,237,35,266), fill = "blue")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("blue"))
    
    id = color.create_rectangle((8,271,35,299), fill = "purple")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("purple"))
    
    id = color.create_rectangle((8,303,35,332), fill = "white")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("white"))
    
color_list() # Shows the color list at left side

#-------------------------------------------------
# -> ERASER BUTTON
Button(win,width=3,height=2, bd=6,text="clear",fg="black",bg="#f2f3f5",
       command = clear).place(x = 32, y = 500)


#-----------------------------------------------
# -> Background fill button
Button(win,text="BG",fg="black",width=3,height=2,bd=6, relief=RAISED,
       bg="#f2f3f5", command=bg).place(x=32, y=450)

#---------------------------------------------
# -> DRAWING AREA
area = Canvas(win, width = 1147, height = 580, bg = "white", cursor = "hand1")
area.place(x = 100, y = 8)

area.bind("<Button-1>", position)
area.bind("<B1-Motion>", Line)

#----------------------------------------
# -> Thickness slider
currentValue = tk.DoubleVar()

def get_currentValue():
    return '{: .2f}'.format(currentValue.get())

def slider_value(event):
    value.config(text=get_currentValue())
    
slider = ttk.Scale(win, from_=1,to=100,orient='horizontal',command=slider_value,variable=currentValue)
slider.place(x=70,y=600)

value=ttk.Label(win,text=get_currentValue())
value.place(x=170,y=603)

#-----------------------------------------
win.mainloop() # This shows the window


