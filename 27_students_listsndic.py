students = []
with open("students.csv") as file:
  for line in file:
    name, classs = line.rstrip().split()
    student = {}

    student['name'] = name
    student['classs'] = classs

    students.append(student)


for student in students:
  print(f"{student['name']} is in {student['classs']}")