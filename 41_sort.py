import random
class Socks:
  def __init__(self):
    self.who = ["male's foot", "female's foot", "baby's foot"]

  def sort(self, color):
    print(color, "is for", random.choice(self.who))

socks = Socks()
socks.sort("red")

#deep remember to import random when you use it in program xoxo and 