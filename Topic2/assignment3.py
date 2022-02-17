import csv
from unicodedata import name

print("Enter student name: ")
name = input(">> ").strip('\n')

print("Enter student course: ")
course = input(">> ").strip('\n')

print("Enter student institute: ")
institute = input(">> ").strip('\n')

print("Enter student fees: ")
fees = input(">> ").strip('\n')


file = open('assignment3.txt', 'a', newline='')

writer = csv.writer(file)
writer.writerow([name, course, institute, str(fees)])
file.close()
