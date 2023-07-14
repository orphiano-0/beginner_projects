# EZ2 is a 2D lotto that selects two number from field of 1 to 31.
# create a 2d lotto that randomly pick two numbers in the drawbox
    # apply arguments, decorators, and functions

from random import randint
def repeat(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat
def lotto_number(start, end):
    number = randint(start, end)
    print(f"The number drawn: {number}")

lotto_number(1, 31)