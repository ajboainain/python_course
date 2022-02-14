from tkinter import *
from tkinter import ttk
root = Tk()

# Set window configuration
root.geometry("500x200")
root.title("Topic 1 - Assignment 6")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()


# Body
text_box_label = ttk.Label(frm, text="Text box: ").grid(column=0, row=0)
text_box = Text(frm, width=50, height=5)
text_box.grid(column=1, row=0)
text_box.insert(index="1.0", chars="12345")
text_box.get("1.0", END)


def delete_first_last():
    text = text_box.get("1.0", END)[1:-2]
    text_box.replace("1.0", END, text)


delete_first_last_btn = ttk.Button(
    frm, text="Trim", command=delete_first_last).grid(column=1, row=1)
root.mainloop()
