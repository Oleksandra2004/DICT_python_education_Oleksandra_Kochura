# переменные пользователя
print("Write how many ml water the coffee machine has:")
water_user = int(input("> "))
print("Write how many ml milk the coffee machine has:")
milk_user = int(input("> "))
print("Write how many grams of coffee beans the coffee machine has:")
beans_user = int(input("> "))
print("Write how many cups of coffee you  will need:")
cups_user = int(input("> "))

# основные переменные
water = 200
milk = 50
beans = 15


def coffee_settings():
    water_many = water_user // water
    milk_many = milk_user // milk
    beans_many = beans_user // beans
    if water_many * milk_many * beans_many == 0:
        cups = 0
    else:
        cups = min(water_many, milk_many, beans_many)

    cups_extra = cups - cups_user

    if cups_user == cups:
        print("Yes, I can make that amount of coffee")
    elif cups >= cups_user:
        print("Yes, I can make that amount of coffee (and even "
              + str(cups_extra) + " more than that)")
    else:
        print("No, I can make only " + str(cups) + " cups of coffee")


coffee_settings()
