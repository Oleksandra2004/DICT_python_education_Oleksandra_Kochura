import collections
import enum


class Action(enum.Enum):
    BUY = "buy"
    FILL = "fill"
    TAKE = "take"
    EXIT = "exit"
    REMAINING = "remaining"


def take_action():
    possible_values = ", ".join([action.value for action in Action])
    while True:
        answer = input(f"Write action {possible_values}:\n")
        try:
            return Action(answer)
        except ValueError:
            print(f"{answer} is not valid action")


def selected_drink():
    valid_drinks = {1: "espresso", 2: "latte", 3: "cappuccino", 9: "back to main menu"}
    possible_values = ", ".join(f"{value}. {name}" for value, name in sorted(valid_drinks.items()))
    while True:
        user_answer = input(f"What do you want to buy? ({possible_values}):\n")
        try:
            value = int(user_answer)
            if value in valid_drinks:
                return value
            print(f"This answer is not valid: {user_answer}")
        except ValueError:
            print(f"This is not a number: {user_answer}")


def take_quantity(msg):
    while True:
        answer = input(msg + "\n")
        try:
            value = int(answer)
            if value >= 0:
                return value
            print(f"This answer is not valid {answer}")
        except ValueError:
            print(f"This is not a number {answer}")


Flow = collections.namedtuple("Flow", "water milk beans cups money")


class NotEnoughSupplyError(Exception):
    def __init__(self, supply):
        msg = f"Sorry, not enough {supply}"
        super(NotEnoughSupplyError, self).__init__(msg)


class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.running = True

    def execute_action(self, action):
        if action == Action.BUY:
            self.buy()
        elif action == Action.FILL:
            self.fill()
        elif action == Action.TAKE:
            self.take()
        elif action == Action.REMAINING:
            self.display_remaining()
        elif action == Action.EXIT:
            self.running = False
        else:
            raise NotImplementedError(action)

    def available_check(self, flow):
        if self.water - flow.water < 0:
            raise NotEnoughSupplyError("water")
        elif self.milk - flow.milk < 0:
            raise NotEnoughSupplyError("milk")
        elif self.beans - flow.beans < 0:
            raise NotEnoughSupplyError("coffee beans")
        elif self.cups - flow.cups < 0:
            raise NotEnoughSupplyError("disposable cups")

    def buy(self):
        drink = selected_drink()
        if drink == 9:
            return
        espresso_cost = Flow(250, 0, 16, 1, 4)
        latte_cost = Flow(350, 75, 20, 1, 7)
        cappuccino_cost = Flow(200, 100, 12, 1, 6)
        flow = {1: espresso_cost, 2: latte_cost, 3: cappuccino_cost}[drink]
        try:
            self.available_check(flow)
        except NotEnoughSupplyError as exception:
            print(exception)
        else:
            print("I've have enough resources, making you a coffee!")
            self.water -= flow.water
            self.milk -= flow.milk
            self.beans -= flow.beans
            self.cups -= flow.cups
            self.money += flow.money

    def fill(self):
        self.water += take_quantity("Write how many ml of water do you want to add:")
        self.milk += take_quantity("Write how many ml of milk do you want to add:")
        self.beans += take_quantity("Write how many grams of coffee beans do you want to add:")
        self.cups += take_quantity("Write how many disposable cups do you want to add:")

    def take(self):
        print(f"I'v gave you {self.money}")
        self.money = 0

    def display_remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


def main():
    machine = CoffeeMachine()
    while machine.running:
        action = take_action()
        machine.execute_action(action)


main()
