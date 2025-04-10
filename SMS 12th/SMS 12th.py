import tkinter as tk

from tkinter.filedialog import *
import tkinter.messagebox
import mysql.connector as m
from PIL import ImageTk, Image

con=m.connect(host='localhost',user='root',passwd='arnav10126') 
cur=con.cursor()
cur.execute('create database if not exists school')
cur.execute('use school')
cur.execute('create table if not exists students(adm int(5) primary key, name varchar(30), class varchar(3), phone int(10))')
con.commit()
con.close()

# connect() will connect to the sql database 
def connect():
    try:
        con=m.connect(host='localhost',user='root',passwd='arnav10126',database='school')
    except:
        print("cannot connect to database")
    return con

# to ensure all details are filled        
def verify_txtbox():
    a=b=c=d=0
    if not name.get():
        a=1
    if not Class.get():
        b=1
    if not adm.get():
        c=1
    if not phone.get():
        d=1
    if a==1 or b==1 or c==1 or d==1:
        return 1
    else:
        return 0

# to add record of a student to the database
def add_student(a,n,c,p):
    ver=verify_txtbox()
    if ver==0:
        con=connect()
        cur=con.cursor()
        cur.execute('create table if not exists students(adm int primary key, name varchar(50), class varchar(5), phone int(10))')
        cur.execute('insert into students(adm, name, class, phone) values (%s,%s,%s,%s)',(a,n,c,p))    
        cur.execute('select * from students')
        data=cur.fetchall()
        txt_adm.delete("1.0","end")
        txt_name.delete("1.0","end")
        txt_class.delete("1.0","end")
        txt_phone.delete("1.0","end")
        for i in data:
            txt_adm.insert(END,' '+str(i[0])+'\n')
            txt_adm.insert(END,'---------\n')
            txt_name.insert(END,' '+str(i[1])+'\n')
            txt_name.insert(END,'------------------------------------------------\n')
            txt_class.insert(END,' '+str(i[2])+'\n')
            txt_class.insert(END,'------\n')
            txt_phone.insert(END,' '+str(i[3])+'\n')
            txt_phone.insert(END,'-----------------\n')
        con.commit()
        con.close()
        txt1.delete("1.0","end")
        txt1.insert(END,'Student Data Added Successfully\n')
    else:
        tk.messagebox.showinfo('Field Empty','Please Enter All The Details')

# to delete a student record from the database
def del_student():
    con=connect()
    cur=con.cursor()
    if not tadm.get():
        tk.messagebox.showinfo('Field Empty','Please Enter Adm No.')
    else:
        cur.execute('select * from students')
        data=cur.fetchall()
        l=[]
        for j in data:
            l.append(int(j[0]))
        
        for i in data:
            if int(tadm.get()) in l:
                cur.execute("delete from students where adm=%s",(tadm.get(),)) 
                txt1.delete("1.0","end")
                txt1.insert(END,'Student Data Deleted Successfully\n')
                cur.execute('select * from students')
                data=cur.fetchall()
                txt_adm.delete("1.0","end")
                txt_name.delete("1.0","end")
                txt_class.delete("1.0","end")
                txt_phone.delete("1.0","end")
                for i in data:
                    txt_adm.insert(END,' '+str(i[0])+'\n')
                    txt_adm.insert(END,'---------\n')
                    txt_name.insert(END,' '+str(i[1])+'\n')
                    txt_name.insert(END,'------------------------------------------------\n')
                    txt_class.insert(END,' '+str(i[2])+'\n')
                    txt_class.insert(END,'------\n')
                    txt_phone.insert(END,' '+str(i[3])+'\n')
                    txt_phone.insert(END,'-----------------\n')
            else:
                txt1.delete("1.0","end")
                txt1.insert(END,'No Such Student Exists')
    con.commit()
    con.close()

# to update a student record in the database        
def update_student(a,n,c,p):
    ver=verify_txtbox()
    if ver==0:
        con=connect()
        cur=con.cursor()
        cur.execute("update students set name=%s where adm=%s",(n,a))
        cur.execute("update students set class=%s where adm=%s",(c,a))
        cur.execute("update students set phone=%s where adm=%s",(p,a))
        con.commit()
        cur.execute('select * from students')
        data=cur.fetchall()
        txt1.delete("1.0","end")
        txt1.insert(END,'Student Data Updated Successfully :\n')
        txt_adm.delete("1.0","end")
        txt_name.delete("1.0","end")
        txt_class.delete("1.0","end")
        txt_phone.delete("1.0","end")
        for i in data:
            txt_adm.insert(END,' '+str(i[0])+'\n')
            txt_adm.insert(END,'---------\n')
            txt_name.insert(END,' '+str(i[1])+'\n')
            txt_name.insert(END,'------------------------------------------------\n')
            txt_class.insert(END,' '+str(i[2])+'\n')
            txt_class.insert(END,'------\n')
            txt_phone.insert(END,' '+str(i[3])+'\n')
            txt_phone.insert(END,'-----------------\n')
        con.close()
    else:
        tk.messagebox.showinfo('Field Empty','Please Enter All The Details')

