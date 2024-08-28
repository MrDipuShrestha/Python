import pandas

marksheet = {
    "students": ["Dipesh", "Ashim", "Nijal"],
    "marks": [98, 45, 33]
}

student_table = pandas.DataFrame(marksheet)

print(student_table)

for index, row in student_table.iterrows():
    print(f"Index:{index}, Rows:{row.marks}")