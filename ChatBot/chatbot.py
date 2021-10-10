print("Hello! My name is MiMi. \nI was created in 2021.")
print("Pleas, remind me your name.")
name_1 = input()
print("What a great name you have, " +name_1+ "!")
print("Let me guess your age.")
print("Enter remainders of dividing you age by 3, 5 and 7.")
for i in range(3):
    age_1 = int(input())
    if i == 0:
        remainder3 = age_1
    elif i == 1:
        remainder5 = age_1
    elif i == 2:
        remainder7 = age_1
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Youre age is " +str(age)+ "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any numbr you want.")
for number_1 in range(int(input())+1):
    print(str(number_1) + "!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multipl times.")
print("2. To decompose a program into several small subroutnes.")
print("3. To detrmine the execution time of a program.")
print("4. To interrupt the execution of a program.")
test_1 = 0
while test_1 != 2:
    test_1 = int(input())
    if test_1 == 2:
        print("Congratulations, have a nice day!")
    else:
        print("Please, try again.")