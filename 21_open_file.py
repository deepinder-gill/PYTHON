name = input("whats yo name")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close