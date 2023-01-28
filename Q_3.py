# 3. Write a Python script to create a GUI-based calculator using Tkinter module, which 
#    can perform basic arithmetic operations addition, subtraction, multiplication, and division.


from tkinter import *
import math

root = Tk()

# Name of the Application
root.title("Calculator")

# Entry box
e = Entry(root, width = 50, borderwidth=10)
e.insert(0, "0")

# Defining input buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Defining clear button
def button_clear():
    e.delete(0, END)
    e.insert(0, "0")

# Defining operators

def button_add():
    global e1
    e1 = float(e.get())
    e.delete(0, END)

    #Equals Button need to be defined for every operator
    def button_equals():
        e2 = float(e.get())
        e3 = e1 + e2
        e.delete(0, END)
        e.insert(0, e3)

    equals = Button(root, text = "=", padx = 30, pady = 20, command = button_equals)
    equals.grid(row=5, column=3)

def button_subtract():
    if e.get()=="0":
        e.insert(0, "-")
    else:
        global e1
        e1 = float(e.get())
        e.delete(0, END)

    def button_equals():
        e2 = float(e.get())
        e3 = e1 - e2
        e.delete(0, END)
        e.insert(0, e3)

    equals = Button(root, text = "=", padx = 30, pady = 20, command = button_equals)
    equals.grid(row=5, column=3)

def button_multiply():
    global e1
    e1 = float(e.get())
    e.delete(0, END)

    def button_equals():
        e2 = float(e.get())
        e3 = e1 * e2
        e.delete(0, END)
        e.insert(0, e3)

    equals = Button(root, text = "=", padx = 30, pady = 20, command = button_equals)
    equals.grid(row=5, column=3)

def button_divide():
    global e1
    e1 = float(e.get())
    e.delete(0, END)

    def button_equals():
        e2 = float(e.get())
        e3 = e1 / e2
        e.delete(0, END)
        e.insert(0, e3)

    equals = Button(root, text = "=", padx = 30, pady = 20, command = button_equals)
    equals.grid(row=5, column=3)

def button_reciprocal():
    e1 = float(e.get())
    e.delete(0, END)
    e2 = 1/e1
    e.insert(0, e2)

def button_square():
    e1 = float(e.get())
    e.delete(0, END)
    e2 = e1*e1
    e.insert(0, e2)

def button_root():
    e1 = float(e.get())
    e.delete(0, END)
    e2 = math.sqrt(e1)
    e.insert(0, e2)


b1 = Button(root, text = "1", padx = 30, pady = 20, command = lambda: button_click(1))
b2 = Button(root, text = "2", padx = 30, pady = 20, command = lambda: button_click(2))
b3 = Button(root, text = "3", padx = 30, pady = 20, command = lambda: button_click(3))
b4 = Button(root, text = "4", padx = 30, pady = 20, command = lambda: button_click(4))
b5 = Button(root, text = "5", padx = 30, pady = 20, command = lambda: button_click(5))
b6 = Button(root, text = "6", padx = 30, pady = 20, command = lambda: button_click(6))
b7 = Button(root, text = "7", padx = 30, pady = 20, command = lambda: button_click(7))
b8 = Button(root, text = "8", padx = 30, pady = 20, command = lambda: button_click(8))
b9 = Button(root, text = "9", padx = 30, pady = 20, command = lambda: button_click(9))
b0 = Button(root, text = "0", padx = 30, pady = 20, command = lambda: button_click(0))
decimal = Button(root, text = ".", padx = 32, pady = 20, command = lambda: button_click('.'))
reciprocal = Button(root, text = "1/x", padx = 27, pady = 24, command = button_reciprocal)
square = Button(root, text = "sq", padx = 30, pady = 24, command = button_square)
sq_root = Button(root, text = "rt", padx = 32, pady = 24, command = button_root)

clear = Button(root, text = "C", padx = 28, pady = 20, command = button_clear)
divide = Button(root, text = "÷", padx = 30, pady = 21, command = button_divide)
multiply = Button(root, text = "×", padx = 30, pady = 20, command = button_multiply)
subtract = Button(root, text = "-", padx = 32, pady = 20, command = button_subtract)
add = Button(root, text = "+", padx = 30, pady = 20, command = button_add)


# Arranging the widgets
e.grid(row=0, column=0, columnspan=4)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)

b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b0.grid(row=5, column=1)
clear.grid(row=5, column=0)
divide.grid(row=1, column=3)
multiply.grid(row=2, column=3)
subtract.grid(row=3, column=3)
add.grid(row=4, column=3)
decimal.grid(row=5, column=2)
reciprocal.grid(row=1, column=0)
square.grid(row=1, column=1)
sq_root.grid(row=1, column=2)


root.mainloop()