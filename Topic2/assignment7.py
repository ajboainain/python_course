import glob
# All files and directories ending with .txt and that don't begin with a dot:

print("Enter path to check for python files: ")
path = input(">> ")

files = glob.glob(path + "/*.py")
for file in files:
    print(file.split("\\")[1])
