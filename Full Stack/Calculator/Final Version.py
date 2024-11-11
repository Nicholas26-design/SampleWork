# Library import
from tkinter import *

# sets up the main window for your Tkinter application, allowing you to add and manage other GUI elements within it.
root = Tk()
# Gives the window a title.
root.title("Simple Calculator")

# Defining the entry window
e = Entry(root, width=35, borderwidth=5)
# Placing the entry window on the grid
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

"""
Creates and places a Label widget in the Tkinter application.

The Label widget is used to display the current operation or expression being entered by the user.
It provides visual feedback, showing the ongoing calculation.

Attributes:
    root (Tk): The parent window where the label will be placed.
    text (str): The initial text of the label, set to an empty string.
    anchor (str): Aligns the text to the right (east) side of the label.
    width (int): Sets the width of the label.

Grid Placement:
    row (int): Places the label in the second row (indexing starts at 0).
    column (int): Places the label in the first column.
    columnspan (int): The label spans across four columns.
"""
operation_label = Label(root, text="", anchor="e", width=35)
operation_label.grid(row=1, column=0, columnspan=4)


# Addresses storage
# Global variables to store the current operation and the first number
current_operation = ""
expression = ""

# Creation and definition of functions used in the software.
def button_click(number):
    """
    Handles the event when a number button is clicked.

    Appends the clicked number to the current expression and updates the entry widget and operation label.

    Args:
        number (int): The number that was clicked.
    """
    global expression
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    expression += str(number)
    operation_label.config(text=expression)

def button_clear():
    """
    Clears the entry widget and the current expression.

    Resets the entry widget and operation label to an empty state.
    """
    e.delete(0, END)
    global expression
    expression = ""
    operation_label.config(text="")

def button_operation(operation):
    """
    Handles the event when an operation button is clicked.

    Appends the clicked operation to the current expression and updates the operation label.

    Args:
        operation (str): The operation that was clicked (e.g., '+', '-', '*', '/').
    """
    global expression
    current = e.get()
    e.delete(0, END)
    expression += operation
    operation_label.config(text=expression)

def button_equal():
    """
    Evaluates the current expression and displays the result.

    Tries to evaluate the expression using the eval function. If successful, updates the entry widget and operation label with the result.
    If an error occurs, displays an error message.
    """
    global expression
    try:
        result = eval(expression)
        e.delete(0, END)
        e.insert(0, result)
        operation_label.config(text=f"{expression} = {result}")
        expression = str(result)
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")
        operation_label.config(text="Error")
        expression = ""

# Define buttons used in UI.
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=4, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=4, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=4, column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=3, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=3, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=3, column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=2, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=2, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=2, column=2)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=5, column=0)

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operation("+")).grid(row=2, column=3)
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: button_operation("-")).grid(row=3, column=3)
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operation("*")).grid(row=4, column=3)
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_operation("/")).grid(row=5, column=3)

button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal).grid(row=5, column=1, columnspan=2)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear).grid(row=6, column=0, columnspan=2)

# Starts the event loop, keeps the window open, and handles user interactions
root.mainloop()
