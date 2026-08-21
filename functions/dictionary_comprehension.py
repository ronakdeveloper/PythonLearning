'''
===========================================================
              DICTIONARY COMPREHENSION
===========================================================

Definition:
    A compact way to create a new dictionary from an
    iterable.

Syntax:

    {key: value for item in iterable}

With condition:

    {key: value for item in iterable if condition}

Example:

    numbers = [1, 2, 3, 4]

    squares = {
        number: number * number
        for number in numbers
    }

Result:

    {
        1: 1,
        2: 4,
        3: 9,
        4: 16
    }


From another dictionary:

    students = {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 91
    }

    passed = {
        name: marks
        for name, marks in students.items()
        if marks >= 60
    }

Result:

    {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 91
    }


Mental model:

    List comprehension:

        [VALUE for ITEM in DATA]

    Dictionary comprehension:

        {KEY: VALUE for ITEM in DATA}


Data Engineering use cases:

    - Transform records
    - Create lookup dictionaries
    - Filter records
    - Convert data structures
    - Rename/transform keys
    - Transform values
'''

numbers = [1, 2, 3, 4, 5]

result = {
    number : number * number
    for number in numbers
}

print(result)

students = {
    "Alice": 85,
    "Bob": 55,
    "Charlie": 91,
    "David": 48,
    "Eva": 72
}

passed = {
    name : mark
    for name, mark in students.items()
    if mark >= 60
}

print(passed)

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 750},
    {"customer": "Charlie", "amount": 300},
    {"customer": "David", "amount": 900},
    {"customer": "Eva", "amount": 1200}
]

transactions = {
    transaction['customer'] : transaction['amount']
    for transaction in transactions
    if transaction['amount'] > 500
}

print(transactions)