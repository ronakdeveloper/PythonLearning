numbers = [1, 2, 3, 4, 5]

squares = (number * number for number in numbers)

print(next(squares))
print(next(squares))
print(next(squares))

numbers = [10, 20, 30, 40, 50]

result = (number for number in numbers if number > 25)

print(next(result))
print(next(result))
print(next(result))

transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 750},
    {"customer": "Charlie", "amount": 300},
    {"customer": "David", "amount": 900},
]

result = (transaction['amount'] for transaction in transactions)

print(next(result))
print(next(result))
print(next(result))
print(next(result))