"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# Expected Answer 3
print(do_it(5))


def do_something(n):
    if n > 0:
        print(n ** 2)
        do_something(n - 1)

# 16 9 4 1
do_something(4)


def do_pyramid(n):
    if n <= 0:
        return 0
    return n + do_pyramid(n - 1)

print(do_pyramid(6))