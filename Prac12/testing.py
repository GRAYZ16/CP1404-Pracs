"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac07.car import Car


def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    str_list = []

    for i in range (0, n):
        str_list.append(s)

    return " ".join(str_list)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def make_sentence(phrase):
    """
    Adds basic grammar to a phrase
    >>> make_sentence("hello world")
    'Hello world.'
    >>> make_sentence("Milton mangoes and powderfinger.")
    'Milton mangoes and powderfinger.'
    """
    sentence = phrase[0].upper()
    sentence += phrase[1:]
    if phrase[-1] is not '.':
        sentence += '.'
    return sentence


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways: using the value passed in or the default
    # You should test both of these
    assert test_car.fuel == 0
    test_car = Car(fuel=10)
    assert test_car.fuel == 10


run_tests()

doctest.testmod()
