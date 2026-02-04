def main():
  student = get_student()
  print(f"{student[0]} from {student[1]}")

def get_student():
  name = input("name : ")
  classs = input("classs : ")
  return (name, classs)

if __name__ == "__main__":
  main()