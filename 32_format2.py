import re

name = input("whats yo name").strip()

matches = re.search(r"^(.+) , (.+)$", name)
if matches:
  last, first = matches.group()
  name = f"{first} {last}"
print(f"hello, {name}")