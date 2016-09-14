from Prac07.guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Fender Stratocaster", 2014, 765.40),
           Guitar("Gibson Les Paul", 2015, 2500.50)]

print("These are my guitars: ")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""

    print("Guitar {}: {:>20} ({}, worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

