import random


name = input("Enter your name:> ")
print(f"Hello, {name}")

ratings_dict = {}
score = 0

with open('rating.txt', 'r') as ratings:
    for line in ratings:
        ratings_dict[line.split(" ")[0]] = line.split(" ")[1].strip()

if name in ratings_dict.keys():
    score = int(ratings_dict[name])
ratings.close()


def win(a, b):
    global score
    p = "paper"
    r = "rock"
    s = "scissors"
    if (a == p and b == r) or (a == s and b == p) or (a == r and b == s):
        print(f"Well done. The computer chose {b} and failed")
        score += 100
    else:
        print(f"Sorry, but the computer chose {b}")


def main():
    global score
    while True:
        option = ["rock", "scissors", "paper"]
        option_r = random.choice(option)

        try:
            user = input("> ")
            assert user in ["rock", "scissors", "paper", "!exit", "!rating"]

            if user in option:
                if user == option_r:
                    print(f"There is a draw ({option_r})")
                    score += 50
                else:
                    win(user, option_r)
            elif user == "!rating":
                with open('rating.txt', 'r+') as writer:
                    writer.write(f"{name} {score}")
                writer.close()
                print(score)
            else:
                print("Bye!")
                break
        except AssertionError:
            print("Invalid input")


if __name__ == '__main__':
    main()
