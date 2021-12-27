import random


def win(a, b):
    p = "paper"
    r = "rock"
    s = "scissors"
    if (a == p and b == r) or (a == s and b == p) or (a == r and b == s):
        print(f"Well done. The computer chose {b} and failed")
    else:
        print(f"Sorry, but the computer chose {b}")


def main():
    try:
        option = ["rock", "scissors", "paper"]
        option_r = random.choice(option)
        user = input("> ")
        msg = "You should enter 'rock', 'paper' or 'scissors'"
        assert user in option, msg
        if user == option_r:
            print(f"There is a draw ({option_r})")
        else:
            win(user, option_r)
    except AssertionError as error:
        print(error)


if __name__ == '__main__':
    main()
