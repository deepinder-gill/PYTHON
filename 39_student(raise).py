class Student:
  def __init__(self, name, classs):
    if not classs:
      raise ValueError("Missing Name")
#it will raise error if there is no class    
    self.name = name
    self.classs = classs
 
def main():
  student = get_student()
  print(f"{student.name} from {student.classs}")

def get_student():
  name = input("name: ")
  classs = input("classs: ")
  return Student(name, classs)

if __name__ == "__main__":
  main()
  