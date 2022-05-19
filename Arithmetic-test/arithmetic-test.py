import random


number = [2, 3, 4, 5, 6, 7, 8, 9]
arithmetic = ["+", "-", "*"]


def multiplication(num_1, num_2):
    answer = num_1 * num_2
    return answer


def addition(num_1, num_2):
    answer = num_1 + num_2
    return answer


def subtraction(num_1, num_2):
    answer = num_1 - num_2
    return answer


def main():
    none = 0
    right = 0
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
    print(f"Your mark is {right}/5")


if __name__ == '__main__':
    main()
