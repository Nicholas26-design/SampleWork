from tkinter import *

root = Tk()

# Creating the widget and putting it onto screen
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Nick").grid(row=1, column =4)
myLabel3 = Label(root, text="Last name Kenney").grid(row=1, column =5)


root.mainloop()