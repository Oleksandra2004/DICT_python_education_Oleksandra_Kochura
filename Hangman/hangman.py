import random

print("HANGMAN")
words = ["python", "java", "javascript", "php"]
word_r = random.choice(words)
word_list = list(word_r)
encrypt_str = len(word_r) * "-"
encrypt_list = list(encrypt_str)
list_null = []
list_null_2 = []
english_letters = list("mnbvcxzasdfghjklpoiuytrewq")
print(encrypt_str)
count = 0
while count != 8:
    count += 1
    enter_letter = str(input("Input a letter: "))
    if enter_letter in list_null:
        print("You've already guessed this letter\n")
        count -= 1
        continue
    list_null.append(enter_letter)
    if enter_letter in word_list:
        if word_list.count(enter_letter) >= 2:
            index = word_list.index(enter_letter)
            encrypt_list[index] = enter_letter
            word_list[index] = "-"
        index = word_list.index(enter_letter)
        encrypt_list[index] = enter_letter
        count -= 1
    elif len(enter_letter) >= 2:
        print("You should input a single letter\n")
        count -= 1
    elif enter_letter not in english_letters:
        print("Please enter a lowercase English letter\n")
        count -= 1
    elif enter_letter not in word_list:
        print("That letter doesn't appear in the word\n")
    print(''.join(encrypt_list))
word_str = ''.join(encrypt_list)
if word_str == word_r:
    print("You guessed the word! \nYou survived!")
else:
    print("No improvements \nYou lost!")
