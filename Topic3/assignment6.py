import pickle


class Student:

    def __init__(self, name: str, marks: list):
        assert(len(marks) == 3)
        for mark in marks:
            assert(mark <= 100)

        self.name = name
        self.marks = marks

    def total(self):
        total_mark = 0
        for mark in self.marks:
            total_mark += int(mark)
        return total_mark

    def result(self):
        if self.total() >= 120:
            for mark in self.marks:
                if mark <= 35:
                    return "Failed"
            return "Passed"

    def grade(self):
        if self.result() == "Passed":
            if self.total() >= 240:
                return "Outstanding"
            elif self.total() < 240 and self.total() >= 180:
                return "Excellent"
            elif self.total() < 180 and self.total() >= 150:
                return "Good"
            elif self.total() < 150 and self.total() >= 120:
                return "Average"

    def __str__(self):
        if self.result() == "Passed":
            return f'Name: {self.name}\nResult: {self.result()}\nGrade: {self.grade()}'
        else:
            return f'Name: {self.name}\nResult: {self.result()}'


def print_menu():
    print("-------------------------------------")
    print("1. Show all students")
    print("2. Show student report")
    print("3. Add student")
    print("4. Remove student")
    print("5. Save data")
    print("6. Retrieve data")
    print("7. Change mark")
    print("8. Reprint menu")
    print("9. Exit")
    print("-------------------------------------")


students = []


def retrieve_data():
    global students
    save_file = 'savefile'
    file = open(save_file, 'rb')
    students = pickle.load(file)
    file.close()


def save_data():
    save_file = 'savefile'
    file = open(save_file, 'wb')
    pickle.dump(students, file)
    file.close()


def add_student():
    print("Enter student name:")
    name = input(">> ")
    print("Enter mark 1:")
    mark1 = int(input(">> "))
    print("Enter mark 2:")
    mark2 = int(input(">> "))
    print("Enter mark 3:")
    mark3 = int(input(">> "))
    students.append(Student(name, [mark1, mark2, mark3]))


def print_students():
    for i in range(len(students)):
        print(f'#{i} - {students[i].name}')


def student_report():
    print("Enter student number: ")
    index = int(input(">> "))
    if index >= len(students):
        return
    print(students[index])


def remove_student():
    print("Enter student number: ")
    index = int(input(">> "))
    students.remove(students[index])


def change_grade():
    print("Enter student number: ")
    index = int(input(">> "))
    print("Enter mark to change (1, 2, or 3)")
    mark_pos = int(input(">> ")) - 1
    print("Enter new mark for mark #", mark_pos+1)
    mark = int(input(">> "))
    students[index].marks[mark_pos] = mark


print_menu()
while True:
    try:
        selected_option = int(input("[Main]>> "))
    except:
        continue
    if (selected_option > 0 and selected_option < 10):
        if selected_option == 1:
            print_students()
        if selected_option == 2:
            student_report()
        if selected_option == 3:
            add_student()
        if selected_option == 4:
            remove_student()
        if selected_option == 5:
            save_data()
        if selected_option == 6:
            retrieve_data()
        if selected_option == 7:
            change_grade()
        if selected_option == 8:
            print_menu()
        if selected_option == 9:
            break
    else:
        print("Invalid option!")
