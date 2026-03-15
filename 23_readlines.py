with open("names.txt", "r") as file:
  lines = file.readlines()

for line in lines:
  print("hello,", line)

#well there iss ugly space in betweem lines habe fixed that in next one using rstrip