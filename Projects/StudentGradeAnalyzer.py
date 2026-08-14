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
    student_dict = {}
    class_avg = None

    for student in students:
        name = student['name']
        marks = student['marks']

        student_dict[name] = round(sum(marks.values()) / len(marks.values()),2)
    
    
    std.append(student_dict)
    
    class_avg = sum(student_dict.values()) / len(student_dict.values())

    print(student_dict)
    return {
    'Students' :  std,
    'Class Avg' : class_avg
    }        


print(analyze_students(students))