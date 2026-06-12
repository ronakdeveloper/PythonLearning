import csv

def read_csv(path):
    with open(path) as file:
        reader = csv.DictReader(file)
        rows = []
        for r in reader:
            rows.append(r)

        return rows

def write_csv(path, record):

    if len(record) == 0:
        return

    with open(path, mode='w') as file:
        col = list(record[0])
        writer = csv.DictWriter(file, fieldnames=col)
        writer.writeheader()
        writer.writerows(record)        


rows = read_csv('phase1/employees.csv')

correct_rows = []
incorrect_rows = []

for row in rows:
    try:
        correct_rows.append({
            "name" : row['name'],
            "salary" : int(row['salary'] if row['salary'] else None)
        })
    except ValueError:
        incorrect_rows.append({
            "name" : row['name'],
            "msg" : 'Invalida Data Type'
        });
    except TypeError:
        incorrect_rows.append({
            "name" : row['name'],
            "msg" : 'Missing Value'
        });

print(correct_rows)
print(incorrect_rows)
write_csv('phase1/employees_correct_rows.csv', correct_rows)
write_csv('phase1/employees_incorrect_rows.csv', incorrect_rows)