
## Variables
name = "Ronak" ## string
age = 25 ## int
salary = 27500.25 ## float 
is_employee = True ## bit

print(name)
print(age)
print(salary)
print(is_employee)

## Type checking
print(type(name))
print(type(age))
print(type(salary))
print(type(is_employee))

## User Input 
name = input("Enter your name :" )
print("Hello,", name)

salary = float(input("Enter your salary :"))
print(salary + 5000)

## Type Conversion
age = "25"
converted_age = int(age)
converted_ages = str(converted_age)
print(converted_age)
print(type(converted_age))
print(converted_ages)
print(type(converted_ages))

a = 15
b = 4

## Arithmetic Operations
print(a+b)   ## Addition
print(a-b)   ## Subtraction
print(a*b)   ## Multiplication
print(a/b)   ## Division
print(a%b)   ## Modules
print(a**b)  ## Exponentiation
print(a//b)  ## Floor Division
## Comparison 
print(a==b) ## Equal
print(a!=b) ## Not equal
print (a>b) ## Greater than
print(a<b)  ## Less than
print(a>=b) ## Greater than or equal to
print(a<=b) ## Less than or equal to
## Logical
print(a>5 and b<10) ## Returns True if both statements are true
print(a>5 or b<10) ## Returns True if one of the statements is true
print(not(a>5 and b<10)) ##Reverse the result, returns False if the result is true

name = "Ronak"
salary = 27300
print(f"My name is {name} and salary is {salary}")

## Ex-1
empname = input("Enter your name :")
empage = int(input("Enter your age :"))
empsalary = float(input("Enter your salary :"))

print(f"Employee {empname} is {empage} years old and earns {salary}")


## Ex-2
salary = int(input("Enter your salary : "))
print(f"your bonus is {salary*10/100} and Final salary {salary+(salary*10/100)}")


## Ex-3
celsius = float(input("Enter Celsius :"))
Fahrenheit = (celsius * 1.8) + 32
print(Fahrenheit)

employee = {"name":"Ronak","salary":50000}
print(employee)
print(employee["name"])


EmpName = input("Enter your name : ")
EmpSalary = float(input("Enter your salary : "))

print(f"Employee {EmpName} annual salary is {EmpSalary*12} and after 10% tax Final salary is {EmpSalary*12-((EmpSalary*12)*10/100)}")