from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("400x200")
root.title("Topic 1 - Assignment 3")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
comboBox = ttk.Combobox(
    frm, values=["first", "second", "third"], postcommand=None).grid(column=1, row=1)


root.mainloop()
