def greetings():
    print("Hello! My name is MiMi. \nI was created in 2021.")
    print("Pleas, remind me your name.")
    name_1 = input("> ")
    print("What a great name you have, " + name_1 + "!")


def age():
    print("Let me guess your age.")
    print("Enter remainders of dividing you age by 3, 5 and 7.")
    remainder3 = int(input("> "))
    remainder5 = int(input("> "))
    remainder7 = int(input("> "))
    age_user = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print("You're age is " + str(age_user) + "; that's a good time to start programming!")


def play():
    print("Now I will prove to you that I can count to any number you want.")
    for number_1 in range(int(input("> ")) + 1):
        print(str(number_1) + "!")


def game():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    test_1 = 0
    while test_1 != 2:
        test_1 = int(input())
        if test_1 == 2:
            print("Completed, have a nice day!")
        else:
            print("Please, try again.")
    print("Congratulations, have a nice day!")


greetings()
age()
play()
game()
