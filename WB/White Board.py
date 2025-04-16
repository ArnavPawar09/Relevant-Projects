"""
White Board
"""

import pyautogui 
import tkinter as Tk


#-----------------------------------------
# -> CREATING A WINDOW
win = Tk()
win.resizable(True, True)
win.title("White Board")
win.geometry("1593x900")
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

def take_ss():
    screenshot = pyautogui.screenshot()
    path = asksaveasfilename()
    screenshot.save(path+"_screenshot.jpeg")

#------------------------------------------------
# -> COLOR PALETTE
color = Canvas(win, bg = "#c4cccf", width = 60, height = 750)
color.place(x = 30, y = 30)

def color_list():
    id = color.create_rectangle((8,8,55,550), fill = "white")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("white"))

    id = color.create_rectangle((8,8,55,495), fill = "purple")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("purple"))

    id = color.create_rectangle((8,8,55,440), fill = "blue")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("blue"))

    id = color.create_rectangle((8,8,55,385), fill = "green")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("green"))

    id = color.create_rectangle((8,8,55,330), fill = "yellow")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("yellow"))

    id = color.create_rectangle((8,8,55,275), fill = "orange")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("orange"))

    id = color.create_rectangle((8,8,55,220), fill = "red")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("red"))

    id = color.create_rectangle((8,8,55,165), fill = "brown")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("brown"))

    id = color.create_rectangle((8,8,55,110), fill = "grey")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("grey"))

    id = color.create_rectangle((8,8,55,60), fill = "black")
    color.tag_bind(id, "<Button-1>", lambda a: showColor("black"))
    
color_list() # Shows the color list at left side

#-------------------------------------------------
# -> CLEAR BUTTON
Button(win,width=4,height=2, bd=6,text="clear",fg="black",bg="#f2f3f5",
       command = clear).place(x = 32, y = 630)


#-----------------------------------------------
# -> Background fill button
Button(win,text="BG",fg="black",width=4,height=2,bd=6, relief=RAISED,
       bg="#f2f3f5", command=bg).place(x=32, y=705)

#---------------------------------------------
# -> DRAWING AREA
area = Canvas(win, width = 1765, height = 945, bg = "white", cursor = "hand1")
area.place(x = 125, y = 16)

area.bind("<Button-1>", position)
area.bind("<B1-Motion>", Line)

#---------------------------------------------
# -> Screenshot Button
Button(win,text="Screenshot",fg="black",width=9,height=1,bd=6,bg="#f2f3f5",
       relief=RAISED, command=take_ss).place(x=10,y=870)

#----------------------------------------
# -> Thickness slider
currentValue = tk.DoubleVar()

def get_currentValue():
    return '{: .2f}'.format(currentValue.get())

def slider_value(event):
    value.config(text=get_currentValue())

slider = ttk.Scale(win, from_=1,to=100,orient='horizontal',command=slider_value,variable=currentValue)
slider.place(x=15,y=800)

value=ttk.Label(win,text=get_currentValue())
value.place(x=15,y=820)

#-----------------------------------------
             # This shows the window

