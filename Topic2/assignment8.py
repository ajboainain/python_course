import glob
# All files and directories ending with .txt and that don't begin with a dot:

print("Enter path to check for python files: ")
path = input(">> ")

files = []
extensions = ['.jpg', '.gif', '.png', 'jpeg', '.svg']
for extension in extensions:
    files.append(glob.glob(path + "/*" + extension))

for file in files:
    if file == []:
        continue
    print(file[0].split("\\")[1])
#
