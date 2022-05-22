import random


def multiplication(num_1, num_2):
    answer = num_1 * num_2
    return answer


def addition(num_1, num_2):
    answer = num_1 + num_2
    return answer


def subtraction(num_1, num_2):
    answer = num_1 - num_2
    return answer


def one():
    right = 0
    none = 0
    number = [2, 3, 4, 5, 6, 7, 8, 9]
    arithmetic = ["+", "-", "*"]
    while none != 5:
        num_1 = random.choice(number)
        num_2 = random.choice(number)
        arith = random.choice(arithmetic)
        if arith == "*":
            answer = multiplication(num_1, num_2)
        elif arith == "+":
            answer = addition(num_1, num_2)
        else:
            answer = subtraction(num_1, num_2)
        print(num_1, arith, num_2)
        running = True
        while running:
            try:
                user = int(input("> "))
                if user == answer:
                    print("Right!")
                    none += 1
                    right += 1
                    running = False
                else:
                    print("Wrong!")
                    none += 1
                    running = False
            except ValueError:
                print("Incorrect format")
    return right


def two():
    right = 0
    none = 0
    while none != 5:
        number = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                  36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                  61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                  87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        num = random.choice(number)
        print(num)
        answer = num * num
        running = True
        while running:
            try:
                user = int(input("> "))
                if user == answer:
                    print("Right!")
                    none += 1
                    right += 1
                    running = False
                else:
                    print("Wrong!")
                    none += 1
                    running = False
            except ValueError:
                print("Incorrect format")
    return right


def txt(right, level):
    if level == 1:
        level_ = "1 (simple operations with number 2-9)"
    else:
        level_ = "2 (integral squares of 11-29)"
    user = input("What is your name?\n> ")
    f = open('results.txt', 'a')
    f.write(f"{user}: {right}/5 in level {level_}\n")
    f.close()
    print("The results are saved in 'results.txt'")


def main():
    running = True
    running_ = True
    while running:
        try:
            user = int(input("Which level do you want? Enter a number:\n"
                             "1 - simple operations with numbers 2-9\n"
                             "2 - integral squares of 11-29\n> "))
            if user == 1:
                right = one()
                running = False
            elif user == 2:
                right = two()
                running = False
            else:
                print("Incorrect format")
        except ValueError:
            print("Incorrect format")

    while running_:
        try:
            yes = ["yes", "YES", "y", "Yes"]
            no = ["no", "n", "NO", "No"]
            user_ = input(f"Your mark is {right}/5. Would you like to save the result? Enter yes or no.\n> ")
            if user_ in yes:
                running_ = False
                txt(right, user)
            elif user_ in no:
                running_ = False
                pass
            else:
                print("Incorrect format")
        except ValueError:
            print("Incorrect format")


if __name__ == '__main__':
    main()
