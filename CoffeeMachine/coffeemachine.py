def coffee():
    print("Write how many cups of coffee you will need: ")
    many_cups = int(input("> "))
    water = many_cups * 200
    milk = many_cups * 50
    coffee_beans = many_cups * 15
    print(f"For {many_cups} cups of coffee you will need:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{coffee_beans} g of coffee beans")


coffee()
