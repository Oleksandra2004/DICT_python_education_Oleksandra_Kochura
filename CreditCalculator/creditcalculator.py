import math


def number_monthly():
    p = float(input("Enter the loan principal:\n> "))
    m = float(input("Enter the monthly payment:\n> "))
    i = float(input("Enter the loan interest:\n> ")) / 1200
    num = (m / (m - (i * p)))
    number_1 = math.log(num, (1 + i))
    number = math.ceil(number_1)
    if number % 12 != 0:
        print(f"It will take {number // 12} years and {number % 12} months to repay this loan!")
    elif number % 12 == 0:
        print(f"It will take {number / 12} years to repay this loan!")
    else:
        print(f"It will take {number} months to repay this loan!")


def loan():
    a = float(input("Enter the annuity payment:\n> "))
    n = float(input("Enter the number of periods:\n> "))
    i = float(input("Enter the loan interest:\n> ")) / 1200
    num = a / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))
    print(f"Your loan principal = {round(num)}!")


def annuity_monthly():
    p = int(input("Enter the loan principal:\n> "))
    n = int(input("Enter the number of periods:\n> "))
    i = int(input("Enter the loan interest:\n> ")) / 1200
    num = p * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))
    print(f"Your monthly payment = {math.ceil(num)}!")


def init():
    print("What do you want to calculate?")
    user = input("type 'n' for number of monthly payments,\n"
                 "type 'a' for annuity monthly payment amount,\n"
                 "type 'p' for the loan principal:\n> ")
    main(user)


def main(user_input):
    if user_input == "n":
        number_monthly()
    elif user_input == "p":
        loan()
    elif user_input == "a":
        annuity_monthly()
    else:
        print("You type incorrect word")
        init()


init()
