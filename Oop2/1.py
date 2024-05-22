class Employee:
    def __init__(self, fullname, email):
        self.name=fullname
        self.fullname = f"{fullname} {email}"
        self.email = f"{fullname.lower()}.{email.lower()}@company.com"


employee = Employee("John", "Smith")
print(f"fullname: {employee.fullname}")
print(f"Email: {employee.email}")
print(f"Firstname: {employee.name}")
    
###################################################################### Digakhel

import random

class Employee:
    def __init__(self, first_name, name):
        self.fullname = first_name + " " + name
        self.rand = random.randrange(99)
        self.email = (first_name + name + str(self.rand) + "@gmail.com")

employees = Employee("Eronshozoda", "Sayod")

print(employees.fullname) 
print(employees.email)
        