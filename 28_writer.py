import csv

name = input("enter name")
classs = input("etner classs")

with open("student.csv", "a") as file:
  writer = csv.writer(file)
  writer.writerow([name, classs])

