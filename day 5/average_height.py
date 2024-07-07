print("Calculate student's height")

student_height = input("Enter the heights of the students: ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total_height = 0
for height in student_height:
    total_height += height

total_student = 0
for student in student_height:
    total_student += 1

average = round(total_height / total_student)

print(f"The average is {average}")
