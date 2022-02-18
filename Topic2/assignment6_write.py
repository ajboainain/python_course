from assignment5 import Patient
import pickle

file_path = 'pickle_file'

out = open(file_path, 'wb')

patient = Patient(patient_name="John", address="123 St.",
                  contact="123456789", complaint="Runny nose")

pickle.dump(patient, out)
