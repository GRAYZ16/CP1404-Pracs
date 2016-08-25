import random

def main():
    number_of_picks = int(input("How many quick picks: "))
    quick_picks = [quick_pick() for i in range(number_of_picks)]

    print_picks(quick_picks)


def quick_pick():
    picks = []

    while len(picks) < 6:
        num = random.randint(1, 45)

        if num not in picks:
            picks.append(num)

        picks.sort()
    return picks

def print_picks(picks):
    for pick in picks:
        print("{:2} {:2} {:2} {:2} {:2}".format(pick[0], pick[1], pick[2],pick[3], pick[4], pick[5]))

main()