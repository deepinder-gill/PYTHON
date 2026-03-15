import re
email = input("whatss yo email?!").strip()


if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
  print("vallid")



else:
  print("invalid")