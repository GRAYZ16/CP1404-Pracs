
outFile = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=outFile)
outFile.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()


in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
 number = int(line)
 total += number
print(total)
in_file.close()