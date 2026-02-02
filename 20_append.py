#wel we'll be first using append function

names = []

for _ in range(3):
  name = input("whats yo name?!")
  names.append(name)

for name in sorted(names):
  print(f"hello. {name}")