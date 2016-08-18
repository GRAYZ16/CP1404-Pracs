"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = get_result()
    print(result)


def get_result(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score < 100:
        return "Excellent"
    else:
        return "Invalid score"

main()
