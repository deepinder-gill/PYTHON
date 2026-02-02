with open("students.csv") as file:
  for line in file:
    name , classs = line.rstrip().split(",")
    print(f"{name} is  in {classs}")


#did it usind dictionary and lists in next one