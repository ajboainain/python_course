from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("300x150")
root.title("Topic 1 - Assignment 8")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
radio_button1 = ttk.Radiobutton(frm).grid(column=0, row=0)
radio_button2 = ttk.Radiobutton(frm).grid(column=1, row=0)
radio_button3 = ttk.Radiobutton(frm).grid(column=2, row=0)


root.mainloop()
