student_marks = {
    "Dipesh" : 81,
    "Nijal" : 50,
    "Ashim" : 64,
    "Shubham" : 80,
    "Pratikshya" : 65,
}

student_grade = {}


for student in student_marks:
    marks = student_marks[student]
    if marks > 90 and marks <= 100:
        student_grade[student] = "Outstanding"
    elif marks > 80 and marks <= 90:
        student_grade[student] = "Exceeds Exceptation"
    elif marks > 70 and marks <= 80:
        student_grade[student] = "Acceptable"
    elif marks <= 70:
        student_grade[student] = "Fail"

print(student_grade)