name = input("whats yo name")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close

#did this using with in 22_with.py
