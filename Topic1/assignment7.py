from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("350x100")
root.title("Topic 1 - Assignment 7")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()


# Body
text_box1_label = ttk.Label(frm, text="Text box 1: ")
text_box1 = Text(frm, width=25, height=1)
text_box2_label = ttk.Label(frm, text="Text box 2: ")
text_box2 = Text(frm, width=25, height=1)
text_box3_label = ttk.Label(frm, text="Text box 3: ")
text_box3 = Text(frm, width=25, height=1)

text_box1_label.grid(column=0, row=0)
text_box1.grid(column=1, row=0)
text_box2_label.grid(column=0, row=1)
text_box2.grid(column=1, row=1)
text_box3_label.grid(column=0, row=2)
text_box3.grid(column=1, row=2)

accept_text = StringVar()
accept_text.set("")
accept_label = ttk.Label(frm, textvariable=accept_text)
accept_label.grid(column=0, row=5)


def put_text():
    text1 = text_box1.get("1.0", END).strip("\n")
    text2 = text_box2.get("1.0", END).strip("\n")
    text3 = text_box3.get("1.0", END).strip("\n")
    accept_text.set(text1 + text2 + text3)


button = ttk.Button(frm, text="idk", command=put_text).grid(column=1, row=3)


root.mainloop()
