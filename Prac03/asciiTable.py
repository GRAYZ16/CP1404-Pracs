"""
Mr. Black the school teacher wants an educational program for his school students to explore the details of
ASCII. He wants the app to allow a student to input a character and see the corresponding ASCII code, and
vice versa. The output of the program should look like (where g and 100 are user inputs):
"""
LOWER = 33
UPPER = 127

char = input("Enter a character: ")

while len(char) != 1:
    print("Invalid Character")
    char = input("Enter a character: ")

ascii = ord(char)

print("The ascii code for {} is {}".format(char, ascii))

ascii = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

while UPPER < ascii < LOWER:
    print("Invalid Number")
    char = input("Enter a number between {} and {}: ".format(LOWER, UPPER))

char = chr(ascii)

for i in range(33,128):
    print("{}{:>4}".format(i, chr(i)))
