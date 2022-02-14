from distutils import command
from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("400x200")
root.title("Topic 1 - Assignment 2")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Hello").grid(column=0, row=0)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
