from tkinter import *
from tkinter import ttk
import csv

root = Tk()

# Set window configuration
root.geometry("900x640")
root.title("Topic 1 - Assignment 14")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
data = []

columns = ('name', 'course', 'institute', 'fees')

tree = ttk.Treeview(root, columns=columns, show='headings')

tree.heading('name', text='Name')
tree.heading('course', text='Course')
tree.heading('institute', text='Institute')
tree.heading('fees', text='Fees')

tree.grid(column=0, row=0, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')


def grab_data():

    with open('assignment13.csv') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            name = row['name']
            course = row['course']
            institute = row['institute']
            fees = row['fees']
            values = (name, course, institute, fees)
            tree.insert("", 0, values=(name, course, institute, fees))


grab_data()

root.mainloop()
