from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text= "Look I clicked")
    myLabel.pack()

# Creating the button (pack version)
myButton0 = Button(root, text="Click me!", padx=50, pady=50, command= myClick)
myButton0.pack()

# Creating the button (grid version)
# myButton0 = Button(root, text="Click me!").grid(row=0, column=0)
# myButton1 = Button(root, text="Click me now!").grid(row=0, column=1)
# myButton2 = Button(root, text="Good job").grid(row=1, column=0)
# myButton3 = Button(root, text="Buddy boy").grid(row=1, column=1)

root.mainloop()