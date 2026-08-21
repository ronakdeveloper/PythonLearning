'''
===========================================================
                    any() AND all()
===========================================================

WHAT IS any()?
--------------

any() checks whether AT LEAST ONE item in an iterable
is True.

In simple words:

    any() -> "Is there at least one True?"

Syntax:

    any(iterable)


WHAT IS all()?
--------------

all() checks whether EVERY item in an iterable is True.

In simple words:

    all() -> "Are all of them True?"

Syntax:

    all(iterable)


MENTAL MODEL
------------

any():
    ONE OR MORE must be True

all():
    EVERYTHING must be True
'''

'''
===========================================================
                    any() AND all()
===========================================================

any()
-----

Definition:
    Returns True if AT LEAST ONE item in an iterable
    is truthy.

Syntax:
    any(iterable)

Common pattern:

    any(condition for item in iterable)

Mental model:
    "Is there at least one?"


all()
------

Definition:
    Returns True if EVERY item in an iterable is truthy.

Syntax:
    all(iterable)

Common pattern:

    all(condition for item in iterable)

Mental model:
    "Are all of them?"


Example:

marks = [85, 72, 91, 45, 78]

# Is anyone failing?
any(mark < 60 for mark in marks)

# Did everyone pass?
all(mark >= 60 for mark in marks)


Difference:

filter()
    → returns matching items

any()
    → tells whether at least one matches

all()
    → tells whether everything matches


Data Engineering uses:

    - Data validation
    - Checking invalid records
    - Checking required fields
    - Quality checks
    - Pipeline validation
    - Business rule validation


Important:

any([]) → False
all([]) → True


Short-circuit:

any() can stop when it finds True.
all() can stop when it finds False.
'''

numbers = [10, 25, 30, 45, 50]

result = any(number > 40 for number in numbers)
print(result)

numbers = [10, 20, 30, 40, 50]
result = all(number > 5 for number in numbers)
print(result)
numbers = [10, 20, 3, 40, 50]
result = all(number > 5 for number in numbers)
print(result)

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 750},
    {"customer": "Charlie", "amount": -100},
    {"customer": "David", "amount": 900}
]

negative_amount = any(transaction['amount'] < 0 for transaction in transactions)
print(negative_amount)
positive_amount = all(transaction['amount'] >= 0 for transaction in transactions)
print(positive_amount)
result = any(transaction['amount'] > 800 for transaction in transactions)
print(result)