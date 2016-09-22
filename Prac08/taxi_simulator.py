from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
 SilverServiceTaxi("Hummer", 200, 4)]

MENU = "q)uit, c)hoose taxi, d)rive\n"
is_running = True

print("Lets Drive!")
taxi = -1
bill = 0

while is_running:
    print(MENU)
    command = input(">>> ")
    if command == 'q':
        is_running = False
    elif command == 'c':
        "Taxis available: "
        [print("{}- {}".format(i, taxi)) for i, taxi in enumerate(taxis)]
        taxi = int(input("choose taxi: "))
        print("Bill to date: ${:.2f}".format(bill))
    elif command == 'd':
        distance = int(input("Drive how far: "))
        taxis[taxi].start_fare()
        taxis[taxi].drive(distance)
        print("Your {} trip cost you ${}".format(taxis[taxi].name, taxis[taxi].get_fare()))
        bill += taxis[taxi].get_fare()
        print("Bill to date: ${:.2f}".format(bill))