# to clear all input text boxes
def clear():
    tname.delete(0,END)
    tclass.delete(0,END)
    tadm.delete(0,END)
    tph.delete(0,END)

def clear_results():
    txt_adm.delete('0.0','end')
    txt_name.delete('0.0','end')
    txt_class.delete('0.0','end')
    txt_phone.delete('0.0','end')
    
# to view the list of all students
def student_list():
    clear_results()
    con=connect()
    cur=con.cursor()
    cur.execute('select * from students')
    data=cur.fetchall()
    con.close()
    txt1.delete("1.0","end")
    txt1.insert(END,'Student List :\n')
    for i in data:
        txt_adm.insert(END,' '+str(i[0])+'\n')
        txt_adm.insert(END,'---------\n')
        txt_name.insert(END,' '+str(i[1])+'\n')
        txt_name.insert(END,'------------------------------------------------\n')
        txt_class.insert(END,' '+str(i[2])+'\n')
        txt_class.insert(END,'------\n')
        txt_phone.insert(END,' '+str(i[3])+'\n')
        txt_phone.insert(END,'-----------------\n')

# to scroll through the list of records
def multiple_scroll(*args):
    txt_adm.yview(*args)
    txt_name.yview(*args)
    txt_class.yview(*args)
    txt_phone.yview(*args)

# to search a name/adm
def search_record(s):
    con=connect()
    cur=con.cursor()
    cur.execute('select * from students')
    data=cur.fetchall()
    clear_results()
    C1=0
    C2=0
    C3=0
    for i in data:
        if str(i[0])==str(s):
            C1+=1
            txt_adm.insert(END,' '+str(i[0])+'\n')
            txt_adm.insert(END,'---------\n')
            txt_name.insert(END,' '+str(i[1])+'\n')
            txt_name.insert(END,'------------------------------------------------\n')
            txt_class.insert(END,' '+str(i[2])+'\n')
            txt_class.insert(END,'------\n')
            txt_phone.insert(END,' '+str(i[3])+'\n')
            txt_phone.insert(END,'-----------------\n')
        if str(i[1])==str(s):
            C2+=1
            txt_adm.insert(END,' '+str(i[0])+'\n')
            txt_adm.insert(END,'---------\n')
            txt_name.insert(END,' '+str(i[1])+'\n')
            txt_name.insert(END,'------------------------------------------------\n')
            txt_class.insert(END,' '+str(i[2])+'\n')
            txt_class.insert(END,'------\n')
            txt_phone.insert(END,' '+str(i[3])+'\n')
            txt_phone.insert(END,'-----------------\n')
        if str(i[2])==str(s):
            C3+=1
            txt_adm.insert(END,' '+str(i[0])+'\n')
            txt_adm.insert(END,'---------\n')
            txt_name.insert(END,' '+str(i[1])+'\n')
            txt_name.insert(END,'------------------------------------------------\n')
            txt_class.insert(END,' '+str(i[2])+'\n')
            txt_class.insert(END,'------\n')
            txt_phone.insert(END,' '+str(i[3])+'\n')
            txt_phone.insert(END,'-----------------\n')
    txt1.delete("1.0","end")
    txt1.insert(END,'Search Results :\n')
    if C1==0 and C2==0 and C3==0:
        txt1.delete("1.0","end")
        txt1.insert(END,'No Such Student Exists\n')
    con.commit()
    con.close()

# Creating a window
win = Tk()
win.resizable(False,False)
win.title("Student Management System")
win.geometry("1250x640")
win.config(bg="#8DEBF6")

image=Image.open(r'board.jpg')  
img=image.resize((560, 570),Image.Resampling.LANCZOS)
my_img=ImageTk.PhotoImage(img)
label_img1=Label(win, image=my_img)
label_img1.place(x=8,y=50)

name=StringVar()
Class=StringVar()
adm=StringVar()
phone=StringVar()
search=StringVar()

bg1=Canvas(bg='#F9F9F9',width=650,height=570)
bg1.place(x=580,y=50)

txt1=Text(win,bg='white',width=69,height=1,fg='black',font=('arial',13))
txt1.place(x=593,y=100)

txt_adm_label=Label(win, text='Adm No',width=7,height=1,font=10,fg='white',bg='#147244')
txt_adm_label.place(x=595,y=130)

