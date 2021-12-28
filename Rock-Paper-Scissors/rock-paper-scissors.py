import random

rating_dict = {}
score = 0
name = input("Enter your name:> ")
win_combinations = {"rock": ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"],
                    "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"],
                    "scissors": ["snake", "human", "tree", "wolf", "sponge", "paper", "air"],
                    "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
                    "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
                    "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
                    "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lightning"],
                    "sponge": ["paper", "air", "water", "dragon", "devil", "lightning", "gun"],
                    "paper": ["air", "water", "dragon", "devil", "lightning", "gun", "rock"],
                    "air": ["water", "dragon", "devil", "lightning", "gun", "rock", "fire"],
                    "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"],
                    "dragon": ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"],
                    "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"],
                    "lightning": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
                    "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"]}


def create_file(filename_):
    file = open(filename_, "x")
    file.close()


def get_user_rating():
    filename = "rating.txt"
    while True:
        try:
            with open(filename, "r") as reader:
                for line in reader:
                    rating_dict[line.split(" ")[0]] = line.split(" ")[1].strip()
                if name in rating_dict.keys():
                    return int(rating_dict[name])
            return 0
        except FileNotFoundError:
            create_file(filename)
            continue


def write_rating(name_, score_):
    filename = "rating.txt"
    while True:
        try:
            with open(filename, "r+") as writer:
                writer.writelines(f"{name_} {score_}")
                break
        except FileNotFoundError:
            create_file(filename)
            continue


def check_winner(player, cpu):
    global score
    if player == cpu:
        print(f"There is a draw {cpu}")
        score += 50
    elif player in win_combinations[cpu]:
        print(f"Sorry, but the computer chose {cpu}")
    else:
        print(f"Well done. The computer chose {cpu} and failed")
        score += 100


def main():
    global score
    print(f"Hello, {name}")
    user_values = input("Enter possible values, separated by commas\n> ").split(",")
    print("Okay, let's start")
    msg = "Invalid input"
    while True:
        try:
            score = get_user_rating()
            list_of_values = []
            user_input = input()
            if len(user_values) > 0 and "" not in user_values:
                list_of_values.extend(user_values)
            else:
                list_of_values = ["rock", "paper", "scissors"]
            assert user_input in [*list_of_values, "!exit", "!rating"], msg
            cpu_choice = random.choice(list_of_values)
            if user_input == "!exit":
                write_rating(name, score)
                print("Bye!")
                break
            elif user_input == "!rating":
                print(f"Your score: {score}")
                continue
            check_winner(user_input, cpu_choice)
            write_rating(name, score)
        except AssertionError as error:
            print(error)


if __name__ == "__main__":
    main()
