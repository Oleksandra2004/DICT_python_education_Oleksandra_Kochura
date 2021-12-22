import math
import argparse


parser = argparse.ArgumentParser(description="CreditCalculator 4-th stage")
parser.add_argument('--type', '-t', choices=["diff", "annuity"],
                    help="Choose type of calculation. Possible values 'diff' or 'annuity'")
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float, help="is specified without a percent sign")
parser.add_argument('--payment', type=int)
args = parser.parse_args()

type_of_calc = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment


def check_type(type_):
    if type_ is not None:
        return type_ if type_ in ["diff", "annuity"] else False


def check_pay_error(type_, payment_):
    return False if check_type(type_) == "diff" and payment_ is not None else True


def check_count_params():
    count = 0
    for param in args.__dict__.values():
        if param is not None:
            count += 1
    return False if count < 4 else True


def check_negative():
    params = [principal, payment, periods, interest]
    count_greater_zero = 0
    non_param = 0
    for param in params:
        if param is None:
            non_param += 1
        elif param > 0:
            count_greater_zero += 1
    return True if len(params) - non_param == count_greater_zero else False


def overpayment(payment_, periods_, principal_):
    return payment_ * periods_ - principal_


def annuity_payment(principal_, payment_, periods_):
    i = interest / 1200
    if principal_ is None:
        principal_ = math.floor(payment_ / ((i * pow(1 + i, periods_)) / (pow(1 + i, periods_) - 1)))
        print(f"Your loan principal = {principal_}!\nOverpayment = {overpayment(payment_, periods_, principal_)}")
    elif periods_ is None:
        periods_ = math.ceil(math.log((payment_ / (payment_ - i * principal_)), 1 + i))
        year, month = divmod(periods_, 12)
        if periods_ % 12 != 0:
            print(f"It will take {year} years and {month} months to repay this loan!")
        elif periods_ % 12 == 0:
            print(f"It will take {year} years to repay this loan!")
        else:
            print(f"It will take {month} months to repay this loan!")
        print(f"Overpayment = {overpayment(payment_, periods_, principal_)}")
    else:
        payment_ = math.ceil(principal_ * (i * pow(1 + i, periods_)) / (pow(1 + i, periods_) - 1))
        print(f"Your annuity payment = {payment_}!\nOverpayment = {overpayment(payment_, periods_, principal_)}")


def diff(principal_, periods_):
    overpayment_ = 0
    i = interest / 1200
    for count in range(1, periods_ + 1):
        dif_payment = math.ceil((principal_ / periods_) + i *
                                (principal_ - ((principal_ * (count - 1)) / periods_)))
        overpayment_ += dif_payment - principal_ // periods_
        print(f"Month {count}: payment is {dif_payment}")
    print(f"\nOverpayment = {overpayment_}")


def main():
    if check_pay_error(type_of_calc, payment) and check_count_params() \
            and check_negative() and interest is not None:
        if type_of_calc == "diff":
            diff(principal, periods)
        else:
            annuity_payment(principal, payment, periods)
    else:
        print("Incorrect parameters")
        exit()


main()
