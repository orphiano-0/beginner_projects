import random
def play():
    player = input("Enter your bet: [R: Rock, P: Paper, S: Scissor] ").lower()
    computer = random.choice(["r", "p", "s"])
    if player == computer:
        print("It's a tie!")
    elif is_win(player, computer):
        print(f"The computer picked {computer}")
        print("You won!")
    else:
        print("You lose!")

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
        return True
    return False
play()