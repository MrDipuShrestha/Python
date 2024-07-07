print("Find max marks from list of marks.")

student_marks = input("Enter the marks of the students: ").split()

for n in range(0, len(student_marks)):
    student_marks[n] = int(student_marks[n])

first_value = student_marks[0]
for mark in student_marks:
    if mark > first_value:
        first_value = mark

print("The highest marks is: ", first_value)