import re
email = input("whatss yo email?!").strip()

#remember deep strip  is for like if by mistake entered a space character on left or right side of the mail they input strip willl remove that space on left and right
if re.search(r"^[^@]+@[^@]+\.com$", email):

#re.search basically searches for specific character we enter
#you can use [] to limit the no of characters allowed    well easy way out is \w which means word character which includes a-z A-Z and 0-9 while \W means not word character and similarly for \s and \S and \d and \D and i bet no further explanation needed as you got smart ass
  print("vallid")

else:
  print("invalid")