# 2. Write a Python script to create a GUI-based Calendar application using Tkinter module  that 
#    display the calendar with respect to the year entered by the user.  
#    Note: import Calendar library.

import calendar

from tkinter import *

root = Tk()

firstLabel = Label(root, text="Enter The Year")
firstLabel.grid(row=0, column=0)

inputBox = Entry(root)
inputBox.grid(row=0, column=1)

def click():
    yy = int(inputBox.get())
    for mm in range(1, 13):
        myLabel = Label(root, text = calendar.month(yy, mm), justify=RIGHT)
        if mm in range(1, 5):
            a = 1
            b = mm-1
        elif mm in range(5, 9):
            a = 2
            b = mm-5
        elif mm in range(9, 13):
            a = 3
            b = mm-9
        myLabel.grid(row = a, column = b)

myButton = Button(root, text="Enter", command=click)
myButton.grid(row=0, column=2)

# nov = Label(root, text = calendar.calender(yy, mm), justify=RIGHT)
# nov.grid(row = 0, column=0)

root.mainloop()