"""
PYTHON CSV HANDLING
===================

CSV = Comma-Separated Values

Example CSV:

customer,amount,city
Alice,500,Ahmedabad
Bob,750,Mumbai
Charlie,300,Delhi


IMPORTANT:
-----------
CSV data is normally read as STRING values.

"500" -> str
int("500") -> 500


MAIN THINGS TO REMEMBER:
-------------------------
import csv

csv.reader()       -> read CSV as lists
csv.DictReader()   -> read CSV as dictionaries ⭐
csv.writer()       -> write CSV
csv.DictWriter()   -> write dictionaries to CSV ⭐

"""


# ============================================================
# 1. CREATE SAMPLE CSV DATA
# ============================================================

import csv

transactions = [
    {"customer": "Alice", "amount": 500, "city": "Ahmedabad"},
    {"customer": "Bob", "amount": 750, "city": "Mumbai"},
    {"customer": "Charlie", "amount": 300, "city": "Delhi"},
    {"customer": "David", "amount": 900, "city": "Pune"},
]

with open("transactions.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["customer", "amount", "city"]
    )

    writer.writeheader()
    writer.writerows(transactions)


# ============================================================
# 2. READ CSV USING csv.reader()
# ============================================================

with open("transactions.csv", "r", newline="") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# Output:

# ['customer', 'amount', 'city']
# ['Alice', '500', 'Ahmedabad']
# ['Bob', '750', 'Mumbai']
# ...


# ============================================================
# 3. READ CSV USING csv.DictReader() ⭐⭐⭐
# ============================================================

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# Each row becomes a dictionary:

# {
#     'customer': 'Alice',
#     'amount': '500',
#     'city': 'Ahmedabad'
# }


# ============================================================
# 4. ACCESS CSV COLUMNS
# ============================================================

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row["customer"])
        print(row["amount"])
        print(row["city"])


# ============================================================
# 5. CONVERT STRING TO INTEGER ⭐⭐⭐
# ============================================================

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        amount = int(row["amount"])

        print(row["customer"], amount)


# Remember:

# CSV:
# "500"
#
# Python:
# 500


# ============================================================
# 6. FILTER CSV DATA
# ============================================================

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        amount = int(row["amount"])

        if amount >= 700:
            print(row["customer"], amount)


# ============================================================
# 7. CALCULATE TOTAL
# ============================================================

total_amount = 0

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        amount = int(row["amount"])

        total_amount += amount

print("Total:", total_amount)


# ============================================================
# 8. CREATE A NEW CSV FROM PROCESSED DATA ⭐⭐⭐
# ============================================================

high_value_transactions = []

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        amount = int(row["amount"])

        if amount >= 700:

            high_value_transactions.append({
                "customer": row["customer"],
                "amount": amount,
                "city": row["city"]
            })


with open("high_value.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["customer", "amount", "city"]
    )

    writer.writeheader()
    writer.writerows(high_value_transactions)


# ============================================================
# 9. CSV -> TRANSFORM -> CSV
# ============================================================

processed_transactions = []

with open("transactions.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        amount = int(row["amount"])

        processed_transactions.append({
            "customer": row["customer"],
            "amount": amount,
            "city": row["city"],
            "status": "High Value" if amount >= 700 else "Normal"
        })


with open("processed_transactions.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "customer",
            "amount",
            "city",
            "status"
        ]
    )

    writer.writeheader()
    writer.writerows(processed_transactions)


# ============================================================
# 10. BASIC CSV ETL PATTERN ⭐⭐⭐
# ============================================================

"""
INPUT CSV
    ↓
DictReader
    ↓
Read row
    ↓
Clean / Convert
    ↓
Validate
    ↓
Filter / Transform
    ↓
DictWriter
    ↓
OUTPUT CSV
"""


# ============================================================
# 11. IMPORTANT THINGS TO REMEMBER
# ============================================================

"""
import csv

csv.reader()
    -> rows as lists

csv.DictReader()
    -> rows as dictionaries ⭐

csv.writer()
    -> write lists

csv.DictWriter()
    -> write dictionaries ⭐

writer.writeheader()
    -> writes column names

writer.writerow()
    -> writes one row

writer.writerows()
    -> writes multiple rows

CSV values are strings.
Convert numeric values yourself:

int(row["amount"])
float(row["price"])


MOST IMPORTANT:
---------------

DictReader
DictWriter
int()
for row in reader
"""


# ============================================================
# 12. YOUR FIRST CSV EXERCISE
# ============================================================

"""
Create this CSV:

sales.csv

customer,amount,city
Alice,500,Ahmedabad
Bob,750,Mumbai
Charlie,300,Delhi
David,900,Pune
Eva,1200,Ahmedabad


TASK:

Read sales.csv using DictReader.

Print ONLY customers whose amount is greater than 700.

Expected:

Bob - 750
David - 900
Eva - 1200


Requirements:

- import csv
- with open()
- csv.DictReader()
- for loop
- int()
- if

Don't use Pandas yet.
"""

import csv

city = {}

with open('sales.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:

        city_name = row['city']
        amount = int(row['amount'])

        if city_name in city:
            city[city_name] += amount
        else:
            city[city_name] = amount

result = []

with open('sales.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = int(row['amount'])
        result.append({
            'customer' : row['customer'],
            'amount' : amount,
            'city' : row['city'],
            'category' : 'High' if amount > 800 else ('Medium' if amount >= 400 and amount <= 800 else 'Low')
        })
        
with open('sales_report.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['customer','amount','city','category'])

    writer.writeheader()
    writer.writerows(result)