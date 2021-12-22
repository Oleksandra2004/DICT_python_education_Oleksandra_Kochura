import math


principal = int(input("Enter the loan principal:\n> "))
print("What do you want to calculate?")


def monthly_payment(months):
    payment = math.ceil(principal / months)
    print(f"It will take {payment} months to repay the loan")


def periods_payment(periods):
    period_payment = math.ceil(principal / periods)
    last_payment = principal - (periods - 1) * period_payment
    print(f"Your monthly payment = {period_payment}" if period_payment == last_payment
          else f"Your monthly payment = {period_payment} and the last payment = {last_payment}")


def init():
    user = input("type 'm' - for number of monthly payments,\n"
                 "type 'p' - for the monthly payment:\n> ")
    main(user)


def main(user_input):
    if user_input == "m":
        months = int(input("Enter the monthly payment:\n> "))
        monthly_payment(months)
    elif user_input == "p":
        periods = int(input("Enter the number of months:\n> "))
        periods_payment(periods)
    else:
        print("You type incorrect word")
        init()


init()
