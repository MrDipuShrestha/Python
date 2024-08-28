# Dictonary Comprehension

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.item()}

# Connditional dictonary Comprehension

# new_dict = {new_key:new_value for (key, value) in dict.items() if condiiton}

import random

names = ["Dipesh", "Sayara", "Riya", "Ashim", "Nijal"]

all_student = {student: random.randint(1, 60) for student in names}

print(all_student)

passed_student = {student: score for (student, score) in all_student.items() if score >= 24}

print(passed_student)
