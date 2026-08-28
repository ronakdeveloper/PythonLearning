transactions = [
    {"customer": "Alice", "amount": 500},
    {"customer": "Bob", "amount": 750},
    {"customer": "Charlie", "amount": 300}
]

with open('transaction.txt', 'w') as file:
    for transaction in transactions:
        content = f"{transaction['customer']} - {transaction['amount']}\n"
        file.write(content)


valid_records = []
invalid_records = []
high_value_transactions  = []
total_amount = 0

with open('transactions.txt', 'r') as file:
    for line in file:
        try:
            customer, amount = line.strip().split(' - ')
            amount = int(amount)
            valid_records.append({
                'customer' : customer,
                'amount' : amount
            })

            if amount >= 700:
                total_amount += amount
                high_value_transactions .append({
                'customer' : customer,
                'amount' : amount
            })
            
                
        except ValueError:
            invalid_records.append(line.strip())

print("Valid Records:", valid_records)
print("Invalid Records:", invalid_records)
print("High Value Transactions:", high_value_transactions)
print("Total High Value Amount:", total_amount)


'''
PYTHON TEXT FILE HANDLING
==========================

1. open()
----------
Used to open a file.

Syntax:
open("filename", "mode")

Important modes:

"r" -> read
"w" -> write / overwrite
"a" -> append


2. with open() ⭐⭐⭐
--------------------

Recommended way to work with files.

with open("data.txt", "r") as file:
    content = file.read()

Python automatically closes the file.


3. read() ⭐⭐⭐
---------------

Reads the entire file.

with open("data.txt", "r") as file:
    data = file.read()


4. write() ⭐⭐⭐
----------------

Writes a string to a file.

with open("data.txt", "w") as file:
    file.write("Hello\n")


5. Read Line by Line ⭐⭐⭐
--------------------------

Very important for large files / Data Engineering.

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


6. strip() ⭐⭐
--------------

Removes whitespace and newline.

"Alice - 500\n".strip()

-> "Alice - 500"


7. split() ⭐⭐⭐
----------------

Splits a string into parts.

"Alice - 500".split(" - ")

-> ["Alice", "500"]


8. \n ⭐⭐
----------

Represents a new line.

"Hello\n"
"World\n"


9. int() ⭐⭐⭐
--------------

File data is read as strings.

"500" -> string
int("500") -> 500


10. try/except ⭐⭐⭐
--------------------

Used to handle bad records without stopping the whole pipeline.

try:
    customer, amount = line.strip().split(" - ")
    amount = int(amount)

except ValueError:
    print("Invalid record")


MOST IMPORTANT TO REMEMBER
==========================

open()
with open()
"r" / "w" / "a"
read()
write()
for line in file
strip()
split()
int()
try/except ValueError


DATA ENGINEERING CONNECTION
===========================

File
 ↓
Read
 ↓
Clean
 ↓
Validate
 ↓
Transform
 ↓
Filter
 ↓
Aggregate
'''