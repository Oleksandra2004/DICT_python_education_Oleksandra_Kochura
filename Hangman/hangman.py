import random

print("HANGMAN")
words = ["python", "java", "javascript", "php"]
word_r = random.choice(words)  # python
word_list = list(word_r)  # [p, y, t, h, o, n]
encrypt_str = len(word_r) * "-"  # ------
encrypt_list = list(encrypt_str)  # [-, -, -, -, -, -]
list_null = []
print(encrypt_str)
for i in range(8):
    enter_letter = str(input("Input a letter: "))
    if enter_letter in list_null:
        print("No improvements")
    list_null.append(enter_letter)
    if enter_letter in word_list:
        if word_list.count(enter_letter) >= 2:
            index = word_list.index(enter_letter)
            encrypt_list[index] = enter_letter
            word_list[index] = "-"
        index = word_list.index(enter_letter)
        encrypt_list[index] = enter_letter
    elif enter_letter not in word_list:
        print("That letter doesn't appear in the word")
    word_str = ''.join(encrypt_list)
    print(''.join(encrypt_list))
word_str = ''.join(encrypt_list)
if word_str == word_r:
    print("You guessed the word! \nYou survived!")
else:
    print("No improvements \nYou lost!")