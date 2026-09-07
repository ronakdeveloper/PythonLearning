class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.__base_salary = base_salary

    def get_salary(self):
        return self.__base_salary
    
    def calculate_bonus(self):
        return 0

class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.team_size * 1000

class Developer(Employee):
    def __init__(self, name, base_salary, project_completed):
        super().__init__(name, base_salary)
        self.project_completed = project_completed

    def calculate_bonus(self):
        return self.project_completed * 2000

employee_list = [Manager('Ronak', 50000, 8), Developer('Sumit', 30000, 5)]

for emp in employee_list:
    print(f"Name : {emp.name} | Salary : {emp.get_salary()} | Bonus : {emp.calculate_bonus()}")