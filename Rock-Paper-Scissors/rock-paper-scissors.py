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
    while True:
        option = ["rock", "scissors", "paper"]
        option_r = random.choice(option)
        try:
            user = input("> ")
            assert user in ["rock", "scissors", "paper", "!exit"]

            if user in option:
                if user == option_r:
                    print(f"There is a draw ({option_r})")
                else:
                    win(user, option_r)
            else:
                print("Bye!")
                break
        except AssertionError:
            print("Invalid input")


if __name__ == '__main__':
    main()
