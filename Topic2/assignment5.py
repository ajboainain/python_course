

from ctypes import addressof
from unicodedata import name


class Patient():

    def __init__(self, patient_name="", address="", contact="", complaint=""):
        self.patient_name = patient_name
        self.address = address
        self.contact = contact
        self.complaint = complaint

    def set_name(self, patient_name):
        self.patient_name = patient_name

    def set_address(self, address):
        self.address = address

    def set_contact(self, contact):
        self.contact = contact

    def set_complaint(self, complaint):
        self.complaint = complaint

    def __str__(self):
        return f'Name: {self.patient_name}\n Address: {self.address}\n Contact: {self.contact}\n Comaplaint: {self.complaint}'


p = Patient("john", "123", "8833221199", "headache")

print(p)
