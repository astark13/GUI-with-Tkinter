from tkinter import *

# Create an empty Tkinter window
window=Tk()               

def kg_to_others():
    # Get user value from input box and multiply by 1000 to get kilograms
    grams=float(e1_value.get())*1000 
    # Empty the Text box if they had text from the previous use and fill them again           
    t1.delete("1.0",END)
    # Fill in the text box with the value of gram variable
    t1.insert(END,grams)            

    # Get user value from input box and multiply by 2.20462 to get pounds
    pounds=float(e1_value.get())*2.20462  
    t2.delete("1.0",END)          
    t2.insert(END,pounds) 
    
    # Get user value from input box and multiply by 35.274 to get ounces
    ounces=float(e1_value.get())*35.274  
    t3.delete("1.0",END)         
    t3.insert(END,ounces)                      

# Create a Label widget with "Kg" as label
l1=Label(window, text="Kg")
l1.grid(row=0,column=0)       # The Label is placed in position 0, 0 in the window

e1_value=StringVar()                      # Create a special StringVar object    
e1=Entry(window,textvariable=e1_value)    # Create an Entry box for users to enter the value     
e1.grid(row=0,column=1)

# Create a button widget
# The kg_to_others() function is called when the button is pushed
b1=Button(window,text="Convert",command=kg_to_others)
b1.grid(row=0,column=2)

l2=Label(window, text="Grams")
l2.grid(row=1,column=0)

# Create empty text box
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

l3=Label(window, text="Pounds")
l3.grid(row=1,column=2)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=3)

l4=Label(window, text="Ounces")
l4.grid(row=1,column=4)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=5)

# This makes sure to keep the main window open
window.mainloop()         
