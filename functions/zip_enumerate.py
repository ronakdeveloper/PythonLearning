'''
===========================================================
                    enumerate()
===========================================================

Definition:

enumerate() allows us to loop through an iterable while
getting both the index and the value.

Syntax:

enumerate(iterable, start=0)

Example:

numbers = [10, 20, 30]

for index, number in enumerate(numbers):
    print(index, number)

Output:

0 10
1 20
2 30


Start from 1:

for index, number in enumerate(numbers, start=1):
    print(index, number)


Use enumerate() when you need:
    - index
    - value

Instead of:

for i in range(len(numbers)):
    print(i, numbers[i])


===========================================================
                        zip()
===========================================================

Definition:

zip() combines multiple iterables position by position.

Syntax:

zip(iterable1, iterable2, ...)

Example:

names = ["Alice", "Bob", "Charlie"]
scores = [85, 72, 91]

for name, score in zip(names, scores):
    print(name, score)


Important:

zip() stops at the shortest iterable.

zip() returns an iterator.


===========================================================
             enumerate() + zip()
===========================================================

Example:

for i, (name, score) in enumerate(
    zip(names, scores),
    start=1
):
    print(i, name, score)


Mental model:

zip()
    ↓
combine values

enumerate()
    ↓
add index
'''

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 750},
    {"customer": "Charlie", "amount": 300}
]


for i, transaction in enumerate(transactions, start=1):
    print(f"Transaction {i}: {transaction['customer']} - {transaction['amount']} ")

customers = ["Alice", "Bob", "Charlie", "David"]
amounts = [500, 750, 300, 900]

for customer, amount in zip(customers, amounts):
    print(f"{customer} Paid {amount}")


customers = ["Alice", "Bob", "Charlie"]
amounts = [500, 750, 300]

for i, (customer, amount) in enumerate(zip(customers, amounts), start=1):
    print(f"{i}. {customer} - {amount}")