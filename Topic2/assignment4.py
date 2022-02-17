import csv


print("Name\t Course\t Institute\t fees\t GST (14%)\t Total Price")

file = open("C:/Users/ajboa/Documents/Python_Course/Assignments/assignment3.txt")

csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows)
for row in rows:
    if row == []:
        continue
    name = row[0].strip('\n')
    course = row[1]
    institute = row[2]
    fees = round(float(row[3]), 2)
    gst_fee = round(float(fees) * 0.14, 2)
    total = round(gst_fee + float(fees), 2)

    temp = [name, course, institute, fees, gst_fee, total]
    print("{: >0} {: >8} {: >10} {: >14} {: >7} {: >16}".format(*temp))


file.close()
