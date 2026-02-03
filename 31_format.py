name = input("enter name").strip()

if "," in name:

  last, first = name.split(", ?")
  name = f"{first} {last}"

print(f"hhello, {name}")

#made it more advanced in nex one using re and import and stuff