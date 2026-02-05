students = [
  {"name": "harry", "classs": "12D"},
  {"name": "garry", "classs": "12C"},
  {"name": "Larry", "classs": "12A"},
  {"name": "Merry", "classs": "12B"},
]
  
classses = set()
for student in students:
  classses.add(student["classs"])

for classs in sorted(classses):
  print(f"{classs}")