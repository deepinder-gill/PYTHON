#x = int(input("whats the num ?!"))

while True:
  try:
    x = int(input("what's x (let it be integer mofo)"))
    print(f"{x} is integer")
  except ValueError:
    print("x is not a integer")
  else:
    break