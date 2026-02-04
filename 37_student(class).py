class Student:
  ...

def main():
  student = get_student()
  print(f"{student.name} from {student.classs}")

def get_student():
  student = Student()
  student.name = input("name: ")
  student.classs = input("classs: ")
  return student
if __name__ == "__main__":
  main()
  