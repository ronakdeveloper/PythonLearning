students = [
    {"name": "Alice", "marks": {"Math": 85, "Science": 92, "English": 78}},
    {"name": "Bob", "marks": {"Math": 72, "Science": 68, "English": 75}},
    {"name": "Charlie", "marks": {"Math": 95, "Science": 88, "English": 91}},
    {"name": "David", "marks": {"Math": 45, "Science": 52, "English": 48}},
    {"name": "Eva", "marks": {"Math": 60, "Science": 65, "English": 58}},
]

# students = [
#     {"name": "John", "marks": {"Math": 80, "Science": 70, "English": 90}},
#     {"name": "Sarah", "marks": {"Math": 90, "Science": 95, "English": 85}},
# ]

# students = [
#     {"name": "John", "marks": {"Math": 80, "Science": 90}},
#     {"name": "Sarah", "marks": {"Math": 70, "Science": 80, "English": 90}},
# ]

def analyze_students(students):
    if len(students) > 0:        
        std = []
        avg_dict = {}    
        std_marks = []
        sub_dict = {}
        subject_count = {}
        
        for student in students:
            name = student["name"]
            marks = student["marks"]
            std_marks.append(marks)
            avg_dict[name] = round(sum(marks.values()) / len(marks.values()), 2)

        for name, avg in avg_dict.items():
            my_dict = {}
            my_dict["name"] = name
            my_dict["Average"] = avg
            my_dict["Result"] = "Pass" if avg >= 60 else "Fail"
            std.append(my_dict)

        
        for mark in std_marks:
            for key, value in mark.items():
                subject_count[key] = subject_count.get(key, 0) + 1
                sub_dict[key] = sub_dict.get(key, 0) + value

        for key in sub_dict.keys() & subject_count.keys():
            sub_dict[key] = sub_dict[key] / subject_count[key]

        top_student = max(avg_dict, key=avg_dict.get)
        lowest_student = min(avg_dict, key=avg_dict.get)
        class_avg = round(sum(avg_dict.values()) / len(avg_dict.values()), 2)
        highest_sub_avg = max(sub_dict, key=sub_dict.get)
        
        return {
            "Students": std,
            "Top Student": top_student,
            "Lowest Student": lowest_student,
            "Class Avg": class_avg,
            "Subject Avg": sub_dict,
            "Highest Subject Avg": highest_sub_avg,
        }
    else:
        return {
            "Students": [],
            "Top Student": None,
            "Lowest Student": None,
            "Class Avg": None,
            "Subject Avg": {},
            "Highest Subject Avg": None
        } 

print(analyze_students(students))