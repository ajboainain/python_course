from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
root = Tk()

# Set window configuration
root.geometry("690x420")
root.title("Topic 1 - Assignment 9")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body

stext = ScrolledText(frm)
stext.grid(column=0, row=0)
root.mainloop()
