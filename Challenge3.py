import math
import json

def calculate_statistics(students_data):
    num_students = len(students_data)
    num_subjects = len(students_data[0]["grades"])

    # Calculate average grades for each student
    average_grades = [sum(student["grades"][i]["grade"] for i in range(num_subjects)) / num_subjects for student in students_data]

    # Calculate average grades for each subject across all students
    subject_grades = [[student["grades"][i]["grade"] for student in students_data] for i in range(num_subjects)]
    average_subjects = [sum(subject) / num_students for subject in subject_grades]

    # Calculate overall average grade across all students
    overall_average = sum(average_grades) / num_students

    # Calculate standard deviation of grades across all students
    squared_diff = [((student["grades"][i]["grade"] - average_grades[j]) ** 2) for j, student in enumerate(students_data) for i in range(num_subjects)]
    mean_squared_diff = sum(squared_diff) / (num_students * num_subjects)
    std_deviation = math.sqrt(mean_squared_diff)

    # Prepare output dictionary
    output = {
        "average_grades": average_grades,
        "average_subjects": average_subjects,
        "overall_average": overall_average,
        "std_deviation": std_deviation
    }

    return output

# Test the function with the provided data
students_data = [
    {
        "name": "John Doe",
        "grades": [
            {"subject": "Math", "grade": 90},
            {"subject": "English", "grade": 85},
            {"subject": "Science", "grade": 92},
            {"subject": "History", "grade": 88},
            {"subject": "Art", "grade": 95}
        ]
    },
    {
        "name": "Jane Smith",
        "grades": [
            {"subject": "Math", "grade": 88},
            {"subject": "English", "grade": 92},
            {"subject": "Science", "grade": 87},
            {"subject": "History", "grade": 90},
            {"subject": "Art", "grade": 93}
        ]
    },
    {
        "name": "Bob Johnson",
        "grades": [
            {"subject": "Math", "grade": 78},
            {"subject": "English", "grade": 85},
            {"subject": "Science", "grade": 80},
            {"subject": "History", "grade": 88},
            {"subject": "Art", "grade": 82}
        ]
    }
]

result = calculate_statistics(students_data)
print(json.dumps(result, indent=2))