scroll1=Scrollbar(win) # creating a scrollbar
scroll1.pack(side=RIGHT,fill=Y)

txt_adm=Text(win,bg='white',yscrollcommand=scroll1.set,wrap='none',width=6,height=19,fg='black',font=('arial',15))
txt_adm.place(x=596,y=170)
txt_adm.tag_configure('tag_name',justify='center')

txt_name_label=Label(win, text='Name',width=38,height=1,font=10,fg='white',bg='#147244')
txt_name_label.place(x=673,y=130)
txt_name=Text(win,bg='white',width=31,height=19,fg='black',font=('arial',15),yscrollcommand=scroll1.set,wrap='none')
txt_name.place(x=675,y=170)
txt_name.tag_configure('tag_name',justify='center')

txt_class_label=Label(win, text='Class',width=5,height=1,font=10,fg='white',bg='#147244')
txt_class_label.place(x=1028,y=130)
txt_class=Text(win,bg='white',width=4,height=19,fg='black',font=('arial',15),yscrollcommand=scroll1.set,wrap='none')
txt_class.place(x=1030,y=170)
txt_class.tag_configure('tag_name',justify='center')

txt_phone_label=Label(win, text='Phone No',width=13,height=1,font=10,fg='white',bg='#147244')
txt_phone_label.place(x=1090,y=130)
txt_phone=Text(win,bg='white',width=11,height=19,fg='black',font=('arial',15),yscrollcommand=scroll1.set,wrap='none')
txt_phone.place(x=1090,y=170)
txt_phone.tag_configure('tag_name',justify='center')

scroll1.config(command=multiple_scroll)

label=Label(win,width=70,anchor='center',text="   Student  Management  System     ",font=("Exo Demi Bold",25),bg='#7abed8',fg='black')
label.place(x=0,y=0)

# creating input text boxes
nameLabel=Label(win,text="     Name :    ",font=10,fg='white',height=1,bg='#3a6b4e')
nameLabel.place(x=80,y=100)
tname=Entry(win,textvariable=name,width=30,font=('arial',13))
tname.place(x=240,y=105)

classLabel=Label(win,text="  Class/Sec : ",font=10,fg='white',bg='#3a6b4e')
classLabel.place(x=80,y=135)
tclass=Entry(win,textvariable=Class,width=30,font=('arial',13))
tclass.place(x=240,y=140)

admLabel=Label(win,text="   Adm No :   ",font=10,fg='white',bg='#3a6b4e')
admLabel.place(x=80,y=170)
tadm=Entry(win,textvariable=adm,width=30,font=('arial',13))
tadm.place(x=240,y=175)

phLabel=Label(win,text="  Phone No :  ",font=10,fg='white',bg='#3a6b4e')
phLabel.place(x=80,y=205)
tph=Entry(win,textvariable=phone,width=30,font=('arial',13))
tph.place(x=240,y=210)

searchLabel=Label(win,text='Search',font=10,height=1)
searchLabel.place(x=590,y=60)
tsearch=Entry(win,textvariable=search,width=55,font=('arial',13),bg='white',fg='black')
tsearch.place(x=670,y=65)

# creating buttons
search=Image.open(r'search button.jpg') 
search=search.resize((35,30),Image.Resampling.LANCZOS)
img1=ImageTk.PhotoImage(search)
label=Label(win,image=img1)
search_button=Button(win,width=35,height=30,image=img1,command=lambda:[search_record(tsearch.get())])
search_button.place(x=1180,y=57)

add_button=Button(win,command=lambda:[add_student(adm.get(),name.get(),Class.get(),phone.get())],text=' Add Student ',width=16,bg='#347849',fg='white',bd=3,font='arial')
add_button.place(x=80,y=300)

delete_button=Button(win,command=lambda:[del_student()],text='Delete Student',width=16,bg='#347849',fg='white',bd=3,font='arial')
delete_button.place(x=320,y=300)

update_button=Button(win, command=lambda:[update_student(adm.get(),name.get(),Class.get(),phone.get())],text='Update Student',width=16,bg='#347849',fg='white',bd=3,font='arial')
update_button.place(x=320,y=350)

clear_button=Button(win,command=lambda:[clear()],text='Clear',width=16,bg='#347849',fg='white',bd=3,font='arial')
clear_button.place(x=80,y=350)

close_button=Button(win,text='Exit',command=win.destroy,width=16,bg='#347849',fg='white',bd=3,font='arial')
close_button.place(x=80,y=400)

view_button=Button(win,text='View List',command=lambda:[student_list()],width=16,bg='#347849',fg='white',bd=3,font='arial')
view_button.place(x=320,y=400)

win.mainloop()