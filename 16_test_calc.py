from calc15 import square 
#it was to test the code writte in calc15.py

def main():
  test_square()

def test_square():
 # if square(2) != 4:]
 try:
   assert square(2) == 4
 except AssertionError :
  print("2 square not showin 4")

 #   print("2 squares not 4?? it aint workin")
 # if square(3) != 9:
 try:
   assert square(3) == 9
 except AssertionError :
   print("3 square was not 9")
 #   print("3 squares not 9?? it aint workin")

if __name__ == "__main__":
  main()