"""
Joshua Gray
"""

def main():
    name = get_name()

    print_letters(name)


def print_letters(name, step):
    for i in range(0, len(name), step):
        print(name[i])


def get_name():
    name = input("What is your name? ")
    while len(name) == 0:
        print("Invalid Name")
        name = input("What is your name? ")
    return name


main()
