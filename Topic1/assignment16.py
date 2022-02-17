from re import U
import mysql.connector
from tkinter import *
from tkinter import ttk
import csv

root = Tk()

# Set window configuration
root.geometry("1280x640")
root.title("Topic 1 - Assignment 16")
# Get the frame and set it to grid mode
frm = ttk.Frame(root, padding=10)
frm.grid()

# Connects to the database in TiDB.
db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="Passw0rd123",
    database="topic1"
)
# Creates the database cursor. Prepared statement for security.
cursor = db.cursor(prepared=True)

data = []

added_students = []

columns = ('id', 'name', 'course', 'institute', 'fees')

tree = ttk.Treeview(root, columns=columns, height=20, show='headings')

tree.heading('id', text='ID')
tree.heading('name', text='Name')
tree.heading('course', text='Course')
tree.heading('institute', text='Institute')
tree.heading('fees', text='Fees')

tree.grid(column=0, row=0, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')


def add_students():
    global added_students
    if len(added_students) == 0:
        return
    statement = "INSERT INTO studentInfo VALUES(NULL, %s, %s, %s, %s);"
    for student in added_students:
        tupled_data = tuple(student)
        cursor.execute(statement, tupled_data)
    added_students = []
    db.commit()
    update_tree()


def delete_student():
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        id = (record[0])
        statement = "DELETE FROM studentInfo WHERE id=%s;"
        cursor.execute(statement, (id,))
    db.commit()
    update_tree()


def edit_student():
    next = True
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        id = record[0]
        name = record[1]
        course = record[2]
        institute = record[3]
        fees = record[4]
        edit_students_window(id, name, course, institute, fees)
    update_tree()


def edit_students_window(id, name, course, institute, fees):

    edit_student_window = Toplevel(root)
    edit_student_window.title("Add Student")
    edit_student_window.geometry("400x200")

    student_name_label = ttk.Label(edit_student_window, text="Student Name: ")
    student_name_box = Text(edit_student_window, width=25, height=1)
    student_name_box.insert(index="1.0", chars=name)

    course_label = ttk.Label(edit_student_window, text="Course: ")
    courses = ["CS50", "CS110", "CS150", "CS220", "CS250", "CS444", "CS450"]
    current_course = courses.index(course)
    course_box = ttk.Combobox(
        edit_student_window, values=courses, postcommand=None)
    course_box.current(current_course)

    institute_label = ttk.Label(edit_student_window, text="Institute: ")
    institutes = ["Institute 1", "Institute 2", "Institute 3", "Institute 4"]
    current_institute = institutes.index(institute)
    institute_box = ttk.Combobox(
        edit_student_window, values=institutes, postcommand=None)
    institute_box.current(current_institute)

    fees_label = ttk.Label(edit_student_window, text="Fees: ")
    fees_box = Text(edit_student_window, width=25, height=1)
    fees_box.insert(index="1.0", chars=fees)

    student_name_label.grid(column=0, row=0)
    student_name_box.grid(column=1, row=0)
    course_label.grid(column=0, row=1)
    course_box.grid(column=1, row=1)
    institute_label.grid(column=0, row=2)
    institute_box.grid(column=1, row=2)
    fees_label.grid(column=0, row=3)
    fees_box.grid(column=1, row=3)

    def edit_student():
        statement = "UPDATE studentInfo SET name=%s, course=%s, institute=%s, fees=%s WHERE id=%s"
        updated_info = tuple([student_name_box.get("1.0", END).strip('\n'),
                              course_box.get().strip('\n'),
                              institute_box.get().strip('\n'),
                              fees_box.get("1.0", END).strip('\n'),
                              id])
        cursor.execute(statement, updated_info)
        db.commit()
        update_tree()

    edit_button = Button(edit_student_window, text="Edit Student",
                         command=edit_student)
    edit_button.grid(column=1, row=4)


def update_tree():
    tree.delete(*tree.get_children())
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS studentInfo (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name varchar(30), course varchar(30), institute varchar(30), fees float);")

    cursor.execute("SELECT * from studentInfo;")
    result = cursor.fetchall()
    for row in result:
        tree.insert("", 0, values=row)


def add_students_window():
    global students
    add_student_window = Toplevel(root)
    add_student_window.title("Add Student")
    add_student_window.geometry("400x200")

    student_name_label = ttk.Label(add_student_window, text="Student Name: ")
    student_name_box = Text(add_student_window, width=25, height=1)
    course_label = ttk.Label(add_student_window, text="Course: ")
    course_box = ttk.Combobox(
        add_student_window, values=["CS110", "CS220", "CS250", "CS444", "CS450"], postcommand=None)
    institute_label = ttk.Label(add_student_window, text="Institute: ")
    institute_box = ttk.Combobox(
        add_student_window, values=["Institute 1", "Institute 2", "Institute 3", "Institute 4"], postcommand=None)
    fees_label = ttk.Label(add_student_window, text="Fees: ")
    fees_box = Text(add_student_window, width=25, height=1)

    student_name_label.grid(column=0, row=0)
    student_name_box.grid(column=1, row=0)
    course_label.grid(column=0, row=1)
    course_box.grid(column=1, row=1)
    institute_label.grid(column=0, row=2)
    institute_box.grid(column=1, row=2)
    fees_label.grid(column=0, row=3)
    fees_box.grid(column=1, row=3)

    def add_student():
        global added_students
        name = student_name_box.get("1.0", END).strip('\n').strip('\t')
        course = course_box.get().strip('\n').strip('\t')
        institute = institute_box.get().strip('\n').strip('\t')
        fees = float(fees_box.get("1.0", END))
        data = tuple([name, course, institute, str(fees)])
        added_students.append(data)

    add_button = Button(add_student_window, text="Add Student",
                        command=add_student)
    add_button.grid(column=3, row=4)


add_students_window_button = Button(root,
                                    text="Add Students",
                                    command=add_students_window).place(x=1020, y=0)
execute_additions = Button(
    root, text="Confirm additions", command=add_students).place(x=1020, y=25)
delete_selections = Button(root, text="Delete",
                           command=delete_student).place(x=1020, y=50)
edit_button = Button(
    root, text="Edit", command=edit_student).place(x=1020, y=75)

update_tree()

root.mainloop()
