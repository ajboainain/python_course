from assignment5 import Patient
import pickle

file_path = 'pickle_file'

in_file = open(file_path, 'rb')

patient = pickle.load(in_file)

print(patient)
