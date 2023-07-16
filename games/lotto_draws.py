from random import randint

def repeat(func):
    def wrapper(*args, **kwargs):
        return [func(*args, **kwargs), func(*args, **kwargs)]
    return wrapper

def lotto_number(start, end):
    number = randint(start, end)
    print(f"The number drawn: {number}")
    return number

@repeat
def play_lotto(start, end):
    drawn_number = lotto_number(start, end)
    return drawn_number

# function that determine if the users number won.
def check_winning_numbers(numbers, drawn_numbers):
    if numbers[0] == drawn_numbers[0] and numbers[1] == drawn_numbers[1]:
        print("Congratulations! You've won 50000 pesos!")
    else:
        print("Better luck next time!")

user_numbers = [18, 23]
drawn_numbers = play_lotto(1, 31)

# Check for winning numbers
check_winning_numbers(user_numbers, drawn_numbers)
