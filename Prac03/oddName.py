"""
Joshua Gray
"""

name = input("What is your name? ")

while len(name) == 0:
    print("Invalid Name")
    name = input("What is your name? ")

for i in range(0, len(name), 2):
    print(name[i])
