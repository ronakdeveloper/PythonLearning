'''
===========================================================
                    filter() IN PYTHON
===========================================================

DEFINITION
----------
filter() is a Python built-in function used to:

    Keep only the items from an iterable that satisfy
    a condition.

In simple words:

    map()    -> TRANSFORM items
    filter() -> SELECT items

Syntax
------
filter(function, iterable)

function  -> decides whether an item should be kept
iterable  -> the data we want to check

The function should return:

    True  -> keep the item
    False -> remove the item

filter() returns an iterator.

If we want a list:

    list(filter(...))
'''

## Normal way 
numbers = [10, 15, 20, 25, 30]

result = []

for number in numbers:
    if number > 20:
        result.append(number)

print(result)

## Using filter
result = list(filter(lambda number : number > 20, numbers))
print(result)

## filter with strings
names = ["Alice", "", "Bob", "", "Charlie"]

result = list(filter(lambda name : name != '', names))
print(result)

## Keep names begining with A
names = ["Alice", "Bob", "Andrew", "Charlie"]

result = list(filter(lambda name : name.endswith('e'), names))
print(result)

# filter with dictionaries
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 55},
    {"name": "Charlie", "marks": 91},
    {"name": "David", "marks": 45}
]

result = list(
    filter(
        lambda student : student['marks'] >= 60,
        students
    )
)
print(result)

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 0},
    {"customer": "Charlie", "amount": 750},
    {"customer": "David", "amount": -100},
]

transaction = list(
    filter(
        lambda transaction : transaction['amount'] > 0,
        transactions
    )
)

print(transaction)

'''
filter()
-------

Definition:
    filter() selects items from an iterable based on a condition.

Syntax:
    filter(function, iterable)

function:
    Receives one item and should return True or False.

    True  -> keep
    False -> remove

Returns:
    A filter iterator.

Convert to list:
    list(filter(...))

Mental model:
    map()    -> transform
    filter() -> select

Example:

numbers = [10, 20, 30, 40]

result = list(
    filter(lambda x: x > 20, numbers)
)

Result:
[30, 40]
'''

numbers = [10, 25, 30, 15, 40, 5, 50]

result = list(filter(lambda number : number > 25, numbers))
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda number : number % 2 == 0, numbers))
print(even_numbers)

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 0},
    {"customer": "Charlie", "amount": 750},
    {"customer": "David", "amount": -100},
    {"customer": "Eva", "amount": 1200}
]

transactions = list(filter(lambda transaction : transaction['amount'] > 500, transactions))
print(transactions)