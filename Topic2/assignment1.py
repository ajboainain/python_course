import os


print("Please enter file path:")
file_path = input(">> ")

if file_path == '':
    print("You must specify a file path!")

print("Enter word to count: ")
word = input(">> ")

counter = 0
with open(file_path) as file:
    content = file.readlines()
    for line in content:
        line = line.split(' ')
        for current_word in line:
            if current_word.strip(',').strip('.').strip('-').strip('\n') == word:
                counter += 1


print(f'{counter} occurences of the word \"{word}\"')

# C:/Users/ajboa/Documents/Python_Course/Assignments/Topic2/words.txt
