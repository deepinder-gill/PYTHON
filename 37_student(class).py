class Student:
  ...

#declared class adn remember it must be in capital

def main():
  student = get_student()
  print(f"{student.name} from {student.classs}")

def get_student():
  student = Student()

#assigner that in variable
  student.name = input("name: ")
#used this to take input and store it in variable
  student.classs = input("classs: ")
  return student
if __name__ == "__main__":
  main()
  