from csv import writer
import os


print("Please enter file path:")
file_path = input(">> ")

if file_path == '':
    print("You must specify a file path!")

print("Enter word to replace: ")
given_word = input(">> ")

print(f'Enter the word that will be replacing \"{given_word}\"')
replace = input(">> ")

new_text = ""
with open(file_path) as file:
    content = file.readlines()
    for sentence in content:
        new_text += sentence.replace(given_word, replace)
file.close()

file = open(file_path, 'w')
file.write(new_text)
file.close()
