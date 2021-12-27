list_friends = []


def total_amount(count):
    try:
        print("Enter the total amount")
        total_amount_ = int(input("> "))
        amount = round((total_amount_ / count), 2)
        return amount
    except ValueError:
        print("You should enter numbers!")


def main():
    try:
        print("Enter the number of friends joining (including you):")
        count = int(input("> "))
        if 0 < count:
            print("Enter the name of every friends (including you), each on a new line:")
            while count != 0:
                name = input("> ")
                list_friends.append(name)
                count -= 1
            amount = total_amount(len(list_friends))
            dict_friends = dict.fromkeys(list_friends, amount)
            print(dict_friends)
        else:
            print("No one is joining for the party!")
    except ValueError:
        print("You should enter numbers!")


if __name__ == '__main__':
    main()
