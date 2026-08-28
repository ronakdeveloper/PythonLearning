'''
What is OOP?

Object-Oriented Programming is a way of structuring code around objects — bundles of data (attributes) 
and behavior (methods/functions) that belong together, instead of scattering related variables and functions separately.

Why it matters for Data Engineering: Airflow DAGs, dbt models, database connectors, and
most pipeline frameworks are built using classes. When you write class MyOperator(BaseOperator):
in Airflow, you need to understand what's actually happening. You'll also write your own reusable pipeline components 
(e.g., a CSVReader class, a DataValidator class) instead of copy-pasting functions everywhere.

First concept: Class and Object
- A class is a blueprint/template.
- An object (instance) is an actual thing built from that blueprint.

Think of it like: class = the idea of "Customer", object = one actual customer, like Alice.

class Customer:
    pass

alice = Customer()

Here, Customer is the class, alice is an object (instance) of that class.

Note: class is empty right now (pass means "do nothing") — it has no data or behavior yet. We'll add that next with __init__ and attributes.
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
       discount_amount = self.price * (percent / 100)
       self.price = self.price - discount_amount


laptop = Product("Dell Laptop", 75000)
mouse = Product("Logitech Mouse", 1200)

print(laptop.name, laptop.price)
print(mouse.name, mouse.price)

laptop.apply_discount(10)

print(laptop.price)
