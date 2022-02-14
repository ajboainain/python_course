from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("400x200")
root.title("Topic 1 - Assignment 5")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
spin_box_label = ttk.Label(
    frm, text="Spin Box (0-100): ").grid(column=0, row=0)
spin_box = ttk.Spinbox(frm, from_=0, to=100).grid(column=0, row=1)


root.mainloop()
