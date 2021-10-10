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
print("Copleted, have a nice day!")