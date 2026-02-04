def main():
  student = get_student()
  print(f"{student['name']} from {student['classs']}")

def get_student():
  student = {}
  student["name"] = input("name: ")
  student["classs"] = input("class: ")
  return student
if __name__ == "__main__":
  main()

#used class in next one