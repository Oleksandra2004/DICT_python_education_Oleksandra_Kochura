# основные переменные
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def init(water_s, milk_s, beans_s, cups_s, money_s):
    print("The coffee machine has:\n" + str(water_s) + " of water\n"
          + str(milk_s) + " of milk\n" + str(beans_s)
          + " of coffee beans\n" + str(cups_s) + " of disposable cups\n"
          + str(money_s) + " of money\n")


def espresso():
    water_espresso = water - 250
    milk_espresso = milk
    beans_espresso = beans - 16
    cups_espresso = cups - 1
    money_espresso = money + 4
    init(water_espresso, milk_espresso, beans_espresso,
         cups_espresso, money_espresso)


def latte():
    water_latte = water - 350
    milk_latte = milk - 75
    beans_latte = beans - 20
    cups_latte = cups - 1
    money_latte = money + 7
    init(water_latte, milk_latte, beans_latte,
         cups_latte, money_latte)


def cappuccino():
    water_cappuccino = water - 200
    milk_cappuccino = milk - 100
    beans_cappuccino = beans - 12
    cups_cappuccino = cups - 1
    money_cappuccino = money + 6
    init(water_cappuccino, milk_cappuccino, beans_cappuccino,
         cups_cappuccino, money_cappuccino)


def fill():
    print("Write how many ml of water you want to add:")
    water_user = int(input("> "))
    print("Write how many ml of milk you want to add:")
    milk_user = int(input("> "))
    print("Write how many grams of coffee beans you want to add:")
    beans_user = int(input("> "))
    print("Write how many disposable coffee cups you want to add:")
    cups_user = int(input("> "))
    water_fill = water + water_user
    milk_fill = milk + milk_user
    beans_fill = beans + beans_user
    cups_fill = cups + cups_user
    init(water_fill, milk_fill, beans_fill, cups_fill, money)


def take():
    print("I gave you " + str(money))
    money_take = money - money
    init(water, milk, beans, cups, money_take)


def play():
    init(water, milk, beans, cups, money)
    print("Write action (buy, fill, take):")
    user = (input("> "))
    if user == "buy":
        print("What do you want to buy? 1 - espresso,"
              " 2 - latte, 3 - cappuccino:")
        buy_coffee = int(input("> "))
        if buy_coffee == 1:
            espresso()
        elif buy_coffee == 2:
            latte()
        elif buy_coffee == 3:
            cappuccino()
    elif user == "fill":
        fill()
    elif user == "take":
        take()


play()
