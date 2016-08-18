try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
except ValueError:
    #This error occurs when the input cannot be parsed to an int value
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    #This error occurs when the division of the
    print("Cannot divide by zero!")
    print("Finished.")