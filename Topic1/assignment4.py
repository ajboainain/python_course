from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("400x200")
root.title("Topic 1 - Assignment 4")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
check_button_label = ttk.Label(
    frm, text="Check button: ").grid(column=0, row=0)
check_button = ttk.Checkbutton(frm).grid(column=0, row=1)


root.mainloop()
