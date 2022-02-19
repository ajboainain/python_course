
import csv


class Employee():

    def __init__(self, emp_name, job, basic_pay, age):
        self.emp_name = emp_name
        self.job = job
        self.basic_pay = float(basic_pay)
        self.age = int(age)

    def hra(self):
        return 0.1 * self.basic_pay

    def da(self):
        return 0.25 * self.basic_pay

    def gross_pay(self):
        return self.basic_pay + self.da() + self.hra()

    def as_list(self):
        return [self.emp_name, self.job, self.basic_pay, self.age]

    def __str__(self):
        return f'Name: {self.emp_name}\nAge:{self.age}\nJob:{self.job}\nBasic Pay:{self.basic_pay}\nHRA:{self.hra()}\nDA:{self.da()}\nGross Pay:{self.gross_pay()}'


def print_menu():
    print("-------------------------------------")
    print("1. Show all employees")
    print("2. Show employee report")
    print("3. Add employee")
    print("4. Remove Employee")
    print("5. Save data")
    print("6. Retrieve data")
    print("7. Reprint menu")
    print("-------------------------------------")


employees = []
print_menu()


def add_employee():
    print("Enter employee name:")
    emp_name = input(">> ")
    print("Enter employee job:")
    job = input(">> ")
    print("Enter employee basic pay:")
    basic_pay = input(">> ")
    print("Enter employee age:")
    age = input(">> ")
    employees.append(Employee(emp_name, job, basic_pay, age))


def employee_report():
    print("Enter employee index:")
    index = int(input(">> "))
    if index < 0 or index >= len(employees):
        print("Invalid employee number!")
    else:
        print(employees[index])


def print_employees():
    for i in range(len(employees)):
        print(f'#{i} - {employees[i].emp_name}')


def remove_employee():
    print("Enter employee index to remove:")
    index = int(input(">> "))
    if index < 0 or index >= len(employees):
        print("Invalid employee number!")
    else:
        employees.remove(employees[index])


def save_data():
    with open('topic3_assignment5.csv', 'w') as save_file:
        cwriter = csv.writer(save_file)
        for emp in employees:
            cwriter.writerow(emp.as_list())
    save_file.close()


def retrieve_data():
    with open('topic3_assignment5.csv', 'r') as save_file:
        for line in save_file:
            if line == "\n":
                continue
            temp = line.split(',')

            employees.append(Employee(*temp))
    save_file.close()


while True:
    try:
        selected_option = int(input("[Main]>> "))
    except:
        continue
    if (selected_option > 0 and selected_option < 8):
        if selected_option == 1:
            print_employees()
        if selected_option == 2:
            employee_report()
        if selected_option == 3:
            add_employee()
        if selected_option == 4:
            remove_employee()
        if selected_option == 5:
            save_data()
        if selected_option == 6:
            retrieve_data()
        if selected_option == 7:
            print_menu()
    else:
        print("Invalid option!")
