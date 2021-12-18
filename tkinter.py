#creating a button 
'''from tkinter import *

root = Tk()
mybutton = Button(root, text="click me  ", state=DISABLED)

mybutton.pack()
root.mainloop()
'''
#to get a output from a button
'''from tkinter import *
root= Tk()
def ok():
     b=Label(root , text = "you have clicked a button ")
     b.pack()
    
button=Button(root , text="click me",command=ok,fg="red",bg="black")
button.pack()

root.mainloop()
'''
# to create a input field
'''
from tkinter import  *
root = Tk()

e = Entry(root, width=50,borderwidth=5,fg="red",bg="black")
e.pack()
def ok():
    hello="hello " + e.get()
    b= Label(root,text=hello)
    b.pack()
button= Button(root, text="Enter your name " , command=ok, fg="red", bg="black")
button.pack()
root.mainloop()
'''
#one more example of input feild 
'''
from tkinter import *
root=Tk()
e = Entry(root,width=50,borderwidth=9,fg="black",bg="red")
e.pack()
e.insert(0,  "enter your name: ")

def ok():
    hello="hello " + e.get()
    b=Label(root, text=hello)
    b.pack()
button=Button(root, text="click",command=ok,bg="black",fg="red")
button.pack()
root.mainloop()
'''
#no need to see
'''
from tkinter import*
root=Tk()
e= Entry(root)
e.pack()
e.insert(0, "mc")
def o():
    h= "hi " + e.get()
    b=Label(root,text=h)
    b.pack()
buttons=Button(root,text="mn",command=o)
buttons.pack()
root.mainloop()
'''
# calculator
from tkinter import *
from math import *
root=Tk()
root.title=("Simple Calculator")
e=Entry(root, width=100, borderwidth=9, fg="red", bg="black")
e.grid(row=0, column=0 , columnspan=4,padx=10,pady=10 )

def button_click(number):
      current= e.get() 
      e.delete(0, END)
      e.insert(0, str(current)+str(number))

def button_clear():
      e.delete(0, END)

def button_add():
       first_number=e.get()
       global f_num
       global math
       math= "addition"
       f_num= int(first_number)
       e.delete(0, END)
def button_subtract():
      first_number = e.get()
      global f_num
      global math
      math= "subtraction"
      f_num=int(first_number)
      e.delete(0, END)
      
def button_multiplication():
      first_number=e.get()
      global f_num
      global math
      math = "multiplication"
      f_num=int(first_number)
      e.delete(0, END)
      
def button_division():
      first_number=e.get()
      global f_num
      global math
      math = "division"
      f_num=int(first_number)
      e.delete(0, END)

      
def button_equal():
       second_number=e.get()
       
       e.delete(0, END)
       if math=="addition":
                   e.insert(0, f_num +int(second_number))
       elif math=="subtraction" :
                   e.insert(0, f_num - int(second_number) )
       elif math=="multiplication" :
                    e.insert(0, f_num * int(second_number))
       elif math=="division":
                      e.insert(0, f_num / int(second_number))       

button_1=Button(root,text="1",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(7)) 
button_8=Button(root,text="8",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(9))
button_10=Button(root,text="0",fg="red",bg="black",padx=110,pady=20,command=lambda: button_click(0))

button_add=Button(root,text="+",fg="red",bg="black",padx=110,pady=20,command=button_add)
button_subtract=Button(root,text="-",fg="red",bg="black",padx=110,pady=20,command=button_subtract)
button_mutliplication=Button(root,text="*",fg="red",bg="black",padx=115,pady=20,command=button_multiplication)
button_divison=Button(root,text="/",fg="red",bg="black",padx=110,pady=20,command=button_division)
button_equal=Button(root,text="=",fg="red",bg="black",padx=130,pady=20,command=button_equal)
button_clr=Button(root,text="clr",fg="red",bg="black",padx=110,pady=20,command=button_clear)

button_1.grid(row=3 , column=0)
button_2.grid(row= 3, column= 1)
button_3.grid(row= 3, column= 2)
button_4.grid(row=2 , column= 0)
button_5.grid(row= 2, column= 1)
button_6.grid(row= 2, column= 2)
button_7.grid(row= 1, column= 0)
button_8.grid(row= 1, column= 1)
button_9.grid(row=  1, column= 2)
button_10.grid(row= 4, column=0 )

button_add.grid(row=1 ,column=3)
button_subtract.grid(row=2 ,column=3)
button_mutliplication.grid(row=3 ,column=3)
button_divison.grid(row=4 ,column=1)
button_equal.grid(row=5 ,column=1, columnspan=2)
button_clr.grid(row=4 ,column=2)



