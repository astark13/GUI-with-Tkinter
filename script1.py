from tkinter import *

window=Tk()               # creates the GUI window

def miles_to_km():
    km=float(e1_value.get())*1.6            # the actual content of the e1_value ai avaliable only if the "get" method is applied
    t1.insert(END,km)                       # inserts the value contained by the "miles" variable at the END of the text widget; similar to the append function

b1=Button(window,text="Execute",command=miles_to_km)
b1.grid(row=0,column=0)

e1_value=StringVar()                          
e1=Entry(window,textvariable=e1_value)         # the value entered by the user in the "Entry" filed gets loaded in the e1_value variable
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()         # prevents the window from closing
