class Employee:
    def __init__(self, name, department, salary, year_of_experience):
        self._name = name
        self._department = department
        self._salary = salary
        self._year_of_experience = year_of_experience
        
    def calculate_bonus(self):
        bonus = self._salary * 1.5 * self._year_of_experience
        return bonus
    
    def display_employee_information(self):
        
        print(f"Name --> {self._name}")
        print(f"Department --> {self._department}")
        print(f"Salary {self._salary}$")
        print(f"Year of experience --> {self._year_of_experience}")
        
        
        
emp1 = Employee("Eronshozoda", "dev/s", 5000, 12)
emp1.display_employee_information()

bonus = emp1.calculate_bonus()
print(f"Bonus: {bonus}$")
