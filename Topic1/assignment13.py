from tkinter import *
from tkinter import ttk
import csv

root = Tk()

# Set window configuration
root.geometry("400x200")
root.title("Topic 1 - Assignment 13")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Body
student_name_label = ttk.Label(frm, text="Student Name: ")
student_name_box = Text(frm, width=25, height=1)
course_label = ttk.Label(frm, text="Course: ")
course_box = Text(frm, width=25, height=1)
institute_label = ttk.Label(frm, text="Institute: ")
institute_box = Text(frm, width=25, height=1)
fees_label = ttk.Label(frm, text="Fees: ")
fees_box = Text(frm, width=25, height=1)

student_name_label.grid(column=0, row=0)
student_name_box.grid(column=1, row=0)
course_label.grid(column=0, row=1)
course_box.grid(column=1, row=1)
institute_label.grid(column=0, row=2)
institute_box.grid(column=1, row=2)
fees_label.grid(column=0, row=3)
fees_box.grid(column=1, row=3)

students = []


def process_data():
    file = open('assignment13.csv', 'a')

    writer = csv.writer(file)
    for student in students:
        writer.writerow(student)

    file.close()


def add_student():
    name = student_name_box.get("1.0", END).strip('\n')
    course = course_box.get("1.0", END).strip('\n')
    institute = institute_box.get("1.0", END).strip('\n')
    fees = float(fees_box.get("1.0", END))
    data = [name, course, institute, str(fees)]

    students.append(data)


add_button = ttk.Button(
    frm, text="Add", command=add_student).grid(column=1, row=4)

button = ttk.Button(frm, text="Save all",
                    command=process_data).grid(column=1, row=5)

root.mainloop()
