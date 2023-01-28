# 1. Write a Python script to make a GUI-based GST Tax Finder Calculator which takes  original 
#    cost and net price as an input from the user and display the GST result. Note: Calculate GST 
#    using formula:  
#     GST rate = ((Net Price – original cost) * 100) / original cost 

from tkinter import *

root = Tk()

l1 = Label(root, text = "Original Cost:")
l1.grid(row = 0, column = 0)

input1 = Entry(root)
input1.grid(row=0, column=1)

l2 = Label(root, text = "Net Price:")
l2.grid(row = 1, column = 0)

input2 = Entry(root)
input2.grid(row=1, column=1)

def click():
    oc = int(input1.get())
    np = int(input2.get())
    gst = ((np-oc)*100)/oc
    gstLabel = Label(root, text = f"GST rate = {gst}")
    gstLabel.grid(row=2, column=1)

button = Button(root, text = "Enter", command = click)
button.grid(row = 2, column=0)


root.mainloop()