def main():
  student = get_student()
  print(f"{student[0]} from {student[1]}")

def get_student():
  name = input("name : ")
  classs = input("classs : ")
  return (name, classs) 
#here we used tuple and its immutable means data in it cant be chhanged if we used [ ]  it would have been a list

if __name__ == "__main__":
  main()