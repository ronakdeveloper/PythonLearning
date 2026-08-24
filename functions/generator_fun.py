'''
===========================================================
              GENERATOR FUNCTIONS / yield
===========================================================

A generator function is a function that uses yield.

Example:

def numbers():
    yield 1
    yield 2
    yield 3


Calling the function:

result = numbers()

creates a generator.


next():

next(result)

asks the generator for its next value.


yield:
    Produces a value and pauses the function.

The next next() call resumes execution from where
the previous yield stopped.


return vs yield:

return:
    - returns a value
    - function ends
    - cannot resume

yield:
    - produces a value
    - function pauses
    - can resume
    - maintains state


Generator functions are useful for:

    - Large datasets
    - Large files
    - ETL pipelines
    - Streaming data
    - Memory-efficient processing


Example:

def generate_numbers():
    for number in range(1, 6):
        yield number

for number in generate_numbers():
    print(number)
'''

def generate_numbers():
    yield 10
    yield 20
    yield 30
    yield 40 
    yield 50

number = generate_numbers()


print(next(number))
print(next(number))
print(next(number))

def generate_squares(numbers):
    for number in numbers:
        yield number * number

numbers = [1, 2, 3, 4, 5]

result = generate_squares(numbers)

for r in result:
    print(r)



def valid_transactions(transactions):
    for transaction in transactions:
        if transaction['amount'] >= 0:
            yield transaction

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": -100},
    {"customer": "Charlie", "amount": 750},
    {"customer": "David", "amount": -50},
    {"customer": "Eva", "amount": 900}
]

for transaction in valid_transactions(transactions):
    print(transaction)