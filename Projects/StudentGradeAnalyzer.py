students = [
    {
        "name": "Alice",
        "marks": {
            "Math": 85,
            "Science": 92,
            "English": 78
        }
    },
    {
        "name": "Bob",
        "marks": {
            "Math": 72,
            "Science": 68,
            "English": 75
        }
    },
    {
        "name": "Charlie",
        "marks": {
            "Math": 95,
            "Science": 88,
            "English": 91
        }
    },
    {
        "name": "David",
        "marks": {
            "Math": 45,
            "Science": 52,
            "English": 48
        }
    },
    {
        "name": "Eva",
        "marks": {
            "Math": 60,
            "Science": 65,
            "English": 58
        }
    }
]

def analyze_students(students):
    
    std = []
    avg_dict = {}

    for student in students:
        name = student['name']
        marks = student['marks']

        avg_dict[name] = round(sum(marks.values()) / len(marks.values()),2)

    for n,avg in avg_dict.items():
        my_dict = {}
        my_dict['name'] = n
        my_dict['Average'] = avg
        my_dict['Result'] = 'Pass' if avg >= 60 else 'Fail'
        
        std.append(my_dict)
    
    class_avg = round(sum(avg_dict.values()) / len(avg_dict.values()),2)

    print(my_dict)

    return {
    'Students' :  std,
    'Class Avg' : class_avg
    }        


print(analyze_students(students))