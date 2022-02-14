from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("400x200")
root.title("Topic 1 - Assignment 1")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Button").grid(column=0, row=0)
root.mainloop()
