def option(option_):
    print(f"Sorry, but the computer chose {option_}")


def main():
    user = input("> ")
    if user == "scissors":
        option("rock")
    elif user == "paper":
        option("scissors")
    elif user == "rock":
        option("paper")


if __name__ == '__main__':
    main()
