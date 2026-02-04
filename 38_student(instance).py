class Student:
  def __init__(self, name, classs):
#we can make instance variable where third attribute should be introduced in which later on we make a bowl in which we add food(varible in which store data)
    self.name = name
#here see it 'self.name'
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
  