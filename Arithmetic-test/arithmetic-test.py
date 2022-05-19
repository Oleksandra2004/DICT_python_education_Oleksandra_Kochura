import random


number = [2, 3, 4, 5, 6, 7, 8, 9]
arithmetic = ["+", "-", "*"]
num_1 = random.choice(number)
num_2 = random.choice(number)
arith = random.choice(arithmetic)


def multiplication():
    answer = num_1 * num_2
    return answer


def addition():
    answer = num_1 + num_2
    return answer


def subtraction():
    answer = num_1 - num_2
    return answer


def main():
    if arith == "*":
        answer = multiplication()
    elif arith == "+":
        answer = addition()
    else:
        answer = subtraction()
    print(num_1, arith, num_2)
    user = int(input("> "))
    if user == answer:
        print("Right!")
    else:
        print("Wrong!")


if __name__ == '__main__':
    main()
