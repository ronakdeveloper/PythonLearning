'''
===========================================================
                         SETS
===========================================================

WHAT IS A SET?
--------------
A set is a Python collection that:

1. Stores unique values
2. Is unordered
3. Is mutable
4. Supports mathematical set operations

Example:

    numbers = {1, 2, 3, 4}

A set cannot contain duplicate values.

    {1, 2, 2, 3, 3}

becomes:

    {1, 2, 3}


IMPORTANT
---------
A set is NOT indexed like a list.

This will NOT work:

    numbers[0]

because sets do not have positions/indexes.


SYNTAX
------
    my_set = {value1, value2, value3}

Empty set:

    my_set = set()

IMPORTANT:
    {} creates an empty dictionary, NOT an empty set.
'''

'''
===========================================================
                         SET
===========================================================

Definition:
    A set is a mutable collection of unique values.

Properties:
    - No duplicate values
    - Unordered
    - Mutable
    - Supports set operations
    - Does not support indexing

Syntax:

    my_set = {1, 2, 3}

Empty set:

    my_set = set()

IMPORTANT:
    {} is an empty dictionary.

Common operations:

    add()
    remove()
    discard()

Membership:

    value in my_set

Set operations:

    Union:
        a | b
        a.union(b)

    Intersection:
        a & b
        a.intersection(b)

    Difference:
        a - b
        a.difference(b)

    Symmetric Difference:
        a ^ b
        a.symmetric_difference(b)


Set comprehension:

    {expression for item in iterable}

With condition:

    {expression for item in iterable if condition}


Common uses in Data Engineering:

    - Remove duplicates
    - Find unique IDs
    - Membership checks
    - Compare datasets
    - Find missing records
    - Find common records
    - Find new records
'''

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

result = set(numbers)
print(result)

system_a = {101, 102, 103, 104, 105}
system_b = {103, 104, 105, 106, 107}

result = system_a.intersection(system_b)
print(result)
result = system_a - system_b
print(result)
result = system_b - system_a
print(result)

numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 10]

square_numbers = {
    number * number
    for number in numbers
    if number % 2 == 0
}

print(square_numbers)

yesterday = [101, 102, 103, 104, 105, 106]
today = [103, 104, 105, 106, 107, 108, 109]

yesterday_data = set(yesterday)
today_data = set(today)

new_today = today_data.difference(yesterday_data)
missing_today = yesterday_data - today_data
both_days = yesterday_data & today_data

print(new_today)
print(missing_today)
print(both_days)