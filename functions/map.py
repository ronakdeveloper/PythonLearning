'''
What is map()?

map() is a Python built-in function used for:

Apply a function to every item in an iterable and produce the resulting values 

Syntax - map(function, iterable)
funtion - what should happen to each item ?
iterable - what should we process ?

example 
map(lambda x: x * 2, numbers)
means Take every x from numbers and return x * 2

map() returns an iterator, and list() can turn that iterator into a list.
'''

## Normal way 
numbers = [1,2,3,4,5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)

## Using map with lambda 
result = list(map(lambda number : number * 2, numbers))
print(result)

## map with normal function 
def double(number):
    return number * 2

number = [1, 2, 3, 4, 5]

result = list(map(double, number))
print(result)

## map with strings 
names = ["alice", "bob", "charlie"]

result = list(map(lambda name : name.upper(), names))
print(result)

## also use normal function
def make_upper(name):
    return name.upper()

result = list(map(make_upper, names))
print(result)

## map with dictionaries
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 72},
    {"name": "Charlie", "marks": 91}
]

## we want only marks
result = list(map(lambda student :student['marks'], students))
print(result)

## map with multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 72, 91]

result = list(
    map(
        lambda name, score: f"{name} : {score}",names,scores
))

print(result)


transactions = [
    {"customer": "Alice", "amount": "500"},
    {"customer": "Bob", "amount": "750"},
    {"customer": "Charlie", "amount": "300"},
    {"customer": "David", "amount": "900"}
]

result = list(
    map(
        lambda transaction : int(transaction['amount']),
        transactions
        )
)
print(result)