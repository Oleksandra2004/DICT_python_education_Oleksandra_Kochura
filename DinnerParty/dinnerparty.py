import random


def total_amount(count, total):
    try:
        return round((total / count), 2)
    except ValueError:
        print("You should enter numbers!")


def main():
    try:
        print("Enter the number of friends joining (including you):")
        count = int(input("> "))
        msg = "\nNo one is joining your party"
        assert count > 0, msg

        print("Enter the name of every friends (including you), each on a new line:")
        list_friends = [input("> ") for _ in range(count)]

        print("Enter the total amount")
        total_amount_ = int(input("> "))

        print("Do you want yo use the 'Who is lucky?' feature? Write Yes/No:")
        lucky_ = input("> ")
        msg = "\nYou should enter Yes or No!"
        assert lucky_ in ["Yes", "No"], msg

        if lucky_ == "Yes":
            amount = total_amount(count - 1, total_amount_)
            dict_friends = dict.fromkeys(list_friends, amount)
            dict_lucky = random.choice(list_friends)
            print(f"{dict_lucky} is the lucky one!\n")
            dict_friends[dict_lucky] = 0
        else:
            print("No one is going to be lucky")
            amount = total_amount(count, total_amount_)
            dict_friends = dict.fromkeys(list_friends, amount)
        print(dict_friends)
    except ValueError:
        print("You should enter numbers!")
    except AssertionError as error:
        print(error)


if __name__ == '__main__':
    main()
