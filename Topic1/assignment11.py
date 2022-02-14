from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
root = Tk()

# Set window configuration
root.geometry("300x150")
root.title("Topic 1 - Assignment 11")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
width_label = ttk.Label(frm, text="Width: ")
width_box = Text(frm, width=25, height=1)
height_label = ttk.Label(frm, text="Height: ")
height_box = Text(frm, width=25, height=1)
length_label = ttk.Label(frm, text="length: ")
length_box = Text(frm, width=25, height=1)

width_label.grid(column=0, row=0)
width_box.grid(column=1, row=0)
height_label.grid(column=0, row=1)
height_box.grid(column=1, row=1)
length_label.grid(column=0, row=2)
length_box.grid(column=1, row=2)


volume_text = StringVar()
volume_text.set("Volume: ")
volume_label = ttk.Label(frm, textvariable=volume_text)
volume_label.grid(column=0, row=5)

tsa_text = StringVar()
tsa_text.set("TSA: ")
tsa_label = ttk.Label(frm, textvariable=tsa_text)
tsa_label.grid(column=0, row=6)


def put_text():
    width = int(width_box.get("1.0", END))
    height = int(height_box.get("1.0", END))
    length = int(length_box.get("1.0", END))
    volume_text.set("Area: " + str(width*height*length))
    tsa_text.set("TSA: " + str((2*length*height) +
                 (2*length*width) + (2*width*height)))


button = ttk.Button(frm, text="Calculate",
                    command=put_text).grid(column=1, row=3)

root.mainloop()
